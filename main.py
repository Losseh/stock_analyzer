import numpy as np
from pandas_datareader.stooq import StooqDailyReader


def slice(data, length, shift):
  start = shift
  end = shift + length

  if end == 0:
    return data[start:]
  else:
    return data[start:end]

def bollinger(data, length, shift):
  array = slice(data, length, shift)
  stdev = np.std(array)
  avg = np.mean(array)
  
  return {
#    'date': data.index,
    'low': avg - 2*stdev,
    'mean': avg,
    'high': avg + 2*stdev
  }

wig40 = "MWIG40TR.PL"
dax = "^DAX"
sp500 = "^SPX"

dax_data = StooqDailyReader(sp500).read()

# variance
print(bollinger(dax_data, 50, 0))
print(bollinger(dax_data, 50, 1))
print(bollinger(dax_data, 50, 2))
