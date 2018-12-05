# mlab_proje1

**veri_parcala.py Calışma Mantığı**

  Bana verilen twcollector12345 klasorunun içerisindeki dosyaları listeledim.Daha sonra bu twcollector 1-2-3-4-5 dosyalarının içerisinde
  yer alan bütün exel dosyalarını tek tek okudum.Exel dosyalarını satır satır okudum.1 satır okuduktan sonra "," ile satırı parçaladım ve 
  veritabanına ekledim.Ve bu ekleme işlemlerini yaparken 2 tane sözlük kullandım.Bunlardan 1 tanesi 'sozluk' diğeride 'klasorSozluk' dir.
  
    sozluk={"kullanıcı_adı":"tweet_sayisi"} ==> kullanıcıların kaç tane tweet attığını barındırıyor.
    klasorSozluk={"klasor_isim":"tweet_sayisi"} ==> 1 klasorun içerinde kaç tane tweet olduğunu tutuyor
   
   
**bar-chart.py Calışma Mantığı**<br>
  Veritabanına kaydettiğim verileri pymongo modülü ile alıp  matplotlib modülü  ile grafiksel olarak gösterdim.


**VERİTABANI TABLOLARI**

VERİTABANINDA BULUN TABLOLAR

![tablolar](https://github.com/halilerisen/mlab_proje1/blob/master/images/tablolar.PNG)

ATILAN TWEETLERİN TUTULDUĞU TABLO

![tweet bilgileri](https://github.com/halilerisen/mlab_proje1/blob/master/images/database%20tablosu.PNG)<BR>
HANGİ KULLANICI KAÇ TANE TWEET ATTIĞINI TUTAN TABLO
![kullanıcı tweet sayisi](https://github.com/halilerisen/mlab_proje1/blob/master/images/sozluk%20tablosu.PNG)<BR>
KLASORLERİN İÇERİNDE YER ALAN TOPLAM TWEET SAYISI TABLOSU
![KLASOR İÇERİNDE YER ALAN TWEET SAYISI](https://github.com/halilerisen/mlab_proje1/blob/master/images/klasor_tweet_tablosu.PNG)

PİE-CHART(KLASOR İÇERİNDE YER ALAN TWEET MİKTARINA GÖRE) <BR>
![PİE-CHART](https://github.com/halilerisen/mlab_proje1/blob/master/images/pie-chart.PNG)

BAR-CHART(KULLANICILARIN ATTIĞI TWEET SAYISINA GÖRE) <BR>
![PİE-CHART](https://github.com/halilerisen/mlab_proje1/blob/master/images/bar-chart.png)
