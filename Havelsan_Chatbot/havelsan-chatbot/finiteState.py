#from elasticsearch import Elasticsearch
#from difflib import get_close_matches 

from gensim.models import Word2Vec

import data

from General_Cleaning import PreProcessing

from process import Process
global process # name_surname
process = Process("Nurbüke TEKER" )




import pandas as pd

global state_stuck_counter 
state_stuck_counter = 0

def korona_maddeler(returned_text):
     returned_text.append("-İlk olarak, sosyal izolasyon çok önemli! Acil bir ihtiyaç olmadıkça lütfen dışarı çıkmayın.<br> -Evden çıkmak zorunda kalırsanız mutlaka maske ve tıbbi eldiven takın; restoran, kafe, spor salonu veya alışveriş merkezi gibi kalabalık yerlerden uzak durun. Toplu taşıma araçlarını mümkün olduğunca kullanmayın.<br> -Son 14 gün içinde COVID-19 hastalığının görüldüğü ülkelerin birinden geldiyseniz veya yurt dışından gelen birileri ile görüştüyseniz, herhangi bir hastalık belirtisi göstermiyor olsanız bile, 14 gün boyunca kendinizi izole etmeniz çok önemli. <br> -Ateş, öksürük ya da solunum sıkıntısı gelişmesi durumunda en yakın sağlık kuruluşuna başvurun. <br> -Detaylı bilgi için Sağlık Bakanlığı Korona Danışma Hattı 'ALO 184'ü arayabilirsiniz. <br>")
#     returned_text.append("-Evden çıkmak zorunda kalırsanız mutlaka maske ve tıbbi eldiven takın; restoran, kafe, spor salonu veya alışveriş merkezi gibi kalabalık yerlerden uzak durun. Toplu taşıma araçlarını mümkün olduğunca kullanmayın.<br>")
#     returned_text.append("-Son 14 gün içinde COVID-19 hastalığının görüldüğü ülkelerin birinden geldiyseniz veya yurt dışından gelen birileri ile görüştüyseniz, herhangi bir hastalık belirtisi göstermiyor olsanız bile, 14 gün boyunca kendinizi izole etmeniz çok önemli. <br>")
#     returned_text.append("-Ateş, öksürük ya da solunum sıkıntısı gelişmesi durumunda en yakın sağlık kuruluşuna başvurun. <br>")
#     returned_text.append("-Detaylı bilgi için Sağlık Bakanlığı Korona Danışma Hattı 'ALO 184'ü arayabilirsiniz. <br>")
     returned_text.append("Dikkatli ve özverili olarak hem kendinizi, hem de çevrenizdekileri koruyabilirsiniz.")
     return returned_text
    
def getAnswer(question):
    question = "havelsn"
    if question == "refresh": 
        process.process_refresh()
        return "everything refreshed"
    
    Obj = PreProcessing.PreProcessing()

    question = Obj.filter_line(question,1)
    print("Filtered Question",question)
    print("State is ::",process.state)
    
    
            
    similarDFList = data.searchFuzzy_havelsan_chatbot(question)
    if len(similarDFList) > 0: 
        process.errorCount = 0
        for i, s in similarDFList.iterrows():
#            print(" score: {1}, soru: {2}".format( s['score'], s['soru']))
            sınıfNo = int(similarDFList['sınıfNo'][0])   
            if sınıfNo == 1:
                process.state = 1
                returned_text = similarDFList['cevap'][0]
                print("Returned Text :",returned_text)
                return [returned_text]
            
            if sınıfNo == 2:
                process.state = 1
                returned_text = [similarDFList['cevap'][0]]
                returned_text =korona_maddeler(returned_text)
                 
                print("Returned Text :",returned_text)
                return returned_text
            if sınıfNo == 3:
                process.state = 1
                returned_text = [similarDFList['cevap'][0]]
                returned_text.append("Aşağıdaki link üzerinden HAVELSAN ürün ve çözümleri hakkında daha fazla bilgi alabilirsiniz.")
#                returned_text.append("https://www.havelsan.com.tr/sektorler/bilgi-ve-iletisim")
                returned_text.append("<a href='https://www.havelsan.com.tr/sektorler/bilgi-ve-iletisim'>Havelsan Sektörler</a>")
                print("Returned Text :",returned_text)
                return returned_text
            
            if sınıfNo == 4:
                process.state = 1
                returned_text = [similarDFList['cevap'][0]]
#                returned_text.append("<link> https://inovasyon.havelsan.com.tr/havelsan/#/submit-suggestion-external </link>")
                returned_text.append("<a href='https://inovasyon.havelsan.com.tr/havelsan/#/submit-suggestion-external'>Havelsan Fikir Önerisi</a>")
                 
                print("Returned Text :",returned_text)
                return returned_text
            if sınıfNo == 5:
                process.state = 1
                returned_text = [similarDFList['cevap'][0]]
                 
                print("Returned Text :",returned_text)
                return returned_text
                
            else:
                return ["Üzgünüm ne dediğinizi anlayamadım. Lütfen tekrar dener misiniz? "]                  
                
                   
            
           
            
           

               
         
    else:
        process.errorCount = process.errorCount +1
        if ( process.errorCount == 3):
            print("kere anlamadık sizi müşteri bey/hanım")
            process.process_refresh()
            return -2  ##işlem sonlandırılmalı

      
        else:
            print("Anlamadık")
            return ["Üzgünüm ne dediğinizi anlayamadım. Lütfen tekrar dener misiniz? "]
        
 
