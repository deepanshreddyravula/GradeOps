import os
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.config import UPLOAD_DIR
from app.utils.image_loader import load_image
from app.schemas.ocr_schema import OCRResponse
from app.utils.auth_guard import get_current_instructor

from app.config import OCR_ENGINE

if OCR_ENGINE == "qwen":
    from app.services.qwen_ocr_service import extract_text_from_image
else:
    from app.services.paddle_ocr_service import extract_text_from_image
router = APIRouter()
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/extract", response_model=OCRResponse)
async def extract_ocr(
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_instructor)
):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())

        image = load_image(file_path)
        text = extract_text_from_image(image)
        return OCRResponse(extracted_text=text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))