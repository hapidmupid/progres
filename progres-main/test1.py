# import os
# import pandas as pd



# def clear():
#     os.system('cls')
    
# # Fungsi menampilkan data

# def tampilkan_data(nama_file, kolom):
#     clear()
#     if os.path.exists(nama_file):
#         df = pd.read_csv(nama_file)
#         print(df)
#     else:
#         print(f"File {nama_file} tidak ditemukan. Belum ada data.")

# # Fungsi menambah data

# def tambah_data(nama_file, kolom):
#     if os.path.exists(nama_file):
#         df = pd.read_csv(nama_file)
#     else:
#         df = pd.DataFrame(columns=kolom)

#     data_baru = {kol: input(f"Masukkan {kol}: ").strip() for kol in kolom}
#     df = pd.concat([df, pd.DataFrame([data_baru])], ignore_index=True)
#     df.to_csv(nama_file, index=False)
#     print("Data berhasil ditambahkan.")

# # Fungsi mengedit data

# def ubah_data(nama_file, kolom):
#     clear()
#     if not os.path.exists(nama_file):
#         print(f"File {nama_file} tidak ditemukan.")
#         return

#     df = pd.read_csv(nama_file)
#     print(df)
#     index = int(input("Masukkan nomor baris yang ingin diubah: "))
#     if index < 0 or index >= len(df):
#         print("Nomor baris tidak valid.")
#         return

#     for kol in kolom:
#         nilai_baru = input(f"Masukkan {kol} baru (kosongkan untuk tetap): ").strip()
#         if nilai_baru:
#             df.at[index, kol] = nilai_baru

#     df.to_csv(nama_file, index=False)
#     print("Data berhasil diubah.")

# # Fungsi menghapus data

# def hapus_data(nama_file):
#     clear()
#     if not os.path.exists(nama_file):
#         print(f"File {nama_file} tidak ditemukan.")
#         return

#     df = pd.read_csv(nama_file)
#     print(df)
#     index = int(input("Masukkan nomor baris yang ingin dihapus: "))
#     if index < 0 or index >= len(df):
#         print("Nomor baris tidak valid.")
#         return

#     df = df.drop(index)
#     df.to_csv(nama_file, index=False)
#     print("Data berhasil dihapus.")

# # Fungsi kelola data (umum)
# def menu_kelola_data(menu_title, nama_file, kolom):
#     clear()
#     while True:
#         print(f"\n--- {menu_title} ---")
#         print("1. Tampilkan Data")
#         print("2. Tambah Data")
#         print("3. Ubah Data")
#         print("4. Hapus Data")
#         print("5. Keluar")

#         pilihan = input("Masukkan pilihan: ").strip()

#         if pilihan == "1":
#             tampilkan_data(nama_file, kolom)
#         elif pilihan == "2":
#             tambah_data(nama_file, kolom)
#         elif pilihan == "3":
#             ubah_data(nama_file, kolom)
#         elif pilihan == "4":
#             hapus_data(nama_file)
#         elif pilihan == "5":
#             clear()
#             print(f"Keluar dari menu {menu_title}.")
#             break
#         else:
#             print("Pilihan tidak valid. Silakan coba lagi.")

# # Fungsi susun KRS

# def susun_krs(file_krs):
#     clear()
#     file_matkul = "matkul.csv"
#     file_kelas = "kelas.csv"

#     if not os.path.exists(file_matkul) or not os.path.exists(file_kelas):
#         print("File mata kuliah atau kelas tidak ditemukan.")
#         return

#     df_matkul = pd.read_csv(file_matkul)
#     df_kelas = pd.read_csv(file_kelas)

#     # Konversi kolom ke string
#     df_matkul["Kode Mata Kuliah"] = df_matkul["Kode Mata Kuliah"].astype(str).str.strip()
#     df_kelas["Kode Kelas"] = df_kelas["Kode Kelas"].astype(str).str.strip()

#     print("\nDaftar Mata Kuliah:")
#     print(df_matkul)
#     print("\nDaftar Kelas:")
#     print(df_kelas)

#     kode_matkul = input("Masukkan kode mata kuliah: ").strip()
#     kode_kelas = input("Masukkan kode kelas: ").strip()

#     matkul = df_matkul[df_matkul["Kode Mata Kuliah"] == kode_matkul]
#     kelas = df_kelas[df_kelas["Kode Kelas"] == kode_kelas]

