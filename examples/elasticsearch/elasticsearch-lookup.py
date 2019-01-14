#iterate over swapi people documents and index them
import json
import requests
from elasticsearch import Elasticsearch
import sys 


es = Elasticsearch('localhost:9200')

r = requests.get('http://localhost:9200') 
i = sys.argv[1]
while r.status_code == 200:
    # r = requests.get('http://swapi.co/api/people/'+ str(i))
    # print(r.content)
    # print('-------------------------------------------')
    es.get(index='starwars', doc_type='people', id=5)
 
print(i)
