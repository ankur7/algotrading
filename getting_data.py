# https://www.learndatasci.com/tutorials/python-finance-part-yahoo-finance-api-pandas-matplotlib/


from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

print("Reached here")

tickers = ['AAPL', 'MSFT', '^GSPC']
start_date = '2010-01-01'
end_date = '2016-12-31'

panel_data = data.DataReader('RELIANCE.NS', 'yahoo', start_date, end_date)

# print(panel_data.__dict__)
# print (dir(panel_data))

print(panel_data.head(9))