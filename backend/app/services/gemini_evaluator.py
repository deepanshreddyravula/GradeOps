import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def evaluate_with_gemini(answer_text, scheme):
    print("Gemini evaluation start")
    prompt = f"""
You are an expert exam evaluator.

Marking Scheme:
{json.dumps(scheme, indent=2)}

Student Answer:
{answer_text}

Evaluate the student's answer according to the marking scheme.

Return ONLY valid JSON.

Required format:

{{
  "extracted_text": "{answer_text}",
  "total_score": 0,
  "max_score": {scheme.get("total_marks", 0)},
  "percentage": 0,
  "question_wise": [
    {{
      "question_no": 1,
      "awarded_marks": 0,
      "max_marks": 0,
      "matched_points": [],
      "missing_points": [],
      "reasoning": ""
    }}
  ],
  "overall_reasoning": ""
}}

Rules:
- Award partial marks where appropriate.
- Use semantic understanding, not exact keyword matching.
- matched_points should contain points covered by the student.
- missing_points should contain points not covered.
- total_score must equal the sum of awarded_marks.
- reasoning in around 10-15 words.
- percentage = (total_score / max_score) * 100.
- Return ONLY JSON.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    result = json.loads(text)
    print("Gemini evaluation end")
    return result