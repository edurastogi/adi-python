from flask import Flask, jsonify, request
import csv
import os

app = Flask(__name__)


# Example endpoint to return a JSON response
# http://127.0.0.1:5000/hello
@app.route('/hello')
def hello():
    print(os.getcwd())
    return jsonify({'message': 'Hello, world! I am coming from flask'})


# Example endpoint that accepts a POST request with JSON data
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data['a']
    b = data['b']
    return jsonify({'result': a + b})


# Example endpoint that accepts two parameters and returns a list of JSON objects
# http://localhost:5000/my_endpoint?param1=Alice&param2=25
# [{"name": "Alice", "age": 25}]
@app.route('/my_endpoint', methods=['GET'])
def my_endpoint():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')

    # Example list of JSON objects
    my_list = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 35}
    ]

    # Filter the list based on the input parameters
    filtered_list = [item for item in my_list if item["name"] == param1 and item["age"] == int(param2)]

    # Return the filtered list as a JSON response
    return jsonify(filtered_list)


# Example endpoint that receives a file name as parameter and sends its contents as JSON
# http://localhost:5000/get_file?file_name=my_file.csv
@app.route('/get_file', methods=['GET'])
def get_file():
    file_name = request.args.get('file_name')

    # Read the CSV file into a list of dictionaries
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_list = [row for row in csv_reader]

    # Return the list as a JSON response
    return jsonify(csv_list)


if __name__ == '__main__':
    app.run(debug=True)
