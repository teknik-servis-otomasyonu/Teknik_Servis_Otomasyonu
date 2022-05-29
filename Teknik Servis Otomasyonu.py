


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
            self.yetkilipersonel()
    def menuSecim(self):
        secim =int( input("**** {} hoş geldiniz ****\n\n 1-Kurulum Yardımı \n 2-Şikayet Bildir \n 3-Arıza Ekle\n 4-Arıza Çıkar\n 5-Arıza Cinsi\n 6-Arıza Tarih:\n 7-yetkilipersonel\n\n Seçiminizi Giriniz ".format(self.ad)))
        while secim < 1 or secim > 8:
            secim = int(input("Lütfen 1 - 8 arasında belirtilen seçeneklerden birini giriniz!"))

     
        return secim
    def kurulumGir(self):
        pass
    def şikayetGir(self):
        pass
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
        dosya.write("Müşteri adı: "+isim+"\n")
        dosya.write("Müşteri soyadı: "+soyisim+"\n")
        dosya.write("Ürün adı: "+urunadi+"\n")
        dosya.write("Ürün şikayeti: "+urunariza+"\n")
        dosya.write("Müşterinin açık adresi: "+acikadres+"\n")
        dosya.write("Ürünün garanti süresi: "+garantisuresi+"\n")
        dosya.write("Tarih: "+tarih+"\n")
        dosya.write("------------\n")

        print("\nTeşekkür ederiz.\n\n Arıza talebiniz başarı ile oluşturulmuştur. ")



    
    
    
    
    
    def arizaCinsi(self):
        pass 
    def arizaAdres(self): 
        pass
    def arizaTarih(self):
        pass

otomasyon = Otomasyon("Teknik Servis Otomasyonu")    

while otomasyon.calisma:
    otomasyon.program()

