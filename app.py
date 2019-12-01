from flask import Flask
app = Flask(__name__)
import json
from flask import jsonify
import re

store = json.loads(open('store.json').read())

terms_lst = []

for shelf in store['shelves']:
    terms_lst.append(shelf['cat'])
    for row in shelf['rows']:
        terms_lst.append(row)

terms_lst = list(dict.fromkeys(terms_lst))



@app.route('/search/<term>', methods=['GET'])
def hello_world(term):
    term = term.lower().strip()
    res = []
    for t in terms_lst:
        if t.startswith(term):
            res.append(t)
    return jsonify(res)