#     if matkul.empty or kelas.empty:
#         print("Kode mata kuliah atau kelas tidak valid.")
#         return

#     hari = input("Masukkan hari: ").strip()

#     data_krs = {
#         "Kode Jadwal": f"{kode_matkul}-{kode_kelas}",
#         "Hari": hari,
#         "Mata Kuliah": matkul.iloc[0]["Nama Mata Kuliah"],
#         "SKS": matkul.iloc[0]["SKS"],
#         "Jam": matkul.iloc[0]["Jam Perkuliahan"],
#         "Kelas": kelas.iloc[0]["Nama Kelas"],
#     }

#     if os.path.exists(file_krs):
#         df_krs = pd.read_csv(file_krs)
#     else:
#         df_krs = pd.DataFrame(columns=data_krs.keys())

#     df_krs = pd.concat([df_krs, pd.DataFrame([data_krs])], ignore_index=True)
#     df_krs.to_csv(file_krs, index=False)
#     print("KRS berhasil disusun.")

# # Fungsi pilih KRS mahasiswa

# def pilih_krs(file_admin_krs, file_mahasiswa_krs):
#     clear()
#     if not os.path.exists(file_admin_krs):
#         print("Data KRS admin tidak ditemukan.")
#         return

#     df_admin_krs = pd.read_csv(file_admin_krs)
#     print("\nDaftar Jadwal KRS:")
#     print(df_admin_krs)

#     kode_jadwal = input("Masukkan kode jadwal yang ingin dipilih: ").strip()

#     jadwal = df_admin_krs[df_admin_krs["Kode Jadwal"].str.strip() == kode_jadwal]

#     if jadwal.empty:
#         print("Kode jadwal tidak valid.")
#         return

#     jadwal_data = jadwal.iloc[0]
#     data_pilihan = {
#         "Hari": jadwal_data["Hari"],
#         "Mata Kuliah": jadwal_data["Mata Kuliah"],
#         "SKS": jadwal_data["SKS"],
#         "Jam": jadwal_data["Jam"],
#         "Kelas": jadwal_data["Kelas"],
#         "Kode Jadwal": jadwal_data["Kode Jadwal"],
#     }

#     if os.path.exists(file_mahasiswa_krs):
#         df_mahasiswa_krs = pd.read_csv(file_mahasiswa_krs)
#     else:
#         df_mahasiswa_krs = pd.DataFrame(columns=data_pilihan.keys())

#     df_mahasiswa_krs = pd.concat([df_mahasiswa_krs, pd.DataFrame([data_pilihan])], ignore_index=True)
#     df_mahasiswa_krs.to_csv(file_mahasiswa_krs, index=False)
#     print("KRS berhasil dipilih.")


# def lihat_krs_mahasiswa(file_mahasiswa_krs):
#     clear()
#     # Periksa apakah file KRS mahasiswa sudah ada
#     if not os.path.exists(file_mahasiswa_krs):
#         print("Belum ada KRS yang dipilih.")
#         return

#     # Baca data KRS mahasiswa
#     df_mahasiswa_krs = pd.read_csv(file_mahasiswa_krs)
#     if df_mahasiswa_krs.empty:
#         print("Belum ada KRS yang dipilih.")
#     else:
#         print("\nKRS yang telah dipilih:")
#         print(df_mahasiswa_krs)


# # Fungsi kelola KRS

# def kelola_krs(menu_title, file_admin_krs, kolom_admin_krs):
#     clear()
#     file_mahasiswa_krs = "krs_mahasiswa.csv"
#     while True:
#         print(f"\n--- {menu_title} ---")
#         print("1. Susun KRS")
#         print("2. Tampilkan KRS Admin")
#         print("3. Pilih KRS (Mahasiswa)")
#         print("4. Keluar")
#         print("5. Tampilkan krs")

#         pilihan = input("Masukkan pilihan: ").strip()

#         if pilihan == "1":
#             susun_krs(file_admin_krs)
#         elif pilihan == "2":
#             tampilkan_data(file_admin_krs, kolom_admin_krs)
#         elif pilihan == "3":
#             pilih_krs(file_admin_krs, file_mahasiswa_krs)
#         elif pilihan == "5":
#             lihat_krs_mahasiswa(file_mahasiswa_krs)
#         elif pilihan == "4":
#             print("Keluar dari menu Kelola KRS.")
#             break
#         else:
#             print("Pilihan tidak valid.")

