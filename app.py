from flask import Flask
app = Flask(__name__)
import json
from flask import jsonify
import re

store = json.loads(open('store.json').read())

# name: xxx, category: xxxx, row: xxx, numberOfRows: xxx

@app.route('/search/<cat>', methods=['GET'])
def search(cat):
    cat = cat.lower().strip()
    if cat not in ['all', 'food', 'drinks', 'other']:
        return jsonify({'error': 'Unkown category!'})

    res = []
    if cat == 'all':
        for shelf in store['shelves']:
            res.append(shelf['name'])
            for r in shelf['rows']:
                res.append({"name": shelf["name"], "category", shelf["category"], "row": int(len(shelf["rows"]/2)), "numberOfRows" : len(shelf["rows"])})
    else:
        for shelf in store['shelves']:
            if shelf['category'].lower().strip() == cat:
                res.append(shelf['name'])
                for r in shelf['rows']:
                    res.append({"name": r, "category", shelf["category"], "row": shelf["rows"].index(r), "numberOfRows" : len(shelf["rows"])})
    return jsonify(list(dict.fromkeys(res)))


@app.route('/search/<cat>/<term>', methods=['GET'])
def search_t(term, cat):
    cat = cat.lower().strip()
    term = term.lower().strip()
    res = []
    if cat not in ['all', 'food', 'drinks', 'other']:
        return jsonify({'error': 'Unkown category!'})

    if cat == 'all':
        for shelf in store['shelves']:
            if shelf['name'].startswith(term):
                res.append({"name": shelf["name"], "category", shelf["category"], "row": int(len(shelf["rows"]/2)), "numberOfRows" : len(shelf["rows"])})
            for r in shelf['rows']:
                if r.startswith(term):
                    res.append({"name": r, "category", shelf["category"], "row": shelf["rows"].index(r), "numberOfRows" : len(shelf["rows"])})
    else:
        for shelf in store['shelves']:
            if shelf['category'].lower().strip() == cat:
                if shelf['name'].startswith(term):
                    res.append(shelf['name'])
                for r in shelf['rows']:
                    if r.startswith(term):
                        res.append(r)
    return jsonify(list(dict.fromkeys(res)))


@app.route('/search-simple/<term>', methods=['GET'])
def search_simple(term):
    res = []
    term = term.lower().strip()
    for shelf in store['shelves']:
        if shelf['name'].startswith(term):
            res.append({"name": shelf["name"], "category", shelf["category"], "row": int(len(shelf["rows"]/2)), "numberOfRows" : len(shelf["rows"])})
        for r in shelf['rows']:
            if r.startswith(term):
                res.append({"name": r, "category", shelf["category"], "row": shelf["rows"].index(r), "numberOfRows" : len(shelf["rows"])})
    return jsonify(list(dict.fromkeys(res)))




@app.route('/plan', methods=['POST'])
def plan():
    return "TEst"
