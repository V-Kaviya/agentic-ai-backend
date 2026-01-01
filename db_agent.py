import sqlite3
from datetime import date, timedelta
import os

DB_FOLDER = "database"
DB_PATH = os.path.join(DB_FOLDER, "meetings.db")


def get_connection():
    # Create database folder if it doesn't exist
    os.makedirs(DB_FOLDER, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def query_meetings(question: str):
    conn = get_connection()
    cur = conn.cursor()

    # Create table if not exists (safe)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS meetings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            date TEXT
        )
    """)

    if "today" in question.lower():
        d = date.today().isoformat()
        cur.execute("SELECT * FROM meetings WHERE date=?", (d,))
    elif "tomorrow" in question.lower():
        d = (date.today() + timedelta(days=1)).isoformat()
        cur.execute("SELECT * FROM meetings WHERE date=?", (d,))
    else:
        cur.execute("SELECT * FROM meetings")

    results = cur.fetchall()
    conn.close()

    return {
        "count": len(results),
        "meetings": results
    }