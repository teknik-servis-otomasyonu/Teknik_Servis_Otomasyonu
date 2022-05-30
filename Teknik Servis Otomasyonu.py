import time





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
             self.web_sitemize_gözatın()   
    # Otomasyon menü seçim ekranı
        time.sleep(3)
    def menuSecim(self):
        print(" \n")
        secim =int( input("**** {}'na hoş geldiniz ****\n\nLütfen yardım talebi almak istediğiniz konuyu seçiniz: \n\n 1-Kurulum Yardımı \n 2-Şikayet Bildir \n 3-Arıza Ekle\n 4-Müşteri hizmetleri\n 5-Web Sitemize Gözatın!\n\nSeçiminizi Giriniz: ".format(self.ad)))
        while secim < 1 or secim > 5:
            secim = int(input("Lütfen 1 - 4 arasında belirtilen seçeneklerden birini giriniz!"))

     
        return secim
        pass

        time.sleep(3)
        print("lütfen bekleyiniz..")
    # Kurulum yardımı oluşturma
    def kurulumGir(self):
        time.sleep(2)
        
        kurulumSecim = int(input("\nLütfen kurulum yapmak istediğiniz ürünü seçiniz.\n\n1-Buzdolabı\n2-Fırın\n3-Çamaşır makinesi\n4-Derin Dondurucu\n5-Ütü\n6-Klima\n7-Şofben\n8-Elektrikli Süpürge\n9-Bulaşık Makinesi\n10-Diğer model\n\nSecim: "))
        
        while kurulumSecim < 1 or kurulumSecim > 10:
            kurulumSecim = int(input("Lütfen 1 ile 10 arasında bir seçim yapınız: "))
        
        if kurulumSecim == 1:
            print("A model buzdolabı için kullanım kılavuzu: ****link****\nB model buzdolabı için kullanım kılavuzu: ****link****\n")
        if kurulumSecim == 2:
            print("A model fırın için kullanım kılavuzu: ****link****\nB model fırın için kullanım kılavuzu: ****link****\n")
        if kurulumSecim == 3:
            print("A model çamaşır makinesi için kullanım kılavuzu: ****link****\nB model çamaşır makinesi için kullanım kılavuzu: ****link****\n")
        if kurulumSecim == 4:
            print(" \nA model derin dondurucu için kullanım kılavuzu: ****link****\nB model derin dondurucu için kullanım kılavuzu: ****link****\n")
        if kurulumSecim == 5:
            print(" \nA model ütü için kullanım kılavuzu: ****link****\nB model ütü için kullanım kılavuzu: ****link****\n")
        if kurulumSecim == 6:
            print(" \nA model klima için kullanım kılavuzu: ****link****\nB model klime için kullanım kılavuzu: ****link****\n")
        if kurulumSecim == 7:
            print(" \nA model şofben için kullanım kılavuzu: ****link****\nB model şofben için kullanım kılavuzu: ****link****\n")
        if kurulumSecim == 8:
            print(" \nA model süpürge için kullanım kılavuzu: ****link****\nB model süpürge için kullanım kılavuzu: ****link****\n")
        if kurulumSecim == 9:
            print(" \nA model bulaşık makinesi için kullanım kılavuzu: ****link****\nB model bulaşık makinesi için kullanım kılavuzu: ****link****\n")
        if kurulumSecim == 10:
            digerModel = str(input("Lütfen kurulum yapmak istediğiniz ürünün modelini giriniz: "))
            print(" \n" + digerModel + " için kullanım kılavuzu linki: ****link****")


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
        isim = input("Adınızı giriniz: ") 
        soyisim = input("Soyadınızı giriniz: ") 
        urunadi = input("Arıza kaydı oluşturacağınız ürün adını giriniz: ")
        urunariza = input ("Arızanın ne olduğunu düşünüyorsunuz: ") 
        acikadres = input("Adresinizi  giriniz: ")
        garantisuresi = input("Garanti sürenizi giriniz: ")
        tarih = input("Tarihi giriniz(GG/AA/YYY): ")

        dosya = open("Arıza Talebi.txt","a",encoding="utf-8")
        dosya.write("Müşteri adı: "+isim+"\n")
        dosya.write("Müşteri soyadı: "+soyisim+"\n")
        dosya.write("Ürün adı: "+urunadi+"\n")
        dosya.write("Ürün şikayeti: "+urunariza+"\n")
        dosya.write("Müşterinin açık adresi: "+acikadres+"\n")
        dosya.write("Ürünün garanti süresi: "+garantisuresi+"\n")
        dosya.write("Tarih: "+tarih+"\n")
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
    def web_sitemize_gözatın(self):
        time.sleep(0)
        print("link yükleniyor...")
        time.sleep(2)
        print(">>>  https://teknikservissciniz.unaux.com  <<<")

otomasyon = Otomasyon("Teknik Servis Otomasyonu")    

while otomasyon.calisma:
    otomasyon.program()