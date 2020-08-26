from gensim.models import Word2Vec

model = Word2Vec.load('w2v_word1_size300_(2082)_havelsan.model')

words = []
features = []
for word in model.wv.vocab:
    words.append(word)
    features.append(model[word])
    

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

for word in words:  
    doc = {
           'word' : word
    }
    res = es.index(index="havelsan_chatbot_w2v",  body=doc)
  
    
def getCloseWord(word):
    doc = {
        'size':1,
            "query": {
                "multi_match": {
                        "fields" : ['word'],
                        "query" : word,
                        "fuzziness" : 2,
                        "prefix_length" : 2 #kelimenin ilk 1 karakteri uyuşmalı
                }
            }
        }   
        
    fuzzy = es.search(index = 'havelsan_chatbot_w2v', body = doc)           
    return fuzzy['hits']['hits'][0]['_source']['word']