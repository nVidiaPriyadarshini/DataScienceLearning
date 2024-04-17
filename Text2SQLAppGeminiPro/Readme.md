## Agenda

Text 2 SQL LLM Application

Prompt --> LLM --> GeminiPro --> Query --> SQLDatabase --> Response

Implementation

1. Sqlite --> Insert some records using Python programming

### Student database
This script ![sql.py](https://github.com/nVidiaPriyadarshini/DataScienceLearning/blob/main/Text2SQLAppGeminiPro/sql.py) creates a single student table with some records:
It stores student name, class, section and marks details

### EmployeeManagement Database
   The script ![Employeesql](https://github.com/nVidiaPriyadarshini/DataScienceLearning/blob/main/Text2SQLAppGeminiPro/employeesql.py)creates below four tables with some records :

**Departments**: Stores information about different departments in the company.
**Employees**: Stores information about employees, including their department ID, salary, and join date.
**Products**: Contains details of products, including their category and price.
**Sales**: Tracks sales transactions, including the product sold, quantity, and sale date.
Each table has its primary key, and appropriate foreign key constraints are added to maintain referential integrity. Adjust the data types and constraints as needed based on your specific requirements.
2. LLM Application --> Gemini Pro --> SQL Programming

# Command to run the app

```streamlit run app.py```

# Demo Screenshots

# Student Database UseCase
![Student db](https://github.com/nVidiaPriyadarshini/DataScienceLearning/blob/main/Text2SQLAppGeminiPro/assets/AverageMarksClassWise.png)

# EmployeeManagement UseCase

![EmployeeManagement db](https://github.com/nVidiaPriyadarshini/DataScienceLearning/blob/main/Text2SQLAppGeminiPro/assets/Highest_Paid_Employee.png)

# Product Sales UseCase
![Product_table](https://github.com/nVidiaPriyadarshini/DataScienceLearning/blob/main/Text2SQLAppGeminiPro/assets/Total_Revenue_by_category.png)

### Reference
![Google Gemini Crash Course](https://github.com/krishnaik06/Google-Gemini-Crash-Course/tree/main/sqlllm)

# About Me
Let’s connect at https://www.linkedin.com/in/vpnarayanan/ and exchange ideas about the latest tech trends and advancements! 🌟