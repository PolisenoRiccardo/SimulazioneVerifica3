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
games['year'] = [int(anno[-4:]) for anno in games['release_date']]

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
    annoInizio, annoFine = request.args.get('annoInizio'), request.args.get('annoFine')
    table = games[(games['year'] >= int(annoInizio)) & (games['year'] <= int(annoFine))]
    return render_template('risultato.html', table = table.to_html())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=32245, debug=True)