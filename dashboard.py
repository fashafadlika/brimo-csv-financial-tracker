import streamlit as st
from main import hitung_ringkasan
from main import load_data
from main import hitung_cashflow_perhari
from main import hitung_savings_rate

st.title("Financial Tracker")

file = st.file_uploader("Upload file CSV", type=["csv"])

if file is not None:
    data = load_data(file)
    cashflow_perhari = hitung_cashflow_perhari(data)
    total_masuk, total_keluar, selisih = hitung_ringkasan(data)
    savings_rate = hitung_savings_rate(total_masuk, total_keluar)

    st.bar_chart(cashflow_perhari)
    st.metric(f"Total pemasukan bulan ini: ", f"Rp {total_masuk:,}".replace(",", "."))
    st.metric(f"Total pengeluaran bulan ini: ", f"Rp {total_keluar:,}".replace(",", "."))
    st.metric("Selisih pemasukan dan pengeluaran: ", f"Rp {selisih:,}".replace(",", "."))
    st.metric("Savings rate bulan ini: ", f"{savings_rate * 100:.2f}%")
else:
    st.write("Silahkan masukkan file CSV nya")
