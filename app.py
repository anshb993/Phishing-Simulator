from flask import Flask, render_template, request, redirect, session
from datetime import datetime
from email_templates import EMAILS #imports the file
from risk_engine import calculations

app = Flask(__name__)
app.secret_key = "dev-secret-key"

def init_session():
    if "behaviour" not in session:
        session["behaviour"] = []

LOGS = []
@app.route('/')
def main():
    return render_template('index.html', emails=EMAILS)

@app.route('/email/<int:email_id>')
def viewEmail(email_id):
    init_session()

    email = next((e for e in EMAILS if e["id"] == email_id), None)
    session["behaviour"].append("Email")
    risk = calculations(session["behaviour"], LOGS)
    print("current risk: ", risk)

    return render_template('email.html', email=email)

@app.route('/notice')
def message():
    init_session()

    entered_email = session.get("entered_email")
    session["behaviour"].append("Phished")
    risk = calculations(session["behaviour"], LOGS)
    print("current risk: ", risk)

    return render_template('notice.html', entered_email=entered_email)

@app.route("/login/<int:email_id>")
def login(email_id):
    init_session()

    session["behaviour"].append("Clicked")
    risk = calculations(session["behaviour"], LOGS)
    print("current risk: ", risk)

    return render_template("login.html", email_id=email_id)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    email_id = request.form.get("email")
    session["entered_email"] = email_id
    password = request.form.get("password")
    LOGS.append({
        "email_id": email_id,
        "password": password,
        "event": "form_submitted",
        "time": datetime.now()
    })
    print(LOGS)

    return redirect('/notice')

if __name__ == "__main__":
    app.run(debug=True)