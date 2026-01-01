from PyPDF2 import PdfReader
from duckduckgo_search import DDGS


def read_document(file):
    if file.filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
        return text
    else:
        return file.file.read().decode("utf-8")


def answer_from_document(question: str, document_text: str):
    # 1. Check inside document first
    if question.lower() in document_text.lower():
        return {
            "source": "document",
            "answer": "Answer exists in document (basic match found)."
        }

    # 2. Fallback to DuckDuckGo search
    with DDGS() as ddgs:
        results = ddgs.text(question, max_results=1)

        for r in results:
            return {
                "source": "web",
                "answer": r.get("body", "No summary available")
            }

    return {
        "source": "web",
        "answer": "No relevant result found"
    }