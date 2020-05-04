from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()
# es = Elasticsearch([{'host': 'd.es.dataapi.rea-asia.com', 'port': 9200}])



doc = {
    'author': 'Kamal',
    "searched_keyword": {"search_keyword": "Sunday spk", "matched_places": { "Sunday spk …": 90, "Sunday spkksjff": 89, "XXXXXXXXX": 80}},
    'timestamp': datetime.now(),
}
res = es.index(index="keyword", doc_type='search_submit', id=1, body=doc)



string_matching = {
    'searchkeyword': 'midvalley',
    'text': 'most relevant search keywords according to db',
    'timestamp': datetime.now(),
    'matched_placekeywords': {1: 'mid valley city', 2 :'mid valley gardens', 3: 'mid valley gardens'}
}
res = es.index(index="midvalley", doc_type='keywords-search', id=4, body=string_matching)
res = es.search(index="midvalley", body={"query": {"match_all": {}}})
for hit in res['hits']['hits']:
    # print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
    print(hit['_source'])
# print(res)

res = es.get(index="test-index", doc_type='tweet', id=1)
print(res['_source'])
# print( res)

es.indices.refresh(index="test-index")
res = es.search(index="test-index", body={"query": {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    # print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
    print(hit)


es = Elasticsearch([{'host': 'http://d.es.dataapi.rea-asia.com', 'port': 9200}])

# http://d.es.dataapi.rea-asia.com:9200/_search?q=search_submit:Sunday spk AND _source:searched_keyword
