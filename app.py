import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask, render_template, request, Response
app = Flask(__name__)

import pandas as pd
games = pd.read_csv('https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/metacritic_games.csv')
piattaformeLista = games['platform'].tolist()
piattaformeLista = list(set(piattaformeLista))
piattaforme = games.groupby('platform').count()[['game']]


@app.route('/', methods=['GET'])
def form():
    return render_template('home.html')

@app.route('/piattaforma', methods=['GET'])
def piattaforma(): 
    piattaformeLista = games['platform'].tolist()
    return render_template('input1.html', piattaforme = piattaformeLista)

@app.route('/risultapiattaforma', methods=['GET'])
def piattaforma1():
    console = request.args.get('piattaforma')
    table = games[games['platform'] == console.upper()]
    return render_template('risultato.html', table = table.to_html())

@app.route('/piattaforma1', methods=['GET'])
def piattaforma2():
    return render_template('input1.1.html', piattaforme = piattaformeLista)

@app.route('/risultapiattaforma1', methods=['GET'])
def piattaforma3():
    console = request.args.getlist('piattaforma1')
    platforms = pd.DataFrame()
    for piattaforma in consol:
       platforms = pd.concat([platforms, games[games['platform'] == piattaforma]])
    return render_template('risultato.html', table = platforms.to_html())

@app.route('/anno', methods=['GET'])
def anno(): 
    return render_template('input2.html')

@app.route('/risultatoAnno', methods=['GET'])
def anno1(): 
    games['year'] = [int(anno[-4:]) for anno in games['release_date']]
    annoInizio, annoFine = request.args.get('annoInizio'), request.args.get('annoFine')
    table = games[(games['year'] >= int(annoInizio)) & (games['year'] <= int(annoFine))]
    return render_template('risultato.html', table = table.to_html())

@app.route('/score', methods=['GET'])
def es3(): 
    games['metauser_score'] = games['metascore'] + games['user_score']
    table = games[games['metauser_score'] == games['metauser_score'].max()]
    return render_template('risultato.html', table = table.to_html())

@app.route('/giochi', methods=['GET'])
def es4(): 
    table = games.groupby('platform').count()[['game']]
    return render_template('risultato.html', table = table.to_html())

@app.route('/giochipiattaforme', methods=['GET'])
def es5(): 
    table = games.groupby('platform').count()[['game']]
    return render_template('input5.html', table = table.to_html())

@app.route('/risultatogiochi', methods=['GET'])
def risultatoes5(): 
    numerodigiochi = request.args.get('numerodigiochi')
    table = piattaforme[piattaforme['game'] > int(numerodigiochi)]
    return render_template('risultato.html', table = table.to_html())

@app.route('/torta', methods=['GET'])
def es6torta():
    dati = piattaforme['game']
    labels = piattaforme.index
    fig, ax = plt.subplots()
    ax.pie(dati, labels=labels)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/treemap', methods=['GET'])
def es6treemap():
    dati = piattaforme['game']
    labels = piattaforme.index
    import squarify 
    fig, ax = plt.subplots()
    squarify.plot(dati, label=labels)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/genere', methods=['GET'])
def es7(): 
    return render_template('input6.html')

@app.route('/risultatogenere', methods=['GET'])
def risultatoes7(): 
    genere, piattaforma = request.args.get('genere'), request.args.get('piattaforma')
    table = games[(games['platform'] == piattaforma.upper()) & (games['genre'] == genere)]
    return render_template('risultato.html', table = table.to_html())
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=32245, debug=True)


