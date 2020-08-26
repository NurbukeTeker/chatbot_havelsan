import pandas as pd

#es = Elasticsearch([{'host': 'elastic.sisasoft.com.tr'}])
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    
     

greetDialogs = [["merhaba","Merhaba. Size nasıl yardımcı olabilirim?"],["selam","Selam.  Size nasıl yardımcı olabilirim?"],["selamlar","Selamlar"],["iyi günler","Size de iyi günler dilerim."],["günaydın","Size de günaydın. Yeni bir bildirimde bulunma veya eski bildirimlerinizi sorgulama işlemlerinden hangisini yapmak istersiniz ?"],["iyi akşamlar","Size de iyi akşamlar dilerim."],["tünaydın","Size de iyi günler dilerim."],
                ["ne haber","Süperim"],["naber","Süperim"],["nasılsın","Süperim"],["nasıl gidiyor","Süper gidiyor"],["günün nasıl geçiyor","Süper geçiyor"],
                ["ne haber","Her şey yolunda"],["naber","Her şey yolunda"],["nasılsın","Her şey yolunda"],["nasıl gidiyor","Her şey yolunda gidiyor"],["günün nasıl geçiyor","Her şey yolunda"],
                
                ["ne haber","Sizi gördüm daha iyi oldum"],["naber","Sizi gördüm daha iyi oldum"],["nasılsın","Sizi gördüm daha iyi oldum"],["nasıl gidiyor","Sizi gördüm daha iyi oldum"],["günün nasıl geçiyor","Sizi gördüm daha iyi oldum"],
                 ["ne haber","Sizinle konuştuğum için mutluyum"],["naber","Sizinle konuştuğum için mutluyum"],["nasılsın","Sizinle konuştuğum için mutluyum"],["nasıl gidiyor","Sizinle konuştuğum için mutluyum"],["günün nasıl geçiyor","Sizinle konuştuğum için mutluyum."],
                ["kaç yaşındasın","En son modelim"],
                ["kaç yaşındasın","Her zaman genç ve enerjiğim"],
                ["kaç yaşındasın","Robotların yaşı sorulmaz ama kendimi her zaman geliştirilecek kadar genç hissediyorum."],
                ["yaşın kaç","En son modelim"],
                ["yaşın kaç","Her zaman genç ve enerjiğim."],
                ["yaşın kaç","Robotların yaşı sorulmaz ama kendimi her zaman geliştirilecek kadar genç hissediyorum."],
                ["yaş kaç","En son modelim"],
                ["yaş kaç","Her zaman genç ve enerjiğim."],
                ["yaş kaç","Robotların yaşı sorulmaz ama kendimi her zaman geliştirilecek kadar genç hissediyorum."],
                
                ["sen robot musun","Ben Havelsan Chatbot, Sizi HAVELSAN hakkında bilgilendirmek ve destek vermek için buradayım."],
                ["adın ne","Ben Havelsan Chatbot, Sizi HAVELSAN hakkında bilgilendirmek ve destek vermek için buradayım."],
                ["adın nedir","Ben Havelsan Chatbot, Sizi HAVELSAN hakkında bilgilendirmek ve destek vermek için buradayım."],
                ["kimsin","Ben Havelsan Chatbot, Sizi HAVELSAN hakkında bilgilendirmek ve destek vermek için buradayım."],
                ["nesin","Ben Havelsan Chatbot, Sizi HAVELSAN hakkında bilgilendirmek ve destek vermek için buradayım."],
                ["işin ne","Ben Havelsan Chatbot, Sizi HAVELSAN hakkında bilgilendirmek ve destek vermek için buradayım."],
                ["görevin ne","Ben Havelsan Chatbot, Sizi HAVELSAN hakkında bilgilendirmek ve destek vermek için buradayım."],
                ["ne yaparsın","Ben Havelsan Chatbot, Sizi HAVELSAN hakkında bilgilendirmek ve destek vermek için buradayım."],
                
                ["sen robot musun","Ben Havelsan Chatbot :) Ben bir Chatbotum. Size yardımcı olmak için geliştirildim."],
                ["adın ne","Ben Havelsan Chatbot :) Ben bir Chatbotum. Size yardımcı olmak için geliştirildim."],
                ["adın nedir","Ben Havelsan Chatbot :) Ben bir Chatbotum. Size yardımcı olmak için geliştirildim."],
                ["kimsin","Ben Havelsan Chatbot :) Ben bir Chatbotum. Size yardımcı olmak için geliştirildim."],
                ["nesin","Ben Havelsan Chatbot :) Ben bir Chatbotum. Size yardımcı olmak için geliştirildim."],
                ["işin ne","Ben Havelsan Chatbot :) Ben bir Chatbotum. Size yardımcı olmak için geliştirildim."],
                ["görevin ne","Ben Havelsan Chatbot :) Ben bir Chatbotum. Size yardımcı olmak için geliştirildim."],
                ["ne yaparsın","Ben Havelsan Chatbot :) Ben bir Chatbotum. Size yardımcı olmak için geliştirildim."],
                
                ["nerelisin","Doğma büyüme HAVELSAN'lıyım."],
                
                ["hava nasıl","Hava nasıl olursa olsun sizin enerjiniz hep yüksek olsun."],
                
                ["teşekkür ederim","Rica ederim ne zaman isterseniz size yardımcı olmaya hazırım."],
                ["teşekkür ederim","Rica ederim benim için bir zevkti."],
                
                ["sağolun","Rica ederim ne zaman isterseniz size yardımcı olmaya hazırım."],
                ["sağolun","Rica ederim benim için bir zevkti."],
                
                ["teşekkürler","Rica ederim ne zaman isterseniz size yardımcı olmaya hazırım."],
                ["teşekkürler","Rica ederim benim için bir zevkti."],
                ["teşekkürler","Size yardımcı olmak için hep buradayım."],
                      
                
                ["güle güle","Tekrar görüşmek üzere"],
                ["görüşmek üzere","Tekrar görüşmek üzere"],
                ["bye bye","Görüşmek üzere, yine beklerim"],
                ["kendine iyi bak","Görüşürüz, kendinize iyi bakın"],
                ["hoşçakal","Görüşmek üzere, yine beklerim"],
                 ["bye bye","Güle güle"],
                  ["bay bay","Hoşçakalın"],
                   ["güle güle","Hoşçakalın, yine beklerim"]]

