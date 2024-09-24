
import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

# Method 4: Using iterrows() method

for i,r in df.iterrows():
    print(r['date'],
          r['iso_a3'],
          r['currency_code'],
          r['name'],
          r['local_price'],
          r['dollar_ex'],
          r['dollar_price'],
          r['USD_raw'],
          r['EUR_raw'],
          r['GBP_raw'],
          r['JPY_raw'],
          r['CNY_raw'],
          r['GDP_bigmac'],
          r['adj_price'],
          r['USD_adjusted'],
          r['EUR_adjusted'],
          r['GBP_adjusted'],
          r['JPY_adjusted'],
          r['CNY_adjusted'])
    
    # Method 6: Using apply() method

print(df.apply(lambda row: row['name'], axis=1))