import os
import pymongo
import csv

from pymongo import MongoClient

class veritabanı:
    #MLAB BAĞLANTI KODLARI
    MONGODB_URI = "mongodb://test:test12@ds159707.mlab.com:59707/tw"
    client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
    db = client.get_database()
    vt_database = db.database
    vt_sozluk=db.sozluk
    vt_klasor=db.klasor
    #METOTLAR
    def veriEkle(self,veri):
           self.vt_database.insert_one(veri)
    
    def sozlukEkle(self,sozluk):
           self.vt_sozluk.insert_one(sozluk)

    def getSozluk(self,user_name):
        records = self.vt_sozluk.find_one({"name":user_name})
        return records
    
    def sozlukGuncelle(self,record, updates):
        self.vt_sozluk.update_one({'name': record['name']},{
                              '$set': updates
                              }, upsert=False)
    
    def klasorEkle(self,klasor):
           self.vt_klasor.insert_one(klasor)

    def getKlasor(self,klasor_isim):
        records = self.vt_klasor.find_one({"klasor_isim":klasor_isim})
        return records
    
    def klasorGuncelle(self,record, updates):
        self.vt_klasor.update_one({'klasor_isim': record['klasor_isim']},{
                              '$set': updates
                              }, upsert=False)


#Atılan tweetlerin olduğu klasor
dosyayolu="C:\\Users\\Halil\\Downloads\\EagleDownload\\Twcollector12345-20181203T184922Z-001\\Twcollector12345\\"

def ayristir(path):
    dirList=os.listdir(path)
    dirList.sort()
    #verilen konumdaki dosyalar
    fnames = []
    #verilen konumdaki klasorler
    dnames = []

    for fname in dirList:
        if os.path.isdir(path + fname):
            dnames.append(fname)
        if os.path.isfile(path + fname):
            fnames.append(fname)

    return dnames,fnames


#VERİTABANI İŞLEMLERİNİ YAPACAGIM NESNE
vtys=veritabanı()


#Twcollector12345 dosyasının içerisindeki dosya ve klasorler
(klasorler,dosyalar) = ayristir(dosyayolu)

#SOZLUK BİR KULLANICININ KAÇ TANE TWEET'İ OLDUGUNU TUTUYOR
sozluk={}
#klasorSozluk TWCOLLECTOR 1-2-3-4-5 KLASORLERININ İÇERİSİNDE KAÇ TANE TWEET
#OLD. TUTUYOR
klasorSozluk={}


for item in klasorler:
    dosyayolu2=dosyayolu+item+"\\"
