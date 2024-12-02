import os
import pandas as pd
from tabulate import tabulate




def clear():
    os.system('cls')

# ------------------------------------------------ PAGE LOGIN ------------------------------------------------ 
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
    elif pilihan == "3":
        start()
    else:
        input("Inputan tidak valid. Silakan klik \"ENTER\" untuk kembali")

# Fungsi untuk login user
def page_user():
    clear()
    print(f'''
    {"="*60}
    |{"A C A D E M I X".center(58)}|
    |{"Sistem Informasi Akademik".center(58)}|
    {'='*60}  
    |{"Halaman Login User".center(58)}|
    |{"-"*58}|
    |{"[1]. Login Dosen".ljust(58)}|
    |{"[2]. Login Mahasiswa".ljust(58)}|
    |{"[3]. Kembali".ljust(58)}|
    {'='*60}
    ''')

    pilihan = input("Masukkan Input = ")
    if pilihan == '1':
        login_dosen()
    if pilihan == '2':
        login_mahasiswa()
    elif pilihan == '3':
        start()
    else:
        input("Inputan tidak valid. Silakan klik \"ENTER\" untuk kembali")


# ------------------------------------------------ FUNGSI UNTUK LOGIN ------------------------------------------------ 
# [1l login admin 
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
        page_admin()

# [2] Fungsi untuk mengubah password
def ubah_password():
    clear()
    file_csv = "data_admin.csv"

    print('='*60)
    print("UBAH PASSWORD".center(60))
    print("-" * 60)
    
    username_target = input('Masukkan Username = ')
    
    # Baca file CSV
    df = pd.read_csv(file_csv)
    
    if username_target not in df['Username'].values:
        print(f"Username '{username_target}' tidak ditemukan.")
        while True:
            yesno = input("Coba Lagi? Ketik 1 untuk mencoba lagi.\"ENTER\" untuk keluar : ")
            if yesno == '1':
                ubah_password()
                return
            elif yesno == "":
                page_admin()
            else:
                print("Mohon menginputkan sesuai perintah (ketik 1 untuk mencoba lagi.\"ENTER\" untuk keluar).")
    
    # Konfirmasi password lama
    password_lama = input('Masukkan Password Lama = ')
    user_data = df.loc[df['Username'] == username_target]
    
    if user_data.iloc[0]['Password'] != password_lama:
        print("Password lama tidak sesuai.")
        while True:
            yesno = input("Coba Lagi? Ketik 1 untuk mencoba lagi.\"ENTER\" untuk keluar : ")
            if yesno == '1':
                ubah_password()
                return
            elif yesno == "":
                page_admin()
            else:
                print("Mohon menginputkan sesuai perintah (ketik 1 untuk mencoba lagi.\"ENTER\" untuk keluar).")

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
        back = input('Masukkan y jika selesai, masukkan n jika ingin merubah password lagi. (y/n): ').strip().lower()
        if back == 'y':
            page_admin()
            return
        elif back == 'n':
            ubah_password()
            return
        else:
            print('Mohon input dengan benar...')
            kembali()
    kembali()




# LOGIN USER
# [1] LOGIN MAHASISWA
def login_mahasiswa(): 
    file_path = r'akun_mahasiswa.csv'

    while True:
        print('=' * 50)
        print('Halaman Login Mahasiswa'.center(50))
        print('=' * 50)
        
        global username
        username = int(input('Masukkan Username: '))
        global password
        password = input('Masukkan Password: ')

        # Cek login mahasiswa langsung di dalam fungsi ini
        df = pd.read_csv(file_path)
        user_data = df[df['Username'] == username]

        if not user_data.empty:
            stored_password = user_data['Password'].values[0]
            if stored_password == password:
                print('Login Berhasil! Selamat Datang!')
                clear()  # Asumsi Anda memiliki fungsi clear() untuk membersihkan layar
                # main_menu_mahasiswa()  # Asumsi Anda memiliki fungsi main_menu_mahasiswa()
                break 
            else:
                print('Username atau Password salah. Coba lagi.')
        else:
            print('Username atau Password salah. Coba lagi.')


