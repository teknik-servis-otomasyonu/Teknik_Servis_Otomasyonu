import time





class Otomasyon():
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True
        

    def program(self):
        secim = self.menuSecim()

    
        if secim == 1:
            self.kurulumGir()
        if secim == 2:
            self.şikayetGir()
        if secim == 3:
            self.arizaEkle()
        if secim == 4:
            self.arizaCikar()
        if secim == 5:
            self.arizaCinsi()
        if secim == 6:
            self.arizaAdres()
        if secim == 7:
            self.arizaTarih()
        if secim == 8:
           self.web_sıtemıze_gozatın()
        
        time.sleep(2)
    def menuSecim(self):
        secim =int( input("\n**** {} hoş geldiniz ****\n\n 1-Kurulum Yardımı \n 2-Şikayet Bildir \n 3-Arıza Ekle\n 4-Arıza Çıkar\n 5-Arıza Cinsi\n 6-Arıza Tarih:\n 8-web sitemize gözatın!\n\n Seçiminizi Giriniz ".format(self.ad)))
        while secim < 1 or secim > 8:
            secim = int(input("Lütfen 1 - 8 arasında belirtilen seçeneklerden birini giriniz!"))

        time.sleep(1)
        return secim
    def kurulumGir(self):
        secim =int( input("\n\n^^^ Kurulum Ekranına Hoşgeldiniz ^^^\n\n 1-Ütü \n 2-Çamaşır Makinası \n 3-Bulaşık Makinası\n 4-Televizyon\n 5-Elektrikli Süpürge\n 6-Tost Makinesi\n 7-Elektrikli Ocak\n 8-Buzdolabı\n 9-Fırın\n\n Lütfen 1 - 9 arasında belirtilen seçeneklerden birini giriniz!".format(self.ad)))
 
        while secim < 1 or secim > 9:
            secim = int(input("Lütfen 1 - 9 arasında belirtilen seçeneklerden birini giriniz!"))
        if secim == 1:
            print("1.1. Makinaya bağlı su deposu doldurulur\n1.2. Makine arka buhar tahliyesi açılır\n1.3. Ana giriş şalteri açılır\n1.4. Kazan anahtarı(I) konumuna getirilir\n1.5. Arka buhar tahliye vanasından buhar geldikten 30-45 saniye sonra vana kapatılır\n1.6. Makine üzerindeki ütü anahtarı (I) konumuna getirilir\nBuhar 3 atüye geldiğinde makine çalışmaya hazırıdr.")



    
    def şikayetGir(self):

        print("Şikayet sayfamıza hoşgeldiniz\n")
        
        with open ("Yetkilipersonel.txt","r")as dosya:
         yetkilipersonel = dosya.readlines()

        şikayet_konusu =input("Şikayet Konunuz nedir?:(personel/memnuniyet)")
        if şikayet_konusu == "personel":
         with open("Yetkilipersonel.txt","r") as dosya: 
            personel = dosya.readlines()

       
        personel_ismi =input("personel ismini lütfen bize bildiriniz:")
        print("\nTeşekkürler Şikayetiniz Başarıyla İletilmiştir.")

    def arizaEkle(self):
        print("Teknik Servis Otomasyonu'na Hoşgeldiniz\n")

        isim = input("Adınızı giriniz: ") 
        soyisim = input("Soyadınızı giriniz: ") 
        urunadi = input("Arıza kaydı oluşturacağınız ürün adını giriniz: ")
        urunariza = input ("Arızanın ne olduğunu düşünüyorsunuz: ") 
        acikadres = input("Adresinizi  giriniz: ")
        garantisuresi = input("Garanti sürenizi giriniz: ")
        tarih = input("Tarihi giriniz(GG/AA/YYY): ")

        dosya = open("Arizatalebi.txt","a",encoding="utf-8")
        dosya.write("Musterı adı: "+isim+"\n")
        dosya.write("Musterı soyadı: "+soyisim+"\n")
        dosya.write("Urun adı: "+urunadi+"\n")
        dosya.write("Urun sıkayetı: "+urunariza+"\n")
        dosya.write("Musterının acık adresı: "+acikadres+"\n")
        dosya.write("Urunun garantı suresı: "+garantisuresi+"\n")
        dosya.write("Tarıh: "+tarih+"\n")
        dosya.write("------------\n")

        print("\nTeşekkür ederiz.\n\n Arıza talebiniz başarı ile oluşturulmuştur. ")



    def arizaCikar(self):
        with open("Arizatalebi.txt","r") as dosya:
            arızatalebi = dosya.readlines()
        
        gArızatalebi = [] #gösterimde olan arıza talebleri

        for arızatalebi in arızatalebi:
            gArızatalebi.append(" ".join(arızatalebi[:-2].split("-")))
        
        for arızatalebi in gArızatalebi:
            print(arızatalebi)
        
        secim = int(input("Lütfen Çıkarmak İstediğniz Arızanın Numarasını Giriniz(1-{}:".format(len(gArızatalebi))))
        
        while secim < 1 or secim > len(gArızatalebi):
            
            secim =  int(input(" Lütfen (1-{})) arasında numara giriniz: ".format(len(gArızatalebi))))
    
            arızatalebi.pop(secim - 1 )
            
            sayac = 1

            dArızatalebi = []

            for arızatalebi in arızatalebi:
                dArızatalebi.append(str(sayac) + ")" + arızatalebi.split(")")[1])
                sayac += 1
        
            with open("Arizatalebi.txt","w") as dosya:
                dosya.writelines(dArızatalebi)


            
        
        print("\nTeşekkür ederiz. Arıza talebiniz başarı ile silinmiştir.\n ")



            


    def arizaAdres(self):
        pass
    def arizaTarih(self):
        pass
    def web_sıtemıze_gozatın(self):
        time.sleep(0)
        print("link yükleniyor...")
        time.sleep(2)
        print(">>>  https://teknikservissciniz.unaux.com  <<<")
     
    

otomasyon = Otomasyon("Teknik Servis Otomasyonu")   

while otomasyon.calisma:
        otomasyon.program()