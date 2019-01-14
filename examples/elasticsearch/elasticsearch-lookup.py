#Get entry by entry number.
import json
import requests
from elasticsearch import Elasticsearch
import sys 


es = Elasticsearch('localhost:9200')

entry_number = sys.argv[1]
index = sys.argv[2]
document= sys.argv[3]

#     print('-------------------------------------------')
res = es.get(index=index, doc_type=document, id=entry_number)
 
print(res)
