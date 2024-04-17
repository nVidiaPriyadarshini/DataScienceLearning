import sqlite3

# Connect to sqlite
connection = sqlite3.connect("EmployeeManagement.db")

# Create a cursor object to insert,create table, retrieve
cursor = connection.cursor()

# Create table
departments_table_info = """
CREATE TABLE Departments (
    DepartmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    DepartmentName VARCHAR(50) NOT NULL
);
"""

# Create table
employees_table_info = """
CREATE TABLE Employees (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DepartmentID INT,
    Salary DECIMAL(10, 2),
    JoinDate DATE,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
"""
#cursor.execute(departments_table_info)
cursor.execute(employees_table_info)

product_table_info = """
CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName VARCHAR(100) NOT NULL,
    Category VARCHAR(50) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL
);
"""
cursor.execute(product_table_info)

sales_table_info = """
CREATE TABLE Sales (
    SaleID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INT,
    Quantity INT,
    SaleDate DATE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
"""
# cursor.execute(sales_table_info)

user_feedback_table_info = """
CREATE TABLE user_feedback (
    "SQLGenerated"	VARCHAR(300),
	"DatabaseName"	VARCHAR(100),
	"Question"	VARCHAR(100),
	"User_feedback"	VARCHAR(300)
);
"""
#cursor.execute(user_feedback_table_info)

# Insert some more records

# cursor.execute('''INSERT INTO Departments (DepartmentName)
# VALUES ('HR'),
#        ('Finance'),
#        ('Marketing'),
#        ('Sales'),
#        ('IT');''')

cursor.execute('''INSERT INTO Employees (FirstName, LastName, DepartmentID, Salary, JoinDate)
VALUES ('John', 'Doe', 1, 60000.00, '2023-01-15'),
       ('Jane', 'Smith', 2, 70000.00, '2022-05-20'),
       ('Michael', 'Johnson', 3, 55000.00, '2024-02-10'),
       ('Emily', 'Williams', 4, 65000.00, '2021-11-28'),
       ('David', 'Brown', 5, 75000.00, '2023-09-03');''')

cursor.execute('''INSERT INTO Products (ProductName, Category, Price)
VALUES ('Laptop', 'Electronics', 1200.00),
       ('Smartphone', 'Electronics', 800.00),
       ('Office Chair', 'Furniture', 150.00),
       ('Desk Lamp', 'Home Decor', 30.00),
       ('Coffee Maker', 'Appliances', 50.00);''')

cursor.execute('''INSERT INTO Sales (ProductID, Quantity, SaleDate)
VALUES (1, 5, '2024-04-01'),
       (2, 8, '2024-04-05'),
       (3, 3, '2024-04-10'),
       (4, 10, '2024-04-15'),
       (5, 6, '2024-04-20');''')

# Display all the records
print("The inserted records are")

data = cursor.execute('''Select * from Departments''')

for row in data:
    print(row)

data = cursor.execute('''Select * from Employees''')

for row in data:
    print(row)

data = cursor.execute('''Select * from Products''')

for row in data:
    print(row)

data = cursor.execute('''Select * from Sales''')

for row in data:
    print(row)
# Close the connection
connection.commit()
connection.close()

