from flask import Flask, render_template, url_for, session, redirect
# import numpy as np
from controller import scoreboard, finals_roster, user_list
from flask_debugtoolbar import DebugToolbarExtension
import secrets
# import pandas as pd

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = secrets.token_urlsafe(24)
toolbar = DebugToolbarExtension(app)

@app.route('/')
@app.route('/index')
def home():
    updated_scoreboard = scoreboard()
    print(updated_scoreboard)
    return render_template('index.html', updated_scoreboard=updated_scoreboard)

@app.route('/admin')
def admin():
    team_list = finals_roster
    users = user_list
    return render_template('admin.html', team_list=team_list, users=users)

@app.route('/select-teams')
def team_selection():
    pass

@app.route('/select-dates')
def date_selection():
    pass

@app.route('/user-order')
def user_order():
    pass

if __name__ == '__main__':
    app.run(debug=True)