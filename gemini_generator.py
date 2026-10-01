import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

if API_KEY:
    genai.configure(api_key=API_KEY)

class GeminiDocumentGenerator:
    def __init__(self):
        self.model = genai.GenerativeModel(MODEL_NAME) if API_KEY else None

    def generate_document(self, document_type, parties, terms, dates):
        if not self.model:
            raise RuntimeError(
                "GEMINI_API_KEY is missing. Add it to the .env file."
            )

        prompt = f"""
You are LegalEase, an AI assistant for drafting structured legal documents.

Create a professional draft of the following document.

Document Type:
{document_type}

Parties Involved:
{parties}

Terms and Conditions:
{terms}

Effective Date:
{dates}

Requirements:
1. Use clear formal legal language.
2. Include a title.
3. Include sections for the parties, purpose, terms, obligations,
   confidentiality where relevant, termination where relevant,
   governing law where appropriate, and signatures.
4. Use the supplied facts only; do not invent personal details.
5. Make the document editable and well structured.
6. Add a short disclaimer at the end stating that the document
   should be reviewed by a qualified legal professional before use.

Return only the document text.
"""
        response = self.model.generate_content(prompt)
        return response.text