# # Fungsi utama
# def main():
#     clear()
#     file_matkul = "matkul.csv"
#     file_kelas = "kelas.csv"
#     file_krs = "krs_admin.csv"

#     kolom_matkul = ["Kode Mata Kuliah", "Nama Mata Kuliah", "SKS", "Jam Perkuliahan"]
#     kolom_kelas = ["Kode Kelas", "Nama Kelas", "Ruang Kelas"]
#     kolom_krs = ["Kode Jadwal", "Hari", "Mata Kuliah", "SKS", "Jam", "Kelas"]

#     while True:
#         print("\n--- Sistem Informasi Akademik ---")
#         print("1. Kelola Mata Kuliah")
#         print("2. Kelola Kelas")
#         print("3. Kelola KRS")
#         print("4. Keluar")

#         pilihan = input("Masukkan pilihan: ").strip()

#         if pilihan == "1":
#             menu_kelola_data("Kelola Mata Kuliah", file_matkul, kolom_matkul)
#         elif pilihan == "2":
#             menu_kelola_data("Kelola Kelas", file_kelas, kolom_kelas)
#         elif pilihan == "3":
#             kelola_krs("Kelola KRS", file_krs, kolom_krs)
#         elif pilihan == "4":
#             print("Terima kasih telah menggunakan sistem!")
#             break
#         else:
#             print("Pilihan tidak valid.")

# # Jal
# if __name__ == "__main__":
#     main()

# import pandas as pd

# # ======== Bagian 1: Inisialisasi Data ========
# # Membuat data awal dan menyimpannya ke dalam file CSV
# mahasiswa_data = [
#     {"Nama": "Mufid", "NIM": "12", "Program Studi": "Teknik Informatika"},
#     {"Nama": "Safal", "NIM": "13", "Program Studi": "Teknik Informatika"},
#     {"Nama": "Danang", "NIM": "14", "Program Studi": "Teknik Informatika"},
#     {"Nama": "Dika", "NIM": "15", "Program Studi": "Teknik Informatika"},
#     {"Nama": "Raden", "NIM": "16", "Program Studi": "Teknik Informatika"},
#     {"Nama": "Ayek", "NIM": "17", "Program Studi": "Teknik Informatika"},
#     {"Nama": "Wulan", "NIM": "18", "Program Studi": "Teknik Informatika"},
#     {"Nama": "Wilma", "NIM": "19", "Program Studi": "Teknik Informatika"},
#     {"Nama": "Ryan", "NIM": "20", "Program Studi": "Teknik Informatika"},
# ]
# matkul_data = [
#     {"Kode Mata Kuliah": "IF101", "Nama Mata Kuliah": "Algoritma", "SKS": 3, "Jam Perkuliahan": "08:00-10:00"},
# ]
# kelas_data = [
#     {"Kode Kelas": "A", "Nama Kelas": "Kelas A", "Ruang Kelas": "R101"},
#     {"Kode Kelas": "B", "Nama Kelas": "Kelas B", "Ruang Kelas": "R102"},
#     {"Kode Kelas": "C", "Nama Kelas": "Kelas C", "Ruang Kelas": "R103"},
# ]
# krs_data = [
#     {"Kode Jadwal": "001", "Hari": "Senin", "Mata Kuliah": "Algoritma", "SKS": 3, "Jam": "08:00-10:00", "Kelas": "A", "NIM": "12"},
#     {"Kode Jadwal": "001", "Hari": "Senin", "Mata Kuliah": "Algoritma", "SKS": 3, "Jam": "08:00-10:00", "Kelas": "A", "NIM": "13"},
#     {"Kode Jadwal": "001", "Hari": "Senin", "Mata Kuliah": "Algoritma", "SKS": 3, "Jam": "08:00-10:00", "Kelas": "A", "NIM": "14"},
#     {"Kode Jadwal": "001", "Hari": "Senin", "Mata Kuliah": "Algoritma", "SKS": 3, "Jam": "08:00-10:00", "Kelas": "B", "NIM": "15"},
#     {"Kode Jadwal": "001", "Hari": "Senin", "Mata Kuliah": "Algoritma", "SKS": 3, "Jam": "08:00-10:00", "Kelas": "B", "NIM": "16"},
#     {"Kode Jadwal": "001", "Hari": "Senin", "Mata Kuliah": "Algoritma", "SKS": 3, "Jam": "08:00-10:00", "Kelas": "B", "NIM": "17"},
#     {"Kode Jadwal": "001", "Hari": "Senin", "Mata Kuliah": "Algoritma", "SKS": 3, "Jam": "08:00-10:00", "Kelas": "C", "NIM": "18"},
#     {"Kode Jadwal": "001", "Hari": "Senin", "Mata Kuliah": "Algoritma", "SKS": 3, "Jam": "08:00-10:00", "Kelas": "C", "NIM": "19"},
#     {"Kode Jadwal": "001", "Hari": "Senin", "Mata Kuliah": "Algoritma", "SKS": 3, "Jam": "08:00-10:00", "Kelas": "C", "NIM": "20"},
# ]

