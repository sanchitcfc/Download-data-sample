import streamlit as st
import pandas as pd
import yfinance as yf
from yahoo_fin.stock_info import get_data

# Define the symbols and date range
symbols = {
    'AAPL': 'Apple',
    '^NSEI': 'Nifty 50',
    '^NSEBANK': 'Nifty Bank',
    'RELI': 'Reliance',
    'SPY': 'S&P 500',
    'EURUSD=X': 'EUR/USD',
    'EURJPY=X': 'EUR/JPY',
    'JPY=X': 'JPY/USD',
    'DOGE-USD': 'Dogecoin',
    'NQT=F': 'E-Mini Nasdaq 100 Futures'
}
start_date = ''
end_date = ''

# Define the interval options
interval_options = ['1m',  '1d','1wk', '1mo']



# Set the sidebar options
st.sidebar.title("Select Options")
selected_symbol = st.sidebar.selectbox("Select a Symbol", list(symbols.keys()), format_func=lambda x: symbols[x])
selected_interval = st.sidebar.selectbox("Select an Interval", interval_options)
start_date_input = st.sidebar.text_input("Start Date (MM/DD/YYYY)", start_date)
end_date_input = st.sidebar.text_input("End Date (MM/DD/YYYY)", end_date)


# Download the data
data = get_data(selected_symbol, start_date = start_date_input, end_date = end_date_input, interval = selected_interval)

# Display the data
st.header(f"{selected_symbol} ({selected_interval})")

st.write(data)



st.download_button(
    "Download", data.to_csv(), file_name=f"{selected_symbol}.csv"
    )
