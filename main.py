while True:
    angka = int(input("masukan angka: "))
    if angka % 2 == 0:
        print("Angka", angka, "adalah bilangan genap")
    else:
        print("Angka", angka, "adalah bilangan ganjil")

    print("Apakah Anda ingin memasukkan angka lagi? (y/n)")
    if input().lower() != "y":
        print("Program selesai.")
        break