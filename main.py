from bilangan import cek_bilangan
from tambahfile import tambah_akun


def main():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Cek bilangan genap/ganjil")
        print("2. Tambah akun")
        print("0. Keluar")

        pilihan = input("Pilih menu (0/1/2): ").strip()

        if pilihan == "1":
            cek_bilangan()
        elif pilihan == "2":
            tambah_akun()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 0, 1, atau 2.")


if __name__ == "__main__":
    main()
