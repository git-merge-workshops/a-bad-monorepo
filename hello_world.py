"""
This module contains a function that prints a greeting.
"""
# import db module
import hello_world_db as db

if __name__ == "__main__":
    # Load the database
    db.load_db()
    # Print the greeting
    print(db.get_greeting_db())
