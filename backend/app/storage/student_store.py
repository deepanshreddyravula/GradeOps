from datetime import datetime, timezone
import uuid

from app.database import db

students_collection = db.students


def create_student(data: dict):

    # Check duplicate student_id only for this instructor
    existing = students_collection.find_one({
        "student_id": data["student_id"],
        "created_by": data["created_by"]
    })

    if existing:
        return None

    new_student = {
        "id": str(uuid.uuid4()),
        "student_id": data["student_id"],
        "name": data["name"],
        "department": data.get("department"),
        "batch": data.get("batch"),
        "created_by": data["created_by"],
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    students_collection.insert_one(new_student)

    return new_student


def get_student_by_student_id(student_id: str, user_id: str):

    student = students_collection.find_one({
        "student_id": student_id,
        "created_by": user_id
    })

    if student:
        student.pop("_id", None)

    return student


def list_students_by_user(user_id: str):

    students = list(
        students_collection.find({
            "created_by": user_id
        })
    )

    for student in students:
        student.pop("_id", None)

    return students