#Twcollector12345 klasorunun içerisinde yer alan Twcollector 1-2-3-4-5 klasorlerinin içerisindeki dosyaları alıyorum.
    (klasorler2,dosyalar2) = ayristir(dosyayolu2)


   

    #buradaki for'da tweetlerin kayıtlı olduğu exel dosyalarını okuma işlemi yapıyorum.
    for item2 in dosyalar2:
        #CSV DOSYA OKUMA
        dos = "C:\\Users\\Halil\\Downloads\\EagleDownload\\Twcollector12345-20181203T184922Z-001\\Twcollector12345\\"+item+"\\"

        #EXEL DOSYA OKUMA
        f = open(dos+item2, 'r',encoding="utf-8")
        
        with f:
            reader=csv.reader(f)
            #tweet_id,tarih gibi bilgileri alma
            for row in reader:
                tweet_id=row[0]
                tarih=row[1]
                kullanici_adi=row[2]
                tweet=row[3]

                #aldığım tweet bilgilerini JSON objesine dönüştürdüm
                veri = {
                "tweet_id": tweet_id,
                "date": tarih,
                "user_name": kullanici_adi,
                "text":tweet
                }
                try:
                    #verileri ekledim eğer veri daha önce eklenmiş ise  pymongo.errors.DuplicateKeyError hatası atacaktır tweet_id UNIQE
                    vtys.veriEkle(veri)

                    #Sozlukten kullanıcı adını alıyorum ve attığı tweet sayısını bir arttırıyorum eğer kullanıcı yok ise
                    #KeyError hatası atacaktır
                    i=int(sozluk[kullanici_adi])
                    i+=1
                    sozluk[kullanici_adi]=str(i)
                    
                except pymongo.errors.DuplicateKeyError:
                    #Tweet_id üniqeu olarak tanımlı bir tweet daha önce eklenmiş ise hata bastım
                    print("Bu tweet zaten eklidir.")

                    
                except KeyError:
                    #hata atmış ise sozlukte kullanıcı ismi yoktur veritabanınada bakıyorum kayıtlımı bu kullanıcı diye
                    cevap=vtys.getSozluk(kullanici_adi)
                    if (cevap == None) :
                        #veritabanında kullanıcı kayıtlı değil ise sozluge kullanıcı adını ekliyorum ve tweet sayısını
                        #1 den başlatıyorum
                        sozluk[kullanici_adi]="1"
                    else :
                        #bu kullanıcıya ait daha önce tweet eklenmiş ise onların sayısını ekle
                        #veritabanında kullanıcının tweet sayısını alma kısmı
                        #tweet_sayisini kullanıcı ismi ile birlikte sozluğe ekledim
                        
                        isim=str(cevap["name"])
                        tweet_adet=str(cevap["tweet_sayisi"])
                        sozluk[isim]=tweet_adet
            
            
            tw_adet_sayi=int(sozluk[kullanici_adi])
            #twcollector klasorlerıne ait daha önce tweet eklenmiş ise onun sayısını alıyorum
            cevap2 =vtys.getKlasor(item)
            
            if(cevap2 == None):
                #eğer daha once eklenmemiş ise klasorSozluge ekliyorum ve ilk değerini sıfır veriyorm
                klasorSozluk[item]="0"
            else :
                #eğer daha önce eklenmiş ise bu bilgiyi alıp klasorSozluge ekliyorum
                klasor_isim=str(cevap2["klasor_isim"])
                tweet_sayisi2=str(cevap2["tweet_sayisi"])
                sozluk[item]=tweet_sayisi2


            #burdada en son işlenen exel'e ait bilgileri ekliyorum
            klasor_tweet_sayisi2=int(klasorSozluk[item])
            klasor_tweet_sayisi2+=tw_adet_sayi
            klasorSozluk[item]=klasor_tweet_sayisi2


            
            
        
        
        #Bu kısım chart şemları için tutulan istatistikleri veritabanına kaydetme yeridir.
        #yukarıdaki tanımladığımız sözluk ve sozlukKLasor'ün son halini veritabanına kayıt edıyorum.
        for i,j in sozluk.items():
            #bu i sozlukteki anahtar kelime j de anahtar kelimeye karşılık gelen bilgi
            sozlukEkleme={
                    "name":i,
                    "tweet_sayisi":j,
                    }
            try:
                #burada try içine alma sebebım sozluk tablosunda 'name' unique tanımlıdır.bir kullanıcı daha önce ekli
                #ise pymongo.errors.DuplicateKeyError hatası atacaktır ve bu durumda ekleme yerine güncelleme yapıyorum
                vtys.sozlukEkle(sozlukEkleme)
            except pymongo.errors.DuplicateKeyError :
                guncelle={"name":i}
                guncelle_tweetler={"tweet_sayisi":j}
                vtys.sozlukGuncelle(guncelle,guncelle_tweetler)

        #yukarıdaki for ile aynı işlemi yapıyor,klasorlerdeki tweet sayısını kayıt ediyor. 
        for i,j in klasorSozluk.items():
            
            klasorleriekleme={
                "klasor_isim":i,
                "tweet_sayisi":j,
                    }

            
            try:
                vtys.klasorEkle(klasorleriekleme)
            except pymongo.errors.DuplicateKeyError :
                guncelle={"klasor_isim":i}
                guncelle_tweetler={"tweet_sayisi":j}
                vtys.klasorGuncelle(guncelle,guncelle_tweetler)




































