from flask import Flask, render_template, session, redirect, request, url_for, flash, abort
from controller import scoreboard, finals_roster, user_list, finals_game_dates, clear_scoreboard_cache, teams, update_finals_teams, finals_team_1, finals_team_2
from models import User, Selection
from __init__ import app, db
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from login import LoginForm
import shelve


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

login_manager.login_view = 'login'

@app.route('/')
@app.route('/index')
def home():
    try:
        updated_scoreboard = scoreboard()
    except:
        updated_scoreboard = []
        raise Exception('scoreboard call failed')
    return render_template(
                            'index.html', 
                            updated_scoreboard=updated_scoreboard,
                            )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None

    # checks the username and password against the DB and logs the user in if valid
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user, remember=form.remember.data)
                return redirect(url_for('admin'))
            else:
                error = "Invalid username or password. Please try again."
        return render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form)


@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if request.method == 'GET':
        team_list = finals_roster()
        users = user_list()
        game_dates = finals_game_dates
        updated_scoreboard = scoreboard()
        return render_template(
                                'admin.html',
                                team_list=team_list,
                                users=users,
                                game_dates=game_dates,
                                updated_scoreboard=updated_scoreboard
                                )
    if request.method == 'POST':
        new_selection = Selection(
                                    id=request.form['user'],
                                    game_date=request.form['game-day'],
                                    selected_player=request.form['player']
                                    )
        db.session.add(new_selection)
        db.session.commit()
        clear_scoreboard_cache()
        return redirect(url_for('admin'))


@app.route('/delete-selection/<int:id>', methods= ['GET', 'POST'])
def delete_selection(id):
    delete_selection = Selection.query.get(id)
    db.session.delete(delete_selection)
    db.session.commit()
    clear_scoreboard_cache()
    return redirect(url_for('admin'))


@app.route('/select-teams', methods=['GET', 'POST'])
def team_selection():
    if request.method == 'GET':
        all_nba_teams = teams
        current_home_team = finals_team_1()
        current_away_team = finals_team_2()
        return render_template(
                                'select-teams.html',
                                    all_nba_teams=all_nba_teams,
                                    current_home_team=current_home_team,
                                    current_away_team=current_away_team
                                )
    if request.method == 'POST':
        home_team = request.form['home']
        away_team = request.form['away']
        update_finals_teams(home_team, away_team)
        with shelve.open('./vars_persist/vars', 'c') as shelf:
            print(shelf['finals_team_1'], shelf['finals_team_2'])
        return(redirect(url_for('admin')))


if __name__ == '__main__':
    app.run()