# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
import csv

import requests
from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download_prices')
def download():
    # TODO: replace API key, borrowed from another user
    api_key = 'E7FDCCBA39FBA0268555B7E81D73CD47'
    url = 'http://api.eia.gov/series/\
?api_key={api_key}\
&series_id={series_id}\
&out={out}'

    # download daily prices and save to csv
    response = requests.get(url.format(api_key=api_key,
                                       series_id='NG.RNGWHHD.D',
                                       out='json'))
    data = response.json()['series'][0]['data']
    with open('/srv/server/data/prices_daily.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    # download monthly prices and save to csv
    response = requests.get(url.format(api_key=api_key,
                                       series_id='NG.RNGWHHD.M',
                                       out='json'))
    data = response.json()['series'][0]['data']
    with open('/srv/server/data/prices_monthly.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return 'ok'


@app.route('/api/data')
def data():
    # convert prices from csv file to json
    with open('srv/server/data/prices_monthly.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    # convert prices to float number
    data = [[item[0], float(item[1])] for item in data]
    return jsonify(data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
