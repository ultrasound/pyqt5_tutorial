#!/usr/bin/env python
# coding: utf-8

import requests
import requests_cache

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

requests_cache.install_cache('github_cache', backend='sqlite', expire_after=180)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        first = request.form.get('first')
        second = request.form.get('second')
        url = "https://api.github.com/search/users?q=location:{0}+language:{1}".format(first, second)
        response_dict = requests.get(url).json()
        return jsonify(response_dict)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)