"""
A module for interacting with the SQL database.
"""
import sqlite3


def get_greeting_db():
    """
    Connects to the database and returns a greeting.

    Returns:
        string: A greeting.
    """
    conn = sqlite3.connect("hello_world.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM greeting")
    greeting = cursor.fetchone()
    conn.close()
    return greeting
