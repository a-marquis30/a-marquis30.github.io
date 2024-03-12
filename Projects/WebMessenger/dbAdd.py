import sys
from flask import Flask, request, jsonify
sys.path.append('/home/austinmarquis30/mysite') 
import env
import os
import MySQLdb
from flask_cors import CORS

appAdd = Flask(__name__)
CORS(appAdd)

@appAdd.route('/Add', methods=['POST'])
def handle_post():
    username = request.form.get('username')

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
            # TODO Add friend to current users firends list
            return
        return

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # close the cursor and connection
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    appAdd.run(debug=True)