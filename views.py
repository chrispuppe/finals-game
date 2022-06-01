from flask import Flask, render_template, session, redirect, request, url_for, flash, abort
from controller import scoreboard, finals_roster, user_list, finals_game_dates, clear_scoreboard_cache
from models import User, Selection
from __init__ import app, db
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from login import LoginForm


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
@app.route('/index')
def home():
    updated_scoreboard = scoreboard()
    return render_template(
                            'index.html', 
                            updated_scoreboard=updated_scoreboard
                            )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None

    # checks the username and password against the DB and logs the user in if valid
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # print(user.password, form.password.data) 
        if user:
            if user.password == form.password.data:
                # print('logged in successfully')
                login_user(user, remember=form.remember.data)
                updated_scoreboard = scoreboard()
                return redirect(url_for('admin', updated_scoreboard=updated_scoreboard))
            else:
                error = "Invalid username or password. Please try again."

        # if not valid replies as such
        return render_template('login.html', form=form, error=error)
    print('not validated')
    return render_template('login.html', form=form)



@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if request.method == 'GET':
        team_list = finals_roster
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
    app.run()