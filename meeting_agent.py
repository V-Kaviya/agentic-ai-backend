import sqlite3
from datetime import date, timedelta
from agents.weather_agent import get_weather

DB_PATH = "database/meetings.db"

def is_good_weather(condition: str):
    bad_weather = ["rain", "storm", "snow"]
    return not any(word in condition.lower() for word in bad_weather)


def schedule_meeting_if_possible(city: str):
    weather = get_weather(city)

    if not is_good_weather(weather["condition"]):
        return {
            "status": "rejected",
            "reason": "Bad weather",
            "weather": weather
        }

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    meeting_date = (date.today() + timedelta(days=1)).isoformat()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS meetings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            date TEXT,
            time TEXT,
            weather_status TEXT
        )
    """)

    cur.execute("SELECT * FROM meetings WHERE date=?", (meeting_date,))
    if cur.fetchone():
        conn.close()
        return {
            "status": "exists",
            "message": "Meeting already scheduled for tomorrow"
        }

    cur.execute(
        "INSERT INTO meetings (title, date, time, weather_status) VALUES (?, ?, ?, ?)",
        ("Team Meeting", meeting_date, "10:00 AM", "Good")
    )

    conn.commit()
    conn.close()

    return {
        "status": "created",
        "message": "Weather is good. Meeting scheduled.",
        "weather": weather
    }
