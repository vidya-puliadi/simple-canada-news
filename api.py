import requests
import json

api_key = "6bc119c5189a49468965475f67f51d10"


# Make the API request to get the top news in Canada
response = requests.get(
    f"https://newsapi.org/v2/top-headlines?country=ca&apiKey={api_key}")

# Load the response data into a Python dictionary
news_data = json.loads(response.text)
print(news_data)
# Print the top news articles
for article in news_data["articles"]:
    print(article["title"])
