from fastapi import FastAPI, UploadFile, File
from agents.weather_agent import get_weather
from agents.document_agent import read_document, answer_from_document
from agents.meeting_agent import schedule_meeting_if_possible
from agents.db_agent import query_meetings

app = FastAPI()
document_text = ""


@app.post("/upload")
def upload_document(file: UploadFile = File(...)):
    global document_text
    document_text = read_document(file)
    return {"message": "Document uploaded successfully"}


@app.post("/chat")
def chat(query: str):
    q = query.lower()

    if "weather" in q:
        city = query.split("in")[-1].strip()
        return get_weather(city)

    if "schedule" in q:
        return schedule_meeting_if_possible("Chennai")

    if "meeting" in q:
        return query_meetings(query)

    if document_text:
        return answer_from_document(query, document_text)

    return {"message": "Unable to understand request"}
