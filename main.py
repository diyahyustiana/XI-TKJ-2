def cek_bilangan():
    while True:
        angka = int(input("masukan angka: "))
        if angka % 2 == 0:
            hasil = "genap"
        else:
            hasil = "ganjil"
        print("Angka", angka, "adalah bilangan", hasil)

        pilihan = input("Apakah Anda ingin memeriksa bilangan lain? (y/n): ").lower().strip()
        if pilihan != 'y':  
            print("Terima kasih telah menggunakan program ini.")
            break 

cek_bilangan()