from elasticsearch import helpers, Elasticsearch
import csv
import sys


# Usage python csv-import <path to csv file> <name of index in elasticsearch> <document type>

#TODO error handling around lack of input
csv_file = sys.argv[1]
index_name = sys.argv[2]
doc = sys.argv[3]


es = Elasticsearch()

# Encoding should be UTF-8, use ISO-8859-1 if you use fancy characters

with open(csv_file,encoding="UTF-8") as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index=index_name, doc_type=doc)
