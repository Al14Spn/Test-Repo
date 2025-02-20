import requests

account_number = "YOUR_accountNumber_PARAMETER"
url = "https://try.access.worldpay.com/accounts/balance/" + account_number

headers = {"WP-CorrelationId": "15cd16b2-7b82-41cb-9b11-21be9dacad88"}

response = requests.get(url, headers=headers, auth=('<username>','<password>'))

data = response.json()
print(data)
