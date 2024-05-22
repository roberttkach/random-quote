import requests
import json

def get_quote():
    response = requests.get("https://api.quotable.io/random")
    json_data = json.loads(response.text)
    quote = json_data['content']
    author = json_data['author']
    return f"{quote} - {author}"

print(get_quote())
