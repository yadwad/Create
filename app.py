import sqlite3
from flask import jsonify
import pandas as pd
import numpy as np
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('portfolios.html')

@app.route('/abseentism')
def abseentism ():
    return render_template('abseentism.html')

@app.route('/poverty')
def poverty():
    return render_template('poverty.html')

@app.route('/uninsured')
def uninsured():
    return render_template('uninsured.html')

@app.route('/childpoverty')
def childpoverty():
    return render_template('childpoverty.html')

@app.route('/metric')
def metric():
    return render_template('metric.html')



if __name__ == "__main__":
    app.run(debug=True)



