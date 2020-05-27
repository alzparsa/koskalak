from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    url = 'https://api.coingecko.com/api/v3/exchange_rates'
    r = requests.get(url)
    BTCValueCad = r.json()["rates"]["cad"]["value"]
    BTCValueCad = str(BTCValueCad)
    return render_template('home.html', BTCValueCad = BTCValueCad)





if __name__ == '__main__':
    app.run(debug=True)