genelSorular = [
                ["müşteri hizmetlerine bağlanabilir miyim","0312 219 5787'i arayarak işlemlerinizi gerçekleştirebilirsiniz."],
                ["müşteri hizmetlerinin numarası", "0312 219 5787'i arayarak işlemlerinizi gerçekleştirebilirsiniz."],
                ["müşteri hizmetleri", "0312 219 5787'i arayarak işlemlerinizi gerçekleştirebilirsiniz."],
                ["çağrı merkezi", "0312 219 5787'i arayarak işlemlerinizi gerçekleştirebilirsiniz."],
                ["iletişim telefon", "0312 219 5787'i arayarak işlemlerinizi gerçekleştirebilirsiniz."],

                ["hizmetler nelerdir", "Sizleri HAVELSAN hakkında bilgilendirmek ve sorularınızı daha hızlı bir şekilde cevaplamak konularında size yardımcı olabilirim."], 
                ["hizmetleriniz nelerdir", "Sizleri HAVELSAN hakkında bilgilendirmek ve sorularınızı daha hızlı bir şekilde cevaplamak konularında size yardımcı olabilirim."],
                ["hizmetlerle bilgi", "Sizleri HAVELSAN hakkında bilgilendirmek ve sorularınızı daha hızlı bir şekilde cevaplamak konularında size yardımcı olabilirim."], 
                ["neler yapabiliyorsun", "Sizleri HAVELSAN hakkında bilgilendirmek ve sorularınızı daha hızlı bir şekilde cevaplamak konularında size yardımcı olabilirim."],
                
                
                
                
                
                
            ["HAVELSAN hangi konularda çalışmalar yapmaktadır?","HAVELSAN savunma,simülasyon,bilişim, ülke güvenliği ve siber güvenlik alanlarında 38 yıllık deneyimi ile uçtan uca yeni nesil teknolojiler sunmaktadır."] ,["HAVELSAN çalışma alanları nelerdir?","HAVELSAN savunma,simülasyon,bilişim, ülke güvenliği ve siber güvenlik alanlarında 38 yıllık deneyimi ile uçtan uca yeni nesil teknolojiler sunmaktadır."] ,
            ["HAVELSAN ne zaman kurulmuştur?","HAVELSAN, Türk Silahlı Kuvvetlerini Güçlendirme Vakfı’nın bir şirketi olarak 1982 yılında kurulmuştur."],
            
            ["HAVELSAN vizyonu nedir?","Savunma, güvenlik ve bilişim alanlarında, ileri teknolojiye dayalı yazılım yoğun özgün çözüm ve ürünlere sahip, alanında ulusal ve uluslararası lider sistem entegratörü firma olmak."],
             ["HAVELSAN misyonu nedir?","İleri teknolojilere ulaşmak amacıyla yüksek performanslı, kaliteli, maliyet etkin ve güvenilir çözümler geliştirmek, teknolojik dönüşüme öncülük etmek.",],
             ["HAVELSAN'ın değerileri neelrdir?","Rekabetçilik ve Verimlilik, Yenilikçilik, Paydaş Memnuniyeti ,Kurumsal Yönetim İlkeleri ve Etik Değerlere Bağlılık bizim değerlerimizdir."],
             ["Etik ilkeleriniz nelerdir?","Etik ilBilişim ve Savunma şirketi olarak HAVELSAN;Bütün işlerinin ahlaki, adil, tarafsız, iş yaptığı ülkelerin yasa ve mevzuatına uygun ve evrensel insan hakları ilkeleriyle uyumlu olmasına dikkat eder. Çalışanlar yaptıkları her işlemde HAVELSAN’ın itibarını zedelememeye azami özeni gösterirler."], ["Ofisiniz nerede?","Ofislerimiz, Mustafa Kemal, 06510 Çankaya/Ankara ve Üniversiteler, Türk Telekom Ar-Ge Binası, 06800 Çankaya/Ankara merkezlerinde yer almaktadır." ],
             ["İş başvurusu yapmak istiyorum","İşe alım kriterlerini https://www.havelsan.com.tr/kariyer/havelsan-da-calismak/ise-alim-kriterleri üzerinden inceleyerek bizimle iletişime geçebilrisiniz"]
            ,["Ekibe dahil omak istiyorum","İşe alım kriterlerini https://www.havelsan.com.tr/kariyer/havelsan-da-calismak/ise-alim-kriterleri adresi üzerinden inceleyerek bizimle iletişime geçebilrisiniz."],
            ["Sizlerle çalışmak isterim","İşe alım kriterlerini https://www.havelsan.com.tr/kariyer/havelsan-da-calismak/ise-alim-kriterleri adresi üzerinden inceleyerek bizimle iletişime geçebilrisiniz."],
            ["işe almak","İşe alım kriterlerini https://www.havelsan.com.tr/kariyer/havelsan-da-calismak/ise-alim-kriterleri adresi üzerinden inceleyerek bizimle iletişime geçebilrisiniz."],
            ["Stajyer olmak isterim","Ekibimize dahil olmak için https://www.havelsan.com.tr/kariyer/havelsan-da-calismak/staj adresi üzerinden başvurunu yapabilirsin. "],
            ["Aday mühendis olmak istiyorum","Ekibimize dahil olmak için https://www.havelsan.com.tr/kariyer/havelsan-da-calismak/aday-muhendislik adresi üzerinden başvurunu yapabilirsin."],
            ["Aday mühendis olmak istiyorum","Ekibimize dahil olmak için https://www.havelsan.com.tr/kariyer/havelsan-da-calismak/aday-muhendislik adresi üzerinden başvurunu yapabilirsin."],
            ["Mail adresinizi öğrenebilir miyim ?","Bizimle iletişime geçmek için info@havelsan.com.tr adresine mail atabilirsin."]
             
             
             ]
               
