from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import requests

app = Flask(__name__)

@app.route('/')

#This function would get the btc exchange to usd and return it to the page
def GetRate_btc():
    url = 'https://api.coingecko.com/api/v3/exchange_rates'
    r = requests.get(url)
    BTCValueCad = r.json()["rates"]["cad"]["value"]
    BTCValueCad = str(BTCValueCad)
    return render_template('home.html', BTCValueCad = BTCValueCad)


#functions under devlopment 

#This would get the IRR rate from jafari.pw and return the exact sell string to be used for exchange
#1. for now it works on refresh  TODO:make it sync every 1 minute + render it into the page 
def GetRate_irr():
    url = 'https://currency.jafari.pw/json'
    r = requests.get(url)
    Rate_irr = r.json()["Currency"][0]['Sell']
    return (Rate_irr)


if __name__ == '__main__':
    app.run(debug=True)
