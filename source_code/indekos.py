from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, jenis_indekos, jml_penghuni, jml_kamar, luas, gambar):
        super().__init__("Indekos", jml_penghuni, jml_kamar, luas, gambar)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.jenis_indekos = jenis_indekos

    def set_namaPemilik(self, nama):
        self.nama_pemilik = nama

    def set_namaPenghuni(self, nama):
        self.nama_penghuni = nama

    def set_jenisIndekos(self, jenis):
        self.jenis_indekos = jenis

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_jenis_indekos(self):
        return self.jenis_indekos

    def get_summary(self):
        return "Hunian Indekos " + self.jenis_indekos + " dengan luas " + str(self.get_luas()) + " m2 dengan " + str(self.get_jml_kamar()) + " kamar milik " + self.nama_pemilik + " dapat dihuni oleh " + str(self.get_jml_penghuni()) + " orang \n" + "Penghuni saat ini : " + self.nama_penghuni