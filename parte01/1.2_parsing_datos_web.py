import requests
import feedparser

url = 'https://github.com/Fhernd/Python-Curso'
respuesta = requests.get(url)
print(respuesta.status_code)

print()

html = respuesta.text
print(html)
print()
print(respuesta.json)

print()

headers = respuesta.headers
print(type(headers))
print(headers)

print()

print(respuesta.encoding)

print()

url = 'https://www.reddit.com/r/Python/.rss'
respuesta = feedparser.parse(url)
print(respuesta['feed']['title'])
