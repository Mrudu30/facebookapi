import requests

# Replace with your actual access token
access_token = "EAAJjeJnW2qkBO0et3WT5an7tGutjJtb0E10eo6vUkYxHvpZAcH8x6Y6SKyPSytdLto21tiRlOGAotBkGkjkwPnEjg612YjcjwhvqMWVJMbQsc8c5uLC0RLilAnsTn3mQoQXEooSCWaY82Sf5ZCbyZB3ikfCDmZCOZA8cjyZBgDh2SZAckzcXASYV2ZAUWTo3NClZBK9TbUVUGVrGtXQG0xbTafZBDjZBYUZD"

# Make the GET request
response = requests.get(f"https://graph.facebook.com/v12.0/me/accounts?access_token={access_token}")

# Parse the response (assuming it's in JSON format)
data = response.json()
print(data)
# Extract the page access token for the desired page
page_access_token = data["data"][0]["access_token"]  # Adjust the index as needed

print(f"Page Access Token: {page_access_token}")
