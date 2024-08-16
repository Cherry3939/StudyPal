from flask import Flask, render_template, url_for, request, session, redirect, jsonify
from datetime import date
import sqlite3
import csv

# im so happy javascipt isnt in the syllabus why is it so hard

app = Flask(__name__)
app.secret_key = 'abcd'

def get_db_connection():
    conn = sqlite3.connect('account_details.db') 
    conn.row_factory = sqlite3.Row # returns rows from db as row objects, allows column access by name
    return conn

@app.route('/', methods=['POST', 'GET'])
def index():
    error_message = ""
    if request.method == 'POST':
        action = request.form.get('action')
        if action == "Login":
            username = request.form.get('username')
            password = request.form.get('password')
        
            conn = get_db_connection() # start connection
            cursor = conn.execute('SELECT * FROM userpassword WHERE username = ?', (username, )).fetchone()
            conn.commit()
            conn.close() 

            if cursor and cursor['password'] == password:
                session['username'] = username  # Store username in session so you don't lose it later
                return redirect(url_for('home', username=username))
            else:
                error_message = "Incorrect username/password. Please try again."  # this will show up as a pop up

        if action == "Register":
            return redirect(url_for("register"))
    return render_template('index.html', error_message=error_message)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = sqlite3.connect("account_details.db")
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO userpassword (username, password) VALUES (?, ?)''', (username, password))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))    
    return render_template('register.html')

@app.route('/home', methods=['POST', 'GET'])
def home():
    username = session.get('username')  # Get username from session not request so it won't disappear when you go back to home from a page that isn't login
    if not username:
        return redirect(url_for('index'))  # Redirect to login if no session found
    today = date.today()
    total_min = 0
    tasks = []
    try:
        with open('study_log.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row[1] = int(row[1]) if row[1].isdigit() else 0
                tasks.append(row)

        for task in tasks:
            total_min += task[1]
        total_hr = total_min // 60
        display_min = total_min % 60
        display_time = f"{total_hr }:{display_min:02d}"
    except FileNotFoundError:
        return "No records found"
    return render_template('home.html', today=today, username=username, display_time=display_time)

@app.route('/calendar', methods=['POST', 'GET'])
def calendar():
    return render_template('calendar.html')

@app.route('/study', methods=['POST', 'GET'])
def study():
    title = request.form.get('title')
    duration = request.form.get('duration')
    subject = request.form.get('subject')
    
    # file closes after with block
    if title and duration and subject:
        with open('study_log.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, duration, subject])
    
    return render_template('study.html', title=title, duration=duration, subject=subject)

@app.route('/overview', methods=["GET", "POST"])
def overview():
    tasks = []
    total_min = 0
    target = session.get('target', None)

    try:
        with open('study_log.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row[1] = int(row[1]) if row[1].isdigit() else 0
                tasks.append(row)

        for task in tasks:
            total_min += task[1]
        total_hr = round(total_min / 60, 2)
    except FileNotFoundError:
        return "No records found"

    if request.method == "POST":
        target = request.form.get("target")
        session['target'] = target
        
    return render_template('overview.html', tasks=tasks, target=target, total_hr=total_hr)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

@app.route('/grades', methods=["GET", "POST"])
def grades():
    grade_logs = []
    grade = ""
    rp = ""
    h2_rp_dict = {"A": 20, "B": 17.5, "C": 15, "D": 12.5, "E": 10, "S": 5, "U": 0}
    h1_rp_dict = {"A": 10, "B": 8.75, "C": 7.5, "D": 6.25, "E": 5, "S": 2.5, "U": 0}
    if request.method == "POST":
        action = request.form.get('action')
        if action == "Submit":
            test_subject = request.form.get("subject")
            exam = request.form.get("exam")
            grade = request.form.get("grade")
            percentage = request.form.get("percent")
            rp = request.form.get("rp")

            # file closes after with block
            with open("grade_log.csv", "a",) as file:
                writer = csv.writer(file)
                writer.writerow([test_subject, exam, grade, percentage, rp])

        if action == "Calculate":
            marks = int(request.form.get("marks"))
            h_level = request.form.get("h_level")
            if marks >= 70:
                grade = "A"
            elif 70 > marks >= 60:
                grade = "B" 
            elif 60 > marks >= 55:
                grade = "C"
            elif 55 > marks >= 50:
                grade = "D"
            elif 50 > marks >= 45:
                grade = "E"
            elif 45 > marks >= 40:
                grade = "S"
            elif marks < 40:
                grade = "U"
            if h_level == "h2":
                rp = h2_rp_dict[grade]
            elif h_level == "h1":
                rp = h1_rp_dict[grade]
        
        # file closes after with block
        with open("grade_log.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                grade_logs.append(row)
                
    return render_template('grades.html', grade_logs=grade_logs, grade=grade, rp=rp)

@app.route('/venue')
def venue():
    return render_template('venue.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')