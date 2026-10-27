def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]

    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x

    return tertinggi

nilai = [80, 60, 90, 70]

print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))

print("\nPengujian rata-rata:")
print(hitung_rata_rata([80, 60, 90, 70]))  # 75.0
print(hitung_rata_rata([100, 80]))         # 90.0
print(hitung_rata_rata([]))                # 0

print("\nPengujian status:")
print(status(60))  # Lulus
print(status(59))  # Tidak lulus

print("\nPengujian nilai tertinggi:")
print(nilai_tertinggi([80, 60, 90, 70]))  # 90
print(nilai_tertinggi([]))                 # None