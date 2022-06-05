from io import TextIOWrapper
import time
import datetime
import webbrowser




class Otomasyon():
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True
    # Otomasyon menü fonksiyon seçimi 
    
    def program(self):
        secim = self.menuSecim()

        if secim == 1:
            self.kurulumGir()
        if secim == 2:
            self.sikayetGir()
        if secim == 3:
            self.arizaEkle()
        if secim == 4:
            self.musteriHizmetleri()
        if secim == 5:
             self.web_sitemize_gozatın()   
    # Otomasyon menü seçim ekranı
        time.sleep(3)#3saniye sonra açılıyor (yenileniyor)
    def menuSecim(self):
        print(" \n")
        try:#hata verebileceğini düşündüğümüz kodlar
         secim =int( input("**** {}'na hoş geldiniz ****\n\nLütfen yardım talebi almak istediğiniz konuyu seçiniz: \n\n 1-Kurulum Yardımı \n 2-Şikayet Bildir \n 3-Arıza Ekle\n 4-Müşteri hizmetleri\n 5-Web Sitemize Gözatın!\n\nSeçiminizi Giriniz: ".format(self.ad)))
         while secim < 1 or secim > 5:
            secim = int(input("Lütfen 1 - 4 arasında belirtilen seçeneklerden birini giriniz!"))
        except ValueError:#hata ayıklama işlemi (hata durumunda yapılacak işlem.)
            print("Lütfen Sayı Değeri Giriniz!")
        time.sleep(1)
      
        return secim
        pass


       
    # Kurulum yardımı oluşturma
    def kurulumGir(self):
        print("Lütfen Bekleyiniz..")
        time.sleep(1)#1 saniye kadar bekletme işlemi öncesinde lütfen bekleyiniz ikazı 
        
        kurulumSecim = int(input("\nLütfen kurulum yapmak istediğiniz ürünü seçiniz.\n\n1-Buzdolabı\n2-Fırın\n3-Çamaşır makinesi\n4-Derin Dondurucu\n5-Ütü\n6-Klima\n7-Şofben\n8-Elektrikli Süpürge\n9-Bulaşık Makinesi\n10-Diğer model\n\nSecim: "))
        
        while kurulumSecim < 1 or kurulumSecim > 10:
            kurulumSecim = int(input("Lütfen 1 ile 10 arasında bir seçim yapınız: "))
        
        if kurulumSecim == 1:
            A = str(input("A MODEL BUZDOLABI İÇİN [a]:\n B MODEL BUZDOLABI İÇİN [b]:\n Lütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("")
            if A : "b"
            webbrowser.open("")
        if kurulumSecim == 2:

            A = str(input("A MODEL FIRIN İÇİN [a]:\n B MODEL FIRIN İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("")
            if A: "b"
            webbrowser.open("")
        if kurulumSecim == 3:
            A = str(input("A MODEL ÇAMAŞIR MAKİNESİ İÇİN [a]:\n B MODEL ÇAMAŞIR MAKİNESİ İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("")
            if A :"b"
            webbrowser.open("")
        if kurulumSecim == 4:
            A = str(input("A MODEL DERİN DONDURUCU İÇİN [a]:\n B MODEL DERİN DONDURUCU İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("")
            if A :"b"
            webbrowser.open("")
        if kurulumSecim == 5:
            A = str(input("A MODEL ÜTÜ İÇİN [a]:\n B MODEL ÜTÜ İÇİN [b]:"))
            if A :"a"
            webbrowser.open("")
            if A : "b"
            webbrowser.open("")
        if kurulumSecim == 6:
            A = str(input("A MODEL KLİMA İÇİN [a]:\n B MODEL KLİMA İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("")
            if A :"b"
            webbrowser.open("")
        if kurulumSecim == 7:
            A = str(input("A MODEL ŞOFBEN İÇİN [a]:\n B MODEL ŞOFBEN İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("")
            if A : "b"
            webbrowser.open("")
        if kurulumSecim == 8:
            A = str(input("A MODEL SÜPÜRGE İÇİN [a]:\n B MODEL SÜPÜRGE İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a" 
            webbrowser.open("")
            if A : "b"
            webbrowser.open("")
        if kurulumSecim == 9:
            A = str(input("A MODEL BULAŞIK MAKİNESİ İÇİN [a]:\n B MODEL BULAŞIK MAKİNESİ  İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("")
            if A :"b"
            webbrowser.open("")
        if kurulumSecim == 10:

         digerModel = str(input("Lütfen kurulum yapmak istediğiniz ürünün modelini giriniz: "))
         print(" \n" + digerModel + " için kullanım kılavuzu linki:>>>  https://teknikservissciniz.unaux.com  <<< ")
            

        pass
        time.sleep(2)
        print("lütfen bekleyiniz..")
    # Şikayet talebi oluşturma (text olarak kaydetme eklenecek)
    def sikayetGir(self):
        time.sleep(1)
        sikayetSebebi=int(input("Şikayet sebebinizi şeçiniz:\n\n1-Personel hakkında\n2-Ürünlerimiz hakkında\n3-Diğer\n\nSeçim: "))
        
        while sikayetSebebi < 1 or sikayetSebebi > 3:
            sikayetSebebi = int(input("Lütfen 1 ile 3 arasında bir seçim yapınız: "))
        
        if sikayetSebebi == 1:
            personelSikayet = int(input("\nPersonel hakkındaki şikaetinizi belirtiniz:\n\n1-Kaba\n2-İşini düzgün yapmıyor\n3-Ürüne zarar verme\n4-Diğer\n\nSeçim: "))
            while personelSikayet < 1 or personelSikayet > 4:
                personelSikayet = int(input("Lütfen 1 ile 4 arasında bir seçim yapınız: "))
            if personelSikayet == 4:
                input("Lütfen personel hakkındaki şikayetinizi belirtiniz:")

        if sikayetSebebi == 2:
            urunSikayet = int(input("Ürün hakkındaki şikayetinizi seçiniz.\n1-Arızalı ürün \n2-Ürün gürültülü çalışıyor \n3-Diğer\nSeçim: "))
            while urunSikayet < 1 or urunSikayet > 3:
                urunSikayet = int(input("Lütfen 1 ile 3 arasında bir seçim yapınız: "))              
            if urunSikayet == 3:
                input("Lütfen ürün hakkındaki şikayetinizi belirtiniz:")
        
        if sikayetSebebi == 3:
            sikayet = input("Lütfen şikayetinizi belirtiniz:")
            dosya = open("Şikayet Talebi.txt","a",encoding="utf-8")
            dosya.write("Müşteri şikayeti: "+sikayet+"\n")
        
        
        print("\n\nŞikayet talebiniz alınmıştır\n")

        pass
        time.sleep(2)
        print("lütfen bekleyiniz..")
    # Ariza talebi oluşturma
    def arizaEkle(self):
        time.sleep(1)
        #Günün tarihini getiren datetime modülü tanımlandı
        tarih = datetime.datetime.now()
        a = str(tarih)
       
        isim = input("Adınızı giriniz: ") 
        soyisim = input("Soyadınızı giriniz: ") 
        urunadi = input("Arıza kaydı oluşturacağınız ürün adını giriniz: ")
        urunariza = input ("Arızanın ne olduğunu düşünüyorsunuz: ") 
        acikadres = input("Adresinizi  giriniz: ")
        garantisuresi = input("Garanti sürenizi giriniz: ")
        

        #dosya adında bi parametre oluşturularak Arıza Talebi.txt adlı text dosyası oluşturuldu
        dosya = open("Arıza Talebi.txt","a",encoding="utf-8")
        
        
        dosya.write("Müşteri adı: "+isim+"\n")
        dosya.write("Müşteri soyadı: "+soyisim+"\n")
        dosya.write("Ürün adı: "+urunadi+"\n")
        dosya.write("Ürün şikayeti: "+urunariza+"\n")
        dosya.write("Müşterinin açık adresi: "+acikadres+"\n")
        dosya.write("Ürünün garanti süresi: "+garantisuresi+"\n")
        #Günün tarihi gün, ay, yıl olarak tanımlanıp hata vermemesi adına string değere dönüştürülerek dosyaya yazdırıldı
        dosya.write("Tarih: "+ str(tarih.day)+"/"+str(tarih.month)+"/"+str(tarih.year)+"\n")
        dosya.write("------------\n")

        print("\nTeşekkür ederiz.\nArıza talebiniz başarı ile oluşturulmuştur.\n")

        time.sleep(2)
        print("lütfen bekleyiniz..")
    #Müşteri hizmetleri ile iletişime geçme
    def musteriHizmetleri(self):
        time.sleep(1)
        iletisimSecim = int(input("Müşteri hizmetleri ile iletişime geçme yönteminizi seçiniz:\n\n1-Telefon görüşmesi\n2-E-posta\nSeçim:"))
        
        while iletisimSecim < 1 or iletisimSecim > 2:
                iletisimSecim = int(input("Lütfen 1 ile 2 arasında bir seçim yapınız: "))
        
        if iletisimSecim == 1:
            print("\nMüşteri hizmetleri sabit telefon numarası: ***telefon numarası***")
        if iletisimSecim == 2:
            print("\nMüşteri hizmetleri e-posta adres: ***e-posta adresi***")
        
            print("İşleminiz Başarıyla Gerçekleştirilmiştir.")
    def web_sitemize_gozatın(self):
        time.sleep(0)
        print("Link yükleniyor...")
        time.sleep(1)
        print(">>>  https://teknikservissciniz.unaux.com  <<<")

otomasyon = Otomasyon("Teknik Servis Otomasyonu")    

while otomasyon.calisma:
    otomasyon.program()