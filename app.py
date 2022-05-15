from flask import Flask, render_template, url_for, session, redirect
import numpy as np
import controller
from flask_debugtoolbar import DebugToolbarExtension
# import pandas as pd

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'This is just a test for a demo of my app'
toolbar = DebugToolbarExtension(app)

user_list = ['Andrew', 'Chris', 'Jake', 'Todd']

@app.route('/')
@app.route('/index')
def home():
    # updated_game_stats = all_player_selected_by_users()
    steph=controller.get_player_finals_stats('Stephen Curry')
    return render_template('index.html', steph=steph)

@app.route('/admin')
def admin():
    player_list = controller.finals_roster
    users = user_list
    return render_template('admin.html', player_list=player_list, users=users)

if __name__ == '__main__':
    app.run(debug=True)