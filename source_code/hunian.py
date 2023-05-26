class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, luas = 0, gambar = ''):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.luas = luas
        self.gambar = gambar

    def set_jenis(self, jenis):
        self.jenis = jenis
    
    def set_jmlPenghuni(self, jmlPenghuni):
        self.jml_penghuni = jmlPenghuni

    def set_jmlKamar(self, jmlKamar):
        self.jml_kamar = jmlKamar

    def set_luas(self, luas):
        self.luas = luas

    def set_gambar(self, gambar):
        self.gambar = gambar

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_dokumen(self):
        pass

    def get_luas(self):
        return self.luas
    
    def get_gambar(self):
        return self.gambar

    def get_summary(self):
        return "Hunian "+ self.jenis +", dengan luas " + str(self.luas) + " m2 memiliki " + str(self.jml_kamar) + " kamar yang dapat ditempati oleh " + str(self.jml_penghuni) + " orang."