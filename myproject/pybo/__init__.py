from flask import Flask, render_template, redirect, request, url_for
# 여기다가 파이썬 함수 import해오기
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resultpage', methods=['POST'])
def post():
    value = request.form
    return value

if __name__ == '__main__':
    app.run(debug=True)