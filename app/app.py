import os
import time
from flask import Flask, jsonify, render_template

# Get the absolute directory where app.py is located
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Explicitly bind Flask to the correct template folder
app = Flask(__name__, template_folder=TEMPLATE_DIR)
@app.route('/', methods=['GET'])
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return jsonify({
            "error": "Could not render index.html template",
            "details": str(e),
            "looking_in": TEMPLATE_DIR
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": int(time.time()),
        "environment": os.getenv("ENV", "production")
    }), 200

@app.route('/api/v1/data', methods=['GET'])
def get_data():
    return jsonify({
        "message": "Secure payload retrieved successfully",
        "node_id": os.getenv("HOSTNAME", "node-01")
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)