# [2] LOGIN DOSEN
def login_dosen(): 
    file_path = r'akun_dosen.csv'  # Path ke file CSV untuk login dosen

    while True:
        print('=' * 50)
        print('Halaman Login Dosen'.center(50))
        print('=' * 50)
        
        username = input('Masukkan Username: ')
        password = input('Masukkan Password: ')

        # Cek login dosen langsung di dalam fungsi ini
        df = pd.read_csv(file_path)
        user_data = df[df['Username'] == username]

        if not user_data.empty:
            stored_password = user_data['Password'].values[0]
            if stored_password == password:
                print('Login Berhasil! Selamat Datang!')
                clear()  # Asumsi Anda memiliki fungsi clear() untuk membersihkan layar
                # main_menu_dosen()  # Panggil dashboard utama dosen jika login berhasil
                break 
            else:
                print('Password salah. Silakan coba lagi.')
        else:
            print('Username tidak ditemukan. Silakan coba lagi.')




# ------------------------------------------------ FUNGSI UNTUK MENGELOLA DATA (CRUD) ------------------------------------------------ 

def menu_kelola_data(menu_title, nama_file, kolom):
    clear()
    while True:

        print(f'''
        {"="*60}
        |{"A C A D E M I X".center(58)}|
        |{"Sistem Informasi Akademik".center(58)}|
        {'='*60}  
        |{f"Kelola Data {menu_title}".center(58)}|
        |{"-"*58}|
        |{"[1]. Tampilkan Data".ljust(58)}|
        |{"[2]. Tambah Data".ljust(58)}|
        |{"[3]. Ubah Data".ljust(58)}|
        |{"[4]. Hapus Data".ljust(58)}|
        |{"[5]. Kembali".ljust(58)}|
        |{"[6]. Keluar".ljust(58)}|
        {'='*60}
        ''')

        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            tampilkan_data(menu_title,nama_file, kolom)
        elif pilihan == "2":
            tambah_data(menu_title,nama_file, kolom)
        elif pilihan == "3":
            ubah_data(menu_title,nama_file, kolom)
        elif pilihan == "4":
            hapus_data(menu_title,nama_file, kolom)
        elif pilihan == "5":
            if menu_title == "Kelas":
                menu_kelas(menu_title, nama_file, kolom)
            else:
                main_menu_admin()
        elif pilihan == "6":
            # print("Terimakasih Telah Menggunakan Aplikasi ACADEMIX !")
            exit()
        else:
            input("Pilihan tidak valid. Klik \"ENTER\" untuk coba lagi.")
            menu_kelola_data(menu_title, nama_file, kolom)


# ------------------------------------------------ FUNGSI UNTUK MAIN MENU ADMIN ------------------------------------------------ 
def main_menu_admin():
    clear()
    file_dosen = "data_dosen.csv"
    file_mahasiswa = "data_mahasiswa.csv"
    file_matkul = "matkul.csv"
    file_kelas = "kelas.csv"
    file_krs = "krs_admin.csv"
    

    kolom_mahasiswa = ["Nama", "NIM", "Program Studi"]
    kolom_dosen = ["Nama", "NIDN", "Jabatan"]
    kolom_matkul = ["Kode Mata Kuliah", "Nama Mata Kuliah", "SKS", "Jam Perkuliahan"]
    kolom_kelas = ["Kode Kelas", "Nama Kelas", "Ruang Kelas"]
    kolom_krs = ["Kode Jadwal", "Hari", "Mata Kuliah", "SKS", "Jam", "Kelas"]

    while True:

        print(f'''
        {"="*60}
        |{"A C A D E M I X".center(58)}|
        |{"Sistem Informasi Akademik".center(58)}|
        {'='*60}  
        |{f"Dashboard Admin".center(58)}|
        |{"-"*58}|
        |{"[1]. Kelola Data Mahasiswa".ljust(58)}|
        |{"[2]. Kelola Data Dosen".ljust(58)}|
        |{"[3]. Kelola Data Mata Kuliah".ljust(58)}|
        |{"[4]. Kelola Data Kelas".ljust(58)}|
        |{"[5]. Kelola Data KRS".ljust(58)}|
        |{"[6]. Kelola Data Jadwal".ljust(58)}|
        |{"[7]. Logout".ljust(58)}|
        |{"[8]. Keluar".ljust(58)}|
        {'='*60}
        ''')


        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            menu_mahasiswa("Mahasiswa", file_mahasiswa, kolom_mahasiswa)
        elif pilihan == "2":
            menu_kelola_data("Dosen", file_dosen, kolom_dosen)
        elif pilihan == "3":
            menu_kelola_data("Mata Kuliah", file_matkul, kolom_matkul)
        elif pilihan == "4":
            menu_kelas("Kelas", file_kelas, kolom_kelas)
        elif pilihan == "5":
            pass
        elif pilihan == "6":
            pass
        elif pilihan == "7":
            start()
        elif pilihan == "8":
            print("Terima kasih telah menggunakan sistem!")
            exit()
        else:
            print("Pilihan tidak valid.")



