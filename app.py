from flask import Flask, render_template, request, redirect
from datetime import datetime
from email_templates import EMAILS #imports the file

app = Flask(__name__)
LOGS = []
@app.route('/')
def main():
    return render_template('index.html', emails=EMAILS)

@app.route('/email/<int:email_id>')
def viewEmail(email_id):
    email = next((e for e in EMAILS if e["id"] == email_id), None)
    return render_template('email.html', email=email)

@app.route('/notice')
def message():
    return render_template('notice.html')

@app.route("/login/<int:email_id>")
def login(email_id):
    return render_template("login.html", email_id=email_id)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    email_id = request.form.get("email")
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