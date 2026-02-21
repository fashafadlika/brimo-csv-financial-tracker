import pandas as pd

#baca csv (masukan file csv)
data = pd.read_csv(" ")

#ambil kolom penting
data = data[
    [
        "TGL_TRAN",
        "DESK_TRAN",
        "MUTASI_DEBET",
        "MUTASI_KREDIT",
        "SALDO_AKHIR_MUTASI"
    ]
]

#konversi tipe data
data["MUTASI_DEBET"] = pd.to_numeric(data["MUTASI_DEBET"], errors="coerce")
data["MUTASI_KREDIT"] = pd.to_numeric(data["MUTASI_KREDIT"], errors="coerce")
data["TGL_TRAN"] = pd.to_datetime(data["TGL_TRAN"])

#cashflow per hari
cashflow_harian = data.groupby("TGL_TRAN")[["MUTASI_KREDIT", "MUTASI_DEBET"]].sum()
cashflow_harian["CASHFLOW"] = (
    cashflow_harian["MUTASI_KREDIT"] - cashflow_harian["MUTASI_DEBET"]
)

#pemasukan terbesar
hari_pemasukan_terbesar = cashflow_harian["MUTASI_KREDIT"].idxmax()
pemasukan_terbesar = cashflow_harian["MUTASI_KREDIT"].max()

#pengeluaran terbesar
hari_terboros = cashflow_harian["MUTASI_DEBET"].idxmax()
pengeluaran_terbesar = cashflow_harian["MUTASI_DEBET"].max()

#penjumlahan uang keluar dan masuk
total_masuk = int(data["MUTASI_KREDIT"].sum())
total_keluar = int(data["MUTASI_DEBET"].sum())
selisih_masuk_keluar = total_masuk - total_keluar

#tampilkan hasil akhir
print(cashflow_harian)
print(f"Total Pemasukan: Rp. {total_masuk:,}")
print(f"Total Pengeluaran: Rp. {total_keluar:,}")
print(f"Cashflow Bersih: Rp. {selisih_masuk_keluar:,}")
print(f"Hari Pemasukan Terbesar: {hari_pemasukan_terbesar} (Rp. {int(pemasukan_terbesar):,})")
print(f"Hari Pengeluaran Terbesar: {hari_terboros} (Rp. {int(pengeluaran_terbesar):,})")

#ambil 5 data pertama
#print(data.head())

#menampilkan nama kolom
#print(data.columns)