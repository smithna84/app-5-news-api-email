import requests
from send_email import send_email

api_key = "170e9c0de4dc4e92a40f12ad8e8d16f4"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-10-11&"
       "sortBy=publishedAt&apiKey=170e9c0de4dc4e92a40f12ad8e8d16f4")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
       body = body + article["title"] + "\n" + article["description"] + 2*"\n"

send_email(message=body)