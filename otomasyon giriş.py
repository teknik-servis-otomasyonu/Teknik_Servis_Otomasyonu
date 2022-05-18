#projenın genel çaışma durumu ve kurguya giriş
#(personel bilgileri talep bilgileri vb.)

#ana ekran sınıfı
class Anaekran:
        def __init__(self,personel_id):
        self.personel_id = personel_id

        self.karsilama()

        def karsilama(self):  
        # self.setupUi(self)
        #menülerin yönlendirilmesi
        self.actionTalep_A.triggered.connect(self.talep_ekle)
        self.actionPersonel_Ekle.triggered.connect(self.personel_ekle)
        self.actionDevam_Eden_Talepler.triggered.connect(self.karsilama)
        self.actionKapanan_Talepler.triggered.connect(self.fkapanan)
        self.actionPersnel_G_ncelle_Sil.triggered.connect(self.fpersonelgs)
        self.tableWidget.setRowCount(0)
        self.facik_isler()
.
