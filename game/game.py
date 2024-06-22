import random

welcome_message = "WELCOME TO HEDGAME"
bear_posisiton = random.randint(1, 4) 

print("************************")
print(f"** {welcome_message} **")
print("************************")

nama_user = input("Masukkan nama kamu : ")

print(f'''
      Halo {nama_user}! Coba perhatikan goa dibawah ini
      |_| |_| |_| |_| 
      ''')

pilihan_user = int(input("Menurut kamu di goa nomor berapa BERUANG itu berada ? [1 / 2 / 3 / 4 ]: "))

if pilihan_user == bear_posisiton:
    print(f"Selamat {nama_user} kamu menang! posisi BERUANG berada di goa nomor {bear_posisiton} dan pilihan mu adalah {pilihan_user}")
else:
    print(f"Pilihan kamu salah! BERUANG tidak ada di posisi itu, tapi ada di nomor {bear_posisiton}, sedangkan kamu memilih nomor {pilihan_user}")


 
