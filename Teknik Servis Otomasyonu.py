from pydoc import TextRepr


class Otomasyon():
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True

    def program(self):
        secim = self.menuSecim()

      
        if secim == 1:
            self.isimGir()
        if secim == 2:
            self.soyisimGir()
        if secim == 3:
            self.arızaEkle()
        if secim == 4:
            self.arızaCikar()
        if secim == 5:
            self.arızaCinsi()
        if secim == 6:
            self.arızaAdres()
        if secim == 7:
            self.arızaTarih()
        if secim == 8:
            self.yetkilipersonel()
    def menuSecim(self):
        secim =int( input("**** {} hoş geldiniz ****\n\n 1-İsim Giriniz: \n 2-Soyisim Giriniz:\n 3-Arıza Ekle:\n 4-Arıza Çıkar:\n 5-Arıza Cinsi:\n 6-Arıza Tarih:\n 7-yetkilipersonel:\n\nseçiminizi giriniz:".format(self.ad)))
        while secim < 1 or secim > 7:
            secim = int(input("Lütfen 1 - 7 arasında belirtilen seçeneklerden birini giriniz!"))

     
        return secim
    def isimGir(self):
        pass
    def soyisimGir(self):
        pass
    def arızaEkle(self):
        id = 1
        isim = input("Adınızı Giriniz: ") 
        soyisim = input("Soyadınızı Giriniz: ") 
        ürünadı = input("Arıza kaydı oluşturacağınız ürün adı: ")
        ürünarıza = input ("Arızanın ne olduğunu düşünüyorsunuz: ") 
        açıkadres = input("Adresinizi  Giriniz: ") 
        garantisüresi = input("garanti süresini giriniz")
        tarih = input("talepte bulunduğunuz tarihi giriniz")
        with open("Arızatalebi.txt","a+") as dosya:
            arızatalebiListesi = dosya.readlines()   
        
        if len(arızatalebiListesi) == 0:
            id = 1
            with open("Arızatalebi.txt","a+") as dosya:
                dosya.write("{})-{}-{}-{}-{}-{}-{}\n".format(id,isim,soyisim,ürünadı,ürünarıza,açıkadres,garantisüresi,tarih))
        else:
            with open("Arızatalebi.txt","r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1
        
        with open("Arızatalebi.txt","a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}-{}-{}\n".format(id,isim,soyisim,ürünadı,ürünarıza,açıkadres,garantisüresi,tarih))
    
    def arızaCikar(self):
        with open ("Arızatalebi.txt","r") as dosya:
            arızatalebi = dosya.readlines()
            arızatalebiListesi = dosya.readlines()
        for arızatalebi in arızatalebiListesi:
                print(arızatalebi)
    def arızaCinsi(self):
        pass 
    def arızaAdres(self):
        pass
    def arızaTarih(self):
        pass

otomasyon = Otomasyon("Teknik Servis Otomasyonu")    

while otomasyon.calisma:
    otomasyon.program()

