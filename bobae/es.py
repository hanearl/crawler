from elasticsearch import Elasticsearch
from datetime import datetime


class EsWrapper:
    def __init__(self, es_addr='localhost:9200'):
        self.es = Elasticsearch(es_addr)

    def insert(self, index, doc_type, body):
        self.es.index(index=index, doc_type=doc_type, body=body)

    def search(self, index, body):
        return self.es.search(index=index, body=body)


es = EsWrapper()

# insert

index = 'test_index'
doc_type = '_doc'
body = {
    'category': 'skirt',
    'c_key': '1234',
    'price': 11400,
    'status': 1,
    '@timestamp': datetime.utcnow().strftime('%Y-%m-%dT%H:%M%S.%f')[:-3]+'z'
}

print(es.insert(index, doc_type, body))

#search
index = 'test_index'
body = {
    'query': {
        'match_all': {}
    }
}

print(es.search(index, body))
