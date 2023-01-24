
import requests
import json
from flask import Flask
import datetime


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    now = datetime.datetime.now()
    text = ''' <html>
    <head>
    <style type="text/css">
        table { border-collapse: collapse;}
        td { text-align: center; border: 2px solid #884499; border-style: dashed; font-size: 20px; }
    </style>
    </head>
    <body>
    '''
    text += '<h1>🏦 Курс валют 💰 [' + str(now) + ']</h1>'
    text += '<table width="100%" height="100%" border="2px">'
    text += '<tr>'
    for _ in valutes[0]:
        text += f'<th><th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr>'
        for v in valute.values():
            text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()