# # Simpan data ke CSV
# pd.DataFrame(mahasiswa_data).to_csv("mahasiswa.csv", index=False)
# pd.DataFrame(matkul_data).to_csv("matkul.csv", index=False)
# pd.DataFrame(kelas_data).to_csv("kelas.csv", index=False)
# pd.DataFrame(krs_data).to_csv("krs.csv", index=False)


# # ======== Bagian 2: Fungsi CRUD Ruang Kelas ========
# def kelola_ruang_kelas():
#     kelas_df = pd.read_csv("kelas.csv")
#     print("Data Ruang Kelas:")
#     print(kelas_df)

#     while True:
#         print("\nKelola Ruang Kelas:")
#         print("1. Tambah Kelas")
#         print("2. Ubah Kelas")
#         print("3. Hapus Kelas")
#         print("4. Kembali ke Menu Utama")
#         pilihan = input("Masukkan pilihan: ")

#         if pilihan == "1":
#             kode = input("Masukkan Kode Kelas: ")
#             nama = input("Masukkan Nama Kelas: ")
#             ruang = input("Masukkan Ruang Kelas: ")
#             kelas_df = kelas_df.append({"Kode Kelas": kode, "Nama Kelas": nama, "Ruang Kelas": ruang}, ignore_index=True)
#         elif pilihan == "2":
#             kode = input("Masukkan Kode Kelas yang ingin diubah: ")
#             if kode in kelas_df["Kode Kelas"].values:
#                 nama = input("Masukkan Nama Kelas baru: ")
#                 ruang = input("Masukkan Ruang Kelas baru: ")
#                 kelas_df.loc[kelas_df["Kode Kelas"] == kode, ["Nama Kelas", "Ruang Kelas"]] = [nama, ruang]
#             else:
#                 print("Kelas tidak ditemukan!")
#         elif pilihan == "3":
#             kode = input("Masukkan Kode Kelas yang ingin dihapus: ")
#             kelas_df = kelas_df[kelas_df["Kode Kelas"] != kode]
#         elif pilihan == "4":
#             break
#         else:
#             print("Pilihan tidak valid!")

#         # Simpan perubahan
#         kelas_df.to_csv("kelas.csv", index=False)
#         print("Perubahan berhasil disimpan.")


# # ======== Bagian 3: Lihat Daftar Kelas ========
# def lihat_daftar_kelas():
#     kelas_df = pd.read_csv("kelas.csv")
#     krs_df = pd.read_csv("krs.csv")
#     mahasiswa_df = pd.read_csv("mahasiswa.csv")

#     print("\nDaftar Mata Kuliah:")
#     mata_kuliah = krs_df["Mata Kuliah"].unique()
#     for i, mk in enumerate(mata_kuliah, 1):
#         print(f"{i}. {mk}")
#     pilihan = int(input("Pilih Mata Kuliah: ")) - 1

#     if pilihan < 0 or pilihan >= len(mata_kuliah):
#         print("Pilihan tidak valid!")
#         return

#     mk_terpilih = mata_kuliah[pilihan]
#     krs_terpilih = krs_df[krs_df["Mata Kuliah"] == mk_terpilih]

#     print(f"\nKelas untuk Mata Kuliah {mk_terpilih}:")
#     for kelas in krs_terpilih["Kelas"].unique():
#         print(f"\nKelas {kelas}:")
#         mahasiswa_kelas = krs_terpilih[krs_terpilih["Kelas"] == kelas]
#         for _, row in mahasiswa_kelas.iterrows():
#             nim = row["NIM"]
#             nama = mahasiswa_df[mahasiswa_df["NIM"] == nim]["Nama"].values[0]
#             print(f"{nim} - {nama}")


