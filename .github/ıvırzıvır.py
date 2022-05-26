class Otomasyon():
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True

    def program(self):
        pass
    def menuSecim(self):
        secim = input("**** {} ottomasyonuna hoş geldiniz ****\n\n 1-İsim Giriniz \n 2-Soyisim Gİriniz 3-Arıza Ekle\n 4-Arıza Çıkar\n 5-Arıza Cinsi\n 6-Arıza Tarih".format(self.ad))
        return secim
    def isimGir(self):
        pass
    def soyisimGir(self):
        pass
    def arızaEkle(self):
        pass
    def arızaCikar(self):
        pass
    def arızaCinsi(self):
        pass 
    def arızaAdres(self):
        pass
    def arızaTarih(self):
        pass

otomasyon = Otomasyon("Teknik Servis Otomasyonu")    

while otomasyon.calisma:
    otomasyon.program()

