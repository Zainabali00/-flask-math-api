from flask import Flask, request, jsonify
import time
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Track API uptime
start_time = time.time()


@app.route('/add', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = a + b
        log_request(f"Addition: {a} + {b} = {result}")
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400


@app.route('/subtract', methods=['GET'])
def subtract():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = a - b
        log_request(f"Subtraction: {a} - {b} = {result}")
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400


@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = a * b
        log_request(f"Multiplication: {a} * {b} = {result}")
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400


@app.route('/divide', methods=['GET'])
def divide():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        if b == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        result = a / b
        log_request(f"Division: {a} / {b} = {result}")
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400


@app.route('/healthz', methods=['GET'])
def health_check():
    uptime = time.time() - start_time
    return jsonify({"status": "healthy", "uptime": f"{uptime:.2f} seconds"})


def log_request(message):
    """Helper function to log API requests"""
    logging.info(message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
