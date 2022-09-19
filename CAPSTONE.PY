data_mobil = {
    "B 111 AA":{
        "merk" : "Honda Accord",
        "warna" : "Hitam",
        "jenis" : "Sedan",
        "status" : "Available"
    },
    "B 222 BB":{
        "merk" : "Mitsubishi Pajero",
        "warna" : "Putih",
        "jenis" : "SUV",
        "status" : "Available"
    },
    "B 333 CC":{
        "merk" : "Toyota Camry",
        "warna" : "Silver",
        "jenis" : "Sedan",
        "status" : "Available"
    },
    "B 444 DD" :{
        "merk" : "Toyota Fortuner",
        "warna" : "Hitam",
        "jenis" : "SUV",
        "status" : "Available"
    }

}

def main_menu(): 
    print(''' SELAMAT DATANG DI RENTAL MOBIL MEWAH
    1. Tampilkan Data Mobil.
    2. Menambah Data Mobil.
    3. Update Data Mobil.
    4. Hapus Data Mobil.
    5. Exit
    ''')
    x = input("Masukan pilihan anda: ")
    if x == "5":
        exit = input("Apa anda yakin ingin keluar? \n1.Iya\n2.Tidak\nMasukan pilihan: ")
        if exit == "1":
            print("TERIMAKASIH")
        elif exit =="2":
            main_menu()
        else:
            print("Input yang anda masukan salah")
            main_menu()
    elif x =="1":
        submenampilkan()
    elif x == "4":
        hapus()
    elif  x == "2":
        tambah()
    elif x == "3":
        update()
    else:
        print("Input anda salah")
        main_menu()

def Menampilkan():
    print(f"Plat\t\tMerk\t\t Warna\t Jenis \t Status")
    for i in data_mobil:
        print(f'{i}|{data_mobil[i]["merk"]}     \t|{data_mobil[i]["warna"]}\t|{data_mobil[i]["jenis"]}\t|{data_mobil[i]["status"]}')

def submenampilkan():
    print("1.Tampilkan semua mobil\n2.Cari Mobil\n3.Kembali")
    pilih = int(input("Masukan pilihan anda: "))
    if pilih == 1:
        Menampilkan()
        submenampilkan()
    elif pilih == 3:
        main_menu()
    elif pilih == 2:
        xmobil = (input("Masukan Plat mobil: "))
        if xmobil in data_mobil:
            print(data_mobil[xmobil])
            submenampilkan()
        else:
            print("Data mobil tidak ada")
            submenampilkan()

def hapus():
    print("1.Hapus data mobil\n2.Kembali")
    subhapus = input("Masukan pilihan anda: ")
    if subhapus == "1":
        id_hapus = input("Masukan Plat mobil: ")
        if id_hapus in data_mobil:
            print("Anda yakin ingin hapus ? \n1.Iya\n2.Tidak")
            yakin_tidak = input("Masukan pilihan anda: ")
            if yakin_tidak == "1":
                data_mobil.pop(id_hapus)
                print("Data telah dihapus")
                hapus()
            elif yakin_tidak == "2":
                hapus()
            else:
                print("Input anda salah")
                hapus()
        else:
            print("Data tidak ditemukan")
            hapus()

    else:
        main_menu()


def tambah():
    print("1.Tambah data mobil\n2.Kembali")
    subtambah = input("Masukan pilihan anda: ")
    if subtambah == "1":
        kode_baru = input("Masukkan Plat mobil: ")
        if kode_baru in data_mobil.keys():
            print("Mobil sudah ada")
            tambah()
        else:
            merkbaru = input("Masukkan merk mobil\t:")
            jenisbaru = input("Masukkan jenis mobil\t:")
            warnabaru = input("Masukkan warna mobil\t:")
            statusbaru = input("Masukan status mobil\t:")
            data_mobil.update(
           {kode_baru : {
                "merk" : merkbaru,
                "jenis" : jenisbaru,
                "warna" : warnabaru,
                "status" : statusbaru
            }
           }
        )
        print("Apa anda yakin ingin tambah data mobil ? \n1.Iya\n2.Tidak")
        yakin_tidak_tambah = input("Masukan pilihan anda: ")
        if yakin_tidak_tambah == "1":
            print("Data mobil telah disimpan")
            tambah()
        elif yakin_tidak_tambah =="2":
            data_mobil.pop(kode_baru)
            tambah()
    elif subtambah == "2":
        main_menu()
    else:
        print("Input anda salah")
        tambah()

def update():
    print("1.Update data mobil \n2.Kembali")
    subupdate = input("Masukan pilihan anda: ")
    if subupdate == "1":
        id_update= input("Masukan Plat mobil: ")
        if id_update in data_mobil:
            kolom_update = input("Masukan kolom yang ingin diupdate: ")
            z = kolom_update.lower()
            update_data = input(f"Masukan {kolom_update} baru: ")
            print("Apakah ingin update data \n1.Iya\n2.Tidak")
            yakinupdate = input("Masukan pilihan anda: ")
            if yakinupdate == "1":
                data_mobil[id_update][z] = update_data
                print("Data mobil telah di update")
                update()
            elif yakinupdate == "2":
                update()
            else:
                print("Input anda salah")
                update()
        else:
            print("Data tidak ditemukan")
            update()
            
    elif subupdate == "2":
        main_menu()
    else:
        print("Input anda salah")
        update()
        

main_menu()