# # ======== Bagian 4: Menu Utama ========
# def main():
#     while True:
#         print("\nDashboard Kelas:")
#         print("1. Kelola Ruang Kelas")
#         print("2. Lihat Daftar Kelas")
#         print("3. Keluar")
#         pilihan = input("Masukkan pilihan: ")

#         if pilihan == "1":
#             kelola_ruang_kelas()
#         elif pilihan == "2":
#             lihat_daftar_kelas()
#         elif pilihan == "3":
#             print("Keluar dari program.")
#             break
#         else:
#             print("Pilihan tidak valid!")




# if __name__ == "__main__":
#     main()





# import os
# import pandas as pd

# def clear():
#     os.system('cls')

# # Fungsi menampilkan data
# def tampilkan_data(nama_file, kolom):
#     clear()
#     if os.path.exists(nama_file):
#         df = pd.read_csv(nama_file)
#         print(df)
#     else:
#         print(f"File {nama_file} tidak ditemukan. Belum ada data.")

# # Fungsi menambah data
# def tambah_data(nama_file, kolom):
#     if os.path.exists(nama_file):
#         df = pd.read_csv(nama_file)
#     else:
#         df = pd.DataFrame(columns=kolom)

#     data_baru = {kol: input(f"Masukkan {kol}: ").strip() for kol in kolom}
#     df = pd.concat([df, pd.DataFrame([data_baru])], ignore_index=True)
#     df.to_csv(nama_file, index=False)
#     print("Data berhasil ditambahkan.")

# # Fungsi mengedit data
# def ubah_data(nama_file, kolom):
#     clear()
#     if not os.path.exists(nama_file):
#         print(f"File {nama_file} tidak ditemukan.")
#         return

#     df = pd.read_csv(nama_file)
#     print(df)
#     index = int(input("Masukkan nomor baris yang ingin diubah: "))
#     if index < 0 or index >= len(df):
#         print("Nomor baris tidak valid.")
#         return

#     for kol in kolom:
#         nilai_baru = input(f"Masukkan {kol} baru (kosongkan untuk tetap): ").strip()
#         if nilai_baru:
#             df.at[index, kol] = nilai_baru

#     df.to_csv(nama_file, index=False)
#     print("Data berhasil diubah.")

# # Fungsi menghapus data
# def hapus_data(nama_file):
#     clear()
#     if not os.path.exists(nama_file):
#         print(f"File {nama_file} tidak ditemukan.")
#         return

#     df = pd.read_csv(nama_file)
#     print(df)
#     index = int(input("Masukkan nomor baris yang ingin dihapus: "))
#     if index < 0 or index >= len(df):
#         print("Nomor baris tidak valid.")
#         return

#     df = df.drop(index)
#     df.to_csv(nama_file, index=False)
#     print("Data berhasil dihapus.")

# # Fungsi susun KRS
# def susun_krs(file_krs):
#     clear()
#     file_matkul = "matkul.csv"
#     file_kelas = "kelas.csv"

#     if not os.path.exists(file_matkul) or not os.path.exists(file_kelas):
#         print("File mata kuliah atau kelas tidak ditemukan.")
#         return

#     df_matkul = pd.read_csv(file_matkul)
#     df_kelas = pd.read_csv(file_kelas)

#     print("\nDaftar Mata Kuliah:")
#     print(df_matkul)
#     print("\nDaftar Kelas:")
#     print(df_kelas)

#     kode_matkul = input("Masukkan kode mata kuliah: ").strip()
#     kode_kelas = input("Masukkan kode kelas: ").strip()

#     matkul = df_matkul[df_matkul["Kode Mata Kuliah"] == kode_matkul]
#     kelas = df_kelas[df_kelas["Kode Kelas"] == kode_kelas]

#     if matkul.empty or kelas.empty:
#         print("Kode mata kuliah atau kelas tidak valid.")
#         return

#     hari = input("Masukkan hari: ").strip()

#     data_krs = {
#         "Kode Jadwal": f"{kode_matkul}-{kode_kelas}",
#         "Hari": hari,
#         "Mata Kuliah": matkul.iloc[0]["Nama Mata Kuliah"],
#         "SKS": matkul.iloc[0]["SKS"],
#         "Jam": matkul.iloc[0]["Jam Perkuliahan"],
#         "Kelas": kelas.iloc[0]["Nama Kelas"],
#     }

