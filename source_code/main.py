# Saya Mia Karisma Haq NIM [2102165] mengerjakan soal Tugas Praktikum-3 dalam mata kuliah DPBO 
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

# Data hunian
hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, 25, "A01", 'Apart1.jpg'))
hunians.append(Rumah("Sekar MK", 3, 2, 21, "21", 'RumahTipe21.jpg'))
hunians.append(Indekos("Bp. Romi", "Cahya", "Khusus Pria", 4, 4, 18, 'indekos.png'))
hunians.append(Rumah("Satria", 1, 3, 36, "36", 'RumahTipe36.jpg'))
hunians.append(Apartemen("Mia K", 2, 1, 24, "B52", 'Apart2.jpg'))

# List untuk menyimpan gambar
listGambar = []

# Function untuk berpindah page
def movePage():
    landingPage.destroy() # menutup landing page
    main() # membuka page daftar hunian

# Function untuk menampilkan page details dari daftar hunian
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis()) # judul page

    # label page details
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # summary ditampilkan di page details
    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary() + "\n" + "Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=0, column=0, sticky="w")

    # menampilkan gambar di page details
    image = Image.open('assets/images/' + hunians[index].get_gambar()) 
    image = image.resize((200, 200)) 
    image = ImageTk.PhotoImage(image)
    listGambar.append(image)
    image_label = Label(d_frame, image=image)
    image_label.grid(row=1, column=0)

    # menampilkan button untuk menutup page detail
    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)

# Function untuk halaman utama (daftar hunian)
def main():
    root = Tk() # Membuat page utama
    root.title("Daftar Hunian") # Judul page utama
    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10) # Label page utama
    frame.pack(padx=10, pady=10) 

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    # Button add data
    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    # Button exit page (menutup halaman utama berarti menyelesaikan proses running)
    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    # Menampilkan list daftar hunian
    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

    # Menampilkan halaman utama selama user tidak menutup page
    root.mainloop

# Landing Page
landingPage = Tk()
landingPage.title("Home Page")
label = Label(landingPage, text="Selamat Datang di Sistem Informasi Hunian\n")
label.pack(padx=50, pady=50)
button = Button(landingPage, text='Open', command=movePage)
button.pack()

# Menampilkan halaman landing page selama user tidak menekan button open
landingPage.mainloop()