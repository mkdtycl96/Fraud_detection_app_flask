import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json ={'V4':10,'V10': 8,'V11': 5,'V12': 2,'V14': 5,'V17': 1})

print(r.json())