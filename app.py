#!/usr/bin/env python
import os
import random
import string

from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)
ADMIN_PASSWORD = os.environ.get(
    'FLAG',
    ''.join(random.choice(string.ascii_letters) for _ in range(256)),
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['POST'])
def admin():
    if request.method != 'POST':
        return redirect(url_for('index'))
    if request.form['password'] != ADMIN_PASSWORD:
        abort(403)
    return 'yay'

if __name__ == '__main__':
    app.run(port=80)
