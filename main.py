from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/ping')
def ping():
    return jsonify({"status": "terhubung"})

if __name__ == '__main__':
    app.run()
