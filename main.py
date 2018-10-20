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

@app.route('/about/characters/Cosette')
def Cosette():
    name = 'Cosette'
    return render_template('characters2.html', name=name)

@app.route('/about/characters/JeanValjean')
def Jean():
    name='Jean'
    return render_template('characters2.html', name=name)

@app.route('/about/characters/Fantine')
def Fantine():
    name ='Fantine'
    return render_template('characters2.html', name=name)

@app.route('/about/characters/Marius')
def Marius():
    name ='Marius'
    return render_template('characters2.html', name=name)

@app.route('/about/characters/Eponine')
def Eponine():
    name ='Eponine'
    return render_template('characters2.html', name=name)

@app.route('/about/characters/MonsieurThenardier')
def Monsieur():
    name ='MonsieurThenardier'
    return render_template('characters2.html', name=name)

@app.route('/about/characters/Javert')
def Javert():
    name ='Javert'
    return render_template('characters2.html', name=name)

@app.route('/about/characters/MadameThenardier')
def Madame():
    name ='MadameThenardier'
    return render_template('characters2.html', name=name)

@app.route('/about/characters/Enjolras')
def Enjolras():
    name ='Enjolras'
    return render_template('characters2.html', name=name)

@app.route('/about/characters/Gavorche')
def Gavorche():
    name ='Gavorche'
    return render_template('characters2.html', name=name)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
