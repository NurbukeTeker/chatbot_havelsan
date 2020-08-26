import json
import pandas as pd
from nltk.corpus import stopwords
import re
#from Sisa.zemberek_python import main_libs as ml
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


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

class PreProcessing():
    def __init__(self):
        
        self.num = 0
       
    def importJsonData(self,path):
        with open(path, "r", encoding = 'utf8') as read_file:
            dataJson = json.load(read_file, strict=False)
                
        dfJson = pd.DataFrame.from_dict(dataJson['RECORDS'])
        return dfJson 

    def filter_line(self,line,ES_getClose = True ,isStopwords = True ,max_lenword = 2 ,lemmatization = False ): 
        
        print(line)
#        line ="havelsa"
        try: 
            line = line.replace('I','ı').replace('İ','i')
            line = line.replace('\n', ' ').replace('\t', ' ')
            line = line.lower()
    #        TR_WHITELIST = 'abcçdefgğhıijklmnoöpqrsştuüvwxyz ' # space is included in whitelist
            #TR_BLACKLIST = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\''
            
    #        line = remove_html_tags(line)          
            # clean_text = line.replace("'"," ")  
            clean_text = line.replace("’","'")  
            clean_text = clean_text.replace("'", " ")
#            clean_text = re.sub("&[a-z]*"," ",clean_text)  #kesme işareti ve sonrasının silindiği durum
#        
    #        clean_text = ' '. join([word for word in clean_text.split() if not re.match("[^a-zA-ZığüşöçİĞÜŞÖÇ]", word)])     # 2017'yi gibi kelimeri ekiyle birlikte              kaldırmak için yapıldı. Bu işlem olmasaydı rakamlar kaldırıldıktan sonra "2017'yi" --> "yi" olarak tek başına kalıyordu
            
            clean_text = re.sub("[^0-9a-zA-ZığüşöçİĞÜŞÖÇ ']"," ", clean_text).split()  # kelimeler arasında fazla boşluklar vardı kelimeleri split edip tekrar 1 boşlukla join yaptık
           
            if(lemmatization):
                parcalı_cumle_list = ml.ZemberekTool(self.zemberek_api).cumleyi_parcalara_ayir(clean_text)
                new_str = ""
                for kelime in clean_text:
                    a = ml.ZemberekTool(self.zemberek_api).ogelere_ayir(kelime)
                    if (a is None):
                         new_str = new_str + kelime +" "
                         print(kelime)
                    elif( a['tip'] != 'FIIL'):
                        new_str = new_str + a['Kok'] +" " 
                    else:
                        new_str = new_str + kelime +" " 
#                print(new_str)
                filtered_text =  new_str
                
            if(isStopwords):
    #            print("Here")
                stop_words = stopwords.words('turkish')
                clean_text = [word for word in clean_text if word not in stop_words]
            
            filterMinWords = [word for word in clean_text if len(word)>2 ]
            filtered_textX = ' '.join(filterMinWords)  
            if(ES_getClose):
                if filtered_textX.isnumeric() == False :
                    filtered = []
                    for word in filterMinWords: 
                            print(word)
                            try:
                                word = getCloseWord(word)
                                filtered.append(word)
                            except Exception as e:
                                print(e)
                    filtered_text = ' '.join(filtered)  
                    if filtered_text == '':
                        filtered_text = filtered_textX
                else:
                    filtered_text = ' '.join(filterMinWords) 
            else:
                  filtered_text = ' '.join(filterMinWords) 
        except Exception as e:
            print(e)
            return
    #    filtered = ' '.join([ ch for ch in line if ch in TR_WHITELIST ])
        
        return filtered_text



