# Financial Tracker

A simple dashboard application to track personal cash flow based on BRI bank statement mutations. Built using Python and Streamlit.

---

## Features

- **Upload CSV** — directly import BRI bank statement mutation files
- **Bar Chart Cashflow** — daily cash flow visualization (income vs expenses)
- **Summary Metrics** — summary of total income, expenses, and this month's balance
- **Savings Rate** — savings percentage from total income

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/fashafadlika/financial-tracker.git
cd financial-tracker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run dashboard.py
```

The application will open automatically in your browser at `http://localhost:8501`

---

## CSV Format

The supported CSV file is the **BRI bank statement export** via BRImo or BRI Internet Banking.

Make sure the CSV file contains the following columns:

| Column | Description |
|---|---|
| `TGL_TRAN` | Transaction date |
| `REMARK_CUSTOM` | Transaction description / notes |
| `MUTASI_KREDIT` | Incoming amount |
| `MUTASI_DEBET` | Outgoing amount |

### How to export from BRImo:
1. Open the BRImo app
2. Select **Account** → **Account Mutations**
3. Set the date range
4. Select **Download** → **CSV** format

---

## 🛠️ Tech Stack

- [Python 3.x](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — dashboard framework
- [Pandas](https://pandas.pydata.org/) — data processing

---

## Requirements

```
streamlit
pandas
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## Roadmap
- Filter by date range
- Export reports to PDF
- Deploy to Streamlit Cloud

---

## Author

Created by **Fasha Fadlika** — feel free to fork and develop it yourself.
