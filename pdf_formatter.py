from io import BytesIO
from fpdf import FPDF
from formatters.utils import sanitize_text

class LegalEasePDF(FPDF):
    def __init__(self, doc_type):
        super().__init__()
        self.doc_type = doc_type
        self.set_auto_page_break(auto=True, margin=18)

    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 8, "LegalEase", align="C")
        self.ln(8)

    def footer(self):
        self.set_y(-12)
        self.set_font("Arial", "I", 8)
        self.cell(0, 8, "LegalEase - AI-generated draft | Page " + str(self.page_no()), align="C")

def format_pdf(text: str, doc_type: str) -> bytes:
    pdf = LegalEasePDF(doc_type)
    pdf.add_page()
    pdf.set_font("Arial", "B", 15)
    pdf.cell(0, 10, doc_type.upper(), ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Arial", size=11)

    for line in sanitize_text(text).split("\n"):
        line = line.strip()
        if not line:
            pdf.ln(3)
            continue
        pdf.multi_cell(0, 6, line)
        pdf.ln(1)

    data = pdf.output(dest="S")
    return bytes(data)
