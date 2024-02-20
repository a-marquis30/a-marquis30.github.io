import sys
from flask import Flask, request, jsonify
sys.path.append('/home/austinmarquis30/mysite') 
import env
import os
import MySQLdb
from flask_cors import CORS

appLogin = Flask(__name__)
CORS(appLogin)

@appLogin.route('/Login', methods=['POST'])
def handle_post():
    username = request.form.get('username')
    email = request.form.get('username')
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
        # Check if username and password match
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        if user:
            return jsonify({'message': 'Login successful', 'username': user['username']}), 200
        
        # Check if email and password match
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        if user:
            return jsonify({'message': 'Login successful', 'username': user['username']}), 200

        return jsonify({'error': 'Invalid username/email or password'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # close the cursor and connection
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    appLogin.run(debug=True)