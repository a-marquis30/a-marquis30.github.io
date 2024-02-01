from flask import Flask

app = Flask(__name__)

@app.route('/call_python_function', methods=['GET','POST'])
def call_python_function(): # Call your Python function here
    return f'TEST'

if __name__ == '__main__':
    app.run(debug=True, port=5501)
