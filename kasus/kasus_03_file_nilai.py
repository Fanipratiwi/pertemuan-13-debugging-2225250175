def baca_nilai(nama_file):
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                print(baris.strip())
    except FileNotFoundError:
        print("File tidak ditemukan")


baca_nilai("nilai.txt")