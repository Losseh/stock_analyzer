import numpy as np
from pandas_datareader.stooq import StooqDailyReader


def slice(data, length, shift):
  start = shift
  end = shift + length

  return data[start:end]

def bollinger(data, length, shift):
  array = slice(data, length, shift)
  stdev = np.std(array)
  avg = np.mean(array)
  
  low = avg - 2*stdev
  high = avg + 2*stdev
  
  return {
#    'date': data.index,
    'low': low,
    'mean': avg,
    'high': high,
    'pos': (data[0]-low) / (high-low)
  }

wig40 = "MWIG40TR.PL"
dax = "^DAX"
sp500 = "^SPX"

dax_data = StooqDailyReader(dax).read()['Close']
mwig40_data = StooqDailyReader(wig40).read()['Close']
spx_data = StooqDailyReader(sp500).read()['Close']

# variance
print('dax')
print(bollinger(dax_data, 50, 0))

print('mwig40')
print(bollinger(mwig40_data, 50, 0))

print('sp500')
print(bollinger(spx_data, 50, 0))
