import pandas as pd
import matplotlib.pyplot as plt

#baca csv (masukan file csv)
def load_data(file_path):
    data = pd.read_csv(file_path)

    #konversi tipe data
    data["MUTASI_DEBET"] = pd.to_numeric(data["MUTASI_DEBET"], errors="coerce")
    data["MUTASI_KREDIT"] = pd.to_numeric(data["MUTASI_KREDIT"], errors="coerce")
    data["TGL_TRAN"] = pd.to_datetime(data["TGL_TRAN"])

    return data

def hitung_cashflow_perhari(data):
    #grouping tanggal, kredit, debet
    perhari = data.groupby("TGL_TRAN")[["MUTASI_KREDIT", "MUTASI_DEBET"]].sum()
    perhari["CASHFLOW"] = (perhari["MUTASI_KREDIT"] - perhari["MUTASI_DEBET"])

    return perhari

def hitung_ringkasan(data):
    total_masuk = int(data["MUTASI_KREDIT"].sum())
    total_keluar = int(data["MUTASI_DEBET"].sum())
    selisih = total_masuk - total_keluar

    return total_masuk, total_keluar, selisih

def plot_pengeluaran_pemasukan(perhari, total_masuk, total_keluar, selisih):
    #Subplot 1: Pengeluaran
    plt.subplot(2, 1, 1)
    plt.plot(perhari.index, perhari["MUTASI_DEBET"])
    plt.title("Pengeluaran per Hari")
    plt.xticks(rotation = 45)

    #Subplot 2: Pemasukan
    plt.subplot(2, 1, 2)
    plt.plot(perhari.index, perhari["MUTASI_KREDIT"])
    plt.title("Pemasukan per Hari")
    plt.xticks(rotation = 45)

    total_masuk_keluar = (
        f"Total Masuk: Rp. {total_masuk:,}\n"
        f"Total Keluar: Rp. {total_keluar:,}\n"
        f"Selisih: Rp. {selisih}"
    )

    plt.text(
        0.02, 0.95,
        total_masuk_keluar,
        transform=plt.gca().transAxes,
        verticalalignment="top"
    )
    
    plt.tight_layout()
    plt.show()

# Main Program
data = load_data("desember2025.csv")
cashflow_perhari = hitung_cashflow_perhari(data)
total_masuk, total_keluar, selisih = hitung_ringkasan(data)
plot_pengeluaran_pemasukan(cashflow_perhari, total_masuk, total_keluar, selisih)

