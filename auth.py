import sqlite3

DB_NAME = "user.db"


def register(username, password):
    conn = sqlite3.connect(DB_NAME)

    try:
        cursor = conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )

        user_id = cursor.lastrowid
        conn.commit()

        return user_id

    except sqlite3.IntegrityError:
        return None

    finally:
        conn.close()


def login(username, password):
    conn = sqlite3.connect(DB_NAME)

    user = conn.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    ).fetchone()

    conn.close()

    return user