# def main_menu_mahasiswa():
#     x = 'akun_mahasiswa.csv'
#     print("berhasil")
#     df = pd.read_csv(x)
#     user_data = df[df['Username'] == username]
#     print(user_data)


# ========= KELAS ==========

def menu_kelas(menu_title, nama_file, kolom):
    clear()
    while True:

        print(f'''
        {"="*60}
        |{"A C A D E M I X".center(58)}|
        |{"Sistem Informasi Akademik".center(58)}|
        {'='*60}  
        |{f"Dashboard Kelas".center(58)}|
        |{"-"*58}|
        |{"[1]. Kelola Ruang Kelas".ljust(58)}|
        |{"[2]. Lihat Daftar Kelas".ljust(58)}|
        |{"[3]. Kembali".ljust(58)}|
        |{"[4]. Keluar".ljust(58)}|
        {'='*60}
        ''')

        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            menu_kelola_data(menu_title, nama_file, kolom)
        elif pilihan == "2":
            lihat_kelas(menu_title, nama_file, kolom)
        elif pilihan == "3":
            main_menu_admin()
        elif pilihan == "4":
            # print("Terimakasih Telah Menggunakan Aplikasi ACADEMIX !")
            exit()
        else:
            input("Pilihan tidak valid. Klik \"ENTER\" untuk coba lagi.")
            menu_kelola_data(menu_title, nama_file, kolom)

def lihat_kelas():
    pass


# ============== MAHASISWA ==============

def menu_mahasiswa(menu_title, nama_file, kolom):
    clear()
    while True:

        print(f'''
        {"="*60}
        |{"A C A D E M I X".center(58)}|
        |{"Sistem Informasi Akademik".center(58)}|
        {'='*60}  
        |{f"Dashboard Kelas".center(58)}|
        |{"-"*58}|
        |{"[1]. Kelola Data Mahasiswa".ljust(58)}|
        |{"[2]. Kelola Login Mahasiswa".ljust(58)}|
        |{"[3]. Kembali".ljust(58)}|
        |{"[4]. Keluar".ljust(58)}|
        {'='*60}
        ''')
        

        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            menu_kelola_data(menu_title, nama_file, kolom)
        elif pilihan == "2":
            login_user_mahasiswa()
        elif pilihan == "3":
            main_menu_admin()
        elif pilihan == "4":
            # print("Terimakasih Telah Menggunakan Aplikasi ACADEMIX !")
            exit()
        else:
            input("Pilihan tidak valid. Klik \"ENTER\" untuk coba lagi.")
            menu_kelola_data(menu_title, nama_file, kolom)



def tampilkan_akun():
    nama_file = 'akun_mahasiswa.csv'
    if os.path.exists(nama_file):
        df = pd.read_csv(nama_file)
        df.index += 1

        if df.empty:
            print(df)
            print("Tidak ada data untuk ditampilkan.")
        else:
            # Tampilkan data dalam format tabel
            print(tabulate(df, headers='keys', tablefmt='grid', colalign=["center"] * len(df.columns)))  # Panggil fungsi `data` untuk menampilkan tabel
    else:
        # Jika file tidak ditemukan, beri pesan
        print(f"File {nama_file} tidak ditemukan. Belum ada data.")
        input("\nKlik \"ENTER\" untuk kembali ke menu.")

