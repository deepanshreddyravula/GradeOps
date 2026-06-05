<div align="center">

# 🎓 GradeOps

### AI-Powered Automated Exam Evaluation Platform

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?style=flat&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-19-blue?style=flat&logo=react&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green?style=flat&logo=mongodb&logoColor=white)
![PaddleOCR](https://img.shields.io/badge/PaddleOCR-Supported-orange?style=flat)
![Qwen2--VL](https://img.shields.io/badge/Qwen2--VL-Supported-yellow?style=flat)
![Gemini](https://img.shields.io/badge/Gemini-AI-blueviolet?style=flat)
![JWT](https://img.shields.io/badge/Auth-JWT-red?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

**AI-powered grading platform that automates answer sheet evaluation using OCR, LLM-based assessment, and secure exam management.**

</div>

---

# 🚀 Overview

**GradeOps** is a full-stack AI-powered exam evaluation platform designed to reduce the time, effort, and inconsistency involved in manual grading.

The platform enables instructors to:

- Create and manage exams
- Register and manage students
- Upload marking schemes
- Upload scanned answer sheets
- Extract handwritten or printed text using OCR
- Evaluate responses using AI
- Generate question-wise scores and detailed reasoning
- Store and retrieve evaluation history securely

By combining OCR and Large Language Models, GradeOps delivers fast, scalable, and transparent assessment workflows for educational institutions.

---

# ✨ Key Features

## 🔐 Secure Authentication

- JWT-based authentication
- Password hashing using bcrypt
- Protected API endpoints
- Instructor-only access control

---

## 📚 Exam Management

- Create exams
- Manage exam records
- Associate marking schemes with exams
- View exam-wise submissions

---

## 👨‍🎓 Student Management

- Register students
- Search student records
- Track evaluation history
- Student-wise result retrieval

---

## 🔄 Pluggable OCR Engine

GradeOps supports multiple OCR backends through a configurable OCR abstraction layer.

### PaddleOCR

- Fast inference
- Lightweight deployment
- Excellent handwritten text recognition
- Suitable for production deployments

### Qwen2-VL OCR

- Vision-Language Model based OCR
- Strong contextual understanding
- Handles complex document layouts
- Useful for advanced document interpretation

OCR engine selection is controlled through a single environment variable:

```env
OCR_ENGINE=paddle

# or

OCR_ENGINE=qwen
```

This allows switching OCR providers without modifying application code.

---

## 📝 Answer Sheet Processing

- PDF support
- Image support (PNG, JPG, JPEG)
- Automatic document loading
- Text extraction pipeline
- Multi-page document handling

---

## 🤖 AI Evaluation Engine

- Google Gemini integration
- Question-wise scoring
- Automated mark allocation
- Detailed reasoning generation
- Percentage calculation
- Overall feedback generation

---

## 📊 Results Management

- Student-wise evaluations
- Exam-wise evaluations
- Submission tracking
- Evaluation history
- Persistent result storage

---

# 🏗️ System Architecture

```text
Instructor Dashboard (React)

            ↓

      FastAPI Backend

            ↓

      JWT Authentication

            ↓

         MongoDB

            ↓

   OCR Abstraction Layer

      ├── PaddleOCR
      └── Qwen2-VL OCR

            ↓

      Gemini Evaluator

            ↓

     Evaluation Results
```

---

# 🛠️ Tech Stack

## Frontend

- React 19
- Vite
- Axios
- Context API
- CSS

## Backend

- FastAPI
- Pydantic
- Uvicorn

## Database

- MongoDB Atlas
- PyMongo

## OCR

- PaddleOCR
- Qwen2-VL OCR

## AI Evaluation

- Google Gemini

## Security

- JWT Authentication
- Passlib (bcrypt)
- Protected Routes

## Deployment

- Render
- MongoDB Atlas

---

# 📂 Project Structure

```text
GradeOps/

├── backend/
│
│   ├── app/
│   │
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── exams.py
│   │   │   ├── students.py
│   │   │   ├── evaluate.py
│   │   │   ├── submissions.py
│   │   │   └── ocr.py
│   │
│   │   ├── services/
│   │   │   ├── paddle_ocr_service.py
│   │   │   ├── qwen_ocr_service.py
│   │   │   ├── gemini_evaluator.py
│   │   │   ├── evaluation_service.py
│   │   │   ├── auth_service.py
│   │   │   └── submission_service.py
│   │
│   │   ├── storage/
│   │   ├── schemas/
│   │   ├── utils/
│   │   ├── database/
│   │   └── main.py
│
│   ├── run.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── services/
│   │   ├── context/
│   │   └── App.jsx
│
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# ⚙️ Environment Variables

Create a `.env` file inside the backend directory.

```env
# MongoDB

MONGO_URI=your_mongodb_connection_string
DB_NAME=gradeops

# JWT

JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Gemini

GEMINI_API_KEY=your_gemini_api_key

# OCR

OCR_ENGINE=paddle

# Uploads

UPLOAD_DIR=uploads
```

---

# 🔧 Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate

# Windows
# venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

# 🎨 Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# 🔑 API Reference

## Authentication

```http
POST /auth/register
POST /auth/login
```

## Exams

```http
POST /exams/create
GET /exams
```

## Students

```http
POST /students/create
GET /students
GET /students/{student_id}
```

## OCR

```http
POST /ocr/extract
```

## Evaluation

```http
POST /evaluate/upload-scheme
POST /evaluate/grade
```

## Submissions

```http
GET /submissions/exam/{exam_id}
GET /submissions/student/{student_id}
```

All endpoints except authentication require:

```http
Authorization: Bearer <JWT_TOKEN>
```

---

# 🔄 Application Workflow

### 1. Instructor Login

- Instructor registers or logs in
- JWT token is issued

### 2. Exam Creation

- Create an exam
- Store exam metadata

### 3. Student Registration

- Add students to the platform

### 4. Marking Scheme Upload

- Upload marking scheme
- Associate with exam

### 5. Answer Sheet Upload

- Upload image or PDF

### 6. OCR Extraction

- PaddleOCR or Qwen2-VL extracts text

### 7. AI Evaluation

- Gemini evaluates responses
- Marks are assigned
- Reasoning is generated

### 8. Result Generation

- Scores are calculated
- Evaluation is stored in MongoDB

### 9. Dashboard Display

- Results become available instantly

---

# 🌟 Future Improvements

- Bulk answer sheet evaluation
- Analytics dashboard
- Class performance insights
- PDF result export
- Role-based access control
- Fine-tuned grading models
- Real-time evaluation tracking

---

# 👨‍💻 Author

### Deepansh Reddy

GradeOps was built to modernize academic evaluation using OCR, AI-powered grading, secure authentication, and scalable cloud technologies.Contributed by Bhaskar Reddy
