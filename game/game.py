import random

welcome_message = "WELCOME TO HEDGAME"
bear_posisiton = random.randint(1, 4) 

print("************************")
print(f"** {welcome_message} **")
print("************************")

nama_user = input("Masukkan nama kamu : ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4

goa = goa_kosong.copy()
goa[bear_posisiton - 1] = "|0_0|"

print(f'''
      Halo {nama_user}! Coba perhatikan goa dibawah ini
      {goa_kosong}
      ''')

pilihan_user = int(input("Menurut kamu di goa nomor berapa BERUANG itu berada ? [1 / 2 / 3 / 4 ]: "))

confirm_answer = input(f"Apakah kamu yakin jawabannya adalah {pilihan_user} ? [y/n]: ")

if confirm_answer == "n":
    print("Program dihentikan!")
    exit()
elif confirm_answer == "y":
    if pilihan_user == bear_posisiton:
        print(f"{goa} \n Selamat Kamu Menang!")
    else:
        print(f"{goa} \n Maaf Kamu Kalah!")
else:
    print("Silahkan ulangi programnya!")
    exit()
        


 
