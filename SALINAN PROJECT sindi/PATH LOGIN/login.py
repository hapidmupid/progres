import os
import pandas as pd
from tabulate import tabulate
import time
import csv

def clear():
    os.system('cls')

# ------------------------------------------------ FUNGSI UNTUK LOGIN ------------------------------------------------ 
#nanti copas kebawah ya, ini yang atas
# Fungsi untuk login admin
def page_admin():
    clear()
    print(f'''
    {"="*60}
    |{"A C A D E M I X".center(58)}|
    |{"Sistem Informasi Akademik".center(58)}|
    {'='*60}  
    |{"Halaman Login Admin".center(58)}|
    |{"-"*58}|
    |{"[1]. Login Admin".ljust(58)}|
    |{"[2]. Ubah Password".ljust(58)}|
    |{"[3]. Kembali".ljust(58)}|
    {'='*60}
    ''')
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        login_admin()
    elif pilihan == "2":
        ubah_password()
        pass
    elif pilihan == "3":
        start()
    else:
        input("Inputan tidak valid. Silakan klik \"ENTER\" untuk kembali")
        page_admin()

#fungsi login selain admin
def page_user():
    clear()
    print("LOGIN USER".center(60))
    print("=" * 60)
    print('Silahkan Pilih Sesuai Akun yang anda Miliki')
    print('1. Dosen')
    print('2. Mahasiswa')
    print("-" * 60)
    x = input("Masukkan Input = ")
    if x == '1':
        login_dosen()
    if x == '2':
        login_mahasiswa()

def check_login_mahasiswa(username, password):
    file_path = r'pwmahasiswa.csv'
    df = pd.read_csv(file_path)
    user_data = df[df['Username'] == username]
    if not user_data.empty:
        stored_password = user_data['Password'].values[0]
        if stored_password == password:
            return True
        else:
            return False
    else:
        return False

def check_login_dosen(username, password):
    file_path = r'pwdosen.csv'
    df = pd.read_csv(file_path)
    user_data = df[df['Username'] == username]
    if not user_data.empty:
        stored_password = user_data['Password'].values[0]
        if stored_password == password:
            return True
        else:
            return False
    else:
        return False

def login_mahasiswa():
    while True:
        print('=' * 50)
        print('Halaman Login Mahasiswa'.center(50))
        print('=' * 50)
        username = input('Masukkan Username: ')
        password = input('Masukkan Password: ')
        if check_login_mahasiswa(username, password):
            print('Login Berhasil! Selamat Datang!')
            time.sleep(2) 
            clear()
            #path DASHBOARD mahasiswa
            break 
        else:
            print('Username atau Password salah. Coba lagi.')
            time.sleep(2) 
            clear()
            login_mahasiswa()

def login_dosen():
    while True:
        print('=' * 50)
        print('Halaman Login Dosen'.center(50))
        print('=' * 50)
        username = input('Masukkan Username: ')
        password = input('Masukkan Password: ')
        if check_login_dosen(username, password):
            print('Login Berhasil! Selamat Datang!')
            time.sleep(2) 
            clear()
            #path DASHBOARD dosen
            break 
        else:
            print('Username atau Password salah. Coba lagi.')
            time.sleep(2) 
            clear()
            login_dosen()

def login_admin():
    print("LOGIN ADMIN".center(60))
    print("-" * 60)
    username = input("Masukkan Username: ").strip()
    password = input("Masukkan Password: ").strip()
    print("=" * 60)
    # Membaca data dari file CSV menggunakan pandas
    try:
        df = pd.read_csv("data_admin.csv")
    except FileNotFoundError:
        print("File 'data_admin.csv' tidak ditemukan! Pastikan file sudah ada.")
        return
    # Mencari kecocokan username dan password
    data_login = df[(df['Username'] == username) & (df['Password'] == password)]
    if len(data_login) > 0:  # Jika data_login tidak kosong
        input("Login Berhasil. Klik \"ENTER\" Untuk Melanjutkan!")
        main_menu_admin()  # Panggil fungsi menu admin di sini
    else:
        print("Username atau Password Salah. Silahkan Coba Lagi!")
        print("-" * 60)
        login_admin()

# Fungsi untuk mengubah password
def ubah_password():
    clear()
    print('='*60)
    print("UBAH PASSWORD".center(60))
    print("-" * 60)
    file_csv = "data_admin.csv"
    username_target = input('Masukkan Username = ')
    
    # Baca file CSV
    df = pd.read_csv(file_csv)
    
    if username_target not in df['Username'].values:
        print(f"Username '{username_target}' tidak ditemukan.")
        yesno = input("Coba Lagi? ketik 1 untuk mencoba lagi = ")
        if yesno == '1':
            ubah_password()
        else:
            page_admin()
            return
    
    # Konfirmasi password lama
    password_lama = input('Masukkan Password Lama = ')
    user_data = df.loc[df['Username'] == username_target]
    
    if user_data.iloc[0]['Password'] != password_lama:
        print("Password lama tidak sesuai.")
        yesno1 = input("Coba Lagi? ketik 1 untuk mencoba lagi = ")
        if yesno1 == '1':
            ubah_password()
        else:
            page_admin()
            return

    # Masukkan password baru
    password_baru = input('Masukkan Password Baru = ')
    
    # Validasi konfirmasi password baru
    def konfpass():
        konfirmasi_password = input('Konfirmasi Password Baru = ')
        if password_baru != konfirmasi_password:
            konfir=input("Konfirmasi password baru tidak cocok. ketik 1 jika batal, ketik Tombol lainnya untuk melanjutkan. = ")
            if konfir == '1':
                page_admin()
                return
            else:
                konfpass()
                return
    
    konfpass()
    # Ubah password
    df.loc[df['Username'] == username_target, 'Password'] = password_baru
    df.to_csv(file_csv, index=False)
    print(f"Password berhasil diperbarui untuk '{username_target}'.")
    def kembali():
        back = input('Masukkan y jika selesai, masukkan n jika ingin merubah password lagi. (y/n): ')
        if back == 'y' or back == 'Y':
            page_admin()
            return
        elif back == 'n' or back == 'N':
            ubah_password()
            return
        else:
            clear()
            print('Mohon input dengan benar...')
            kembali()
    kembali()