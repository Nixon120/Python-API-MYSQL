from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306  
app.config['MYSQL_USER'] = 'nixon'
app.config['MYSQL_PASSWORD'] = 'Maya100$'
app.config['MYSQL_DB'] = 'logging_db'

# Initialize MySQL
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    # Insert the data into the MySQL database
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (first_name, last_name) VALUES (%s, %s)", (first_name, last_name))
    mysql.connection.commit()
    cur.close()

    return 'Data submitted successfully!'


if __name__ == '__main__':
    app.run(debug=True)
