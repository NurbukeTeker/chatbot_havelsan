from elasticsearch import Elasticsearch
import pandas as pd

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

def getPandas_havelsan_chatbot(result):  
    
    data = pd.DataFrame()
        
    for num, doc in enumerate(result['hits']['hits']):      
            
        _id = doc["_id"]
        score = doc["_score"]      
        soru = doc["_source"]['soru']
        sınıfNo = doc["_source"]['sınıfNo']  
        cevap = doc["_source"]['cevap'] 
        data = data.append( {"_id": _id, "score": score, "soru": soru,"sınıfNo":sınıfNo, "cevap":cevap}, ignore_index=True)
        data = data[['_id', 'score', 'soru','sınıfNo','cevap']]
        
        data = data.sort_values(by = ['score'], ascending = False)
    return data



def searchFuzzy_havelsan_chatbot(question):
    doc = {
        'size':100,
            "query": {
                "multi_match": {
                        "fields" : ['soru'],
                        "query" : question,
                        "fuzziness" : 1,
                        "prefix_length" : 1 #kelimenin ilk 1 karakteri uyuşmalı
                }
            }
        }   
        
    try:
        fuzzy = es.search(index = 'havelsan_chatbot', body = doc)     #havelsan_chatbot             
        fuzzyDF = getPandas_havelsan_chatbot(fuzzy)  ####???
        return fuzzyDF
    except Exception as e:
        print(e)
        