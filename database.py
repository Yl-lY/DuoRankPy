from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

def connect_db():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        sslmode="require"
    )

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS competitors (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            avatar_url TEXT NOT NULL,
            display_name TEXT NOT NULL,
            language TEXT NOT NULL,
            xp INT NOT NULL
        );
    """)
    
    conn.commit()
    conn.close()