from flask import Flask, request
import env
import mysql.connector

app = Flask(__name__)

@app.route('/dbLogin', methods=['POST'])
def handle_post():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # get the credentials from the environment variables
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')

    # create a connection to the database
    cnx = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_name)

    # create a cursor object
    cursor = cnx.cursor()

    # create an INSERT INTO SQL query
    add_user = ("INSERT INTO users "
                "(username, email, password) "
                "VALUES (%s, %s, %s)")

    # data to insert
    data_user = (username, email, password)

    # execute the query
    cursor.execute(add_user, data_user)

    # commit the changes
    cnx.commit()

    # close the cursor and connection
    cursor.close()
    cnx.close()

    return '', 204



if __name__ == "__main__":
    app.run(debug=True, port=5501)