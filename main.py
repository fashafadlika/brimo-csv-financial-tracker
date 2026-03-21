import pandas as pd
import json
from decimal import Decimal

#baca csv (masukan file csv)
def load_data(file_path):
    data = pd.read_csv(file_path)

    #konversi tipe data
    data["MUTASI_DEBET"] = pd.to_numeric(data["MUTASI_DEBET"], errors="coerce")
    data["MUTASI_KREDIT"] = pd.to_numeric(data["MUTASI_KREDIT"], errors="coerce")
    data["TGL_TRAN"] = pd.to_datetime(data["TGL_TRAN"])

    return data

def load_rules(file_path):
    with open(file_path, "r") as file:
        rules = json.load(file)
    return rules

def kategori_pengeluaran(deskripsi, rules):
    deskripsi = str(deskripsi).upper()

    for kategori, keywords in rules.items():
        for keyword in keywords:
            if keyword in deskripsi:
                return kategori
            
    return "Lainnya"

def proses_data(data, rules):
    data["KATEGORI"] = data["REMARK_CUSTOM"].apply(
        lambda x: kategori_pengeluaran(x, rules)
    )
    return data

def hitung_cashflow_perhari(data):
    #grouping tanggal, kredit, debet
    data_perhari = data.groupby("TGL_TRAN")[["MUTASI_KREDIT", "MUTASI_DEBET"]].sum()
    data_perhari["CASHFLOW"] = (data_perhari["MUTASI_KREDIT"] - data_perhari["MUTASI_DEBET"])

    return data_perhari

def hitung_ringkasan(data):
    total_masuk = int(data["MUTASI_KREDIT"].sum())
    total_keluar = int(data["MUTASI_DEBET"].sum())
    selisih = total_masuk - total_keluar

    return total_masuk, total_keluar, selisih

def hitung_savings_rate(total_masuk, total_keluar):

    if total_masuk <= 0:
        raise ValueError("Total pemasukan harus lebih dari 0")
    elif total_keluar < 0:
        raise ValueError("Total pengeluaran negatif")
    elif total_keluar > total_masuk:
        raise ValueError("Total pengeluaran lebih besar dari total pemasukan")
    
    pemasukan = Decimal(str(total_masuk))
    pengeluaran = Decimal(str(total_keluar))

    savings_rate = (pemasukan - pengeluaran) / pemasukan

    return savings_rate

def main():

# Main Program
    if __name__ == "__main__":
        main()


