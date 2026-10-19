import getpass
import hashlib
import json
import secrets
from pathlib import Path

from openpyxl import Workbook


FILE_JSON = Path(__file__).with_name("akun.json")
FILE_EXCEL = Path(__file__).with_name("akun.xlsx")
ITERASI_HASH = 600_000
HEADER_EXCEL = ("username", "password_hash", "salt")


def _buat_hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), bytes.fromhex(salt), ITERASI_HASH
    ).hex()


def _simpan_excel(akun):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Akun"
    worksheet.append(HEADER_EXCEL)

    for data in akun:
        worksheet.append(
            (data["username"], data["password_hash"], data["salt"])
        )
        worksheet.cell(row=worksheet.max_row, column=1).data_type = "s"

    workbook.save(FILE_EXCEL)


def tambah_akun():
    """Tambahkan akun ke file JSON dan ekspor seluruh data ke Excel."""
    if FILE_JSON.exists():
        with FILE_JSON.open("r", encoding="utf-8") as file:
            akun = json.load(file)
        if not isinstance(akun, list):
            raise ValueError("Format data akun.json harus berupa daftar.")
    else:
        akun = []

    username = input("Masukkan username: ").strip()
    if not username:
        print("Username tidak boleh kosong.")
        return

    if any(data.get("username", "").casefold() == username.casefold() for data in akun):
        print("Username tersebut sudah terdaftar.")
        return

    password = getpass.getpass("Masukkan password: ")
    if not password:
        print("Password tidak boleh kosong.")
        return
    if password != getpass.getpass("Ulangi password: "):
        print("Password tidak cocok. Data tidak disimpan.")
        return

    salt = secrets.token_hex(16)
    akun.append(
        {
            "username": username,
            "password_hash": _buat_hash_password(password, salt),
            "salt": salt,
        }
    )

    with FILE_JSON.open("w", encoding="utf-8") as file:
        json.dump(akun, file, ensure_ascii=False, indent=2)

    _simpan_excel(akun)
    print("Data akun berhasil disimpan ke akun.json dan akun.xlsx.")