#<a href='https://www.havelsan.com.tr/kariyer/havelsan-da-calismak/staj'> Staj Başvuruları</a>
#<a href='https://www.havelsan.com.tr/kariyer/havelsan-da-calismak/ise-alim-kriterleri'> HAVELSAN İşe Alım Kriterleri</a>

#<a href='https://www.havelsan.com.tr/kariyer/havelsan-da-calismak/aday-muhendislik'> Aday Mühendislik Başvuruları</a>

#<a href='info@havelsan.com.tr'> info@havelsan.com.tr</a>
#<a href='0312 219 5787'> 0312 219 5787</a>






greeting = pd.DataFrame(greetDialogs,columns=['soru','cevap'])
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
for i, d in greeting.iterrows():   
        doc = {
               'sınıfNo' : 1,
               'soru' : d.soru,
               'cevap' : d.cevap
        }
        res = es.index(index="havelsan_chatbot",  body=doc)  


genelsorular = pd.DataFrame(genelSorular,columns=['soru','cevap'])
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


for i, d in genelsorular.iterrows():   
        doc = {
               'sınıfNo' : 1,
               'soru' : d.soru,
               'cevap' : d.cevap
        }
        res = es.index(index="havelsan_chatbot",  body=doc)  
           
################################################################################
        
korona_bilgilendirme = [["Korona kapsamında neler yapmalıyım ?","Korona virüs ve sebep olduğu COVID-19 hastalığı hakkındaki merak ve endişenizi anlıyorum. Bu süreçte kendinizi ve çevrenizdekileri korumak için, T.C. Sağlık Bakanlığı'nın yayınladığı 14 Kural'a uymanızı tavsiye ederim:"],["Öksürük, hapşuruk vb. durumlarda neler yapmalıyım?","Korona virüs ve sebep olduğu COVID-19 hastalığı hakkındaki merak ve endişenizi anlıyorum. Bu süreçte kendinizi ve çevrenizdekileri korumak için, T.C. Sağlık Bakanlığı'nın yayınladığı 14 Kural'a uymanızı tavsiye ederim:"],["Covid-19","Korona virüs ve sebep olduğu COVID-19 hastalığı hakkındaki merak ve endişenizi anlıyorum. Bu süreçte kendinizi ve çevrenizdekileri korumak için, T.C. Sağlık Bakanlığı'nın yayınladığı 14 Kural'a uymanızı tavsiye ederim:"]]

