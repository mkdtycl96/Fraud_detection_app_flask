import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json ={'V14':10,'V10': 8,'V12': 5,'V11': 2,'V4': 5,'V17': 1,'V3': 1,'V16': 2 })

print(r.json())