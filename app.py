from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/1')
def viewEmail1():
    return render_template('1.html')

@app.route('/2')
def viewEmail2():
    return render_template('2.html')

@app.route('/3')
def viewEmail3():
    return render_template('3.html')

if __name__ == "__main__":
    app.run(debug=True)