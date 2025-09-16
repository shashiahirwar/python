import requests

r = requests.get('https://api.github.com')
print(r.status_code)
print(r.headers['content-type'])
print(r.__sizeof__())
print(r.cookies)