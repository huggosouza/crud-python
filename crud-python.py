from errno import errorcode
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
                    )
                    """
                )
                
            except mysql.connector.Error as err:
                if "1050" in str(err):
                    print("The table already exists, continuing.")
                    pass
                else:
                    print(err)
                    
                
    
Crud.mountDB()

