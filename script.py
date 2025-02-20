import os
import requests

account_number = "YOUR_accountNumber_PARAMETER"
url = "https://try.access.worldpay.com/accounts/balance/" + account_number

headers = {"WP-CorrelationId": "15cd16b2-7b82-41cb-9b11-21be9dacad88"}

# Citire username și password din variabile de mediu
username = os.getenv("WORLDPAY_USERNAME")
password = os.getenv("WORLDPAY_PASSWORD")

if not username or not password:
    raise ValueError("Username și/sau parola nu sunt setate corect în GitHub Secrets!")

# Efectuarea request-ului
response = requests.get(url, headers=headers, auth=(username, password))

# Debugging: vezi statusul răspunsului
print("Status Code:", response.status_code)
print("Response:", response.text)
