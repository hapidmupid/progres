using Npgsql;
using System;
using System.Collections.Generic;
using System.Data;
using System.Windows.Forms;

namespace CRUD_PBO_1
{
    public partial class Dash_Data : Form
    {
        public Dash_Data()
        {
            InitializeComponent();
            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
            LoadData();
        }

        private void LoadData()
        {
            using (NpgsqlConnection conn = new NpgsqlConnection("Host=localhost;Username=postgres;Password=hafid123;Database=Perpustakaan_Biasa"))
            {
                conn.Open();
                string query = "SELECT id_buku, judul, penerbit, tahun_terbit, kategori FROM buku";
                using (NpgsqlCommand cmd = new NpgsqlCommand(query, conn))
                {
                    NpgsqlDataReader read = cmd.ExecuteReader();
                    DataTable data = new DataTable();
                    data.Load(read);
                    dataGridView1.DataSource = data;
                }
            }
        }

        private void btnhapus_Click(object sender, EventArgs e)
        {
            var caution = MessageBox.Show("Anda Yakin Ingin Menghapus Data?", "Warning", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
            if (caution == DialogResult.Yes)
            {
                if (dataGridView1.SelectedRows.Count == 0)
                {
                    MessageBox.Show("Pilih Baris Yang Ingin Dihapus.", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    return;
                }

                DataGridViewRow selectedRow = dataGridView1.SelectedRows[0];

                if (selectedRow.Cells["id_buku"].Value == null)
                {
                    MessageBox.Show("ID buku tidak ditemukan.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                int deleteId = Convert.ToInt32(selectedRow.Cells["id_buku"].Value);

                using (NpgsqlConnection conn = new NpgsqlConnection("Host=localhost;Username=postgres;Password=hafid123;Database=Perpustakaan_Biasa"))
                {
                    conn.Open();
                    string query = "DELETE FROM buku WHERE id_buku = @id";
                    using (var cmd = new NpgsqlCommand(query, conn))
                    {
                        cmd.Parameters.AddWithValue("id", deleteId);
                        int affectedRows = cmd.ExecuteNonQuery();

                        if (affectedRows > 0)
                        {
                            MessageBox.Show("Data berhasil dihapus.", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information);
                            LoadData();
                        }
                        else
                        {
                            MessageBox.Show("Data gagal dihapus dari database.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        }
                    }
                }
            }
        }

        private void btnedit_Click(object sender, EventArgs e)
        {
            if (dataGridView1.SelectedRows.Count == 0)
            {
                MessageBox.Show("Pilih Salah Satu Baris Untuk Mengubah Data.", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information);
                return;
            }

            var warn = MessageBox.Show("Yakin Ingin Merubah Data?", "Warning", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
            if (warn == DialogResult.Yes)
            {
                var row = dataGridView1.SelectedRows[0];

                if (row.Cells["id_buku"].Value == null)
                {
                    MessageBox.Show("ID buku tidak ditemukan.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                int id = Convert.ToInt32(row.Cells["id_buku"].Value);
                string judul = row.Cells["judul"].Value.ToString();
                string penerbit = row.Cells["penerbit"].Value.ToString();
                string tahun = row.Cells["tahun_terbit"].Value.ToString();
                string kategori = row.Cells["kategori"].Value.ToString();

                Form1 ubahForm = new Form1();
                ubahForm.Text = "Mode Edit";

                // Mengirim data via Tag
                ubahForm.Tag = new Dictionary<string, string>
                {
                    { "id_buku", id.ToString() },
                    { "judul", judul },
                    { "penerbit", penerbit },
                    { "tahun_terbit", tahun },
                    { "kategori", kategori }
                };

                ubahForm.Show();
                this.Hide();
            }
        }

        private void btnkembali_Click(object sender, EventArgs e)
        {
            Form1 formUtama = new Form1();
            formUtama.Show();
            this.Hide();
        }

        private void btnkeluar_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
