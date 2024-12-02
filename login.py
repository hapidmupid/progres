import os

def clear():
    os.system('cls')

def dashboard_dosen():
    clear()
    print(f'''
    {"="*60}
    |{"A C A D E M I X".center(58)}|
    |{"Sistem Informasi Akademik".center(58)}|
    {'='*60}  
    |{"Dashboard Dosen".center(58)}|
    |{"-"*58}|
    |{"[1]. Lihat Jadwal".ljust(58)}|
    |{"[2]. Logout".ljust(58)}|
    |{"[3]. Keluar".ljust(58)}|
    {'='*60}
    ''')
    pilih = input("Pilih menu: ")

    if pilih == "1":
        #jadwal_dosen
        print('yo')
    elif pilih == "2":
        #start()
        print('ok')
    elif pilih == "3":
        clear()
        exit()
    else : 
        print("Nomor yang Anda masukkan salah! Silakan coba lagi.")
        dashboard_dosen()
dashboard_dosen()

def dashboard_mahasiswa():
    clear()
    print(f'''
    {"="*60}
    |{"A C A D E M I X".center(58)}|
    |{"Sistem Informasi Akademik".center(58)}|
    {'='*60}  
    |{"Dashboard Mahasiswa".center(58)}|
    |{"-"*58}|
    |{"[1]. Lihat Jadwal".ljust(58)}|
    |{"[2]. Kartu Rencana Studi".ljust(58)}|
    |{"[3]. Logout".ljust(58)}|
    |{"[4]. Keluar".ljust(58)}|
    {'='*60}
    ''')
    pilih = input("Pilih menu: ")

    if pilih == "1":
        #jadwal_mahasiswa()
        print('yo')
    elif pilih == "2":
        #krs()
        print('ok')
    elif pilih == "3":
        #start()
        print('ya')
    elif pilih == "4":
        clear()
        exit()
    else : 
        print("Nomor yang Anda masukkan salah! Silakan coba lagi.")
        dashboard_mahasiswa()
dashboard_mahasiswa()