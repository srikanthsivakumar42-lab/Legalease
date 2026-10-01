# LegalEase - AI-Powered Legal Document Generator

This project follows the architecture and functionality described in the supplied LegalEase PDF:

- Streamlit frontend
- FastAPI backend
- Gemini AI document generation
- Editable document preview
- TXT export
- DOCX export
- PDF export
- Environment-variable API key
- `/generate` FastAPI endpoint

## Project structure

LegalEase_Project/
├── main.py
├── routes.py
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── ai_core/
│   ├── __init__.py
│   └── gemini_generator.py
└── formatters/
    ├── __init__.py
    ├── utils.py
    ├── txt_formatter.py
    ├── docx_formatter.py
    └── pdf_formatter.py

## 1. Install Python

Use Python 3.10 or newer.

## 2. Create virtual environment

Windows:
python -m venv venv
venv\Scripts\activate

macOS/Linux:
python3 -m venv venv
source venv/bin/activate

## 3. Install packages

pip install -r requirements.txt

## 4. Configure Gemini API

Copy `.env.example` to `.env`.

Then put your Gemini API key:

GEMINI_API_KEY=your_api_key

Do not share the API key publicly.

## 5. Start FastAPI backend

uvicorn main:app --reload

Backend:
http://127.0.0.1:8000

API documentation:
http://127.0.0.1:8000/docs

## 6. Start Streamlit frontend

Open another terminal with the virtual environment activated:

streamlit run app.py

Then open the Streamlit URL shown in the terminal.

## 7. Test

Enter:
- Document Type
- Parties Involved
- Terms & Conditions
- Effective Date

Click Generate Document.

Then you can:
- Preview the document
- Edit the generated text
- Download TXT
- Download DOCX
- Download PDF

## Important

This is an AI-assisted document drafting project. Generated legal text should be reviewed by a qualified legal professional before actual use.
