import sys
from flask import Flask, request, jsonify
sys.path.append('/home/austinmarquis30/mysite') 
import env
import os
import MySQLdb
from flask_cors import CORS

appSignUp = Flask(__name__)
CORS(appSignUp)

@appSignUp.route('/SignUp', methods=['POST'])
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
    cnx = MySQLdb.connect(
        host = db_host,
        user = db_user,
        password = db_password,
        database = db_name
    )


    # create a cursor object
    cursor = cnx.cursor()

    try:
        # Check if username already exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_username = cursor.fetchone()
        if existing_username:
            return jsonify({'error': 'Username already exists!'}), 400

        # Check if email exists
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_email = cursor.fetchone()
        if existing_email:
            return jsonify({'error': 'Email already exists!'}), 400

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

        return jsonify({'message': 'User successfully added'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # close the cursor and connection
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    appSignUp.run(debug=True)