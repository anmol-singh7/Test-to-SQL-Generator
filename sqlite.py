import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert records, create table
cursor = connection.cursor()

# Create the table if it doesn't already exist
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25)
)
"""
cursor.execute(table_info)

# Insert initial data
cursor.execute("""INSERT INTO STUDENT VALUES ("Krish", "Data Science", "A")""")

# Additional dummy data
students = [
    ("John", "Mathematics", "B"),
    ("Alice", "Physics", "A"),
    ("Mike", "Chemistry", "C"),
    ("Sophia", "Biology", "A"),
    ("Emma", "Computer Science", "B"),
    ("Liam", "Statistics", "C"),
    ("Olivia", "Engineering", "A"),
    ("Noah", "Data Science", "B"),
    ("Ava", "Mathematics", "C"),
    ("William", "Physics", "A"),
]

# Insert additional records into the STUDENT table
cursor.executemany("INSERT INTO STUDENT VALUES (?, ?, ?)", students)



print("Data inserted successfully.")

data = cursor.execute("""Select * from STUDENT""")

for row in data:
    print(row)