from app.storage.submission_store import create_submission
from app.storage.evaluation_store import create_evaluation

def create_submission_record(data: dict,user_id : str):
    return create_submission(data,user_id)

def create_evaluation_record(data: dict,user_id : str):
    return create_evaluation(data,user_id)