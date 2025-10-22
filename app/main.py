from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import psycopg2




conn = psycopg2.connect(
    host="db",
    database="postgres",
    user="postgres",
    password="saksham04"
)
cursor = conn.cursor()
cursor.execute("SELECT version();")
print("Connected to:",cursor.fetchone())
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
""")
conn.commit()


app = FastAPI()

class Note(BaseModel):
    title: str
    content: str

@app.get("/")
def home():
    return {"message": "Welcome to Saksham's first API 🚀"}

@app.get("/hello/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/weather")
def weather(city:str,unit: str = "celcius"):
    return {
        "city":city,
        "unit":unit,
        "message":f"Weather for {city} is {unit}"
    }


notes_db = []



@app.post("/notes")
def create_note(note : Note):
    cursor.execute(
        "INSERT INTO notes (title, content) VALUES (%s, %s)",
        (note.title,note.content)
    )
    conn.commit()

    # notes_db.append(note)
    return{
        "Message":"Note created successfully",
        # "title":note.title,
        # "content":note.content
        # "Total Notes":len(notes_db)
    }



@app.get("/notes")
def get_notes():
    cursor.execute(
        "SELECT * FROM notes"
    )
    rows = cursor.fetchall()
    return [{"id":row[0], "title":row[1], "content":row[2]} for row in rows]

# @app.put("/notes/{note_id}")
# def update_notes(note_id :int,update_note:Note):
#     if note_id-1>=len(notes_db) or note_id < 0:
#         raise HTTPException(status_code=404,detail="Note not found")
#     notes_db [note_id-1]= update_note
#     return {"message":"Notes updated"}