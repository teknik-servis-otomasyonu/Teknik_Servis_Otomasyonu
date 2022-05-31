from io import TextIOWrapper
import time#time modülünü import ettik
#zaman ve saaat içeren işlemreli kullanmak için import ediyoruz
import datetime#date time modülünü import ettik
#işlem sırasında birleşimini kullanıyoruz


class Otomasyon():#öncelikle otomasyon adında bir klasörü oluşturuyoruz
    def __init__(self,ad):#ad değişkeni atıyoruz bu sayede ad yazan yere istediğimiz isimi koyabiliriz
        self.ad = ad #fonksiyonda kulllanacağımız ad değişkenini kaydediyoruz
        self.calisma = True #programı çalıştırdıktan sonra sınırsız döngüde çalışabilmesi için "true" ifadesini kullanıyoruz
    
    
    def program(self):#metinbelgesini dosya içine göndererek seçim menüsü ayarlıyoruz
        secim = self.menuSecim()#bu menüdeki secim değişkenlerini sırasıyla ayarlıyoruz

        if secim == 1:
            self.kurulumGir()   #kurulum gir secimi 1 rakamına basınca aktif olacak    
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
        #seçim yapıldıktan sonra 3 saniyelik bir bekleme süresi ayarlıyoruz
    def menuSecim(self):
        print(" \n") #işleme bir satır boşlukla devam ediyoruz
        try:#hata verebileceğini düşündüğümüz kodlar
         secim =int( input("**** {}'na hoş geldiniz ****\n\nLütfen yardım talebi almak istediğiniz konuyu seçiniz: \n\n 1-Kurulum Yardımı \n 2-Şikayet Bildir \n 3-Arıza Ekle\n 4-Müşteri hizmetleri\n 5-Web Sitemize Gözatın!\n\nSeçiminizi Giriniz: ".format(self.ad)))
         while secim < 1 or secim > 5:#kullanıcıyı karşılıyoruz ardından bir satır boşluk atttıktan sonra yardım almak istediği sonuyu sorarak seçeneklere yönlendiriyoruz
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
         #kurulum seçimine giren kullanıcının kullanım kılavuzunu almak istediği ürünleri seçmesi için ürünleri alt alta sıralıyoruz
        while kurulumSecim < 1 or kurulumSecim > 10:   #1 ila 10 arası olan koşul olana kadar döngünün devam etmesi için while döngüsünü kullanıyoruz
            kurulumSecim = int(input("Lütfen 1 ile 10 arasında bir seçim yapınız: "))
        
        if kurulumSecim == 1:
            time.sleep(1)
            print("lütfen bekleyiniz..")
            print("A model buzdolabı için kullanım kılavuzu:file:///C:/Users/ALCE_GUVENLIK/Downloads/tr-TR-7283020415-201807191722545-User-Manual-File-Long-tr-TR.pdf \nB model buzdolabı için kullanım kılavuzu:http://download.beko.com/Download.UsageManualsBeko/9614-nfiy-neofrost-buzdolabi-buzdolaplari-kullanim-kilavuzu-tr_TR_7264520414_BK9611NE_572706_TR.pdf\n")
        if kurulumSecim == 2:
            time.sleep(2) #bütün seçimleri belirlenen süre sonrasında açılması için ayarlıyoruz
            print("A model fırın için kullanım kılavuzu:https://statik.vestel.com.tr/webfiles/20262674_k.pdf\nB model fırın için kullanım kılavuzu:file:///C:/Users/ALCE_GUVENLIK/Downloads/tr-TR-7769570104-201912061413817-User-Manual-File-Long-tr-TR%20(1).pdf\n")
        if kurulumSecim == 3:
            time.sleep(2)
            print("A model çamaşır makinesi için kullanım kılavuzu:file:///C:/Users/ALCE_GUVENLIK/Downloads/tr-TR-7769570104-201912061413817-User-Manual-File-Long-tr-TR%20(1).pdf \nB model çamaşır makinesi için kullanım kılavuzu: file:///C:/Users/ALCE_GUVENLIK/Downloads/tr-TR-201902141305320-User-Manual-File-Long-tr-TR.pdf\n")
        if kurulumSecim == 4:
            time.sleep(2)
            print(" \nA model derin dondurucu için kullanım kılavuzu:https://www.ugur.com.tr/uploads/products/100094/files/b2410000173_dikey_720ac.pdf\nB model derin dondurucu için kullanım kılavuzu: ****link****\n")
        if kurulumSecim == 5:
            time.sleep(2)
            print(" \nA model ütü için kullanım kılavuzu: https://www.singer.com.tr/assets/img/uploads/product-files/e40cfaa91cb1052a2bfc9f77f081fc17.pdf\nB model ütü için kullanım kılavuzu:https://www.miele.com.tr/pmedia/ZGA/TX3587/10941290-000-00_10941290-00.pdf\n")
        if kurulumSecim == 6:
            time.sleep(2)
            print(" \nA model klima için kullanım kılavuzu: https://www.arcelik.com.tr/destek/isitma-sogutma/klima/klimanin-sicaklik-ayari-nasil-yapilir?gclid=EAIaIQobChMI-LjbsLSH-AIVy49oCR17lAOIEAAYASAAEgJwiPD_BwE&gclsrc=aw.ds\nB model klime için kullanım kılavuzu: https://www.daikin.eu/content/dam/document-library/operation-manuals/ac/split/ftxb-c/FTXB20-35C2V1B_3PTR341266-3H_Operation%20manuals_Turkish.pdf\n")
        if kurulumSecim == 7:
            time.sleep(2)
            print(" \nA model şofben için kullanım kılavuzu:https://urunler.demirdokum.com.tr/getattachment/05a0de2b-4d51-4b08-9f05-ce446d15e370/Kullanma-K%C4%B1lavuzu.aspx\nB model şofben için kullanım kılavuzu:https://www.baymak.com.tr/media/3085/montaj-kullanma-k%C4%B1lavuzu.pdf\n")
        if kurulumSecim == 8:
            time.sleep(2)  
            print(" \nA model süpürge için kullanım kılavuzu:http://download.beko.com/Download.UsageManualsBeko/bks-5422-toz-torbasiz-elektrikli-supurge-kullanim-kilavuzu-tr_TR_201407231937801_Kullanma-20K-C4-B1lavuzu-Dosyatur-A.pdf\nB model süpürge için kullanım kılavuzu: https://manuals.plus/tr/miele/elektrikli-s%C3%BCp%C3%BCrge-k%C4%B1lavuzu-5#axzz7UmTkEXOd\n")
        if kurulumSecim == 9:
            time.sleep(2)
            print(" \nA model bulaşık makinesi için kullanım kılavuzu: https://download.arcelik.com.tr/Download.UsageManuals/FACELIFT_ARCELIK/tr_TR_201712071226195_User%20Manual%20-%20Filetr_TR.pdf\nB model bulaşık makinesi için kullanım kılavuzu: https://www.miele.com.tr/pmedia/ZGA/TX2070/10274450-000-03_10274450-03.pdf\n")
        if kurulumSecim == 10:#yapılan her seçimlerde o ürüne ait olan her iki modelinde kullanım klavUzlarının linkini kullanıcıya sunuyoruz. Bu sayede kullanıcı kurulımdan kullanım koşullarına ,istediği bütün bilgilere buradan sahip olacak
            time.sleep(2)
            digerModel = str(input("Lütfen kurulum yapmak istediğiniz ürünün modelini giriniz: "))
        if  digerModel :
            print(" \n" + digerModel + " için kullanım kılavuzu linki:>>>  https://teknikservissciniz.unaux.com  <<< ")


        pass
        time.sleep(2)
        print("lütfen bekleyiniz..")
    # Şikayet talebi oluşturma (text olarak kaydetme eklenecek)
    def sikayetGir(self):#bu işlemde şikayet değişkenini ayarlıyoruz
        time.sleep(1)
        sikayetSebebi=int(input("Şikayet sebebinizi şeçiniz:\n\n1-Personel hakkında\n2-Ürünlerimiz hakkında\n3-Diğer\n\nSeçim: "))
        
        while sikayetSebebi < 1 or sikayetSebebi > 3: #kullanıcıya şikayet seçenekleri sunuyoruz
            #1 ile 3 arasındaki seçimseçeneklerini döngüye alıyoruz
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
            dosya = open("Şikayet Talebi.txt","a",encoding="utf-8")#yazılan bütün şikayetler şikayet talebi dosyasına gider
            dosya.write("Müşteri şikayeti: "+sikayet+"\n")#yazılan şikayetlerin hepsi aynı zamanda müşteri şikayeti olarak dosya
        
        
        print("\n\nŞikayet talebiniz alınmıştır\n")

        pass
        time.sleep(2)
        print("lütfen bekleyiniz..")
    # arıza talebi oluşturuyoruz, bu şekilde kullanıcının kullandığı ürünün ve şahsi bilgilerini alıyoruz
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
    #yine aynı şekilde müşteri hizmetlerinin değişkenini ayarlıyoruz , verilen eposta adresi veya telefon numarası aracılığında müşteri ile kontak kuruyoruz
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

while otomasyon.calisma:#otomasyon çalışmasını while döngüsüne alıyoruz
    otomasyon.program()