koronaBilgilendirme = pd.DataFrame(korona_bilgilendirme,columns=['soru','cevap'])
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


for i, d in koronaBilgilendirme.iterrows():   
        doc = {
               'sınıfNo' : 2,
               'soru' : d.soru,
               'cevap' : d.cevap
        }
        res = es.index(index="havelsan_chatbot",  body=doc)  
           
##############################################################################
        
              
havelsan_urunler = [["HAVELSAN Diyalog","HAVELSAN Diyalog, kurulumu ve yönetimi kolay, güvenli, yüksek kalitede görüntülü ve sesli görüşme imkanı sağlayan, tamamen yerli bir video konferans sistemidir. "],
                    ["HAVELSAN ASTARBI","HAVELSAN tarafından geliştirilen bir iş zekası ve veri analitiği çözümü olan ASTARBI alan uzmanlarının güvenlik, sağlık, eğitim, ulaşım, bankacılık ve finans gibi alanlarda bilgi işlem teknolojileri ve veritabanı sorgu dili yetkinlikleri gereksinimlerinden bağımsız olarak derinlemesine veri analizi yapabilmelerini sağlamaktadır."],
                    ["HAVELSAN H-ARF","HAVELSAN H-ARF, bir Artırılmış Gerçeklik Uygulama Geliştirme Platformu’dur. Sunduğu modüler yapı ile yüksek performanslı, uygun maliyetli, kaliteli ve hızlı uygulamalar geliştirilebilmektedir. Farklı programlama dillerini destekleyen H-ARF; işletim sistemi, donanım ve cihaz bağımsızdır."],
                    ["HAVELSAN Drive","HAVELSAN Drive bir güvenli dosya depolama ve paylaşım platformudur. Platform, kullanıcıların çeşitli dosyaları kendi sunucularında saklamalarına, tüm mobil cihaz ve bilgisayarlardan erişmelerine ve bunları insanlarla paylaşmalarına izin vermektedir."],
                    ["HAVELSAN T-RAY","HAVELSAN T-RAY, denetim gerektiren havalimanı, sınır ve kritik bina girişleri için tasarlanan aktif Terahertz (THz) görüntüleme teknolojili otonom (insansız) biyometrik güvenli geçiş kontrol ve izleme sistemidir. Havaalanları, limanlar, kara hudutları gibi sınır kapılarında ve kritik bina girişlerinde kullanılması amacıyla çok aşamalı olarak geliştirilen T-RAY sistemi, müdahale gerektiren kişi ve durumlara acil çözüm olanağı sunmaktadır."],
                    ["HAVELSAN ileti","Kurumsal iletişimde bilgi güvenliğini sağlamak ve iletişim sağlanırken verilerin üçüncü şahısların eline geçmesini engellemek için HAVELSAN ileti, kurumun kendi sunucularında çalışmaktadır. Yönetim konsolu ile kullanıcı ilklendirme, kurumsal grup oluşturma gibi işlemler kurum tarafından gerçekleştirilebilmektedir."],
                    ["Havelsan Veri Diyotu","HAVELSAN Veri Diyotu, savunma, güvenlik, enerji, dağıtım şebekeleri, finans kurumları ve hassas veri barındıran izole ağlara sahip olan kurum ve işletmelerin ağlar arası veri aktarımı ihtiyacını karşılamak üzere modüler yapıda geliştirilmiş Yeni Nesil Veri Diyotudur. Farklı güvenlik seviyesindeki ağların kesiştiği noktalarda tek yönlü veri iletimini garanti ederek, yüksek güvenlikli ağdaki hassas verilerin düşük güvenlikli ağlara geçmesini engellemektedir."],
                    ["HAVELSAN EVRAKA’yı ","'Kaynakların etkin ve verimli kullanılması' ve 'Çevreye duyarlılık' ilkelerini kurumsal değerlerinden biri olarak benimsemiş olan HAVELSAN, kâğıda dayalı tüm iş süreçlerini dijital bir ortama taşımak ve kolay, hızlı ve güvenli doküman paylaşımını sağlamak amacıyla tümüyle yerli ve milli imkânlar ile EVRAKA’yı geliştirmiştir."],
                    ["HAVELSAN ATLASCARE ","HAVELSAN, savunma alanındaki yazılım kabiliyet ve deneyimlerini sağlık sektörüne de aktararak güçlü bir katma değer yaratmayı amaçlamaktadır. Bu amaçla, verdiği hizmetlerin etkinliğini arttırmayı hedefleyen sağlık kurumları için bütün operasyonlarını sürekli ve anlık olarak yönetim ve takibini yapabilmelerini sağlayan ATLASCARE e-Sağlık ürün ailesini (e-Health Suite) geliştirmiştir."],
                    ["HAVELSAN GİS","HAVELSAN GİS; farklı işlemci mimarilerine ve donanım yapılandırmalarına uyarlanabilecek şekilde geliştirilmiş bir Gerçek Zamanlı İşletim Sistemidir ve Katmanlı İşlevsel bir mimariye sahiptir. Böylece HAVELSAN GİS, donanım soyutlama katmanlarını -Mimari Destek Paketi (ASP) ve Board Destek Paketi (BSP)- farklı mimarilere ve donanım yapılandırmalarına uyarlayarak birçok platformda kolayca taşınabilir. GİS; çeşitli işlemci mimarileri, donanım yapılandırmaları üzerinde ve emniyet kritik görevlerde misyonunu başarıyla yerine getirmektedir. Yeni platformlar için donanım desteği zamanla arttırılmaktadır."],
                    ["HAVELSAN GÖZCÜ","HAVELSAN GÖZCÜ, Siber Olay Yönetim ve Alarm Sistemi; kurumunuzun bilişim altyapısı bileşenlerinin oluşturdukları kayıtların merkezi olarak toplanmasını, ilişkilendirilmesini, sorgulanmasını ve alarm üretilmesini sağlayan; tamamen HAVELSAN mühendisleri tarafından milli imkanlarla geliştirilmiş yerli bir SIEM yazılımıdır."],
                    ["HAVELSAN KALKAN","HAVELSAN KALKAN, yüzde yüz milli imkanlar ile geliştirilmiş ve çok yüksek seviye ağ trafikleri için yük dengeleme sağlayan, siber saldırı hedeflerinin başında yer alan web uygulamalarına yönelik saldırıları tespit edip engelleyebilen Yük Dengeleme/Web Uygulama Güvenlik Duvarı ürünüdür. Web uygulamalarını korumak üzere özel olarak tasarlanmış bu ürün ile klasik güvenlik duvarları, saldırı engelleme sistemleri gibi yazılımlar tarafından tespit edilmesi mümkün olmayan saldırıların engellenmesine imkân sağlanmaktadır."],
                    ["HAVELSAN BARİYER","HAVELSAN BARİYER, kurum dışına izinsiz veri çıkışının önlenmesi, belirlenen engelleme kurallarına uygun olarak bilgi güvenliğinin sağlanması, verinin olması gereken yerde bulunduğu ve doğru kullanıcılar tarafından erişildiğinin denetlenmesi ve kontrol edilmesine imkan sağlayan PARDUS ile uyumlu yerli bir veri sızıntısı önleme (Data Leakage Prevention - DLP) ürünüdür. HAVELSAN tarafından tamamen yerli ve milli kaynaklar ile geliştirilmiş olan HAVELSAN BARİYER, büyük ve küçük kamu kurumlarının, diğer sivil kurum ve kuruluşların ve askeri kurumların özel güvenlik ihtiyaçlarını sağlayacak düzeyde yüksek performansa sahiptir."],
                    ["Siber Güvenlik hizmetleri","HAVELSAN, tüm kurumların elektronik ortamda muhafaza ettikleri verilerin her türlü siber güvenlik tehdidine karşı korunmasına yönelik ürün, danışmanlık ve eğitim gibi Siber Güvenlik hizmetleri sunmaktadır."],
                    ["ANALİZ VE TEST HİZMETLERİ","Türk Standartları Enstitüsü (TSE) ‘‘TS 13638 Sızma Testi Hizmeti Veren Firma Yetkilendirme’’ esaslarına göre “A Yetkinlik Seviyesinde Firma” gereksinimlerini sağlayan ilk firma olan HAVELSAN, Sızma Testi ve Zafiyet Denetimleri konularındaki hizmetlerini halen A Yetkinlik Seviyesi ile sürdürmektedir. HAVELSAN tarafından sunulan Sızma Testi, Zafiyet Denetimi ve Kaynak Kod Güvenlik Analizi gibi hizmetler TS ISO/IEC 27001:2013 Bilgi Güvenliği Yönetim Sistemi sertifikasyonu kapsamında, deneyimli ve uluslararası geçerliliği bulunan CISSP, GPEN, OCSP, OCSE, OSWE, CEH, GREM vb. sertifikalarına sahip uzman personelimiz ile sunulmaktadır."],["DANIŞMANLIK HİZMETLERİ","HAVELSAN kapsamın belirlenmesi aşamasından sertifikasyon sonrasındaki garanti ve bakım dönemi dahil Bilgi Güvenliği Yönetim Sistemi kurulum ve işletim süreçlerinin her aşamasında kurumlar tarafından ihtiyaç duyulan danışmanlık, eğitim ve test hizmetlerini sağlamakta, kurumlara BGYS alanında anahtar teslim çözümler sunmaktadır."],["SİBER GÜVENLİK AKADEMİSİ","HAVELSAN Siber Savunma Teknoloji Merkezi (SİSATEM), siber güvenlik personelinizin yeteneklerini güçlendirmek ve kurumunuzun bu alandaki kapasitesini arttırmak için çeşitli seviyelerde teorik ve uygulamalı siber güvenlik eğitimleri sunan bir uzmanlık merkezidir."],["Hızlandırılmış Proje Desteği","Hızlandırılmış Proje Yönetimi desteği, işletme ve mühendislik varlıklarını özünde birbirine bağlayan “Teslim Edilebilir Tabanlı Proje Yönetimi” sağlamaktadır. Bu birleşik mimari, yönetim yükünü önlerken, zamanlama, kilometre taşları, kaynaklar, maliyetler ve faydalar açısından gerçek proje durumu üzerinde gerçek zamanlı görünürlük için dinamik proje panoları sağlamaktadır. Bu panolar kullanılarak projenin; entegrasyon, kapsam, takvim, maliyet, kalite, kaynak, iletişim, risk, tedarik süreçlerindeki yönetim kapasitesi artırılmaktadır."],["HAVELSAN tarafından sunulan BT Çözümleri","Kurumların; dijital teknolojilerin, yenilikçi fırsatlarıyla iş süreçlerine uyarlanması ve dijital teknolojiler doğrultusunda yeni katma değerli hizmet ve süreçler oluşturulması dijital dönüşümün en öncelikli amacı olmaktadır. Dijital dönüşüm ihtiyaçlarını analiz edip referanslar doğrultusunda yönlendirecek bir model oluşturulması gerekmektedir. Bu çalışma sonucunda eksik, yetersiz veya verimsiz süreçlerin tespit edilerek, uygun çözüm, ürün veya hizmetlerin konumlandırılması hedeflenmektedir."],["ÜRÜNLEŞTİRME VE ÜRÜN GERÇEKLEŞTİRME HİZMETLERİ","Teknik Danışmanlık, Değerlendirme ve Denetleme, Etüd, Proje konularında teknik danışmanlık hizmeti sağlanmaktadır."],["Lojistik Hizmeti","Bilgi teknolojileri ve iletişim alanındaki sistemler ile ilgili lojistik hizmet ihtiyacı duyulduğunda HAVELSAN uzman kadrosu ile destek vermektedir. Sözleşmeye esas lojistik ihtiyacı kapsamında ihtiyaç duyulan malzemenin tedariki, kabulü, depolanması, doğru malzemenin doğru yere, doğru zamanda gönderilmesi, iadesinin planlanması ve yerine getirilmesi, hurda/terkin/hibe işlemleri sağlanabilmektedir."],["HAVELSAN Servis Masası","HAVELSAN Servis Masası, taahhüt edilen servis seviyelerinde çağrılarınızın karşılanması, kayıt altına alınması, doğru kanala iletilmesi, takibi, raporlanması, çözümü ve analizi için tek temas noktasıdır."],["BÜYÜK VERİ VE MADENCİLİĞİ","Sayısallaştırma, Büyük Veri İşleme, Veri Madenciliği, Makine Öğrenmesi / Derin Öğrenme, Sentiment Analiz ve İleri İş Zekâsı, Veri Entegrasyonu ve İçerik Yönetimi, Veri Sözlüğü Oluşturma, Geliştirme ve Güncelleme konu başlıklarındaki konularda çalışmalar yapmaktadır."]]

