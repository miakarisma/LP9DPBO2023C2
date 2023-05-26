from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas, no_apart, gambar):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, luas, gambar)
        self.nama_pemilik = nama_pemilik
        self.no_apartemen = no_apart

    def set_namaPemilik(self, nama):
        self.nama_pemilik = nama

    def set_noApart(self, nomor):
        self.no_apartemen = nomor

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_no_apart(self):
        return self.no_apartemen
    
    def get_summary(self):
        return "Hunian Apartemen " + self.no_apartemen + " milik " + self.nama_pemilik + " dengan luas " + str(self.get_luas()) + " m2 dan terdiri dari " + str(self.get_jml_kamar()) + " kamar dihuni sebanyak " + str(self.get_jml_penghuni()) + " orang."