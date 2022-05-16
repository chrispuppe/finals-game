from flask import Flask, render_template, url_for, session, redirect
import numpy as np
import controller
from flask_debugtoolbar import DebugToolbarExtension
import secrets
# import pandas as pd

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = secrets.token_urlsafe(24)
toolbar = DebugToolbarExtension(app)

user_list = ['Andrew', 'Chris', 'Jake', 'Todd']

@app.route('/')
@app.route('/index')
def home():
    # updated_game_stats = all_player_selected_by_users()
    user_choices = controller.all_user_selections
    game_data = []
    for choice in user_choices:
        selected_player = controller.get_player_finals_stats(choice[0])
        selected_player.append(choice[2])
        game_data.append(selected_player)
    # steph=controller.get_player_finals_stats('Stephen Curry')
    return render_template('index.html', game_data=game_data)

@app.route('/admin')
def admin():
    player_list = controller.finals_roster
    users = user_list
    return render_template('admin.html', player_list=player_list, users=users)

if __name__ == '__main__':
    app.run(debug=True)