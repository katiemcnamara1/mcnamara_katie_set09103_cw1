from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('home.html')

@app.route('/about')
def roots():
    return render_template('about.html')

@app.route('/about/characters')
def character():
    return render_template('characters.html')

@app.route('/about/characters/Cosette/')
def Cosette():
    name = 'Cosette'
    return render_template('characters2.html', name=name)


@app.route('/about/characters/JeanValjean')
def Jean():
    name='Jean'
    return render_template('characters2.html', name=name)

@app.route('/about/characters/Fantine')
def characters():
    name ='Fantine'
    return render_template('characters2.html', name=name)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
