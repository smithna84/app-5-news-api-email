import requests, certifi
from send_email import send_email

topic = "tesla"

api_key = "170e9c0de4dc4e92a40f12ad8e8d16f4"
url = "https://newsapi.org/v2/everything?"  \
       f"q={topic}"  \
        "&from=2024-11-21&"  \
       "sortBy=publishedAt"  \
       "&apiKey=170e9c0de4dc4e92a40f12ad8e8d16f4"  \
       "&language=en"

# Make request
request = requests.get(url, verify=False)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][0:20]:
       if article["title"] is not None:
           body = "Subject: Daily news"  \
                  + "\n" + body + article["title"] + "\n" \
                  + str(article["description"]) + "\n" \
                  + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)