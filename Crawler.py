import requests

data = {'q': '武漢+肺炎+統計+全球'}
r = requests.get('https://www.google.com/search', params=data)
print(r.text)
with open("test.html","w",encoding="utf-8")as f:
  f.write(r.text)
