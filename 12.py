import requests

m = 'Who you are?'
url = 'http://api.multillect.com/translate/json/1.0/314?method=translate/api/translate&from=eng&to=rus&text=”%s”&sig=67e4aec2601714cfd0856bdb7eebf228' % m

response = requests.get(url)
print(response.json())