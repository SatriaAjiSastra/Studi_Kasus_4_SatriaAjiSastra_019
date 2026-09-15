# Dictionary buku yang berisi judul, penulis, dan tahun terbit
buku = {
    "judul": "Cara Membaca",
    "penulis": "Aji Sastra",
    "tahun_terbit": 2026
}

# perulangan biar menu terus jalan sampai pengguna memilih keluar
while True:
    print()
    print("MENU PENGELOLAAN DATA BUKU")
    print("1. Tampilkan Data Buku")
    print("2. Tambah Data Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        # Menampilkan data buku ketika pengguna memilih menu tampilkan data
        print()
        print("Data Buku Saat Ini")
        print("Judul:", buku["judul"])
        print("Penulis:", buku["penulis"])
        print("Tahun Terbit:", buku["tahun_terbit"])
        if "penerbit" in buku:
            print("Penerbit:", buku["penerbit"])

    elif pilihan == "2":
        # Menambahkan data penerbit ke dalam Dictionary
        penerbit_baru = input("Masukkan nama penerbit: ")
        buku["penerbit"] = penerbit_baru
        print("Data penerbit berhasil ditambahkan!")
        
        # Menampilkan data buku setelah dilakukan perubahan
        print()
        print("Data Buku Terbaru")
        print("Judul:", buku["judul"])
        print("Penulis:", buku["penulis"])
        print("Tahun Terbit:", buku["tahun_terbit"])
        print("Penerbit:", buku["penerbit"])

    elif pilihan == "3":
        # Ubah data penulis pada Dictionary
        print("Penulis saat ini:", buku.get("penulis"))
        penulis_baru = input("Masukkan nama penulis baru: ")
        buku["penulis"] = penulis_baru
        print("Data penulis berhasil diubah!")
        
        # Menampilkan data buku setelah dilakukan perubahan
        print()
        print("Data Buku Terbaru")
        print("Judul:", buku["judul"])
        print("Penulis:", buku["penulis"])
        print("Tahun Terbit:", buku["tahun_terbit"])
        if "penerbit" in buku:
            print("Penerbit:", buku["penerbit"])

    elif pilihan == "4":
        # Hapus data penerbit dari Dictionary
        if "penerbit" in buku:
            del buku["penerbit"]
            print("Data penerbit berhasil dihapus!")
        else:
            print("Data penerbit belum ada di dalam Dictionary.")
        
        # Menampilkan data buku setelah dilakukan perubahan
        print()
        print("--- Data Buku Terbaru ---")
        print("Judul:", buku["judul"])
        print("Penulis:", buku["penulis"])
        print("Tahun Terbit:", buku["tahun_terbit"])

    elif pilihan == "5":
        # Perulangan berhenti ketika memilih keluar
        print("Terima kasih telah menggunakan program pengelolaan data buku!")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1 sampai 5.")