from flask import Flask, request, jsonify

app = Flask(__name__)

# Addition
@app.route('/add')
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"result": a + b})
    except:
        return jsonify({"error": "Invalid input"}), 400

# Subtraction
@app.route('/subtract')
def subtract():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"result": a - b})
    except:
        return jsonify({"error": "Invalid input"}), 400

# Multiplication
@app.route('/multiply')
def multiply():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"result": a * b})
    except:
        return jsonify({"error": "Invalid input"}), 400

# Division
@app.route('/divide')
def divide():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        if b == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        return jsonify({"result": a / b})
    except:
        return jsonify({"error": "Invalid input"}), 400

# Health check endpoint
@app.route('/healthz')
def healthz():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