havelsanuUrun = pd.DataFrame(havelsan_urunler,columns=['soru','cevap'])

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


for i, d in havelsanuUrun.iterrows():   
        doc = {
               'sınıfNo' : 3,
               'soru' : d.soru,
               'cevap' : d.cevap
        }
        res = es.index(index="havelsan_chatbot",  body=doc) 
        
#############################################################################################

fikir_talebi = [["Fikir sunmak istiyorum","Fikirlerin bizim için çok önemli. Unutma fikirlerini her zaman bizimle paylaşabilir ve gerçekleşmesine bir adım daha yaklaşabilirsin. Aşağıdaki linkteki öneri formunu kullanarak yenilikçi fikir ve  önerilerini bizimle paylaşabilirsin."],[" yenilikçi fikirim var","Fikirlerin bizim için çok önemli. Unutma fikirlerini her zaman bizimle paylaşabilir ve gerçekleşmesine bir adım daha yaklaşabilirsin. Aşağıdaki linkteki öneri formunu kullanarak yenilikçi fikir ve  önerilerini bizimle paylaşabilirsin."],["hayal ettiğim yeni bir proje bulunuyor","Fikirlerin bizim için çok önemli. Unutma fikirlerini her zaman bizimle paylaşabilir ve gerçekleşmesine bir adım daha yaklaşabilirsin. Aşağıdaki linkteki öneri formunu kullanarak yenilikçi fikir ve  önerilerini bizimle paylaşabilirsin."],]

