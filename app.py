from flask import Flask, render_template, url_for, session, redirect
import numpy as np
import controller
# import pandas as pd

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    steph=controller.get_player_finals_stats('Stephen Curry')
    return render_template('index.html', steph=steph)

if __name__ == '__main__':
    app.run(debug=True)