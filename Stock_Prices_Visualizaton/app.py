import yfinance as yf
import streamlit as st

st.write("""
# Stock Price App
### Shown are the stock closing price and volume of Google!
""")

#Define the ticker symbol
tickerSymbol = 'GOOGL'

#Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-05-31', end='2021-05-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

st.write("""
### Shown are the stock closing price and volume of Apple!
""")

#Define the ticker symbol
tickerSymbol2 = 'APPL'

#Get data on this ticker
tickerData2 = yf.Ticker(tickerSymbol)

#Get the historical prices for this ticker
tickerDf2 = tickerData2.history(period='1d', start='2010-05-31', end='2021-05-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf2.Close)
st.line_chart(tickerDf2.Volume)