import psycopg2
import credentials_db

conn = psycopg2.connect(
        host=credentials_db.credentials_db['host'],
        database=credentials_db.credentials_db['database'],
        user=credentials_db.credentials_db['user'],
        password=credentials_db.credentials_db['password'])

cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS books;')
cursor.execute(
    '''
    CREATE TABLE books (id serial PRIMARY KEY,
    title varchar (150) NOT NULL,
    author varchar (50) NOT NULL,
    pages_num integer NOT NULL,
    review text,
    date_added date DEFAULT CURRENT_TIMESTAMP);
    '''
)

cursor.execute(
    '''
    INSERT INTO books (title, author, pages_num, review)
    VALUES (%s, %s, %s, %s)
    ''',
    ('A Tale of Two Cities',
     'Charles Dickens',
     489,
     'A great classic!')
)

cursor.execute(
    '''
    INSERT INTO books (title, author, pages_num, review)
    VALUES (%s, %s, %s, %s)
    ''',
    ('Anna Karenina',
     'Leo Tolstoy',
     864,
     'Another great classic!')
)

conn.commit()

cursor.close()
conn.close()
