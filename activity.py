from flask import Flask, render_template
import mysql.connector

app = Flask(__name__, template_folder='template')

# MySQL connection configuration


@app.route('/')
def index():
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        port=3306,
        password="root",
        database="c361"
    )
    cursor = connection.cursor()

    # Retrieve data from the table
    create_table_query = """CREATE TABLE if not exists Activity(id int auto_increment primary key , first_name varchar(255), last_name varchar(255), phone_number int)"""
    cursor.execute(create_table_query)
    print("Table created successfully")

    insert_query = "INSERT INTO Activity (first_name, last_name, phone_number) VALUES (%s,%s,%s)"
    tdata = [("Bharathi","G", 12345), ("Astha","Astha", 11111), ("Avani","Ch", 43233)]
    cursor.executemany(insert_query, tdata)
    
    cursor.execute("SELECT * FROM Activity")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

    # Close the database connection
    cursor.close()
    connection.close()
    return  render_template('table.html', data=myresult)


if __name__ == '__main__':
    app.run()