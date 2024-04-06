import credentials_db
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host=credentials_db.credentials_db['host'],
        database=credentials_db.credentials_db['database'],
        user=credentials_db.credentials_db['user'],
        password=credentials_db.credentials_db['password']
    )

    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books;')
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', books=books)