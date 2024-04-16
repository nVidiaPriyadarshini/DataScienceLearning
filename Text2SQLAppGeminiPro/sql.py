import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert,create table, retrieve
cursor = connection.cursor()

# Create table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

# Insert some more records
cursor.execute('''Insert into STUDENT values('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''Insert into STUDENT values('Vidya', 'Data Science', 'A', 100)''')
cursor.execute('''Insert into STUDENT values('Madhu', 'MLOps', 'B', 80)''')
cursor.execute('''Insert into STUDENT values('Sudha', 'Data Science', 'B', 88)''')
cursor.execute('''Insert into STUDENT values('Vikram', 'MLOps', 'A', 92)''')

# Display all the records
print("The inserted records are")

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()
