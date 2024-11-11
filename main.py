import requests

api_key = "170e9c0de4dc4e92a40f12ad8e8d16f4"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-10-11&"
       "sortBy=publishedAt&apiKey=170e9c0de4dc4e92a40f12ad8e8d16f4")

request = requests.get(url)
content = request.json()
print(content["articles"])