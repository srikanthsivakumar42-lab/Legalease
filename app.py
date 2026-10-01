import os
import requests
import streamlit as st
from dotenv import load_dotenv

from formatters.docx_formatter import format_docx
from formatters.pdf_formatter import format_pdf
from formatters.txt_formatter import format_txt

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 0;
}
.subtitle {
    text-align: center;
    color: #888;
    margin-bottom: 30px;
}
.preview {
    background: #111827;
    color: #f9fafb;
    padding: 24px;
    border-radius: 12px;
    white-space: pre-wrap;
    max-height: 600px;
    overflow-y: auto;
    font-family: Georgia, serif;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">⚖️ LegalEase</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI-Powered Legal Document Generator</div>',
    unsafe_allow_html=True
)

if "document" not in st.session_state:
    st.session_state.document = ""
if "editing" not in st.session_state:
    st.session_state.editing = False

col1, col2 = st.columns(2)

with col1:
    document_type = st.text_input(
        "Document Type",
        placeholder="Example: Freelance Work Contract"
    )

    parties = st.text_area(
        "Parties Involved",
        placeholder="Example: Jane Doe (Service Provider), TechNova Inc. (Client)"
    )

with col2:
    dates = st.text_input(
        "Effective Date",
        placeholder="Example: April 15, 2025"
    )

    terms = st.text_area(
        "Terms & Conditions",
        placeholder="Separate clauses using semicolons; Payment within 30 days; Confidentiality must be maintained"
    )

if st.button("Generate Document", type="primary", use_container_width=True):
    if not all([document_type, parties, terms, dates]):
        st.warning("Please fill all required fields.")
    else:
        with st.spinner("Generating legal document with Gemini..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/generate",
                    json={
                        "document_type": document_type,
                        "parties": parties,
                        "terms": terms,
                        "dates": dates
                    },
                    timeout=120
                )
                response.raise_for_status()
                st.session_state.document = response.json()["document"]
                st.session_state.editing = False
            except Exception as e:
                st.error(f"Backend error: {e}")

if st.session_state.document:
    st.divider()
    st.subheader("Generated Document")

    if st.button("Click to Edit Document"):
        st.session_state.editing = True

    if st.session_state.editing:
        edited = st.text_area(
            "Edit Document",
            value=st.session_state.document,
            height=500
        )
        if st.button("Save Changes"):
            st.session_state.document = edited
            st.session_state.editing = False
            st.rerun()
    else:
        st.markdown(
            f'<div class="preview">{st.session_state.document}</div>',
            unsafe_allow_html=True
        )

    st.divider()
    st.subheader("Download / Save")

    txt_data = format_txt(st.session_state.document)
    docx_data = format_docx(st.session_state.document, document_type or "Legal Document")
    pdf_data = format_pdf(st.session_state.document, document_type or "Legal Document")

    d1, d2, d3 = st.columns(3)

    with d1:
        st.download_button(
            "Download TXT",
            data=txt_data,
            file_name="legalease_document.txt",
            mime="text/plain",
            use_container_width=True
        )

    with d2:
        st.download_button(
            "Download DOCX",
            data=docx_data,
            file_name="legalease_document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True
        )

    with d3:
        st.download_button(
            "Download PDF",
            data=pdf_data,
            file_name="legalease_document.pdf",
            mime="application/pdf",
            use_container_width=True
        )

st.caption(
    "LegalEase generates AI-assisted drafts. Review the document with a qualified legal professional before use."
)
