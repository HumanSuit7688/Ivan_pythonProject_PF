from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    # user = { 'nickname': 'Ivan' } # выдуманный пользователь
    return render_template("index.html")

