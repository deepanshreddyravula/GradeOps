from datetime import datetime, timezone
import uuid

from app.database import db

exams_collection = db.exams


def create_exam(data: dict):

    existing = exams_collection.find_one({
        "exam_id": data["exam_id"]
    })

    if existing:
        return None

    new_exam = {
        "id": str(uuid.uuid4()),
        "exam_id": data["exam_id"],
        "title": data["title"],
        "subject": data.get("subject"),
        "description": data.get("description"),
        "total_marks": data["total_marks"],
        "uploaded_by": data["uploaded_by"],
        "scheme_id": None,
        "is_active": True,
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    exams_collection.insert_one(new_exam)

    return new_exam


def get_exam_by_exam_id(exam_id: str,user_id: str):

    exam = exams_collection.find_one({
        "exam_id": exam_id,
        "uploaded_by" : user_id
    })

    if exam:
        exam.pop("_id", None)

    return exam


def list_exams_by_user(user_id: str):

    exams = list(
        exams_collection.find({
            "uploaded_by": user_id
        })
    )

    for exam in exams:
        exam.pop("_id", None)

    return exams


def attach_scheme_to_exam(exam_id: str, scheme_id: str):

    exams_collection.update_one(
        {"exam_id": exam_id},
        {"$set": {"scheme_id": scheme_id}}
    )

    exam = exams_collection.find_one({
        "exam_id": exam_id
    })

    if exam:
        exam.pop("_id", None)

    return exam