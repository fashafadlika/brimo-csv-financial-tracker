import streamlit as st
import main as bri
from styles import load_css

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

#CSS
st.markdown(load_css(), unsafe_allow_html=True)

#Header
col_title, col_upload = st.columns([3, 2], vertical_alignment="center")

with col_title:
    st.markdown("<p class='section-label'>Personal Finance</p>", unsafe_allow_html=True)
    st.title("Financial Tracker")
with col_upload:
    file = st.file_uploader("Upload bank statement CSV file", type=["csv"])

st.divider()

#Main Program
if file is not None:
    data = bri.load_data(file)
    daily_data = bri.calculate_daily_cashflow(data)
    total_income, total_expenses, difference = bri.calculate_summary(data)

    try:
        savings_rate = bri.calculate_savings_rate(total_income, total_expenses)
        savings_pct = float(savings_rate) * 100
    except ValueError as e:
        savings_pct = None
        savings_error = str(e)

    #Metrics
    col_income, col_expenses, col_difference, col_savings_rate = st.columns(4)

    with col_income:
        st.metric(f"Total income this month: ", f"Rp {total_income:,}".replace(",", "."))
    with col_expenses:
        st.metric(f"Total expenses this month: ", f"Rp {total_expenses:,}".replace(",", "."))
    with col_difference:
        delta_color = "normal" if difference >= 0 else "inverse"
        st.metric("Difference: ", f"Rp {abs(difference):,}".replace(",", "."),
                  delta="surplus" if difference >= 0 else "deficit",
                  delta_color=delta_color)
    with col_savings_rate:
        if savings_pct is not None:
            st.metric("Savings Rate", f"{savings_pct:.1f}%")
        else:
            st.metric("Savings Rate", "N/A")

    st.divider()

    #Charts
    st.markdown("<p class='section-label'>Arus Kas Harian</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.subheader("Income Chart this month")
        st.bar_chart(daily_data, 
                     x="TGL_TRAN", 
                     y="MUTASI_KREDIT",
                     color="#c8f55a",
                     use_container_width=True
                     )

    with col2:
        st.subheader("Expenses Chart this month")
        st.bar_chart(daily_data, 
                     x="TGL_TRAN", 
                     y="MUTASI_DEBET",
                     color="#ff6b6b"
                     )
        
    st.divider()

    #Daily Cashflow Chart
    st.markdown("<p class='section-label'>Net Cashflow Daily</p>", unsafe_allow_html=True)
    st.markdown("#### Cashflow (Income − Expenses)")
    st.bar_chart(
        daily_data,
        x="TGL_TRAN",
        y="CASHFLOW",
        color="#74b9ff",
        use_container_width=True,
    )

    st.divider()

    #Daily transaction table
    with st.expander("View transaction details per day"):
        st.dataframe(
            daily_data.rename(columns={
                "TGL_TRAN": "Date",
                "MUTASI_KREDIT": "Income (Rp)",
                "MUTASI_DEBET": "Expenses (Rp)",
                "CASHFLOW": "Cashflow (Rp)",
            }).style.format({
                "Income (Rp)": "{:,.0f}",
                "Expenses (Rp)": "{:,.0f}",
                "Cashflow (Rp)": "{:,.0f}",
            }),
            use_container_width=True,
            hide_index=True,
        )

        st.divider()

    #Expenditure category
    st.markdown("<p class='section-label'>Expenditure category</p>", unsafe_allow_html=True)
  
else:
    st.markdown("""
    <div style="text-align:center; padding: 80px 0;">
        <div style="font-size: 3.5rem; margin-bottom: 16px;">💳</div>
        <p style="font-family:'Syne',sans-serif; font-size:1.4rem; font-weight:700; color:#f0ebe0;">
            Upload your bank statement CSV file
        </p>
        <p style="font-family:'DM Mono',monospace; font-size:0.8rem; color:#6b6b72; letter-spacing:1px;">
            Supported format: CSV export from BRI bank application
        </p>
    </div>
    """, unsafe_allow_html=True)