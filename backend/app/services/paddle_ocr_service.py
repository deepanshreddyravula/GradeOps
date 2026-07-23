from paddleocr import PaddleOCR
import numpy as np

ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)

def extract_text_from_image(image):

    print("PADDLE OCR START")

    MAX_DIM = 1000

    if max(image.size) > MAX_DIM:
        image.thumbnail((MAX_DIM, MAX_DIM))
        image_np = np.array(image)

    result = ocr.predict(image_np)

    print("PADDLE OCR END")

    lines = []

    for page in result:
        if "rec_texts" in page:
            lines.extend(page["rec_texts"])

    return "\n".join(lines)