from flask import Flask, request, Response
import csv
import json

app = Flask(__name__)


# Example endpoint that streams the contents of a CSV file as a JSON response
# http://localhost:5000/my_endpoint?file_name=my_file.csv
@app.route('/my_endpoint', methods=['GET'])
def my_endpoint():
    file_name = request.args.get('file_name')

    # Define a generator function to read the CSV file and yield JSON objects
    def generate():
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                yield json.dumps(row) + '\n'

    # Use Flask's streaming response feature to send the JSON objects to the client incrementally
    return Response(generate(), mimetype='application/json',
                    headers={'Content-Disposition': 'inline; filename=data.json'})


if __name__ == '__main__':
    app.run(debug=True)

# In this updated example, we're defining a generator function called generate that reads the CSV file and yields
# JSON objects as strings, one object at a time. We're using the json.dumps function to convert each row of the CSV
# file to a JSON object string, and adding a newline character (\n) at the end of each string to separate the objects.

# We're then using Flask's Response class to create a streaming response with the MIME type application/json. We're
# passing the generate function as the response content, which allows us to stream the JSON objects to the client
# incrementally. We're also setting the Content-Disposition header to attachment; filename=data.json to suggest to
# the client that the response should be downloaded as a file named data.json.
