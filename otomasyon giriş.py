
import PyQt5


# PyQt5 ile grafiksel kullanıcı arayüzü oluşturup kütüphanesini tanımlıyoruz.
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_AnaPencere(object):

    def setupUi(self, AnaPencere):
        AnaPencere.setObjectName("AnaPencere")
        # ekran ölçülerini tanımlıyoruz.
        AnaPencere.resize(800, 600)
        # qtwidgets ile ana pencere bölmelerini oluşturuyoruz ve tanımlıyoruz.
        self.ana_icerik = QtWidgets.QWidget(AnaPencere)
        self.ana_icerik.setObjectName("ana_icerik")
        self.tableWidget = QtWidgets.QTableWidget(self.ana_icerik)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 751, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(self.ana_icerik)
        self.label.setGeometry(QtCore.QRect(90, 40, 601, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        AnaPencere.setCentralWidget(self.ana_icerik)
        self.menubar = QtWidgets.QMenuBar(AnaPencere)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuTalep_i_lemleri = QtWidgets.QMenu(self.menubar)
        self.menuTalep_i_lemleri.setObjectName("menuTalep_i_lemleri")
        self.menuPersonel_lemleri = QtWidgets.QMenu(self.menubar)
        self.menuPersonel_lemleri.setObjectName("menuPersonel_lemleri")
        AnaPencere.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnaPencere)
        self.statusbar.setObjectName("statusbar")
        AnaPencere.setStatusBar(self.statusbar)
        self.actionPersonel_Ekle = QtWidgets.QAction(AnaPencere)
        self.actionPersonel_Ekle.setObjectName("actionPersonel_Ekle")
        self.actionPersnel_G_ncelle_Sil = QtWidgets.QAction(AnaPencere)
        self.actionPersnel_G_ncelle_Sil.setObjectName("actionPersnel_G_ncelle_Sil")
        self.actionTalep_A = QtWidgets.QAction(AnaPencere)
        self.actionTalep_A.setObjectName("actionTalep_A")
        self.actionDevam_Eden_Talepler = QtWidgets.QAction(AnaPencere)
        self.actionDevam_Eden_Talepler.setObjectName("actionDevam_Eden_Talepler")
        self.actionKapanan_Talepler = QtWidgets.QAction(AnaPencere)
        self.actionKapanan_Talepler.setObjectName("actionKapanan_Talepler")
        self.menuTalep_i_lemleri.addAction(self.actionTalep_A)
        self.menuTalep_i_lemleri.addAction(self.actionDevam_Eden_Talepler)
        self.menuTalep_i_lemleri.addAction(self.actionKapanan_Talepler)
        self.menuPersonel_lemleri.addAction(self.actionPersonel_Ekle)
        self.menuPersonel_lemleri.addAction(self.actionPersnel_G_ncelle_Sil)
        self.menubar.addAction(self.menuTalep_i_lemleri.menuAction())
        self.menubar.addAction(self.menuPersonel_lemleri.menuAction())

        self.retranslateUi(AnaPencere)
        QtCore.QMetaObject.connectSlotsByName(AnaPencere)

    def retranslateUi(self, AnaPencere):
        _translate = QtCore.QCoreApplication.translate
        AnaPencere.setWindowTitle(_translate("AnaPencere", "Ana Pencere"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AnaPencere", "Talep Durumu"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AnaPencere", "Talep Adi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AnaPencere", "Açılış Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AnaPencere", "Talep Tanımı"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("AnaPencere", "Yetkili Personel"))
       #
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("AnaPencere", "Onayla"))
        self.label.setText(_translate("AnaPencere", "yapmak istediğiniz işlemi seçiniz"))
        self.menuTalep_i_lemleri.setTitle(_translate("AnaPencere", "Talep işlemleri"))
        self.menuPersonel_lemleri.setTitle(_translate("AnaPencere", "Personel İşlemleri"))
        self.actionPersonel_Ekle.setText(_translate("AnaPencere", "Personel Ekle"))
        self.actionPersnel_G_ncelle_Sil.setText(_translate("AnaPencere", "Personel Güncelle - Sil"))
        self.actionTalep_A.setText(_translate("AnaPencere", "Talep Aç"))
        self.actionDevam_Eden_Talepler.setText(_translate("AnaPencere", "Devam Eden Talepler"))
        self.actionKapanan_Talepler.setText(_translate("AnaPencere", "Kapanan Talepler"))


if __name__ == "__main__":
    # sys kütüphanesini tanımlıyoruz.
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnaPencere = QtWidgets.QMainWindow()
    ui = Ui_AnaPencere()
    ui.setupUi(AnaPencere)
    AnaPencere.show()
    sys.exit(app.exec_())




