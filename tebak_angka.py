import random

# Mendefinisikan fungsi untuk memeriksa tebakan
def periksa_tebakan(tebakan, angka_rahasia):
  """
  Fungsi ini memeriksa apakah tebakan pengguna benar atau salah.

  Args:
    tebakan: Angka tebakan pengguna.
    angka_rahasia: Angka rahasia yang harus ditebak.

  Returns:
    String yang menunjukkan apakah tebakan benar ("Benar!"), terlalu tinggi ("Terlalu tinggi!"), atau terlalu rendah ("Terlalu rendah!").
  """
  if tebakan == angka_rahasia:
    return "Benar!"
  elif tebakan > angka_rahasia:
    return "Terlalu tinggi!"
  else:
    return "Terlalu rendah!"

# Menentukan batas tebakan
batas_bawah = 1
batas_atas = 100

# Menentukan angka rahasia
angka_rahasia = random.randint(batas_bawah, batas_atas)

# Perulangan untuk tebakan
tebakan_benar = False
while not tebakan_benar:
  # Mendapatkan tebakan pengguna
  tebakan = int(input(f"Masukkan tebakan Anda ({batas_bawah}-{batas_atas}): "))

  # Memeriksa tebakan
  hasil_periksa = periksa_tebakan(tebakan, angka_rahasia)
  print(hasil_periksa)

  # Jika tebakan benar, keluar dari perulangan
  if hasil_periksa == "Benar!":
    tebakan_benar = True

# Menampilkan pesan kemenangan
print(f"Selamat! Anda berhasil menebak angkanya. Angka rahasianya adalah {angka_rahasia}.")
