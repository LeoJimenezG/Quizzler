import requests

# Endpoint parameters
parameters = {"amount": 10, "type": "boolean"}
# Get the API response with the parameters
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
# Raise an Exception in case of response error
response.raise_for_status()
# Create a dictionary with the information
question_data = response.json()["results"]
