import tkinter as tk
from tkinter import messagebox

def submit_tamu():
    nama_tamu = entry_nama_tamu.get()
    keperluan = entry_keperluan.get()
    if nama_tamu and keperluan:
        text_output.insert(tk.END, f"[Tamu] Nama: {nama_tamu}, Keperluan: {keperluan}\n")
        entry_nama_tamu.delete(0, tk.END)
        entry_keperluan.delete(0, tk.END)
        messagebox.showinfo("Tersimpan", "Data tamu berhasil dicatat.")
    else:
        messagebox.showwarning("Peringatan", "Lengkapi data tamu.")

def submit_barang():
    deskripsi_barang = entry_barang.get()
    lokasi = entry_lokasi.get()
    if deskripsi_barang and lokasi:
        text_output.insert(tk.END, f"[Barang Tertinggal] Deskripsi: {deskripsi_barang}, Lokasi: {lokasi}\n")
        entry_barang.delete(0, tk.END)
        entry_lokasi.delete(0, tk.END)
        messagebox.showinfo("Tersimpan", "Informasi barang tertinggal berhasil dicatat.")
    else:
        messagebox.showwarning("Peringatan", "Lengkapi data barang.")

def submit_laporan():
    laporan = entry_laporan.get()
    if laporan:
        text_output.insert(tk.END, f"[Laporan Keamanan] {laporan}\n")
        entry_laporan.delete(0, tk.END)
        messagebox.showinfo("Tersimpan", "Laporan keamanan berhasil dicatat.")
    else:
        messagebox.showwarning("Peringatan", "Laporan tidak boleh kosong.")

# Membuat window utama
root = tk.Tk()
root.title("Aplikasi Keamanan Sekolah")
root.geometry("500x600")

# Frame untuk Data Tamu
frame_tamu = tk.LabelFrame(root, text="Pendataan Tamu", padx=10, pady=10)
frame_tamu.pack(padx=10, pady=10, fill="both")

tk.Label(frame_tamu, text="Nama Tamu:").pack()
entry_nama_tamu = tk.Entry(frame_tamu, width=50)
entry_nama_tamu.pack()

tk.Label(frame_tamu, text="Keperluan:").pack()
entry_keperluan = tk.Entry(frame_tamu, width=50)
entry_keperluan.pack()

tk.Button(frame_tamu, text="Catat Tamu", command=submit_tamu).pack(pady=5)

# Frame untuk Barang Tertinggal
frame_barang = tk.LabelFrame(root, text="Informasi Barang Tertinggal", padx=10, pady=10)
frame_barang.pack(padx=10, pady=10, fill="both")

tk.Label(frame_barang, text="Deskripsi Barang:").pack()
entry_barang = tk.Entry(frame_barang, width=50)
entry_barang.pack()

tk.Label(frame_barang, text="Lokasi Ditemukan:").pack()
entry_lokasi = tk.Entry(frame_barang, width=50)
entry_lokasi.pack()

tk.Button(frame_barang, text="Catat Barang", command=submit_barang).pack(pady=5)

# Frame untuk Laporan Keamanan
frame_laporan = tk.LabelFrame(root, text="Laporan Keamanan", padx=10, pady=10)
frame_laporan.pack(padx=10, pady=10, fill="both")

tk.Label(frame_laporan, text="Laporan:").pack()
entry_laporan = tk.Entry(frame_laporan, width=50)
entry_laporan.pack()

tk.Button(frame_laporan, text="Catat Laporan", command=submit_laporan).pack(pady=5)

# Text Output
tk.Label(root, text="Log Aktivitas:").pack()
text_output = tk.Text(root, height=10, width=60)
text_output.pack(padx=10, pady=10)

root.mainloop()