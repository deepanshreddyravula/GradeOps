from datetime import datetime, timezone
import uuid

from app.database import db

evaluations_collection = db.evaluations


def create_evaluation(data: dict):

    new_eval = {
        "id": str(uuid.uuid4()),
        "submission_id": data["submission_id"],
        "scheme_id": data["scheme_id"],
        "exam_id": data["exam_id"],
        "student_id": data["student_id"],
        "evaluated_by": data["evaluated_by"],
        "extracted_text": data["extracted_text"],
        "total_score": data["total_score"],
        "max_score": data["max_score"],
        "percentage": data["percentage"],
        "question_wise": data["question_wise"],
        "overall_reasoning": data["overall_reasoning"],
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    evaluations_collection.insert_one(new_eval)

    return new_eval


def list_evaluations_by_exam(exam_id: str,user_id: str):

    evaluations = list(
        evaluations_collection.find({
            "exam_id": exam_id,
            "evaluated_by" : user_id
        })
    )

    for evaluation in evaluations:
        evaluation.pop("_id", None)

    return evaluations


def list_evaluations_by_student(student_id: str,user_id: str):

    evaluations = list(
        evaluations_collection.find({
            "student_id": student_id,
            "evaluated_by" : user_id
        })
    )

    for evaluation in evaluations:
        evaluation.pop("_id", None)

    return evaluations