import sqlite3

# Connect to the database (create it if it doesn't exist)
conn = sqlite3.connect('testdb.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL statement
cursor.execute('''CREATE TABLE IF NOT EXISTS knowledge (id INTEGER PRIMARY KEY, topic TEXT, other TEXT)''')


def create(conn, topic, other):
    """Insert a new record into the table"""
    command = "INSERT INTO knowledge (topic, other) VALUES (?, ?)"
    cursor.execute(command, (topic, other))
    conn.commit()
    conn.close()


def read(conn):
    """Retrieve all records from the table"""
    cursor.execute("SELECT * FROM knowledge")
    rows = cursor.fetchall()
    return rows




if __name__ == '__main__':
    print(read(conn))
