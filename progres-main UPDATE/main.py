import os
import pandas as pd
from tabulate import tabulate
import csv

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
        return
    elif pilihan == "2":
        ubah_password()
        return
    elif pilihan == "3":
        start()
        return
    else:
        input("Inputan tidak valid. Silakan klik \"ENTER\" untuk kembali")
        page_admin()
        return

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
        return
    if pilihan == '2':
        login_mahasiswa()
        return
    elif pilihan == '3':
        start()
        return
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

    df = pd.read_csv("data_admin.csv")
    # Mencari kecocokan username dan password
    data_login = df[(df['Username'] == username) & (df['Password'] == password)]

    if len(data_login) > 0:  # Jika data_login tidak kosong
        input("Login Berhasil. Klik \"ENTER\" Untuk Melanjutkan!")
        main_menu_admin()  # Panggil fungsi menu admin di sini
        return
    else:
        print("Username atau Password Salah. Silahkan Coba Lagi!")
        print("-" * 60)
        page_admin()
        return

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
                return
            else:
                print("Mohon menginputkan sesuai perintah (ketik 1 untuk mencoba lagi.\"ENTER\" untuk keluar).")
                return
    
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
            return
    kembali()

# LOGIN USER
# [1] LOGIN MAHASISWA
def login_mahasiswa():
    clear()
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
                clear()
                dashboard_mahasiswa()
                break 
            else:
                print('Username atau Password salah. Coba lagi.')
                input('Tekan ENTER untuk melanjutkan')
                clear()
                login_mahasiswa()
                return
        else:
            print('Username atau Password salah. Coba lagi.')
            input('Tekan ENTER untuk melanjutkan')
            clear()
            login_mahasiswa()
            return


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
                input('Tekan ENTER untuk melanjutkan')
                clear()
                dashboard_dosen()
                pass
                break 
            else:
                print('Password salah. Silakan coba lagi.')
                input('Tekan ENTER untuk melanjutkan')
                clear()
                login_dosen()
                return
        else:
            print('Username tidak ditemukan. Silakan coba lagi.')
            input('Tekan ENTER untuk melanjutkan')
            login_dosen()
            return

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

#============================= SISTEM KRS ====================================
mata_kuliah = {
    1: {"nama": "Matematika", "sks": 3, "Jam": "07.00-10.00", "Kelas": "A"},
    2: {"nama": "Algoritma", "sks": 3, "Jam": "09.00-11.00", "Kelas": "A"},
    3: {"nama": "Pengantar Rekayasa Perangkat Lunak", "sks": 3, "Jam": "12.00-14.00", "Kelas": "A"},
    4: {"nama": "Pendidikan Agama Islam", "sks": 2, "Jam": "07.00-09.00", "Kelas": "A"},
}
data = [{"kode": kode, "nama": mk["nama"], "sks": mk["sks"]} for kode, mk in mata_kuliah.items()]
df = pd.DataFrame(data)

df.to_csv("mata_kuliah.csv", index=False)
print("\nData telah disimpan ke mata_kuliah.csv")

def tampilkan_mata_kuliah():
    print("Tabel Mata Kuliah")
    print(df.to_string(index=False))

def pilih_mata_kuliah():
    krs = []
    total_sks = 0
    while True:
        tampilkan_mata_kuliah()
        try:
            kode = int(input("\nPilih mata kuliah berdasarkan kode (0 untuk selesai): "))
            if kode == 0:
                break
            elif kode in mata_kuliah:
                clear()
                mata_kuliah_terpilih = mata_kuliah[kode]
                if total_sks + mata_kuliah_terpilih['sks'] <= 24:
                    if mata_kuliah_terpilih not in krs:
                        krs.append(mata_kuliah_terpilih)
                        total_sks += mata_kuliah_terpilih['sks']
                        print(f"[{mata_kuliah_terpilih['nama']} TELAH DITAMBAHKAN KE KRS ANDA]")
                        clear()
                    else:
                        input('Mata Kuliah Sudah Dipilih, Mohon tekan ENTER untuk melanjutkan')
                else:
                    print("Jumlah SKS Anda melebihi batas maksimal (24 SKS).")
            else:
                print("Kode mata kuliah tidak valid.")
        except ValueError:
            print("Masukkan kode yang valid.")
    
    return krs, total_sks

