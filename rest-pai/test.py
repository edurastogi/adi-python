from flask import Flask, jsonify, request

app = Flask(__name__)


# Example endpoint to return a JSON response
@app.route('/hello')
def hello():
    return jsonify({'message': 'Hello, world! I am coming from flask'})


# Example endpoint that accepts a POST request with JSON data
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data['a']
    b = data['b']
    return jsonify({'result': a + b})


if __name__ == '__main__':
    app.run(debug=True)
