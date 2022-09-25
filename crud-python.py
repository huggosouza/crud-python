# † J.M.J
# Author: Hugo Souza
# Date: 09/13/2022

import mysql.connector

# Connecting to database and checking if necessary table already exists, if not, it'll create it
class Crud():
    connection = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'crud_python',
    )
    
    cursor = connection.cursor()
    
    if connection.is_closed() == True:
        print("The connection is closed.")
    else:
        print("The connection is sucessfully established :)!")
        

    def mountDB():
            # Tries to use the database, if it doesn't exists, it'll create it.
            try:
                Crud.cursor.execute("USE crud_python")
            # Raises the exception and tries to created the db
            except mysql.connector.Error as err:
                print(err)
                # Prints the error if can't create the database.
                try:
                    Crud.cursor.execute(
                        "CREATE DATABASE crud_python DEFAULT CHARACTER SET 'utf8';"
                    )
                    print("Database crud_python created!")
                except mysql.connector.Error as err:
                    print(err)
                    
            # Now with the db already created, it tries to create the table and its rows.
            try:
                Crud.cursor.execute(
                    """CREATE TABLE employees (
                        user_ID int NOT NULL AUTO_INCREMENT,
                        first_name varchar(15) NOT NULL,
                        last_name varchar(15) NOT NULL,
                        age int,
                        PRIMARY KEY (user_ID)
                    );
                    """
                )
                
            except mysql.connector.Error as err:
                if "1050" in str(err):
                    print("The table already exists, continuing.")
                    pass
                else:
                    print(err)
                    
    def fetchUsers():
        try:
            listUsers = []
            Crud.cursor.execute("SELECT * FROM employees;")
            fetch = Crud.cursor.fetchall()
            for i in fetch:
                print(f"ID: {i[0]}\nFirst name: {i[1]}\nLast name: {i[2]}\nAge: {i[3]}\n---------")
        except mysql.connector.Error as err:
            print(err)
            
    def addUser(fname, lname, agee):
        try:
            query = f"""INSERT INTO employees(first_name, last_name, age) VALUES ('{fname}', '{lname}', {agee});
                    """
            Crud.cursor.execute(query)
            Crud.connection.commit()
        except mysql.connector.Error as err:
            print(err)
    def removeUser(userID):
        try:
            cmd = f"""DELETE FROM employees WHERE user_ID = {userID};
                    """
            Crud.cursor.execute(cmd)
            Crud.connection.commit()
        except mysql.connector.Error as err:
            print(err)

def menu():
    print("""------------- MENU -------------            
             1 - Show all employees
             2 - Add new employee
             3 - Remove an employee
             4 - Edit an existing employee 
             5 - Look for an employee by name
             6 - Look for an employee by ID""")
    choice = int(input(": "))
    # Show all employees
    if choice == 1:
        Crud.fetchUsers()
        menu()
    # Add new employee
    elif choice == 2:
        Crud.addUser(fname = input("First name: ", lname = input("Last name: "), age = input("Age: ")))
        menu()
    # Remove an employee
    elif choice == 3:
        Crud.removeUser(input("Type the user ID: "))
        menu()
    # Edit an existing employee
    elif choice == 4:
        menu()
    # Look for an employee by name
    elif choice == 5:
        menu()
    # Look by ID
    elif choice == 6:
        menu()
    else:
        print("This entry doesn't exists!")
        menu()
        
menu()