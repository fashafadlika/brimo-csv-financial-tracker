# Financial Tracker

Aplikasi dashboard sederhana untuk melacak arus kas keuangan pribadi berdasarkan mutasi rekening BRI. Dibangun menggunakan Python dan Streamlit.

---

## Fitur

- **Upload CSV** — import langsung file mutasi rekening dari BRI
- **Bar Chart Cashflow** — visualisasi arus kas harian (pemasukan vs pengeluaran)
- **Summary Metrics** — ringkasan total pemasukan, pengeluaran, dan selisih bulan ini
- **Savings Rate** — persentase tabungan dari total pemasukan

## Cara Menjalankan

### 1. Clone repository

```bash
git clone https://github.com/username/financial-tracker.git
cd financial-tracker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan aplikasi

```bash
streamlit run dashboard.py
```

Aplikasi akan terbuka otomatis di browser pada `http://localhost:8501`

---

## Format CSV

File CSV yang didukung adalah **ekspor mutasi rekening BRI** melalui BRImo atau Internet Banking BRI.

Pastikan file CSV memiliki kolom berikut:

| Kolom | Keterangan |
|---|---|
| `TGL_TRAN` | Tanggal transaksi |
| `REMARK_CUSTOM` | Keterangan / deskripsi transaksi |
| `MUTASI_KREDIT` | Nominal uang masuk |
| `MUTASI_DEBET` | Nominal uang keluar |

### Cara ekspor dari BRImo:
1. Buka aplikasi BRImo
2. Pilih **Rekening** → **Mutasi Rekening**
3. Tentukan rentang tanggal
4. Pilih **Unduh** → format **CSV**

---

## 🛠️ Tech Stack

- [Python 3.x](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — framework dashboard
- [Pandas](https://pandas.pydata.org/) — pengolahan data

---

## Requirements

```
streamlit
pandas
```

Install sekaligus:

```bash
pip install -r requirements.txt
```

---

## Roadmap

Kategorisasi pengeluaran otomatis (makan, transportasi, belanja, dll)
Pie chart pengeluaran per kategori
Filter berdasarkan rentang tanggal
Export laporan ke PDF
Deploy ke Streamlit Cloud

---

## Author

Dibuat oleh **[Fasha Fadlika]** — feel free to fork dan kembangkan sendiri.