import sqlite3

try:
    conn = sqlite3.connect('sample.db')
except:
    print("Failed to connect to db")
else:
    print("Connected to database")

#SQL - structured query language

#create a new table
cursor = conn.cursor()

def createTables():
    command = """
        CREATE TABLE IF NOT EXISTS TABLE1
        (id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
        )
    """
    try:
        cursor.execute(command)
    except:
        print("Table already exists")
    else:
        print("SQL PERFORMED SUCCESSFULLY")
        conn.commit()

#CRUD - CREATE, RETRIEVE, UPDATE, DELETE
def insertRecord(name, age):
    sqlString = """
        INSERT INTO students (name, age)
        VALUES (?,?)
    """
    cursor.execute(sqlString, (name, age))
    print("Inserted successfully.")
    conn.commit()

def retrieveRecord(id=None):
    sqlString = """
        SELECT * FROM students
    """
    if id is not None:
        sqlString += f" WHERE id = {id}"

    cursor.execute(sqlString)
    print("Retrieved successfully.")
    
    rows = cursor.fetchall()
    return rows

def updateRecord(name, age, id):
    sqlString = """
        UPDATE students SET name = ?, age = ? WHERE id = ?
    """
    cursor.execute(sqlString, (name, age, id))
    print("update successfully.")
    conn.commit()

def deleteRecord(id):
    sqlString = """
        DELETE FROM students WHERE id = ?
    """
    cursor.execute(sqlString, (id,))
    print("deleted successfully.")
    conn.commit()


deleteRecord(1)