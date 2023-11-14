import requests
import send_email as se

api_key = "0ae7df4094b845f3843167315ff482b1"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-10-14&sortBy=publishedAt&apiKey=0ae7df4094b845f3843167315ff482b1"

data = requests.get(url)
contents = data.json()

message = ""
for article in contents["articles"]:
    title = article['title']
    description = article['description']
    if article['title'] is not None:
        message = message + f"News Title: {title} \n Description: {description} \n\n"

message = message.encode('utf-8')
se.send_email(message)
