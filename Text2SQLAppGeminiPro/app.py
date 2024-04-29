from dotenv import load_dotenv

load_dotenv()  # load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure our api key
# Create a file .env with GOOGLE_API_KEY="[GOOGLE_API_KEY]"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to load Google Gemini Model and provide query as response
def get_gemini_response(question, prompt, selected_db):
    model = genai.GenerativeModel('gemini-pro')

    selected_prompt = prompt[0]
    if selected_db == "Student":
        selected_prompt = prompt[1]
    print("User chosen prompt" + selected_prompt)
    query_response = model.generate_content([selected_prompt, question])
    gen_sql = query_response.parts[0].text
    return gen_sql


# Function to retrieve query from the sql database
def write_user_feedback(sql, db):
    selected_db = db + ".db"
    print("Connecting db: " + selected_db)
    # Connect to sqlite
    connection = sqlite3.connect(selected_db)

    # Create a cursor object to insert,create table, retrieve
    cursor = connection.cursor()
    # Execute query
    print("Executing query: " + sql)
    cursor.execute(sql)
    connection.commit()
    connection.close()


def read_sql_query_secrets_file(sql_query, db):
    # Create the SQL connection to db as specified in your secrets file.
    conn = st.connection(db, type='sql')
    with conn.session as s:
        s.execute(sql_query)
        rows = s.execute('Select * from ' + db)
        st.dataframe(rows)


def read_given_sql_query(sql, db):
    query_db = db + ".db"
    print("Querying db: " + query_db)
    with sqlite3.connect(query_db) as db:
        cursor = db.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    db.commit()
    db.close()
    return rows


# Define the prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name EmployeeManagement 
    \n\nFor example,\nExample 1 - What is the total number of employees in the "Employees" table?, 
    the SQL command will be something like this SELECT COUNT(*) AS TotalEmployees FROM Employees;
    \nExample 2 - Tell the names of all employees who have a salary greater than $50,000?, 
    the SQL command will be something like this SELECT FirstName, LastName FROM Employees 
    WHERE Salary > 50000.00;
    \nExample 3 - List the departments along with the number of employees in each department?
    the SQL command will be something like this SELECT d.DepartmentName, COUNT(e.EmployeeID) AS 
    NumberOfEmployees FROM Departments d LEFT JOIN Employees e ON d.DepartmentID = e.DepartmentID
    GROUP BY d.DepartmentName;
    \nExample 4 - Find the average salary of employees in the "Sales" department?
    the SQL command will be something like this SELECT AVG(e.Salary) AS AverageSalary
    FROM Employees e JOIN Departments d ON e.DepartmentID = d.DepartmentID
    WHERE d.DepartmentName = 'Sales';
    \nExample 5 - Identify the employee with the highest salary?
    the SQL command will be something like this SELECT * FROM Employees WHERE 
    Salary = (SELECT MAX(Salary) FROM Employees);
    \nExample 6 - List the employees who joined the company in the year 2022?
    the SQL command will be something like this SELECT *
    FROM Employees WHERE strftime('%Y', JoinDate) = '2022';
    \nExample 7 - Determine the number of employees who have been with the company for 
    more than 5 years?
    the SQL command will be something like this SELECT COUNT(*) AS num_employees
    FROM employees WHERE (julianday('now') - julianday(JoinDate)) / 365 > 5;
    \nExample 8 - Calculate the total revenue generated by each product category?
    the SQL command will be something like this SELECT p.Category, SUM(s.Quantity * p.Price) 
    AS TotalRevenue FROM Products p JOIN Sales s ON p.ProductID = s.ProductID GROUP BY p.Category;
    \nExample 9 - Find the top 5 best-selling products?
    the SQL command will be something like this SELECT p.ProductID, p.ProductName, p.Category, 
    SUM(s.Quantity) AS TotalQuantitySold FROM Products p JOIN Sales s ON p.ProductID = s.ProductID
    GROUP BY p.ProductID, p.ProductName, p.Category ORDER BY TotalQuantitySold DESC LIMIT 5;
    \nExample 10 - List the employees who have not been assigned to any department?
    the SQL command will be something like this SELECT e.EmployeeID, e.FirstName, e.LastName
    FROM Employees e LEFT JOIN Departments d ON e.DepartmentID = d.DepartmentID WHERE 
    d.DepartmentID IS NULL;
    also the sql code should not have ``` in beginning or end and sql word in output
    """,
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

# StreamLit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data across multiple databases")

# List of options for the select box
db_options = ['EmployeeManagement', 'Student']

# Create a select box
selected_db = st.selectbox('Select a database option:', db_options)

# Display the selected option
st.write('You selected:', selected_db)

question = st.text_input("Input Natural Language Text: ", key="input")

submit = st.button("Search")
st.divider()
gen_sql = ""
# if submit is clicked
if submit:
    gen_sql = get_gemini_response(question, prompt, selected_db)
    st.subheader("Generated sql: ", divider='rainbow')
    st.code(gen_sql, language='sql')
    sub_header_text = "The Answer to: " + question
    st.subheader(sub_header_text, divider='rainbow')

    response = read_given_sql_query(gen_sql, selected_db)
    #response = read_sql_query_secrets_file(gen_sql, selected_db)
    for row in response:
        print(row)
        st.header(row)
    #insert_sql = ("Insert into User_feedback values(" + "'" + gen_sql + "'," + "'"
                  #+ selected_db + "'," + "'" + question + "', \"no_comments\")")
    #st.code(insert_sql, language='sql')
    #write_user_feedback(insert_sql, selected_db)
user_comments = st.text_area("Kindly let us know your feedback if any")
feedback = st.button("Submit Feedback!")

if feedback:
    #insert_sql = "Insert into User_feedback values('" + user_comments + "'," + "'" + selected_db + "'," + "'" + question + "',\"Not Applicable\");"
    #st.code(insert_sql, language='sql')
    st.subheader("':sunglasses:' Thank you!!':sunglasses:'", divider='rainbow')
    #write_user_feedback(insert_sql, selected_db)


