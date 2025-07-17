import psycopg2
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT


def connect_db():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    return conn


def insert_comment(brand_name, reddit_username, comment_text, sentiment):
    conn = connect_db()
    cur = None
    try:
        cur = conn.cursor()
        insert_query = """
        INSERT INTO brand_insights (brand_name, reddit_username, comment_text, sentiment)
        VALUES (%s, %s, %s, %s)
        """
        cur.execute(insert_query, (brand_name, reddit_username, comment_text, sentiment))
        conn.commit()
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()