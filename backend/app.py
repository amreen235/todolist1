from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Make sure to set a secret key for session management

# Database connection setup
def get_db_connection():
    conn = psycopg2.connect(
        dbname='postgres',  # Your database name
        user='postgres',        # Your PostgreSQL username
        password='amreen123',   # Your PostgreSQL password
        host='localhost',       # Your host (localhost if you're running locally)
        port='5432'             # Default PostgreSQL port
    )
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            # Store the user ID in the session
            session['user_id'] = user[0]  # Assuming 'user[0]' is the user ID from the database
            return redirect(url_for('todo'))  # Redirect to the todo page
        else:
            return 'Invalid credentials. Please try again.'
    return render_template('login.html', title='Login')  # Ensure CSS is linked in login.html

@app.route('/todo')
def todo():
    # Get the user_id from the session (assuming the user is logged in)
    user_id = session.get('user_id')

    if not user_id:
        return redirect(url_for('login'))  # Redirect to login if user is not logged in

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM todos WHERE user_id = %s', (user_id,))
    todos = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('todo.html', todos=todos)

@app.route('/logout')
def logout():
    session.clear()  # Clear the session
    return redirect(url_for('login'))  # Redirect to the login page

if __name__ == '__main__':
    app.run(debug=True)
