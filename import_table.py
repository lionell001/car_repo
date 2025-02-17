import pandas as pd
import pyodbc
import sqlalchemy
from sqlalchemy import create_engine

# con_string = 'jdbc:mysql://localhost:3306/employees'
con_string = 'mysql+pymysql://root:college@localhost/employees'
engine = create_engine(con_string)

query_employee= """SELECT emp_no, birth_date, first_name, last_name, gender, hire_date
FROM employees.employees
where birth_date>'1965-01-01'"""

query_employee_salaries = """SELECT *
FROM employees.salaries
where salary>130000"""

df_employee = pd.read_sql(query_employee, engine)

df_salaries = pd.read_sql(query_employee_salaries, engine)

df_employee_salary = pd.merge(df_employee, df_salaries, on = 'emp_no_test', how = 'inner')


print(sqlalchemy.__version__)