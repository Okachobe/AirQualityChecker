import requests
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# Define the base URL of the API
base_url = 'https://airnowapi.org/aq/observation/zipCode/current/'

# Read the API key from a file
with open('apikey.txt', 'r') as file:
    api_key = file.read().strip()

# Read the zip codes from a file
with open('zipcodes.txt', 'r') as file:
    zip_codes = [line.strip() for line in file]

# Create the main window
window = tk.Tk()
window.title('Air Quality')
window.geometry('600x400')

# Create a scrolled text widget
text_widget = ScrolledText(window)
text_widget.pack(expand=True, fill='both')

# Function to fetch and display air quality data
def display_air_quality():
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
                # Format and append the desired fields
                text = f"Reporting Area: {forecast['ReportingArea']}\n" \
                       f"Date Forecast: {forecast['DateObserved']}\n" \
                       f"Quality: {forecast['Category']['Name']}\n" \
                       f"Parameter: {forecast['ParameterName']}\n" \
                       f"AQI: {forecast['AQI']}\n\n"
                text_widget.insert(tk.END, text)

# Run the function to fetch and display air quality data
display_air_quality()

# Start the main event loop
window.mainloop()
