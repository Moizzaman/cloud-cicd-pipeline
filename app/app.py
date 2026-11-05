import os
import time
from flask import Flask, jsonify

app = Flask(__name__)

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
    app.run(host='0.0.0.0', port=5000)