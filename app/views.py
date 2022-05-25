from flask import Flask, render_template, session, redirect, request, url_for
from app.controller import scoreboard, finals_roster, user_list, finals_game_dates
from app.models import User, Selection
from app import app, db


@app.route('/')
@app.route('/index')
def home():
    updated_scoreboard = scoreboard()
    print(updated_scoreboard)
    return render_template('index.html', updated_scoreboard=updated_scoreboard)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        team_list = finals_roster
        users = user_list
        game_dates = finals_game_dates
        return render_template('admin.html', team_list=team_list, users=users, game_dates=game_dates)
    
    if request.method == 'POST':
        new_selection = Selection(
                                    user_id=request.form['user'],
                                    game_date=request.form['game-day'],
                                    selected_player=request.form['player'],
                                    user_selection_order=1
                                    )
        db.session.add(new_selection)
        db.session.commit()

        return redirect(url_for('admin'))

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