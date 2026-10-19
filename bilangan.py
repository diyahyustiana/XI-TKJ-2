def cek_bilangan():
    while True:
        try:
            angka = int(input("Masukkan angka: "))
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat.")
            continue

        if angka % 2 == 0:
            hasil = "genap"
        else:
            hasil = "ganjil"
        print("Angka", angka, "adalah bilangan", hasil)

        pilihan = input("Apakah Anda ingin memeriksa bilangan lain? (y/n): ").lower().strip()
        if pilihan != "y":
            print("Terima kasih telah menggunakan program ini.")
            break 
