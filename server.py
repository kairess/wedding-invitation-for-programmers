from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import json, os
from datetime import datetime, timezone, timedelta

app = Flask(__name__, static_folder='dist', static_url_path='')
CORS(app)

barrage_path = 'data/barrages.json'

@app.route('/', methods=['GET'])
def index():
    return send_file('dist/index.html')

@app.route('/barrages', methods=['GET'])
def get_barrages():
    if not os.path.exists(barrage_path):
        with open(barrage_path, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False)

    with open(barrage_path, 'r') as f:
        barrages = json.load(f)

    return jsonify(barrages)

@app.route('/barrage', methods=['POST'])
def post_barrage():
    barrage = request.form.get('barrage', None)

    if barrage is None:
        return {
            'result': False
        }

    if not os.path.exists(barrage_path):
        with open(barrage_path, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False)

    with open(barrage_path, 'r', encoding='utf-8') as f:
        barrages = json.load(f)

    barrages.append({
        'barrage': barrage,
        'createdAt': datetime.now(timezone(timedelta(hours=+9))).strftime('%-m월 %-d일 %-H시쯤')
    })

    with open(barrage_path, 'w', encoding='utf-8') as f:
        json.dump(barrages, f, ensure_ascii=False)

    return {
        'result': True
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
