from flask import Flask, render_template, request, redirect, url_for, session, flash
import psycopg2
import datetime  # Import the datetime module

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Database connection function
def get_db_connection():
    return psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='amreen123',
        host='localhost',
        port='5432'
    )

# Homepage
@app.route('/')
def home():
    return render_template('index.html', title='Home')

# Login
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
            session['user_id'] = user[0]  # Assuming ID is at index 0
            return redirect(url_for('todo'))
        else:
            return render_template('login.html', title='Login', error='Invalid credentials. Please try again.')

    return render_template('login.html', title='Login')

# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        # Validation
        if not username or not password or not first_name or not last_name or not email:
            error = "All fields are required."
        elif '@' not in email:
            error = "Invalid email format."
        else:
            conn = get_db_connection()
            cur = conn.cursor()

            # Check if username already exists
            cur.execute('SELECT * FROM users WHERE username = %s', (username,))
            existing_user = cur.fetchone()

            if existing_user:
                error = "Username already exists. Please choose a different username."
            else:
                # Insert new user into the database
                try:
                    cur.execute(
                        'INSERT INTO users (username, password, first_name, last_name, email) VALUES (%s, %s, %s, %s, %s)',
                        (username, password, first_name, last_name, email)
                    )
                    conn.commit()
                    flash('Signup successful! Please update your profile.', 'success')
                    # user_id = session.get('user_id')
                    return redirect(url_for('profile'))
                except Exception as e:
                    conn.rollback()
                    error = f"Database error: {str(e)}"

            cur.close()
            conn.close()

    return render_template('signup.html', title='Signup', error=error)

# To-Do Page
@app.route('/todo')
def todo():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM todos WHERE user_id = %s ORDER BY id DESC', (user_id,))
    todos = cur.fetchall()
    cur.close()
    conn.close()

    # Convert the date string to a datetime object
    formatted_todos = []
    for todo in todos:
        date_object = None  # Initialize date_object to None
        if todo[2]:  # Check if todo[2] is not None
            try:
                # Assuming todo[2] is the date string in 'YYYY-MM-DD HH:MM:SS.SSSSSS' format
                date_object = datetime.datetime.strptime(str(todo[2]), '%Y-%m-%d %H:%M:%S.%f')  # Adjust format if needed
            except ValueError:
                pass  # If the date is invalid, date_object remains None

        formatted_todos.append((todo[0], todo[1], date_object, todo[3], todo[4]))

    return render_template('todo.html', todos=formatted_todos, title='Your Tasks')

# Add a new task
@app.route('/add-task', methods=['GET', 'POST'])
def add_task():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    if request.method == 'POST':
        description = request.form['description']
        status = request.form['status']

        print("DESCRIPTION RECEIVED:", description)

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO todos (user_id, is_completed, description) VALUES (%s, %s, %s)',
            (user_id, status == 'Completed', description)
        )
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('todo'))

    return render_template('add_task.html', title='Add Task')

# Mark task as completed
@app.route('/mark_completed/<int:task_id>', methods=['POST'])
def mark_completed(task_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE todos SET is_completed = TRUE WHERE id = %s AND user_id = %s', (task_id, user_id))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('todo'))

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Coming Soon Placeholders
@app.route('/completed-tasks')
def completed_tasks():
    return 'Completed Tasks Page (coming soon)'

# Profile Page
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cur = conn.cursor()

    # Fetch user data for display
    cur.execute('SELECT username, first_name, last_name, dob, phone_no, email, password FROM users WHERE id = %s', (user_id,))
    user = cur.fetchone()

    if not user:
        cur.close()
        conn.close()
        return "User not found", 404

    username, first_name, last_name, dob, phone_no, email, password_hash = user
    error = None

    if request.method == 'POST':
        if 'update_profile' in request.form:
            # Handle profile information update
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            dob = request.form.get('dob')
            phone_no = request.form.get('phone_no')
            email = request.form.get('email')

            # Validation
            if not first_name or not last_name or not email:
                error = "First Name, Last Name, and Email are required."
            elif '@' not in email:
                error = "Invalid email format."
            elif phone_no and len(phone_no) != 10:
                error = "Phone number must be 10 digits."
            else:
                # Update user information in the database
                try:
                    cur.execute(
                        'UPDATE users SET first_name = %s, last_name = %s, dob = %s, phone_no = %s, email = %s WHERE id = %s',
                        (first_name, last_name, dob, phone_no, email, user_id)
                    )
                    conn.commit()
                    flash('Profile updated successfully!', 'success')
                except Exception as e:
                    conn.rollback()
                    error = f"Database error: {str(e)}"

        elif 'update_password' in request.form:
            # Handle password update
            current_password = request.form.get('current_password')
            new_password = request.form.get('new_password')

            # Validate current password
            if current_password:
                cur.execute('SELECT password FROM users WHERE id = %s', (user_id,))
                user_password = cur.fetchone()
                if user_password:
                    if current_password == password_hash:
                        # Update password
                        if new_password:
                            cur.execute('UPDATE users SET password = %s WHERE id = %s', (new_password, user_id))
                            conn.commit()
                            flash('Password updated successfully!', 'success')
                        else:
                            error = "New password cannot be empty."
                    else:
                        error = "Incorrect current password."
                else:
                    error = "User not found."
            else:
                error = "Current password is required."

    cur.close()
    conn.close()

    return render_template(
        'profile.html',
        username=username,
        first_name=first_name,
        last_name=last_name,
        dob=dob,
        phone_no=phone_no,
        email=email,
        error=error,
        title='Profile'
    )

if __name__ == '__main__':
    app.run(debug=True)
