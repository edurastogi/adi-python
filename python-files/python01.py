import requests
import json
import csv
import pyodbc

# First, we need to get an access token by providing the login credentials to the authentication server
auth_endpoint = 'https://your-authentication-endpoint.com'
api_endpoint = 'https://your-api-endpoint.com'
username = 'your-username'
password = 'your-password'
client_id = 'your-client-id'
client_secret = 'your-client-secret'

# Construct the request body
data = {
    'username': username,
    'password': password,
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'password'
}

# Make the request to get the access token
response = requests.post(auth_endpoint, data=data)
access_token = json.loads(response.text)['access_token']

# Now we can make requests to the API endpoint using the access token
headers = {'Authorization': f'Bearer {access_token}'}

# Make the request to get the list of ready files
response = requests.get(f"{api_endpoint}/ready-files", headers=headers)

# Parse the response JSON to get the list of ready files
ready_files = json.loads(response.text)

# Loop over the ready files and download them using the Get File API
for file_name, status in ready_files.items():
    if status == 'Ready':
        # Make the request to download the file
        response = requests.get(f"{api_endpoint}/get-file/{file_name}", headers=headers)

        # Parse the CSV data and save it to the database
        csv_data = response.text.split('\n')
        reader = csv.DictReader(csv_data)
        rows = [row for row in reader]

        # Save the CSV data to SQL Server
        server = 'your-server-name'
        database = 'your-database-name'
        username = 'your-username'
        password = 'your-password'
        driver = '{ODBC Driver 17 for SQL Server}' # Update the driver name to match your installed driver

        # Construct the connection string
        conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

        # Connect to the database
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        table_name = file_name.split('.')[0] # Use the filename as the table name
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (column1 VARCHAR(50), column2 VARCHAR(50), column3 VARCHAR(50))")

        # Insert the rows into the table
        for row in rows[1:]:
            cursor.execute(f"INSERT INTO {table_name} (column1, column2, column3) VALUES (?, ?, ?)", (row['column1'], row['column2'], row['column3']))

        conn.commit()
        conn.close()



#In this code, we make a call to the /ready-files endpoint to get the list of ready files, which is returned in JSON format.
#We then loop over the files and download any files that are in the "Ready" status using the /get-file endpoint.
#The downloaded CSV data is then parsed and saved to SQL Server using the same process as in the previous example.
#Note that in this example, we're using the filename as the table name, but you may want to modify this to fit your naming convention.
