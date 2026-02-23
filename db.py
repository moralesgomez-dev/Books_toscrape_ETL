import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def create_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS books (
        id SERIAL PRIMARY KEY,
        title TEXT UNIQUE,
        price NUMERIC,
        availability BOOLEAN,
        rating INTEGER,
        loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()

def insert_books(conn, books):
    query = """
    INSERT INTO books (title, price, availability, rating)
    VALUES (%s, %s, %s, %s)
    """
    cur = conn.cursor()
    for book in books:
        cur.execute(query, (
            book["title"],
            book["price"],
            book["availability"],
            book["rating"]
        ))
    conn.commit()
    cur.close()