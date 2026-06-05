from datetime import datetime, timezone
import uuid

from app.database import db

users_collection = db.users


def create_user(name: str, email: str, hashed_password: str):

    existing = users_collection.find_one({
        "email": email.lower()
    })

    if existing:
        return None

    new_user = {
        "id": str(uuid.uuid4()),
        "name": name,
        "email": email.lower(),
        "hashed_password": hashed_password,
        "role": "instructor",
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    users_collection.insert_one(new_user)

    return new_user


def get_user_by_email(email: str):

    user = users_collection.find_one({
        "email": email.lower()
    })

    if user:
        user.pop("_id", None)

    return user


def get_user_by_id(user_id: str):

    user = users_collection.find_one({
        "id": user_id
    })

    if user:
        user.pop("_id", None)

    return user