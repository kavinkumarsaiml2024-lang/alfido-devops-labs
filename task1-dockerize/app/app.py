from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")


def get_db():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )


@app.route("/")
def home():
    return jsonify({"message": "Hello from Dockerized Flask App! (updated)"})


@app.route("/users")
def users():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT
        )
    """)
    cur.execute("INSERT INTO users (name) VALUES ('Docker User')")
    conn.commit()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(rows)


if __name__ == "__main__":
    # debug=True enables the built-in reloader for development
    app.run(host="0.0.0.0", port=5000, debug=True)






