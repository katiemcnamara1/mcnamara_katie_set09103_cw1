from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('home.html')

@app.route('/about')
def roots():
    return render_template('about.html')

@app.route('/about/characters')
def characters(name=None):
    return render_template('characters.html', name=name)







if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