#     if os.path.exists(file_krs):
#         df_krs = pd.read_csv(file_krs)
#     else:
#         df_krs = pd.DataFrame(columns=data_krs.keys())

#     df_krs = pd.concat([df_krs, pd.DataFrame([data_krs])], ignore_index=True)
#     df_krs.to_csv(file_krs, index=False)
#     print("KRS berhasil disusun.")

# # Fungsi kelola KRS
# def kelola_krs(menu_title, file_admin_krs, kolom_admin_krs):
#     clear()
#     while True:
#         print(f"\n--- {menu_title} ---")
#         print("1. Susun KRS")
#         print("2. Tampilkan KRS Admin")
#         print("3. Keluar")

#         pilihan = input("Masukkan pilihan: ").strip()

#         if pilihan == "1":
#             susun_krs(file_admin_krs)
#         elif pilihan == "2":
#             tampilkan_data(file_admin_krs, kolom_admin_krs)
#         elif pilihan == "3":
#             print("Keluar dari menu Kelola KRS.")
#             break
#         else:
#             print("Pilihan tidak valid.")

# # Fungsi utama
# def main():
#     clear()
#     file_matkul = "matkul.csv"
#     file_kelas = "kelas.csv"
#     file_krs = "krs_admin.csv"

#     kolom_matkul = ["Kode Mata Kuliah", "Nama Mata Kuliah", "SKS", "Jam Perkuliahan"]
#     kolom_kelas = ["Kode Kelas", "Nama Kelas", "Ruang Kelas"]
#     kolom_krs = ["Kode Jadwal", "Hari", "Mata Kuliah", "SKS", "Jam", "Kelas"]

#     while True:
#         print("\n--- Sistem Informasi Akademik ---")
#         print("1. Kelola Mata Kuliah")
#         print("2. Kelola Kelas")
#         print("3. Kelola KRS")
#         print("4. Keluar")

#         pilihan = input("Masukkan pilihan: ").strip()

#         if pilihan == "1":
#             pass
#         elif pilihan == "2":
#             pass
#         elif pilihan == "3":
#             kelola_krs("Kelola KRS", file_krs, kolom_krs)
#         elif pilihan == "4":
#             print("Terima kasih telah menggunakan sistem!")
#             break
#         else:
#             print("Pilihan tidak valid.")

# # Jalankan program
# if __name__ == "__main__":
#     main()

        # if menu_title == "Mahasiswa": #1
        #     print("=" * 69)
        #     print(f"MENAMPILKAN DATA {menu_title.upper()}".center(69))
        #     print("-" * 60)
        # elif menu_title == "Dosen": #2
        #     print("=" * 76)
        #     print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
        #     print("-" * 76)
        # elif menu_title == "Mata Kuliah": #3
        #     print("=" * 76)
        #     print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
        #     print("-" * 76)
        # elif menu_title == "Kelas": #4
        #     print("=" * 76)
        #     print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
        #     print("-" * 76)
        # elif menu_title == "KRS": #5
        #     print("=" * 76)
        #     print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
        #     print("-" * 76)
        # elif menu_title == "Jadwal": #6
        #     print("=" * 76)
        #     print(f"MENAMPILKAN DATA {menu_title.upper()}".center(76))
        #     print("-" * 76)
import os
import pandas as pd
from tabulate import tabulate

def clear():
    os.system('cls')
def hapus_data():
    import os
    import pandas as pd
    from tabulate import tabulate
    nama_file = 'mahasiswa.csv'
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
    print(f"Menampilkan data :")
    print(tabulate(df, headers='keys', tablefmt='grid', colalign=['center'] * len(df.columns)))

    # Mengembalikan indeks ke mode berbasis 0 agar sesuai dengan logika pandas
    # df.index -= 1

    while True:
        df.index -= 1
        user_input = input("Masukkan nomor baris yang ingin dihapus (atau ketik 'keluar' untuk kembali): ").strip()

        # Cek jika user ingin keluar
        if user_input.lower() == "keluar":
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
                    print("Semua data telah dihapus.")
                    break
                else:
                    df.index+=1
                    print("Data yang tersisa:")
                    print(tabulate(df, headers='keys', tablefmt='grid', colalign=['center'] * len(df.columns)))

        except ValueError:
            print("Input tidak valid. Harap masukkan nomor baris yang benar atau ketik 'keluar'.")


hapus_data()