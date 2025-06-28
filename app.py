from flask import Flask, jsonify, render_template
from flask_cors import CORS
# Serve emergency data
import json

app = Flask(__name__)
CORS(app)  # ← This enables cross-origin requests

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/emergency/<country_code>')
def get_numbers(country_code):
    country_code= country_code.upper()
    try:
        with open('data/data.json', 'r') as file:
            
            data = json.load(file)
        if country_code in data:
            return jsonify(data[country_code])
        else:
            return jsonify({"error": "Country code not found"}), 404
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON data"}), 500

if __name__ == "__main__":
    app.run(debug=True)