def login_user_mahasiswa():
    clear()
    nama_file = 'akun_mahasiswa.csv'

    print("="*60)
    print("LOGIN MAHASISWA".center(60))
    print("="*60)
    
    # Cek apakah file CSV ada
    if not os.path.exists(nama_file):
        print(f"File {nama_file} tidak ditemukan.")
        return

    # Baca file CSV
    df = pd.read_csv(nama_file)
    print(df)
    print(f'''
    {"="*60}
    |{"A C A D E M I X".center(58)}|
    |{"Sistem Informasi Akademik".center(58)}|
    {'='*60}  
    |{f"Dashboard Kelas".center(58)}|
    |{"-"*58}|
    |{"[1]. Tampilkan Data".ljust(58)}|
    |{"[2]. Tambah Data".ljust(58)}|
    |{"[3]. Ubah Data".ljust(58)}|
    |{"[4]. Hapus Data".ljust(58)}|
    |{"[5]. Kembali".ljust(58)}|
    |{"[6]. Keluar".ljust(58)}|
    {'='*60}
    ''')


    pilihan = input("Masukkan pilihan: ").strip()

    if pilihan == "1":
        tampilkan_akun()
        input("\nKlik \"ENTER\" untuk kembali ke menu.")
        login_user_mahasiswa() # Navigasi kembali ke menu


    elif pilihan == "2":
        # Daftar Mahasiswa Baru (Create)
        username_new = input('Masukkan Username Baru: ').strip()
        password_new = input('Masukkan Password Baru: ').strip()
        # Pastikan username belum ada
        if username_new in df['Username'].values:
            print(f"Username '{username_new}' sudah terdaftar.")
        else:
            new_data = pd.DataFrame([[username_new, password_new]], columns=df.columns)
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(nama_file, index=False)
            print(f"Mahasiswa dengan Username '{username_new}' berhasil terdaftar.")

    elif pilihan == "3":
        tampilkan_akun()
        # Ubah Password (Update)
        username_target = int(input('Masukkan Username untuk mengubah password: '))
        if username_target not in df['Username'].values:
            print(f"Username '{username_target}' tidak ditemukan.")
        else:
            password_lama = input('Masukkan Password Lama: ').strip()
            user_data = df.loc[df['Username'] == username_target]
            if user_data.iloc[0]['Password'] != password_lama:
                print("Password lama tidak sesuai.")
            else:
                password_baru = input('Masukkan Password Baru: ').strip()
                df.loc[df['Username'] == username_target, 'Password'] = password_baru
                df.to_csv(nama_file, index=False)
                print(f"Password untuk username '{username_target}' berhasil diubah.")

    elif pilihan == "4":
        tampilkan_akun()
        # Hapus Akun (Delete)
        username_target = int(input('Masukkan Username untuk dihapus: '))
        if username_target not in df['Username'].values:
            print(f"Username '{username_target}' tidak ditemukan.")
        else:
            df = df[df['Username'] != username_target]  # Menghapus row berdasarkan username
            df.to_csv(nama_file, index=False)
            print(f"Mahasiswa dengan Username '{username_target}' berhasil dihapus.")

    elif pilihan == "5":
        return  # Kembali ke menu kelas

    elif pilihan == "6":
        exit()  # Keluar dari aplikasi

    else:
        input("Pilihan tidak valid. Tekan Enter untuk coba lagi.")











# ========= CRUD ==========
# FUNGSI MENAMPILKAN DATA


def tampilkan_data(menu_title,nama_file, kolom):
    clear()
    if os.path.exists(nama_file):
        df = pd.read_csv(nama_file)
        df.index += 1

        if df.empty:
            print("Tidak ada data untuk ditampilkan.")
        else:
            # Tampilkan data dalam format tabel
            print(tabulate(df, headers='keys', tablefmt='grid', colalign=["center"] * len(df.columns)))  # Panggil fungsi `data` untuk menampilkan tabel
            input("\nKlik \"ENTER\" untuk kembali ke menu.")
            menu_kelola_data(menu_title,nama_file,kolom) # Navigasi kembali ke menu
    else:
        # Jika file tidak ditemukan, beri pesan
        print(f"File {nama_file} tidak ditemukan. Belum ada data.")
        input("\nKlik \"ENTER\" untuk kembali ke menu.")
         


# FUNGSI MENAMBAH DATA
def tambah_data(menu_title, nama_file, kolom):
    clear()
    if os.path.exists(nama_file):
        df = pd.read_csv(nama_file)
    else:
        df = pd.DataFrame(columns=kolom)

    while True:
        print("=" * 60)
        print(f"MASUKKAN DATA {menu_title.upper()}".center(60))
        print("-" * 60)

        # Input data baru
        data_baru = {}
        for kol in kolom:
            data_baru[kol] = input(f"Masukkan {kol}: ").strip()

        # Tambahkan data baru ke DataFrame
        df = pd.concat([df, pd.DataFrame([data_baru])], ignore_index=True)
        df.to_csv(nama_file, index=False)

        print("-" * 60)
        print("Data berhasil ditambahkan.")
        print("-" * 60)

        # Validasi input pilihan
        while True:
            tambah_lagi = input("Apakah Anda ingin menambah data lagi? [y/n]: ").strip().lower()
            if tambah_lagi == 'y':
                break  # Kembali ke awal loop untuk menambah data
            elif tambah_lagi == 'n':
                input("Klik ENTER untuk kembali ke menu.")
                menu_kelola_data(menu_title, nama_file, kolom)
                return  # Keluar dari fungsi setelah kembali ke menu
            else:
                print("Masukkan karakter yang benar [y/n].")


    
    
