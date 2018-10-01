from flask import *
app = flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')
