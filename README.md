# LP9DPBO2023C2
## Janji
Saya Mia Karisma Haq NIM [2102165] mengerjakan soal Latihan Praktikum-9 dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

## Deskripsi Program
Spesifikasi:
Lengkapi fitur summary
Buat landing Page (button yg ngarah ke halaman daftar residen)
Tampilin gambar
Tambahin 1 metode yang masih relevan untuk setiap kelas

## Desain Program
Program terdiri dari 4 kelas dan 1 fungsi utama, yaitu kelas hunian, apartemen, indekos, rumah. Terdapat 3 objek yang sama yaitu apartemen, indekos dan rumah, yaitu sama-sama hunian/tempat tinggal. Sehingga ketiga kelas tersebut merupakan subclass dari kelas Hunian.
1. Kelas Hunian
   Kelas ini merupakan representasi dari objek hunian (tempat tinggal) terdiri dari atribut jenis, jumlah penghuni, jumlah kamar, luas, dan gambar. Kelas ini merupakan superclass dari kelas apartemen, indekos dan rumah, sehingga semua atribut pada kelas hunian akang diwariskan pada kelas turunannya. Pada kelas hunian terdapat method setter, getter, dokumen untuk bukti kepemilikan, dan summary berisi informasi mengenai hunian tersebut.
2. Kelas Apartemen
   Kelas ini merupakan representasi dari objek apartemen terdiri dari atribut nama pemilik dan nomor unit apartemen. Kelas ini merupakan subclass dari kelas hunian, sehingga mewarisi semua atribut pada kelas hunian. Pada kelas apartemen terdapat method setter, getter, dokumen untuk bukti kepemilikan, dan summary berisi informasi mengenai apartemen tersebut.
3. Kelas Indekos
   Kelas ini merupakan representasi dari objek indekos terdiri dari atribut nama pemilik, nama penghuni dan jenis indekos (khusus pria, wanita atau campur). Kelas ini merupakan subclass dari kelas hunian, sehingga mewarisi semua atribut pada kelas hunian. Pada kelas indekos terdapat method setter, getter, dokumen untuk bukti kepemilikan, dan summary berisi informasi mengenai indekos tersebut.
4. Kelas Rumah 
   Kelas ini merupakan representasi dari objek rumah terdiri dari atribut nama pemilik dan tipe rumah. Kelas ini merupakan subclass dari kelas hunian, sehingga mewarisi semua atribut pada kelas hunian. Pada kelas rumah terdapat method setter, getter, dokumen untuk bukti kepemilikan, dan summary berisi informasi mengenai rumah tersebut.
   
## Penjelasan Alur
Ketika pertama kali membuka program, maka user akan ditampilkan halaman landing page. Setelah itu, jika user menekan tombol "Open", maka akan terbuka page beranda yang berisi list daftar hunian. Pada setiap hunian terdapat tombol details, yang mana bila user tekan, akan menampilkan halaman detail dari hunian tersebut. Halaman detail berisi summary, dokumen serta foto dari jenis hunian yang dipilih. Jika user telah selesai melihat salah satu detail hunian, dan ingin melihat detail hunian jenis lain maka user dapat menekan tombol "close" dan user akan kembali ke halaman beranda, serta bisa memilih detail hunian jenis lain yang ingin dilihat. Apabila user telah selesai melihat semua data, maka user dapat menekan tombol close di beranda dan program akan terhenti.

## Dokumentasi
- Screenshot menjalankan contoh kode (database) yang dikirim 
  ![codeRunDB](https://github.com/miakarisma/LP9DPBO2023C2/assets/100817609/5b5fe329-618d-464a-9ca7-9c22b8e1bd87)
  <br>
- Landing Page
  <br>
  ![LandingPage](https://github.com/miakarisma/LP9DPBO2023C2/assets/100817609/46c04f9b-9a2b-4059-9bd6-6ea99f1a4272)
  <br>
- Beranda
  <br>
  ![ListPage](https://github.com/miakarisma/LP9DPBO2023C2/assets/100817609/e6243866-1d19-4171-9991-dcb16e1ee709)
  <br>
- Detail Page Apartment
  <br>
  ![DetailPageApartment](https://github.com/miakarisma/LP9DPBO2023C2/assets/100817609/6e96504e-c714-4b83-8ae4-a9c0dff79930)
  <br>
- Detail Page House
  <br>
  ![DetailPageHouse](https://github.com/miakarisma/LP9DPBO2023C2/assets/100817609/8e64f34a-18cb-405c-96a7-3e00f8da5d4b)
  <br>
- Detail Page Indekos
  <br>
  ![DetailPageIndekos](https://github.com/miakarisma/LP9DPBO2023C2/assets/100817609/8323436f-2bbf-42ff-946a-524d9646286b)

## Video Preview


https://github.com/miakarisma/LP9DPBO2023C2/assets/100817609/8878ea2a-be21-46f7-9d37-fa4f1d53c37c

