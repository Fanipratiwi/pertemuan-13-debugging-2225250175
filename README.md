Nama: Fani Pratiwi Nur Indah

NIM: 2225250175

Kelas: 3B

## Kasus

Praktik ini membahas debugging dan testing pada program Python. Pengujian dilakukan untuk menemukan dan memperbaiki bug pada perhitungan rata-rata, penentuan status kelulusan, dan pencarian nilai tertinggi.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | [80, 60, 90, 70] | 75.0 | 60.0 | FAIL |
| T2 | [100, 80] | 90.0 | 36.0 | FAIL |
| T3 | 60 | Lulus | Tidak lulus | FAIL |
| T4 | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | [80, 60, 90, 70] | 90 | 0 | FAIL |

## Bug Report

### Bug 1: Perhitungan Rata-rata
Gejala: Hasil rata-rata tidak sesuai.

Akar penyebab: Program selalu membagi jumlah nilai dengan angka 5.

Perbaikan: Menggunakan len(nilai) sebagai pembagi dan menangani list kosong.

### Bug 2: Status Kelulusan
Gejala: Nilai 60 dianggap tidak lulus.

Akar penyebab: Menggunakan operator >, sehingga nilai 60 tidak memenuhi syarat.

Perbaikan: Mengubah operator menjadi >=.

### Bug 3: Nilai Tertinggi
Gejala: Program menghasilkan nilai tertinggi yang salah.

Akar penyebab: Operator perbandingan terbalik dan nilai awal ditetapkan 0.

Perbaikan: Menggunakan nilai pertama sebagai nilai tertinggi awal dan operator >.

## Retest

| ID | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|
| T1 | 75.0 | 75.0 | PASS |
| T2 | 90.0 | 90.0 | PASS |
| T3 | Lulus | Lulus | PASS |
| T4 | Tidak lulus | Tidak lulus | PASS |
| T5 | 90 | 90 | PASS |

## Cara Menjalankan

python praktik/praktik_4_debugging.py

## Refleksi

Teknik debugging membantu menemukan penyebab kesalahan melalui tracing dan test case. Setelah kode diperbaiki, seluruh pengujian dijalankan kembali untuk memastikan hasil sesuai dengan yang diharapkan.