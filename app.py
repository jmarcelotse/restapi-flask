#!/usr/bin/env python3
"""
Flask App de Teste para CI/CD Pipeline
"""

from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Flask App CI/CD Test",
            "status": "running",
            "version": "1.0.0",
            "build": os.environ.get("BUILD_NUMBER", "dev"),
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "flask-app"}), 200


@app.route("/info")
def info():
    return jsonify(
        {
            "app": "Flask CI/CD Test",
            "python_version": "3.9",
            "framework": "Flask",
            "pipeline": "Jenkins + GitHub",
        }
    )


import os

if __name__ == "__main__":
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
