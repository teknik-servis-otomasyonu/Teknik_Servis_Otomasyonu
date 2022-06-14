from io import TextIOWrapper
import time#time modülünü import ettik
import timedate #time modülünü import ettik
#işlem sırasında birleşimini kullanıyoruz
import webbrowser#web sayfasını kullanabilmek için import işlemini yaptık



#öncelikle otomasyon adında bir klasörü oluşturuyoruz
class Otomasyon():
    def __init__(self,ad):#ad değişkeni atıyoruz bu sayede ad yazan yere istediğimiz isimi koyabiliriz
        self.ad = ad#fonksiyonda kulllanacağımız ad değişkenini kaydediyoruz
        self.calisma = True #programı çalıştırdıktan sonra sınırsız döngüde çalışabilmesi için "true" ifadesini kullanıyoruz
    # Otomasyon menü fonksiyon seçimi 
    
    def program(self):#metinbelgesini dosya içine göndererek seçim menüsü ayarlıyoruz
        secim = self.menuSecim()#bu menüdeki secim değişkenlerini sırasıyla ayarlıyoruz
        if secim == 1:
            self.kurulumGir() #kurulum gir secimi 1 rakamına basınca aktif olacak    
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
        print(" \n")#işleme bir satır boşlukla devam ediyoru
        try:#hata verebileceğini düşündüğümüz kodlar
         secim =int( input("**** {}'na hoş geldiniz ****\n\nLütfen yardım talebi almak istediğiniz konuyu seçiniz: \n\n 1-Kurulum Yardımı \n 2-Şikayet Bildir \n 3-Arıza Ekle\n 4-Müşteri hizmetleri\n 5-Web Sitemize Gözatın!\n\nSeçiminizi Giriniz: ".format(self.ad)))
         while secim < 1 or secim > 5::#kullanıcıyı karşılıyoruz ardından bir satır boşluk atttıktan sonra yardım almak istediği sonuyu sorarak seçeneklere yönlendiriyoruz
            secim = int(input("Lütfen 1 - 4 arasında belirtilen seçeneklerden birini giriniz!"))
        except ValueError:#hata ayıklama işlemi (hata durumunda yapılacak işlem.)
            print("Lütfen Sayı Değeri Giriniz!")
        time.sleep(1)
      
        return secim#yazılmış olan secimlerin hepsini dönüşüme alıyoruz
        pass


       
    # Kurulum yardımı oluşturma
    def kurulumGir(self):
        print("Lütfen Bekleyiniz..")
        time.sleep(1)#1 saniye kadar bekletme işlemi öncesinde lütfen bekleyiniz ikazı 
        
        kurulumSecim = int(input("\nLütfen kurulum yapmak istediğiniz ürünü seçiniz.\n\n1-Buzdolabı\n2-Fırın\n3-Çamaşır makinesi\n4-Derin Dondurucu\n5-Ütü\n6-Klima\n7-Şofben\n8-Elektrikli Süpürge\n9-Bulaşık Makinesi\n10-Diğer model\n\nSecim: "))
        
        while kurulumSecim < 1 or kurulumSecim > 10:   #kurulum seçimine giren kullanıcının kullanım kılavuzunu almak istediği ürünleri seçmesi için ürünleri alt alta sıralıyoruz
            kurulumSecim = int(input("Lütfen 1 ile 10 arasında bir seçim yapınız: "))
        
        if kurulumSecim == 1:
            A = str(input("A MODEL BUZDOLABI [a]:\n B MODEL BUZDOLABI İÇİN [b]:\n Lütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("/Downloads/tr-TR-7283020415-201807191722545-User-Manual-File-Long-tr-TR.pdf")
            if A : "b"
            webbrowser.open("http://download.beko.com/Download.UsageManualsBeko/9614-nfiy-neofrost-buzdolabi-buzdolaplari-kullanim-kilavuzu-tr_TR_7264520414_BK9611NE_572706_TR.pdf")
        if kurulumSecim == 2:

            A = str(input("A MODEL FIRIN İÇİN [a]:\n B MODEL FIRIN İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("tr-TR-7769570104-201912061413817-User-Manual-File-Long-tr-TR.pdf")
            if A: "b"
            webbrowser.open("https://media3.bsh-group.com/Documents/9000737996_F.pdf")
        if kurulumSecim == 3:
            A = str(input("A MODEL ÇAMAŞIR MAKİNESİ İÇİN [a]:\n B MODEL ÇAMAŞIR MAKİNESİ İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("https://download.arcelik.com.tr/Download.UsageManuals/FACELIFT_ARCELIK/tr_TR_Manual_7144850100_tr_TR20171222-130958-092.pdf")
            if A :"b"
            webbrowser.open("https://media3.bsh-group.com/Documents/9001089397_A.pdf")
        if kurulumSecim == 4:
            A = str(input("A MODEL DERİN DONDURUCU İÇİN [a]:\n B MODEL DERİN DONDURUCU İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("Downloads/tr-TR-7278440111-202005111049636-User-Manual-File-Long-tr-TR.pdf")
            if A :"b"
            webbrowser.open("https://media3.bsh-group.com/Documents/9000842200_C.pdf")
        if kurulumSecim == 5:
            A = str(input("A MODEL ÜTÜ İÇİN [a]:\n B MODEL ÜTÜ İÇİN [b]:"))
            if A :"a"
            webbrowser.open("https://manuall.info.tr/profilo-ubs1401-utu/")
            if A : "b"
            webbrowser.open("https://manuall.info.tr/hotpoint-ariston-si-c35-ckg-utu/")
        if kurulumSecim == 6:
            A = str(input("A MODEL KLİMA İÇİN [a]:\n B MODEL KLİMA İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("https://download.arcelik.com.tr/download.usagemanuals/12044-active-plasma-plus-serisi-ev-tipi-klima-kullanim-kilavuzu-tr_TR_5400571301_Revg.g.pdf")
            if A :"b"
            webbrowser.open("https://manuall.info.tr/profilo-p3zma18907-klima/")
        if kurulumSecim == 7:
            A = str(input("A MODEL ŞOFBEN İÇİN [a]:\n B MODEL ŞOFBEN İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("https://www.epey.com/dosya/367582/arcelik-t-7365-b-3474.pdf/")
            if A : "b"
            webbrowser.open("https://www.epey.com/dosya/558614/arcelik-t-7350-b-3474.pdf/")
        if kurulumSecim == 8:
            A = str(input("A MODEL SÜPÜRGE İÇİN [a]:\n B MODEL SÜPÜRGE İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a" 
            webbrowser.open("https://manuall.info.tr/profilo-psu5b111-elektrikli-supurge/")
            if A : "b"
            webbrowser.open("https://download.arcelik.com.tr/download.usagemanuals/32592_3_S-7430-User-Manual.pdf")
        if kurulumSecim == 9:
            A = str(input("A MODEL BULAŞIK MAKİNESİ İÇİN [a]:\n B MODEL BULAŞIK MAKİNESİ  İÇİN [b]:\nLütfen Seçiminizi yapın:"))
            if A :"a"
            webbrowser.open("https://www.arcelik.com.tr/bulasik-makinesi/6144-bulasik-makinesi?gclid=Cj0KCQjwqPGUBhDwARIsANNwjV6zi9DUnd0ZwO62gmC3FQ0faup1jqXWW0mY1nVeC9rpP-bmoylnoykaAsqPEALw_wcB&gclsrc=aw.ds")
            if A :"b"
            webbrowser.open("https://manuall.info.tr/profilo-bm4220eg-bulasik-makinesi/")
        if kurulumSecim == 10::#yapılan her seçimlerde o ürüne ait olan her iki modelinde kullanım klavUzlarının linkini kullanıcıya sunuyoruz. Bu sayede kullanıcı kurulımdan kullanım koşullarına ,istediği bütün bilgilere buradan sahip olacak

         digerModel = str(input("Lütfen kurulum yapmak istediğiniz ürünün modelini giriniz: "))
         print(" \n" + digerModel + " için kullanım kılavuzu linki:>>>  https://teknikservissciniz.unaux.com  <<< ")
            

        pass
        time.sleep(2)
        print("lütfen bekleyiniz..")
    # Şikayet talebi oluşturma (text olarak kaydetme eklenecek)
    def sikayetGir(self):#bu işlemde şikayet değişkenini ayarlıyoruz
        time.sleep(1)
        sikayetSebebi=int(input("Şikayet sebebinizi şeçiniz:\n\n1-Personel hakkında\n2-Ürünlerimiz hakkında\n3-Diğer\n\nSeçim: "))
        
        while sikayetSebebi < 1 or sikayetSebebi > 3: #kullanıcıya şikayet seçenekleri sunuyoruz
            sikayetSebebi = int(input("Lütfen 1 ile 3 arasında bir seçim yapınız: "))
        
        if sikayetSebebi == 1:#eğer 1. seçenek seçlirse personel şikayetleri hakkında seçenekler sıralanıyor
            personelSikayet = int(input("\nPersonel hakkındaki şikaetinizi belirtiniz:\n\n1-Kaba\n2-İşini düzgün yapmıyor\n3-Ürüne zarar verme\n4-Diğer\n\nSeçim: "))
            while personelSikayet < 1 or personelSikayet > 4:
                personelSikayet = int(input("Lütfen 1 ile 4 arasında bir seçim yapınız: "))
            if personelSikayet == 4:
                input("Lütfen personel hakkındaki şikayetinizi belirtiniz:")

        if sikayetSebebi == 2:#eğer ürün hakkında şikayet seçilirse ürün hakkındaki şikayet seçenekleri sıralanıyor
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
    def musteriHizmetleri(self):  #yine aynı şekilde müşteri hizmetlerinin değişkenini ayarlıyoruz , verilen eposta adresi veya telefon numarası aracılığında müşteri ile kontak kuruyoruz
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