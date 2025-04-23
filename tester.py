import requests

url = 'http://127.0.0.1:5000/predict'
data = {'text': "Skilled machine learning engineer experienced in NLP and computer vision."}
response = requests.post(url, json=data)

print(response.json())