fikirTalebi = pd.DataFrame(fikir_talebi,columns=['soru','cevap'])

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


for i, d in fikirTalebi.iterrows():   
        doc = {
               'sınıfNo' : 4,
               'soru' : d.soru,
               'cevap' : d.cevap
        }
        res = es.index(index="havelsan_chatbot",  body=doc) 

######################################################################################3
        
is_ekosistemi = [["HAVELSAN İŞ EKOSİSTEMİ YAKLAŞIMI nasıldır?","HAVELSAN olarak, Savunma, Güvenlik ve Bilişim sektörlerinde Yerli ve Milli markalı Ürün/Hizmet/Sistem üretmeye ve geliştirmeye yönelik stratejilerimizin, alanlarında uzmanlaşmış, yenilikçi, rekabetçi maliyet-kalite-zaman-performans odaklı firmalarımızla iletişimin ve eşgüdümün kuvvetli bir tedarik zinciri yönetimi ile mümkün olduğuna inanmaktayız. Bu doğrultuda Güç Birliği, Güçlü İşbirliği yaklaşımı üzerine yapılandırmış olduğumuz “İş Ortaklıkları Yönetim Sistemi'miz ile hareket etmekteyiz."],["İŞ EKOSİSTEMİ UYGULAMA SÜRECİ nasıl ilerler ?","Süreçimizle 7 aşamada yürütülmektedir:1)Başvuru/Ön değerlendirme, 2)Ön Değerlendirme Onay Tedarikçi Portali şifresi gönderilerek kayıt altına alma, 3)İdari-Kalite ve teknik yönlerden Değerlendirme, 4)Puanlama /Sınıflandırma, 5)Değerlendirme Analiz Raporu, 6)İhale Süreci/Firma seçimi İşbirliği/Sözleşme, 7)Genel performans değerlendirme"],["İş Ortağı/Tedarikçi Başvuru ve Ön Değerlendirme"," Sisteme kayıtlı olmayan firma iseko@havelsan.com.tr adresine firmasını tanıtan bir sunumu ileterek HAVELSAN İş Ekosistemine başvuru yapmak istediğini bildirmesi gerekmektedir. Başvuru değerlendirilerek HAVELSAN faaliyet alanlarına uygun faaliyetlerde bulunan firmalara HAVELSAN tarafından gönderilecek İş Ekosistemi Ön Değerlendirme Portalinde istenilen bilgileri doldurup onaylayarak ön değerlendirme işlemini tamamlayacaktır. Ön değerlendirmede sürecinde toplamda 100 puan üzerinden 50 ve üzeri puan alan ve faaliyet alanları ile uygun görülen Firma onaylanarak İş Ekosistemi Tedarikçi Portal Şifresi gönderilir"],
    
    ["Tedarikçi Portali Kayıt İşlemi","Firmanıza özel Tedarikçi Portal Giriş Şifresi Firmanız ile HAVELSAN arasında kurulacak işbirliği adımlarının atılmasına yönelik bir anahtar olduğu kabul edilerek, firmanızdan bu süreçte Portal İçerisinde istenilen bilgilerin detaylı doldurulması uzun yıllara dayanan bir işbirliği ortamının kurulmasına adım ve katkı sağlayacaktır. HAVELSAN İş Ekosistemi Tedarikçi Portalinde sizden istenilen tüm bilgileri ve ekleri tamamlayarak ilk aşamada Kayıtlı Aday İş Ortağı/Alt Yüklenici durumuna geçilmiş olunacaktır. Söz konusu doldurulan bilgilere yönelik detaylı bilgiye ihtiyaç duyulması halinde sizinle ayrıca temasa geçilebilecektir."],["Firmanıza Yönelik Yerinde İnceleme yapılır mı? ","Firmanız tarafından doldurulan bilgiler doğrultusunda, HAVELSAN A.Ş. personeli ve/veya HAVELSAN tarafından yetkilendirilmiş Bağımsız Denetim Firması tarafından Firmanıza Yönelik yapılacak İdari, Kalite ve Teknik uygulamalarına yönelik değerlendirme yapılacaktır. Değerlendirmeler neticesinde toplamda 100 Puan üzerinden firmanız tarafından sunulacak bilgi, dökümantasyon, kaynaklar ve yetkinlikler değerlendirilerek A-B-C-D Grubu olmak üzere bir sınıflandırılma yapılarak, firmanıza yönelik Değerlendirme Analizi raporu hazırlanmaktadır. Bu çalışmalar kapsamında, firmanız tarafından sağlanacak tüm bilgi ve belgeler üçüncü taraflarla paylaşılmayacaktır. “TİCARİ GİZLİ” olarak muhafaza edilecektir. Söz konusu çalışmalar firmanızı ve/veya HAVELSAN’ı hiçbir yükümlülük altına sokmayacak olup herhangi bir taahhüt içermemektedir."] ,["iş ortaklığında bulunmak için ne yapabiliriz ?","Sisteme kayıtlı olmayan firma iseko@havelsan.com.tr adresine firmasını tanıtan bir sunumu ileterek HAVELSAN İş Ekosistemine başvuru yapmak istediğini bildirmesi gerekmektedir. Başvuru değerlendirilerek HAVELSAN faaliyet alanlarına uygun faaliyetlerde bulunan firmalara HAVELSAN tarafından gönderilecek İş Ekosistemi Ön Değerlendirme Portalinde istenilen bilgileri doldurup onaylayarak ön değerlendirme işlemini tamamlayacaktır. Ön değerlendirmede sürecinde toplamda 100 puan üzerinden 50 ve üzeri puan alan ve faaliyet alanları ile uygun görülen Firma onaylanarak İş Ekosistemi Tedarikçi Portal Şifresi gönderilir"]]
    
