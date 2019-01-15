#iterate over swapi people documents and index them
import json
import requests
from elasticsearch import Elasticsearch

es = Elasticsearch('localhost:9200')

r = requests.get('http://localhost:9200')
i = 1

while r.status_code == 200:
    r = requests.get('https://swapi.co/api/species/'+ str(i))
    print(r.content)
    print('-------------------------------------------')
    es.index(index='species', doc_type='sw', id=i, body=json.loads(r.content.decode('UTF-8')))
    i=i+1

print(i)
