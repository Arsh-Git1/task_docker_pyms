# app.py

import sqlite3
from flask import Flask, jsonify

# Initialize Flask application
app = Flask(__name__)

# SQLite database configuration
DATABASE = '/app/data.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    print("Opened database successfully")
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        );
    ''')
    print("Table created successfully")
    conn.close()

@app.route('/')
def index():
    return "Welcome to the Dockerized Flask with SQLite!"

if __name__ == '__main__':
    # Initialize the SQLite database
    init_db()
    
    # Run the Flask application
    app.run(host='0.0.0.0', port=3000)
