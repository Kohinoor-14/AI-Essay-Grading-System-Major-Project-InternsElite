import sqlite3
import pandas as pd

DB_PATH = "database/essays.db"


def create_database():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS essays (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT,
        essay_topic TEXT,
        grade_level TEXT,
        essay_text TEXT,
        overall_score REAL,
        grammar_score REAL,
        vocabulary_score REAL,
        readability_score REAL,
        topic_score REAL,
        plagiarism_score REAL,
        word_count INTEGER,
        sentence_count INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_essay(
        student_name,
        essay_topic,
        grade_level,
        essay_text,
        result):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO essays(
        student_name,
        essay_topic,
        grade_level,
        essay_text,
        overall_score,
        grammar_score,
        vocabulary_score,
        readability_score,
        topic_score,
        plagiarism_score,
        word_count,
        sentence_count
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        student_name,
        essay_topic,
        grade_level,
        essay_text,

        result["overall_score"],
        result["grammar_score"],
        result["vocabulary_score"],
        result["readability_score"],
        result["topic_score"],
        result["plagiarism_score"],
        result["word_count"],
        result["sentence_count"]

    ))

    conn.commit()
    conn.close()


def get_all_records():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM essays ORDER BY created_at DESC",
        conn
    )

    conn.close()

    return df


def get_previous_essays():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT essay_text
    FROM essays
    """)

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows if row[0]]