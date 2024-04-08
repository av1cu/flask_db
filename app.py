import credentials_db
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

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


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)', (title, author, pages_num, review))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')