import requests
# r = requests.get('https://api.github.com/events')
# t = requests.post('https://httpbin.org/post', data={'key': 'value'})
# payload = {'name': 'Gleb', 'web': 'nginx'}
# r = requests.get('https://httpbin.org/get', params=payload)
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# print(r.url)
r = requests.get('https://api.github.com/events')
print(r.encoding)
print(r.text)
# print(r.url)