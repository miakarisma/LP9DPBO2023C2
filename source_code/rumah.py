from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas, tipe, gambar):
        super().__init__("Rumah", jml_penghuni, jml_kamar, luas, gambar)
        self.nama_pemilik = nama_pemilik
        self.tipe = tipe

    def set_namaPemilik(self, nama):
        self.nama_pemilik = nama

    def set_tipe(self, tipe):
        self.tipe = tipe

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_tipe(self):
        return self.set_tipe
    
    def get_summary(self):
        return "Hunian Rumah tipe " + self.tipe + " milik " + self.nama_pemilik + " dengan luas " + str(self.get_luas()) + " m2 dan " + str(self.get_jml_kamar()) + " kamar dihuni sebanyak " + str(self.get_jml_penghuni()) + " orang."