# FUNGSI MENGUBAH DATA
def ubah_data(menu_title,nama_file , kolom):
    clear()
    if os.path.exists(nama_file):
        df = pd.read_csv(nama_file)
        df.index += 1

        if df.empty:
            print("Tidak ada data untuk ditampilkan.")
        else:
            # Tampilkan data dalam format tabel
            print(tabulate(df, headers='keys', tablefmt='grid', colalign=["center"] * len(df.columns)))
    df.index -= 1
    index = input("Masukkan nomor baris yang ingin diubah (tekan ENTER untuk kembali): ").strip() 
    if index == "":
        clear()
        return
    index = int(index) - 1
    if index < 0 or index >= len(df):
        input("Nomor baris tidak valid. Klik \"ENTER\" untuk memasukan nomor baris lagi")
        ubah_data(menu_title,nama_file , kolom)

    for kol in kolom:
        nilai_baru = input(f"Masukkan {kol} baru (kosongkan untuk tetap): ").strip()
        if nilai_baru:
            df.at[index, kol] = nilai_baru

    df.to_csv(nama_file, index=False)
    print("Data berhasil diubah.")
    input("Klik \"ENTER\" untuk selesai")
    menu_kelola_data(menu_title,nama_file,kolom)

    

# FUNGSI MENGHAPUS DATA
def hapus_data(menu_title, nama_file, kolom):
    clear()
   
    # Mengecek apakah file CSV ada
    if not os.path.exists(nama_file):
        print(f"File {nama_file} tidak ditemukan.")
        return

    # Membaca file CSV
    df = pd.read_csv(nama_file)

    # Mengecek apakah data kosong
    if df.empty:
        print("Tidak ada data untuk ditampilkan.")
        return

    # Menampilkan data dalam format tabel dengan indeks berbasis 1
    df.index += 1
    print(f"Menampilkan data {menu_title} :")
    print(tabulate(df, headers='keys', tablefmt='grid', colalign=['center'] * len(df.columns)))

    # Mengembalikan indeks ke mode berbasis 0 agar sesuai dengan logika pandas
    # df.index -= 1

    while True:
        df.index -= 1
        user_input = input("Masukkan nomor baris yang ingin dihapus (atau ketik 'keluar' untuk kembali): ").strip()

        # Cek jika user ingin keluar
        if user_input.lower() == "keluar":
            menu_kelola_data(menu_title, nama_file, kolom)
            break

        try:
            # Konversi input pengguna ke integer
            index = int(user_input) - 1  # Konversi dari indeks berbasis 1 ke 0
            if index < 0 or index >= len(df):
                print("Nomor baris tidak valid. Silakan coba lagi.")
            else:
                # Menghapus baris dan menyimpan perubahan
                df = df.drop(index).reset_index(drop=True)  # Reset indeks agar tetap urut
                df.to_csv(nama_file, index=False)
                print(f"Data pada baris {user_input} berhasil dihapus.")

                # Tampilkan data yang tersisa
                if df.empty:
                    input("Semua data telah dihapus. Klik \"ENTER\" untuk kembali.")
                    menu_kelola_data(menu_title, nama_file, kolom)
                else:
                    df.index+=1
                    clear()
                    print("Data yang tersisa:")
                    print(tabulate(df, headers='keys', tablefmt='grid', colalign=['center'] * len(df.columns)))

        except ValueError:
            print("Input tidak valid. Harap masukkan nomor baris yang benar atau ketik 'keluar'.")







def start():
    clear()
    print(f'''
    {"="*60}
    |{"A C A D E M I X".center(58)}|
    |{"Sistem Informasi Akademik".center(58)}|
    {'='*60}  
    |{"Dashboard Login".center(58)}|
    |{"-"*58}|
    |{"[1]. Login Admin".ljust(58)}|
    |{"[2]. Login User".ljust(58)}|
    {'='*60}
    ''')
    
    option = input("Masukkan Pilihan: ")
    if option == "1":
        page_admin()
    elif option == "2":
        page_user()
    else:
        input("Pilihan INVALID. Klik ENTER untuk memilih kembali!")
        start()
        
start()
