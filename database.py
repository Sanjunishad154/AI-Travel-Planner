import sqlite3

def init_db():
    conn = sqlite3.connect("travel.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS trips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        budget INTEGER,
        days INTEGER,
        interest TEXT,
        travel_style TEXT,
        itinerary TEXT
    )
    """)

    conn.commit()
    conn.close()
