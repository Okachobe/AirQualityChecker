import requests

# Define the base URL of the API
base_url = 'https://airnowapi.org/aq/observation/zipCode/current/'

# Read the API key from a file
with open('apikey.txt', 'r') as file:
    api_key = file.read().strip()
    
# Read the zip codes from a file
with open('zipcodes.txt', 'r') as file:
    zip_codes = [line.strip() for line in file]

for zip_code in zip_codes:

    # Define the parameters for the API request
    params = {
        'format': 'application/json',
        'zipCode': zip_code,
        'API_KEY': api_key
    }

    # Send the GET request
    response = requests.get(base_url, params=params)

    # Convert the response to JSON
    data = response.json()

    # Loop through the data
    for forecast in data:
        # Check if the parameter is PM2.5
        if forecast['ParameterName'] == 'PM2.5':
            # Print the desired fields
            print(f"Reporting Area: {forecast['ReportingArea']}")
            print(f"Date Forecast: {forecast['DateObserved']}")
            print(f"Quality: {forecast['Category']['Name']}")
            print(f"Parameter: {forecast['ParameterName']}")
            print(f"AQI: {forecast['AQI']}")
            print("\n")  # Print a newline for readability
