def hitung_total(data):
    total = 0

    for nilai in data:
        total += nilai

    return total


angka = [10, 20, 30]
hasil = hitung_total(angka)

print("Total:", hasil)