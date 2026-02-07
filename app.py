from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/api/reports/generate", methods=["POST"])
def generate_report():
    return jsonify({
        "status": "success",
        "message": "Report generated successfully"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)