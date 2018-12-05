import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pymongo

from pymongo import MongoClient


#VERİTABANI BAĞLANTILARI

class veritabanı:
    #MLAB BAĞLANTI KODLARI
    MONGODB_URI = "mongodb://test:test12@ds159707.mlab.com:59707/tw"
    client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
    db = client.get_database()
    #VERİTABANI TABLOLAR
    vt_sozluk=db.sozluk
    vt_klasor=db.klasor
    
    
    #FONKSIYONLAR 
    def getSozluk(self):
        records = self.vt_sozluk.find({})
        return records
    
    def getKlasor(self):
        records = self.vt_klasor.find({})
        return records
    
    
    
    

vtys=veritabanı()
#BAR-CHART SUTUNLARI
sutun1=0
sutun2=0
sutun3=0
sutun4=0
sutun5=0
sutun6=0

sonuc=vtys.getSozluk()

for i in sonuc :
    tws=int(i["tweet_sayisi"])
    if tws >=1 and tws < 200:
        sutun1+=1
    elif tws >= 200 and tws < 500:
        sutun2+=1
    elif tws >= 500 and tws < 1000:
        sutun3+=1
    elif tws >= 1000 and tws < 2000:
        sutun4+=1
    elif tws >= 2000 and tws < 3000:
        sutun5+=1
    elif tws >= 3000 :
        sutun6+=1

sonuc2=vtys.getKlasor()
#PİE-CHART BİLGİLERİ

tw1=str(sonuc2[0]["klasor_isim"])
tw2=str(sonuc2[1]["klasor_isim"])
tw3=str(sonuc2[2]["klasor_isim"])
tw4=str(sonuc2[3]["klasor_isim"])
tw5=str(sonuc2[4]["klasor_isim"])

tws1=int(sonuc2[0]["tweet_sayisi"])
tws2=int(sonuc2[1]["tweet_sayisi"])
tws3=int(sonuc2[2]["tweet_sayisi"])
tws4=int(sonuc2[3]["tweet_sayisi"])
tws5=int(sonuc2[4]["tweet_sayisi"])


labels = tw1, tw2, tw3,tw4,tw5

sizes = [tws1, tws2, tws3, tws4,tws5]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','blue']
explode = (0, 0, 0, 0,0)

 
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()#PİE-CHART

 
objects = ('1-200', '200-500', '500-1000', '1000-2000', '2000-3000', '3000-...')
y_pos = np.arange(len(objects))
performance = [sutun1,sutun2,sutun3,sutun4,sutun5,sutun6]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Kullanıcısı Sayısı')
plt.title('Tweet sayısı')

plt.show()#BAR-CHART
