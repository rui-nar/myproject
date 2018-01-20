#!/usr/bin/env python
"""This file defines the Person class to be used in the user database"""

from flask import Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app
from pymongo import MongoClient

# create our blueprint :)
user = Blueprint('user', __name__)


def connect_db():
    """Connects to the specific database."""
    rv = MongoClient()
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'client_db'):
        g.client_db = connect_db()
    return g.client_db[current_app.config['DATABASE']]


@user.route('/')
def show_entries():
    db = get_db()
    cur = db['users'].find()
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@user.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
               [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('flaskr.show_entries'))


@user.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != current_app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != current_app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('flaskr.show_entries'))
    return render_template('login.html', error=error)


@user.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('flaskr.show_entries'))
