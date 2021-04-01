import requests

isbn='080213825X'
response = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:%22+isbn").json()
info = response["items"][0]["volumeInfo"]
print(info["averageRating"])
print(info["ratingsCount"])