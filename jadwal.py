import os 
import pandas as pd
import csv

def clear(): 
    os.system('cls')

def jadwal_mahasiswa():
    clear()
    df = pd.read_csv('krs.csv')
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
    jadwal()

def lihat_jadwal_dosen():
    clear()
    df = pd.read_csv("krs_admin.csv")

    print("Jadwal Perkuliahan".center(49))
    print("="*50)
    print(df)
    print("="*50)

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
    df = pd.read_csv('krs.csv')
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
    if os.path.exists('krs_admin.csv'):
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
jadwal()