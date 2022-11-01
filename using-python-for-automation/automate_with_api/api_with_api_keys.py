import requests

base_url = "https://openweathermap.org/data/2.5/forecast"
parameters = {'APPID': 'FAKE_API_ad3e34b5024d78bea786d6b50d184f01', 'q': 'Dallas,US'}
response = requests.get(base_url, params=parameters)
print(response.content)
