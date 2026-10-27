def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


test_case = [75, 60, 59]

for nilai in test_case:
    print("Nilai:", nilai)
    print("Status:", status_lulus(nilai))
    print()