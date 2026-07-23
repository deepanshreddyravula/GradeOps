from datetime import datetime, timezone
import uuid

from sympy import use

from app.database import db

submissions_collection = db.submissions


def create_submission(data: dict):

    new_submission = {
        "id": str(uuid.uuid4()),
        "exam_id": data["exam_id"],
        "scheme_id": data["scheme_id"],
        "student_id": data["student_id"],
        "uploaded_by": data["uploaded_by"],
        "image_path": data["image_path"],
        "extracted_text": data["extracted_text"],
        "status": data.get("status", "evaluated"),
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    submissions_collection.insert_one(new_submission)

    return new_submission


def get_submission_by_id(submission_id: str):

    submission = submissions_collection.find_one({
        "id": submission_id
    })

    if submission:
        submission.pop("_id", None)

    return submission


def list_submissions_by_exam(exam_id: str ,user_id : str):

    submissions = list(
        submissions_collection.find({
            "exam_id": exam_id,
            "uploaded_by":user_id
        })
    )

    for submission in submissions:
        submission.pop("_id", None)

    return submissions


def list_submissions_by_student(student_id: str,user_id : str):

    submissions = list(
        submissions_collection.find({
            "student_id": student_id,
            "uploaded_by":user_id
        })
    )

    for submission in submissions:
        submission.pop("_id", None)

    return submissions