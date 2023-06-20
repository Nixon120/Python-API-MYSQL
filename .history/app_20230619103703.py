from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__, static_url_path='/static')

# Configure MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'nixon'
app.config['MYSQL_PASSWORD'] = 'Maya100$'
app.config['MYSQL_DB'] = 'logging_db'

# Initialize MySQL
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html', show_video=False)


@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']

    try:
        # Insert the data into the MySQL database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO logs (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)",
                    (first_name, last_name, email, phone))
        mysql.connection.commit()
        cur.close()

        # Pass a variable to the template indicating that the video should be shown
        return render_template('index.html', show_video=True)
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return 'An error occurred during data submission.'


if __name__ == '__main__':
    app.run(debug=True)
