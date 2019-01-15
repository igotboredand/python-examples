from elasticsearch import Elasticsearch

esclient = Elasticsearch(['localhost:9200'])
response = esclient.search(
index='movies',

body = {
    "query": {
        "query_string": {
            "query": "drama"
        }
    }
}
)

print(response)
