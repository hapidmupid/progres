import os
import pandas as pd
from tabulate import tabulate




def clear():
    os.system('cls')


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
        # ubah password()
        pass
    elif pilihan == "3":
        start()
    else:
        input("Inputan tidak valid. Silakan klik \"ENTER\" untuk kembali")


def page_user():
    pass


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
            menu_kelola_data("Mahasiswa", file_mahasiswa, kolom_mahasiswa)
        elif pilihan == "2":
            menu_kelola_data("Dosen", file_dosen, kolom_dosen)
        elif pilihan == "3":
            menu_kelola_data("Mata Kuliah", file_matkul, kolom_matkul)
        elif pilihan == "4":
            menu_kelola_data("Kelas", file_kelas, kolom_kelas)
        elif pilihan == "5":
            menu_kelola_data("KRS", file_krs, kolom_krs)
        elif pilihan == "6":
            pass
        elif pilihan == "7":
            start()
        elif pilihan == "8":
            print("Terima kasih telah menggunakan sistem!")
            exit()
        else:
            print("Pilihan tidak valid.")










# ========= CRUD ==========
# FUNGSI MENAMPILKAN DATA


def tampilkan_data(menu_title,nama_file, kolom):
    clear()
    if os.path.exists(nama_file):
        df = pd.read_csv(nama_file)

        if menu_title == "Mahasiswa": #1
            print("=" * 69)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(69))
            print("-" * 60)
        elif menu_title == "Dosen": #2
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)
        elif menu_title == "Mata Kuliah": #3
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)
        elif menu_title == "Kelas": #4
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)
        elif menu_title == "KRS": #5
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)
        elif menu_title == "Jadwal": #6
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)


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

        if menu_title == "Mahasiswa": #1
            print("=" * 69)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(69))
            print("-" * 60)
        elif menu_title == "Dosen": #2
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)
        elif menu_title == "Mata Kuliah": #3
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)
        elif menu_title == "Kelas": #4
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)
        elif menu_title == "KRS": #5
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)
        elif menu_title == "Jadwal": #6
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)


        if df.empty:
            print("Tidak ada data untuk ditampilkan.")
        else:
            # Tampilkan data dalam format tabel
            print(tabulate(df, headers='keys', tablefmt='grid', colalign=["center"] * len(df.columns)))

    index = input("Masukkan nomor baris yang ingin diubah (tekan ENTER untuk kembali): ").strip() 
    if index == "":
        clear()
        return
    index = int(index)
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
def hapus_data(menu_title,nama_file,kolom):
    clear()
    if os.path.exists(nama_file):
        df = pd.read_csv(nama_file)

        if menu_title == "Mahasiswa": #1
            print("=" * 69)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(69))
            print("-" * 60)
        elif menu_title == "Dosen": #2
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)
        elif menu_title == "Mata Kuliah": #3
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)
        elif menu_title == "Kelas": #4
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)
        elif menu_title == "KRS": #5
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)
        elif menu_title == "Jadwal": #6
            print("=" * 76)
            print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
            print("-" * 76)


        if df.empty:
            print("Tidak ada data untuk ditampilkan.")
        else:
            # Tampilkan data dalam format tabel
            print(tabulate(df, headers='keys', tablefmt='grid', colalign=["center"] * len(df.columns)))


    while True:
        # Minta input nomor baris untuk dihapus
        user_input = input("Masukkan nomor baris yang ingin dihapus (atau ketik 'keluar' untuk kembali): ").strip()

        if user_input.lower() == "keluar":
            menu_kelola_data(menu_title, nama_file, kolom)
            break  # Keluar dari loop hapus_data

        try:
            index = int(user_input)  # Mengonversi input ke integer
            if index < 0 or index >= len(df):
                print("Nomor baris tidak valid.")
            else:
                df = df.drop(index)  # Menghapus baris dengan index tertentu
                df.to_csv(nama_file, index=False)  # Menyimpan perubahan ke file CSV
                print("Data berhasil dihapus.")
                continue
                  # Setelah data dihapus, keluar dari loop
        except ValueError:
            # Jika input tidak bisa diubah menjadi integer, tampilkan error dan minta input lagi
            print("Input tidak valid. Harap masukkan nomor baris yang valid atau ketik 'keluar'.")








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