import streamlit as st
import main as bri

#Page Config
st.set_page_config(
    page_title= "Financial Tracker",
    page_icon="💰",
    layout="wide"
)

#Background
st.markdown("""
    <style>
    .stApp {
        background-color: #0d0d0f;
    }
    </style>
""", unsafe_allow_html=True)

col_title, col_upload = st.columns(2)

with col_title:
    st.markdown("<p class='section-label'>Personal Finance</p>", unsafe_allow_html=True)
    st.title("Financial Tracker")
with col_upload:
    file = st.file_uploader("Upload file CSV mutasi bank", type=["csv"])

st.divider()

if file is not None:
    data = bri.load_data(file)
    data_perhari = bri.hitung_cashflow_perhari(data)
    pemasukan, pengeluaran = bri.pengeluaran_pemasukan(data_perhari)
    total_masuk, total_keluar, selisih = bri.hitung_ringkasan(data)
    savings_rate = bri.hitung_savings_rate(total_masuk, total_keluar)

    col_pemasukan, col_pengeluaran, col_selisih, col_savings_rate = st.columns(4)

    with col_pemasukan:
        st.metric(f"Total pemasukan bulan ini: ", f"Rp {total_masuk:,}".replace(",", "."))
    with col_pengeluaran:
        st.metric(f"Total pengeluaran bulan ini: ", f"Rp {total_keluar:,}".replace(",", "."))
    with col_selisih:
        st.metric("Selisih pemasukan dan pengeluaran: ", f"Rp {selisih:,}".replace(",", "."))
    with col_savings_rate:
        st.metric("Savings rate bulan ini: ", f"{savings_rate * 100:.2f}%")

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Chart Pemasukan bulan ini")
        st.bar_chart(data_perhari, 
                     x="TGL_TRAN", 
                     y="MUTASI_KREDIT",
                     color="#c8f55a",
                     use_container_width=True
                     )

    with col2:
        st.subheader("Chart Pengeluaran bulan ini")
        st.bar_chart(data_perhari, 
                     x="TGL_TRAN", 
                     y="MUTASI_DEBET",
                     color="#ff6b6b"
                     )

    st.divider()

    st.subheader("Cashflow bulan ini")
    st.bar_chart(data_perhari, x="TGL_TRAN", y="CASHFLOW")

    
else:
    st.markdown("""
    <div style="text-align:center; padding: 80px 0;">
        <div style="font-size: 3.5rem; margin-bottom: 16px;">💳</div>
        <p style="font-family:'Syne',sans-serif; font-size:1.4rem; font-weight:700; color:#f0ebe0;">
            Upload file CSV mutasi bank Anda
        </p>
        <p style="font-family:'DM Mono',monospace; font-size:0.8rem; color:#6b6b72; letter-spacing:1px;">
            Format yang didukung: CSV ekspor dari aplikasi bank BRI
        </p>
    </div>
    """, unsafe_allow_html=True)
