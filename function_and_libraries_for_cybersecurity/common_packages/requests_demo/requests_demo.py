import requests

website = requests.get("https://www.example.com")

print("Status Code: " + str(website.status_code))
print("\n" + str(website.headers))
print("\n" + str(website.url))

print(website.text)  # response in unicode
print(website.content)  # response in bytes
