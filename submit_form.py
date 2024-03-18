import mysql.connector
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

db_host = 'localhost'
db_user = 'admin'
db_password = 'saiisking1'
db_name = 'atm_db'

db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

@app.route('/', methods=['GET', 'POST'])
def atm_interface():
    if request.method == 'POST':
        account = request.form['account']
        pin = request.form['pin']

        cursor = db.cursor()
        insert_query = "INSERT INTO atm_data (account_number, pin) VALUES (%s, %s)"
        cursor.execute(insert_query, (account, pin))
        db.commit()  
        cursor.close()

        return redirect(url_for('success'))



@app.route('/success')
def success():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM atm_data")
    data = cursor.fetchall()
    cursor.close()

    return f"Data inserted successfully! Current data in database: {data}"

if __name__ == '__main__':
    app.run(debug=True)