isEkosistemi = pd.DataFrame(is_ekosistemi,columns=['soru','cevap'])

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


for i, d in isEkosistemi.iterrows():   
        doc = {
               'sınıfNo' : 5,
               'soru' : d.soru,
               'cevap' : d.cevap
        }
        res = es.index(index="havelsan_chatbot",  body=doc) 
        
        
       
#    
#from elasticsearch import Elasticsearch
#es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#
#canceledWords = ["iptal","kapat", "vazgeç", "değişiklik", "geri dön", "başka yanıt","bilmiyorum"]
#iptal = pd.DataFrame(canceledWords,columns=['soru'])
#for i, d in iptal.iterrows():   
#        doc = {
#               'sınıfNo' : 1,
#               'tipNo' : -2,
#               'soru' : d.soru,
#        }
#        res = es.index(index="havelsan_chatbot",  body=doc)  
#        
#    
    





# =============================================================================
## ONAY CÜMLELERİ VERİ GİRİŞİ
#approve = ["onayla","onaylıyorum" , "kabul" , "isterim" ,"onayladım", "onaylarım", "onaylamak "  , "evet", "onaylayın" , "evet lütfen","mümkünse evet", "onay veriyorum", "onayladık" , "onaylanmıştır", "kabuldür" , "evet ilerleyelim", "elbette" ,"kesinlikle" ,"olur"]
#
#
#
#
#dissapprove = [ "hayır", "onaylama","onaylamıyorum", "kabul etmiyorum" , "istemiyorum","istemem", "onaylamam", "onaylamayacağım" , "onaylamak istemem" , "hayır", "kesinlikle hayır", "iptal" , "iptal edilsin" , "işlemi sonlandırın" , "vazgeçtim", "kararımı değiştirdim" , "işlem iptali istiyorum", "çıkış yap" ,"asla", "öyle değil","imkansız", "yok", "vazgeçtik" , "vazgeçiyorum" , "onay vermiyorum", "kabul değil" , "onay değil", "onay yok" , "fikrimi değiştirdim" , "karar değiştirdim", "güncelleme yapmak istiyorum" , "işlem değiştirmek istiyorum" , "bilgi değiştirmek istiyorum", "iptal istiyorum" ,"geri dön", "geri döner misin" ,"telefon bilgisi değiştirmek istiyorum", "yanlış adres girmişim", "tekliften vazgeçtim" , "sonuç güzel değil", "bilgilerimi değiştireceğim", "teklifleri beğenmedim" ,"tekliften vazgeçtim", "firmadan vazgeçtim" , "onay vermek istemiyorum", "onaylamayın", "onay vermeyeceğim"]
#for sent in approve:
#    doc = {
#        'tip' : 'onay',
#        'cevap' : sent
#    }
#    res = es.index(index="onay_red", body=doc)
#    
#for sent in dissapprove:
#    doc = {
#        'tip' : 'red',
#        'cevap' : sent
#    }
#    res = es.index(index="onay_red", body=doc)
# =============================================================================
#from elasticsearch import Elasticsearch
#es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#
#onay_red = ["tamam","ok", "okey", "tamamdır"]
#iptal = pd.DataFrame(onay_red,columns=['soru'])
#for i, d in iptal.iterrows():   
#        doc = {
#               'sınıfNo' : 2,
#               'tipNo' : -2,
#               'soru' : d.soru,
#        }
#        res = es.index(index="havelsan_chatbot",  body=doc)  
#        
#        
#          
#       
