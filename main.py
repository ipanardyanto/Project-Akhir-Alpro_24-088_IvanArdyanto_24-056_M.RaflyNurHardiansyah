# atribut tiket
daftar_atribut = ["nama_pertandingan", "harga_tiket", "stok_tiket", "tanggal_pertandingan"]

# menyimpan riwayat transaksi
daftar_riwayat_transaksi = {}

# menyimpan menu pilihan
daftar_menu = [
    "Lihat semua tiket",
    "Tambah tiket",
    "Ubah tiket",
    "Hapus tiket",
    "Pesan tiket",
    "Riwayat transaksi",
    "Keluar"
]

# menyimpan tiket
daftar_tiket = {
    1: {
        "nama_pertandingan": "Manchester United VS Liverpool",
        "harga_tiket": 12000,
        "stok_tiket": 100,
        "tanggal_pertandingan": "05-12-2024",
        "tanggal_pembuatan": "28-11-2024"
    }
}

# fungsi mengecek apakah tiket soldout
def cek_soldout(id_tiket):
    # kembalian true jika stok sudah habis, dan false jika tidak
    hasil = True if int(daftar_tiket[id_tiket]["stok_tiket"]) <= 0 else False
    return hasil

# fungsi mengecek apakah terdapat tiket dengan suatu id
def cek_tiket(id_tiket):
    # kembalian true jika id tiket terdapat pada daftar tiket, dan false untuk sebaliknya
    hasil = True if id_tiket in daftar_tiket else False
    return hasil

# fungsi mengecek apakah terdapat pesanan/transaksi dengan suatu id
def cek_pesanan(id_pesanan):
    # kembalian true jika id pesanan terdapat dalam riwayat transaksi, dan false untuk sebaliknya
    hasil = True if id_pesanan in daftar_riwayat_transaksi else False
    return hasil

# fungsi melihat daftar tiket
def lihat_daftar_tiket():
    return daftar_tiket

# fungsi melihat daftar riwayat transaksi
def lihat_daftar_riwayat_transaksi():
    return daftar_riwayat_transaksi

# fungsi untuk membuat tiket
def buat_tiket(nama_pertandingan, harga_tiket, stok_tiket, tanggal_pertandingan, tanggal_pembuatan):
    id_tiket = 0

    # jika tiket kosong
    if not daftar_tiket:
        # mengambil panjangnya dan menambahkannya dengan 1
        id_tiket = len(daftar_tiket) + 1

    # jika tidak kosong
    else:
        # mengambil urutan terakhir, dan menambahkannya dengan 1
        id_tiket = list(daftar_tiket)[-1] + 1

    # dictionary data baru
    data_baru = {
        "nama_pertandingan": nama_pertandingan,
        "harga_tiket": harga_tiket,
        "stok_tiket": stok_tiket,
        "tanggal_pertandingan": tanggal_pertandingan,
        "tanggal_pembuatan": tanggal_pembuatan,
    }

    # memasukkan data baru pada daftar tiket
    daftar_tiket[id_tiket] = data_baru

    return id_tiket

# fungsi untuk mengubah/edit tiket
def ubah_tiket(id_tiket, atribut, nilai_baru):
    # mengubah data lama dengan data baru
    daftar_tiket[id_tiket][atribut] = nilai_baru

    return daftar_tiket[id_tiket][atribut]

# fungsi untuk memesan tiket
def pesan_tiket(id_tiket, nama_pemesan,  uang_pemesan):
    id_riwayat = len(daftar_riwayat_transaksi) + 1
    stok_tiket = int(daftar_tiket[id_tiket]["stok_tiket"])
    harga_tiket = int(daftar_tiket[id_tiket]["harga_tiket"])
    uang_pemesan = int(uang_pemesan)

    # jika uang pemesan dibawah harga tiket
    if uang_pemesan < harga_tiket:
        return False
    
    # stok tiket dikurangi
    daftar_tiket[id_tiket]["stok_tiket"] = stok_tiket - 1

    # uang kembalian pemesan
    uang_kembalian = uang_pemesan - harga_tiket

    # data baru
    data_baru = {
        "Nama Pemesan": nama_pemesan,
        "Uang Pemesan": uang_pemesan,
        "Uang Kembalian": uang_kembalian,
        "tiket": daftar_tiket[id_tiket]
    }
    
    # penambahan riwayat
    daftar_riwayat_transaksi[id_riwayat] = data_baru
    return {"id_riwayat": id_riwayat, "uang_kembalian": uang_kembalian}

# fungsi untuk menghapus tiket
def hapus_tiket(id_tiket):
    # menghapus suatu tiket menggunakan id tiket
    daftar_tiket.pop(id_tiket)

    return id_tiket

