# Imports
from flask import Flask, render_template, request
import requests

# Initialize flask app
app = Flask(__name__)

# Fixer.io API key
api_key = 'YOUR API Key FROM FIXER.IO'

url = 'http://data.fixer.io/api/latest?access_key=' + api_key

# Index page route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Take form informations
        firstCurrency = request.form.get('firstCurrency')
        secondCurrency = request.form.get('secondCurrency')
        amount = float(request.form.get('amount'))

        # Currency rates from url as json file
        currencies = requests.get(url).json()['rates']

        firstAmount = currencies[firstCurrency[:3]]
        secondAmount = currencies[secondCurrency[:3]]

        # Currencies informations with the converted price as a dict
        result = {
            'firstCurrency': firstCurrency,
            'secondCurrency': secondCurrency,
            'amount': amount,
            'price': round(amount*secondAmount/firstAmount, 4),
        }

        return render_template('index.html', result=result)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