def simpan_krs(krs, total_sks, nama_file = r'krs.csv'):
    with open(nama_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nama Mata Kuliah', 'SKS'])
        for mk in krs:
            writer.writerow([mk['nama'], mk['sks']])
        writer.writerow(['Total SKS', total_sks])
    print(f"KRS Anda telah disimpan!")

def tampilkan_krs(krs, total_sks):
    print("\nKartu Rencana Studi (KRS) Anda:")
    for mk in krs:
        print(f"- {mk['nama']} (SKS: {mk['sks']})")
    print(f"Total SKS yang diambil: {total_sks} SKS")

def main_krs():
    clear()
    print()
    print("Selamat datang di Program Kartu Rencana Studi (KRS)")
    krs, total_sks = pilih_mata_kuliah()
    tampilkan_krs(krs, total_sks)
    simpan_krs(krs, total_sks)
    n=input('Tekan ENTER untuk kembali')
    dashboard_mahasiswa()
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
            jadwal()
        elif pilihan == "7":
            start()
        elif pilihan == "8":
            print("Terima kasih telah menggunakan sistem!")
            exit()
        else:
            print("Pilihan tidak valid.")

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

def menu_mahasiswa():
    clear()
    kolom_akun = ["Username", "Password"]
    while True:

        print(f'''
        {"="*60}
        |{"A C A D E M I X".center(58)}|
        |{"Sistem Informasi Akademik".center(58)}|
        {'='*60}  
        |{f"Dashboard Mahasiswa".center(58)}|
        |{"-"*58}|
        |{"[1]. Kelola Data Mahasiswa".ljust(58)}|
        |{"[2]. Kelola Login Mahasiswa".ljust(58)}|
        |{"[3]. Kembali".ljust(58)}|
        |{"[4]. Keluar".ljust(58)}|
        {'='*60}
        ''')

        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            menu_kelola_data()
        elif pilihan == "2":
            menu_kelola_data('Akun Mahasiswa', 'akun_mahasiswa.csv', kolom_akun)
        elif pilihan == "3":
            main_menu_admin()
        elif pilihan == "4":
            print("Terimakasih Telah Menggunakan Aplikasi ACADEMIX !")
            exit()
        else:
            input("Pilihan tidak valid. Klik \"ENTER\" untuk coba lagi.")
            menu_kelola_data()



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
        if menu_title == 'Akun Mahasiswa':
            username_new = int(input(f"Masukan Username :"))
            password_new = input(f"Masukan Password :")

            data_baru['Username'] = username_new
            data_baru['Password'] = password_new

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
        
        else:
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
        lihat_jadwal_dosen()
        return
    elif pilih == "2":
        start()
        return
    elif pilih == "3":
        clear()
        exit()
    else : 
        print("Nomor yang Anda masukkan salah! Silakan coba lagi.")
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
        jadwal_mahasiswa()
    elif pilih == "2":
        main_krs()
        print('ok')
    elif pilih == "3":
        start()
    elif pilih == "4":
        clear()
        print('Terima Kasih telah menggunakan AcademiX!')
        exit()
    else : 
        print("Nomor yang Anda masukkan salah! Silakan coba lagi.")
        dashboard_mahasiswa()

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

def jadwal_mahasiswa():
    clear()
    df = pd.read_csv('krs_mahasiswa.csv')
    nama = str(input('Masukkan Nama: '))
    NIM = int(input('Masukkan NIM: '))
    clear()

    print(f'Nama: {nama}')
    print(f'NIM: {NIM}')
    print("="*50)
    print("JADWAL PERKULIAHAN".center(49))
    print("="*50)
    print(df)
    print("="*50)
    n=input('Tekan ENTER untuk kembali')
    clear()
    dashboard_mahasiswa()

def lihat_jadwal_dosen():
    clear()
    df = pd.read_csv("krs_admin.csv")

    print("Jadwal Perkuliahan".center(49))
    print("="*50)
    print(df)
    print("="*50)
    n=input('Tekan ENTER untuk kembali')
    clear()
    dashboard_dosen()

def ganti_jadwal():
    # Membaca data dari file CSV
    df = pd.read_csv("jadwal_dosen.csv")
    with open("jadwal_dosen.csv", mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Menampilkan data yang ada untuk referensi
    print("Data saat ini di jadwal.csv:")
    print("="*50)
    print(df)
    print("="*50)

    # Minta inputan Kode Jadwal yang ingin diganti
    kode_jadwal_ganti = input("\nMasukkan Kode Jadwal yang ingin diganti: ")

    # Cari dan ganti baris yang sesuai dengan Kode Jadwal yang diberikan
    found = False
    for i, row in enumerate(rows):
        if row[2] == kode_jadwal_ganti:
            print("="*50)
            print("\nKode Jadwal ditemukan! Masukkan data baru untuk mengganti data lama:")
            print("="*50)
            
            # Minta input data baru dari pengguna

            print("="*50)
            new_hari = input(f"Masukkan Hari baru (sekarang: {row[1]}): ")
            print("="*50)
            new_jam = input(f"Masukkan Jam baru (sekarang: {row[4]}): ")
            print("="*50)

            # Update data yang ada pada baris yang ditemukan
            rows[i] = [row[0], new_hari, row[2], row[3], new_jam, row[5]]
            found = True
            break

    if not found:
        print(f"Kode Jadwal {kode_jadwal_ganti} tidak ditemukan.")
        return

    # Menulis data yang telah diperbarui ke file CSV
    with open('jadwal_dosen.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("="*50)
    print(f"Kode Jadwal {kode_jadwal_ganti} berhasil diganti.")
    print("="*50)

    while True : 
        lagi = input('Apakah ingin mengganti mata kuliah lain? (y/n): ')

        if lagi == "y":
            ganti_jadwal()
        elif lagi == "n":
            clear()
            dfn = pd.read_csv("jadwal_dosen.csv")
            print("JADWAL BARU")
            print("="*50)
            print(dfn)
            print("="*50)
            n = input("Tekan ENTER untuk kembali ke menu jadwal dosen")
            jadwal_dosen()
        else : 
            print("Inputan Anda tidak valid!")
            n = input("Tekan ENTER untuk kembali")
            clear()

def jadwal_dosen():
    clear()
    print("="*50)
    print("JADWAL DOSEN".center(49))
    print("="*50)
    print("1. Lihat Jadwal")
    print("2. Ganti Jadwal")
    print("3. Kembali")
    print("4. Keluar")
    print("="*50)
    user_input = input("Masukkan nomor yang dipilih: ")

    if user_input == "1":
        lihat_jadwal_dosen()
    elif user_input == "2":
        ganti_jadwal()
    elif user_input == "3": 
        jadwal()
    elif user_input == "4":
        exit()
    else : 
        print("Nomor yang Anda masukkan salah! silakan ulangi kembali")
        clear()
        jadwal_dosen()

def lihat_jadwal_dosen():
    clear()
    df = pd.read_csv("jadwal_dosen.csv")
    print(df)

    n = input("Tekan ENTER untuk kembali ke menu dosen")
    clear()
    jadwal_dosen()

def tampilkan_jadwal():
    clear()
    df = pd.read_csv('krs_admin.csv')
    dfn = pd.read_csv('krs_admin.csv')
    
    print("="*50)
    print("TAMPILKAN JADWAL".center(49))
    print("="*50)
    print("1. Jadwal Admin")
    print("2. Jadwal Mahasiswa")
    print("3. Kembali")
    print("="*50)
    user_input = input("Masukkan nomor yang dipilih: ")
    clear()

    if user_input == "1": 
        print("="*50)
        print("JADWAL ADMIN".center(49))
        print("="*50)
        print(dfn)
        n=input("Tekan ENTER untuk kembali")
        tampilkan_jadwal()
    elif user_input == "2": 
        print("="*50)
        print("JADWAL MAHASISWA".center(49))
        print("="*50)
        print(df)
        n=input("Tekan ENTER untuk kembali")
        tampilkan_jadwal()
    elif user_input == "3":
        jadwal_admin()
    else : 
        print("Nomor yang anda masukkan tidak valid, silakan masukkan kembali")
        tampilkan_jadwal()
    

def hapus_jadwal(): 
    clear()
    df = pd.read_csv('krs_admin.csv')
    while True:
        # Minta input nomor baris untuk dihapus
        print("="*50)
        print("JADWAL").center(49)
        print("="*50)
        print(df)
        user_input = input("Masukkan nomor baris yang ingin dihapus (atau ketik 'keluar' untuk kembali): ").strip()

        if user_input.lower() == "keluar":
            jadwal_admin()  # Keluar dari loop hapus_data

        try:
            index = int(user_input)  # Mengonversi input ke integer
            if index < 0 or index >= len(df):
                print("Nomor baris tidak valid.")
                user_input = input("Masukkan nomor baris yang ingin dihapus (atau ketik 'keluar' untuk kembali): ").strip()
                if user_input.lower() == "keluar":
                    jadwal_admin()
                else:
                    hapus_jadwal()
            else:
                df = df.drop(index)  # Menghapus baris dengan index tertentu
                df.to_csv('krs_admin.csv', index=False)  # Menyimpan perubahan ke file CSV
                print("Data berhasil dihapus.")
                continue
                  # Setelah data dihapus, keluar dari loop
        except ValueError:
            # Jika input tidak bisa diubah menjadi integer, tampilkan error dan minta input lagi
            print("Input tidak valid. Harap masukkan nomor baris yang valid atau ketik 'keluar'.")

def jadwal_admin():
    clear()
    print("="*50)
    print("JADWAL".center(49))
    print("=" * 50)
    print("1. Tampilkan Jadwal")
    print("2. Hapus Jadwal")
    print("3. Kembali")
    print("="*50)
    user_input = input("Masukkan nomor pilihanmu: ")
    clear()

    if user_input == "1" : 
        tampilkan_jadwal()
    elif user_input == "2" :
        hapus_jadwal()
    elif user_input == "3" :
        jadwal()
    else : 
        print("Nomor yang anda masukkan tidak valid! silakan ulangi lagi")
        jadwal_admin()

def jadwal() : 
    clear()
    print("="*50)
    print("MENU JADWAL".center(50))
    print("=" * 50)
    print("1. Admin")
    print("2. Mahasiswa")
    print("3. Dosen")
    print("4. Keluar")
    print("=" * 50)
    user_input = str(input("Masukkan nomor yang ingin anda jalankan: "))
    clear()

    if user_input == "1" :
        jadwal_admin()
    elif user_input == "2" :
        jadwal_mahasiswa()
    elif user_input == "3":
        jadwal_dosen()
    elif user_input == "4" : 
        clear()
        exit()
    else : 
        print("Nomor yang Anda masukkan tidak valid! silakan ulangi lagi")
        clear()
        jadwal()
        
start()
