


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
        secim =int( input("**** {} hoş geldiniz ****\n\n 1-Kurulum Yardımı \n 2-Şikayet Bildir \n 3-Arıza Ekle\n 4-Arıza Çıkar\n 5-Arıza Cinsi\n 6-Arıza Tarih:\n 7-yetkilipersonel\n\n Seçiminizi Giriniz ".format(self.ad)))
        while secim < 1 or secim > 8:
            secim = int(input("Lütfen 1 - 8 arasında belirtilen seçeneklerden birini giriniz!"))

     
        return secim
    def kurulumGir(self):
        pass
    def şikayetGir(self):
        pass
    def arızaEkle(self):
        id = 1
        isim = input("Adınızı Giriniz: ") 
        soyisim = input("Soyadınızı Giriniz: ") 
        ürünadı = input("Arıza kaydı oluşturacağınız ürün adı: ")
        ürünarıza = input ("Arızanın ne olduğunu düşünüyorsunuz: ") 
        açıkadres = input("Adresinizi  Giriniz: ") 
        garantisüresi = input("garanti süresini giriniz: ")
        tarih = input("talepte bulunduğunuz tarihi giriniz: ")
       
       
        with open("Arızatalebi.txt","r") as dosya:
            arızatalebiListesi = dosya.readlines()   
        
        if len(arızatalebiListesi) == 0:
            id = 1
        else:            
            with open("Arızatalebi.txt","r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1
        
        with open("Arızatalebi.txt","a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}-{}-{}\n".format(id,isim,soyisim,ürünadı,ürünarıza,açıkadres,garantisüresi,tarih))
    
    def arızaCikar(self):
        with open ("Arızatalebi.txt","r") as dosya:
            arızatalebi = dosya.readlines()

        garızatalebi = []

        for arızatalebi in arızatalebi:
            garızatalebi.append(" ".join(arızatalebi[:-2].split("-")))
        for arızatalebi in garızatalebi:
            print(arızatalebi)    
    
        secim = int(input("lütfen çıkarmak istediğiniz arızayı seçiniz(1-{}:".format(len(garızatalebi))))
        while secim < 1 or secim > len(garızatalebi):
            secim = int(input("lütfen (1-{}) arasında numara seçiniz:".format(len(garızatalebi))))

        arızatalebi.pop(secim - 1)
        
        maxsayi = len(arızatalebi)    
        darızatalebi = []       
        sayac = 1
        for arızatalebi in arızatalebi:
             darızatalebi.append(str(sayac) + "/" + arızatalebi.split(")")[1])
             sayac += 1   
        
        with open("Arızatalebi.txt","w") as dosya:
         dosya.writelines(darızatalebi)
    
    
    
    
    
    
    
    def arızaCinsi(self):
        pass 
    def arızaAdres(self): 
        pass
    def arızaTarih(self):
        pass

otomasyon = Otomasyon("Teknik Servis Otomasyonu")    

while otomasyon.calisma:
    otomasyon.program()

