import pandas as pd
import json
from decimal import Decimal

#read csv (input csv file)
def load_data(file_path):
    data = pd.read_csv(file_path)

    #convert data types
    data["MUTASI_DEBET"] = pd.to_numeric(data["MUTASI_DEBET"], errors="coerce")
    data["MUTASI_KREDIT"] = pd.to_numeric(data["MUTASI_KREDIT"], errors="coerce")
    data["TGL_TRAN"] = pd.to_datetime(data["TGL_TRAN"]).dt.normalize()

    return data

def calculate_daily_cashflow(data):
    #grouping by date, credit, debit
    daily_data = data.groupby("TGL_TRAN")[["MUTASI_KREDIT", "MUTASI_DEBET"]].sum()
    daily_data["CASHFLOW"] = (daily_data["MUTASI_KREDIT"] - daily_data["MUTASI_DEBET"])
    daily_data = daily_data.reset_index()

    return daily_data

def calculate_summary(data):
    total_income = int(data["MUTASI_KREDIT"].sum())
    total_expenses = int(data["MUTASI_DEBET"].sum())
    difference = total_income - total_expenses

    return total_income, total_expenses, difference

def calculate_savings_rate(total_income, total_expenses):

    if total_income <= 0:
        raise ValueError("Total income must be greater than 0")
    elif total_expenses < 0:
        raise ValueError("Total expenses is negative")
    elif total_expenses > total_income:
        raise ValueError("Total expenses exceed total income")
    
    income = Decimal(str(total_income))
    expenses = Decimal(str(total_expenses))

    savings_rate = (income - expenses) / income

    return savings_rate