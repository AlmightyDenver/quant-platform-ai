import yfinance as yf
import pandas as pd
from functools import reduce

# Create Ticker objects for each index
nq = yf.Ticker('^NDX')    # NASDAQ 100
sp = yf.Ticker('^GSPC')   # S&P 500
dj = yf.Ticker('^DJI')    # Dow Jones Industrial Average
ks = yf.Ticker('^KS11')   # KOSPI (Korea)
kq = yf.Ticker('^KQ11')   # KOSDAQ (Korea)
nk = yf.Ticker('^N225')   # Nikkei 225 (Japan)
hs = yf.Ticker('^HSI')    # Hang Seng Index (Hong Kong)

# Fetch the most recent closing prices (1-day history)
nq_data = nq.history(period='1d')['Close']
sp_data = sp.history(period='1d')['Close']
dj_data = dj.history(period='1d')['Close']
ks_data = ks.history(period='1d')['Close']
kq_data = kq.history(period='1d')['Close']
nk_data = nk.history(period='1d')['Close']
hs_data = hs.history(period='1d')['Close']
'''
Output Example : 
Date
2025-06-27 00:00:00-04:00    20273.460938
'''

# Store the data in a dictionary with index names as keys
dfs = {
    'NDX': nq_data,
    'GSPC': sp_data,
    'DJI': dj_data,
    'KS11': ks_data,
    'KQ11': kq_data,
    'N225': nk_data,
    'HSI': hs_data,
}

renamed_dfs = []

# Reset index and rename columns to standard format
for name, df in dfs.items():
    df = df.reset_index()        # Convert DateTimeIndex to column
    df.columns = ['Date', name]  # Rename columns to ['Date', 'IndexName']
    renamed_dfs.append(df)

# Format Date to 'YYYY-MM-DD' (remove time and timezone info)
for df in renamed_dfs:
    df['Date'] = pd.to_datetime(df['Date']).dt.date

# Merge all DataFrames on the 'Date' column (outer join to preserve all dates)
merged_df = reduce(lambda left, right: pd.merge(left, right, on='Date', how='outer'), renamed_dfs)

# Keep only the most recent date's row (to account for time zone differences)
latest_date = merged_df['Date'].max()
merged_df = merged_df[merged_df['Date'] == latest_date]

# Display result
# print(merged_df)

'''
Output Example :

         Date       NDX     GSPC     DJI         KS11    KQ11          N225           HSI
1  2025-06-30      NaN      NaN     NaN  3071.699951  781.5  40487.390625  24072.279297
'''
