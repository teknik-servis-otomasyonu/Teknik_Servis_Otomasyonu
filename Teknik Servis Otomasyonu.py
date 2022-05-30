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
        

    def menuSecim(self):
        secim =int( input("\n**** {} hoş geldiniz ****\n\n 1-Kurulum Yardımı \n 2-Şikayet Bildir \n 3-Arıza Ekle\n 4-Arıza Çıkar\n 5-Arıza Cinsi\n 6-Arıza Tarih:\n 8-web sitemize gözatın!\n\n Seçiminizi Giriniz ".format(self.ad)))
        while secim < 1 or secim > 8:
            secim = int(input("Lütfen 1 - 8 arasında belirtilen seçeneklerden birini giriniz!"))

    
        return secim
    def kurulumGir(self):
        pass
    
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