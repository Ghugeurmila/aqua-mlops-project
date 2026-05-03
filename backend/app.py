from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/predict')
def predict():
    try:
        h = float(request.args.get('humidity', 0))
        t = float(request.args.get('temp', 0))
        r = float(request.args.get('rainfall', 0))
        w = float(request.args.get('water', 0))
        # Professional Logic: Average + 10 (as discussed for your demo)
        prediction = ((h + t + r + w) / 4) + 10
        return jsonify({'prediction': round(prediction, 2)})
    except:
        return jsonify({'error': 'Invalid Input'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
