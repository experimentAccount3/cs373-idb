from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('Index.html')


@app.route('/about')
def about():
    return render_template('Groups.html')


@app.route('/group/<name>')
def group(name=None):
    if name == 'alkali':
        return render_template('alkaliLayout.html', name=name)
    elif name == 'alkaline-earth':
        return render_template('alkalinearthLayout.html', name=name)
    elif name == 'halogen':
        return render_template('halogenLayout.html', name=name)
    else:
        return "Page not found!"


@app.route('/element/<name>')
def element(name=None):
    if name == 'helium':
        return render_template('Helium.html', name=name)
    elif name == 'hydrogen':
        return render_template('Hydrogen.html', name=name)
    elif name == 'fluorine':
        return render_template('Fluorine.html', name=name)
    else:
        return "Page not found!"


@app.route('/period/<name>')
def period(name=None):
    if name == '1':
        return render_template('periodOneLayout.html', name=name)
    elif name == '2':
        return render_template('periodTwoLayout.html', name=name)
    elif name == '3':
        return render_template('periodThreeLayout.html', name=name)
    else:
        return "Page not found!"