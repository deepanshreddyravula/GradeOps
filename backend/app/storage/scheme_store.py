from datetime import datetime, timezone
import uuid

from app.database import db

schemes_collection = db.schemes


def create_scheme(exam_id: str, uploaded_by: str, scheme_data: dict):

    new_scheme = {
        "id": str(uuid.uuid4()),
        "scheme_id": str(uuid.uuid4()),
        "exam_id": exam_id,
        "uploaded_by": uploaded_by,
        "exam_name": scheme_data["exam_name"],
        "total_marks": scheme_data["total_marks"],
        "questions": scheme_data["questions"],
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    schemes_collection.insert_one(new_scheme)

    return new_scheme


# def get_scheme_by_scheme_id(scheme_id: str):

#     scheme = schemes_collection.find_one({
#         "scheme_id": scheme_id
#     })

#     if scheme:
#         scheme.pop("_id", None)

#     return scheme


def get_scheme_by_exam_id(exam_id: str,user_id: str):

    scheme = schemes_collection.find_one(
        {"exam_id": exam_id,
         "uploaded_by": user_id},
        sort=[("created_at", -1)]
    )

    if scheme:
        scheme.pop("_id", None)

    return scheme