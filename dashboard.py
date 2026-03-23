import streamlit as st
import main as bri

st.set_page_config(
    page_title= "Financial Tracker",
    page_icon="💰",
    layout="wide"
)

col_title, col_upload = st.columns(2)

with col_title:
    st.title("Financial Tracker")
with col_upload:
    file = st.file_uploader("Upload file CSV", type=["csv"])

if file is not None:
    data = bri.load_data(file)
    data_perhari = bri.hitung_cashflow_perhari(data)
    pemasukan, pengeluaran = bri.pengeluaran_pemasukan(data_perhari)
    total_masuk, total_keluar, selisih = bri.hitung_ringkasan(data)
    savings_rate = bri.hitung_savings_rate(total_masuk, total_keluar)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Chart Pemasukan bulan ini")
        st.bar_chart(data_perhari, x="TGL_TRAN", y="MUTASI_KREDIT")

    with col2:
        st.subheader("Chart Pengeluaran bulan ini")
        st.bar_chart(data_perhari, x="TGL_TRAN", y="MUTASI_DEBET")

    col_pemasukan, col_pengeluaran, col_selisih, col_savings_rate = st.columns(4)

    with col_pemasukan:
        st.metric(f"Total pemasukan bulan ini: ", f"Rp {total_masuk:,}".replace(",", "."))
    with col_pengeluaran:
        st.metric(f"Total pengeluaran bulan ini: ", f"Rp {total_keluar:,}".replace(",", "."))
    with col_selisih:
        st.metric("Selisih pemasukan dan pengeluaran: ", f"Rp {selisih:,}".replace(",", "."))
    with col_savings_rate:
        st.metric("Savings rate bulan ini: ", f"{savings_rate * 100:.2f}%")
else:
    st.write("Silahkan masukkan file CSV nya")