# program utama
while True:
    print("Daftar menu:")
    
    # menampilkan menu
    for i in range(len(daftar_menu)):
        print(f"{i + 1}. {daftar_menu[i]}")
    
    # meminta input pilihan
    menu_input = input("Masukkan pilihan anda (1 - 7): ")
    print()

    # daftar tiket
    if menu_input == "1":
        hasil = lihat_daftar_tiket()
        
        # jika tiket kosong
        if not hasil:
            print("Tiket kosong.\n")
            continue

        # menampilkan semua tiket
        for id_tiket, tiket in hasil.items():
            print(f"{id_tiket}:")
            for atribut, data_tiket in tiket.items():
                print(f" {atribut}: {data_tiket}")
        
        print()

    # tambah tiket
    elif menu_input == "2":
        # meminta input
        nama_pertandingan = input("Masukkan nama pertandingan: ")
        harga_tiket = int(input("Masukkan harga tiket: "))
        stok_tiket = int(input("Masukkan stok tiket: "))
        tanggal_pertandingan = input("Masukkan tanggal pertandingan (dd-mm-yyyy): ")
        tanggal_pembuatan = input("Masukkan tanggal pembuatan (dd-mm-yyyy): ")

        # proses penambahan tiket
        hasil = buat_tiket(nama_pertandingan, harga_tiket, stok_tiket, tanggal_pertandingan, tanggal_pembuatan)

        print(f"\nTiket berhasil dibuat, dengan id: {hasil}")

    # ubah tiket
    elif menu_input == "3":
        daftar_tiket = lihat_daftar_tiket()

        # jika daftar tiket kosong
        if not daftar_tiket:
            print("Tiket kosong.")
            continue

        # menampilkan tiket yang dapat diubah
        print("ID tiket yang dapat dipilih:")
        for id_tiket, tiket in daftar_tiket.items():
            for atribut, data_tiket in tiket.items():
                if atribut == "nama_pertandingan":
                    print(f"{id_tiket}. {data_tiket}")
        
        # input pilihan
        id_tiket = int(input("Masukkan ID tiket: "))

        # apakah id tiket tidak ditemukan
        if not cek_tiket(id_tiket):
            print("Tiket tidak ditemukan.\n")
            continue

        # menampilkan atribut yang dapat diubah
        print("Masukkan atribut yang akan diubah: ")
        for i in range(len(daftar_atribut)):
            print(f"{i + 1}. {daftar_atribut[i]}")
        
        # input pilihan
        pilih_atribut = int(input("Pilih atribut: "))

        # jika atribut yang dipilih tidak tersedia
        if pilih_atribut < 0 or pilih_atribut > len(daftar_atribut) + 1:
            print("Atribut yang anda pilih tidak tersedia.\n")
            continue

        pilih_atribut = daftar_atribut[pilih_atribut - 1]

        # input nilai baru
        nilai_baru = input("masukkan nilai baru: ")

        # proses ubah tiket
        hasil = ubah_tiket(id_tiket, pilih_atribut, nilai_baru)

        # jika proses ubah berhasil
        if hasil:
            print("Data berhasil diubah.\n")

    # hapus tiket
    elif menu_input == "4":
        daftar_tiket = lihat_daftar_tiket()

        # jika tiket kosong
        if not daftar_tiket:
            print("Tiket kosong.")
            continue

        # menampilkan tiket apa saja yang dapat dihapus
        print("ID tiket yang dapat dipilih:")
        for id_tiket, tiket in daftar_tiket.items():
            for atribut, data_tiket in tiket.items():
                if atribut == "nama_pertandingan":
                    print(f"{id_tiket}. {data_tiket}")
        
        # input pilihan
        id_tiket = int(input("Masukkan ID tiket: "))

        # jika tiket tidak ditemukan
        if not cek_tiket(id_tiket):
            print("Tiket tidak ditemukan.\n")
            continue

        # proses hapus tiket
        hasil = hapus_tiket(id_tiket)

        # jika proses hapus berhasil
        if hasil:
            print("Tiket berhasil dihapus.\n")
            continue

    # pesan tiket
    elif menu_input == "5":
        daftar_tiket = lihat_daftar_tiket()

        # jika tiket kosong
        if not daftar_tiket:
            print("Tiket kosong.")
            continue

        # menampilkan tiket apa saja yang dapat dipesan
        print("ID tiket yang dapat dipilih:")
        for id_tiket, tiket in daftar_tiket.items():
            for atribut, data_tiket in tiket.items():
                if atribut == "nama_pertandingan":
                    print(f"{id_tiket}. {data_tiket}")
        
        # input pilihan
        id_tiket = int(input("Masukkan ID tiket: "))

        # jika tiket tidak ditemukan
        if not cek_tiket(id_tiket):
            print("Tiket tidak ditemukan.\n")
            continue

        # jika tiket soldout
        if cek_soldout(id_tiket):
            print("Tiket soldout.\n")
            continue

        # input nama dan uang pemesan
        nama_pemesan = input("Masukkan nama pemesan: ")
        uang_pemesan = int(input("Masukkan uang pemesan: "))

        # proses pemesanan tiket
        hasil = pesan_tiket(id_tiket, nama_pemesan, uang_pemesan)

        # jika uang tidak mencukupi
        if not hasil:
            print("Uang anda tidak mencukupi.\n")
            continue

        print("Tiket berhasil dipesan.")
        print(f"Kembalian pemesan: {hasil['uang_kembalian']}.\n")

    # riwayat transaksi
    elif menu_input == "6":
        hasil = lihat_daftar_riwayat_transaksi()

        # jika riwayat transaksi kosong
        if not hasil:
            print("Riwayat kosong.\n")
            continue

        # menampilkan riwayat transaksi
        for id_riwayat, riwayat in hasil.items():
            print(f"{id_riwayat}:")
            for atribut, data_riwayat in riwayat.items():
                if atribut == "tiket":
                    print(f" {atribut}:")
                    print(f"  - Nama pertandingan: {data_riwayat['nama_pertandingan']}")
                    print(f"  - Tanggal Pertandingan: {data_riwayat['tanggal_pertandingan']}")

                    continue

                print(f" {atribut}: {data_riwayat}")
        
        print()
                
    # keluar program
    elif menu_input == "7":
        print("\nKeluar dari program utama")

        # keluar dari loop
        break

    # pilihan tidak valid
    else:
        print("Maaf, menu yang anda pilih tidak valid.\n")