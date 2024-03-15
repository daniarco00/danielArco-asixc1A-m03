import requests

city = 'london'
api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': 'HLrQOPWqTpyEhqLnayr8Qg==AdLe8Pq9DaTLjgo7'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)