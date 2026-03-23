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
    file = st.file_uploader("Upload bank statement CSV file", type=["csv"])

st.divider()

if file is not None:
    data = bri.load_data(file)
    daily_data = bri.calculate_daily_cashflow(data)
    income, expenses = bri.get_income_expenses(daily_data)
    total_income, total_expenses, difference = bri.calculate_summary(data)
    savings_rate = bri.calculate_savings_rate(total_income, total_expenses)

    col_income, col_expenses, col_difference, col_savings_rate = st.columns(4)

    with col_income:
        st.metric(f"Total income this month: ", f"Rp {total_income:,}".replace(",", "."))
    with col_expenses:
        st.metric(f"Total expenses this month: ", f"Rp {total_expenses:,}".replace(",", "."))
    with col_difference:
        st.metric("Difference between income and expenses: ", f"Rp {difference:,}".replace(",", "."))
    with col_savings_rate:
        st.metric("Savings rate this month: ", f"{savings_rate * 100:.2f}%")

    st.divider()

    col1, col2 = st.columns(2)
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

    st.subheader("Cashflow this month")
    st.bar_chart(daily_data, x="TGL_TRAN", y="CASHFLOW")

    
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