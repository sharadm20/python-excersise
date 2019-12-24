import pandas as pd
import quandl
import math
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

df = quandl.get("BSE/BOM539678")
df = df[['Open', 'High', 'Low', 'Close', 'No. of Shares', 'Total Turnover']]
df['HI_PCT'] = (df['High']-df['Close'])/df['Close'] * 100.0
df['PCT_change'] = (df['Close']-df['Open'])/df['Close'] * 100.0

df = df[['Close', 'HI_PCT', 'PCT_change', 'No. of Shares']]

forecast_col = 'Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
print(forecast_out)
df['label'] = df[forecast_col].shift(-forecast_out)

df.dropna(inplace=True)
X = np.array(df.drop(['label'], 1))
y = np.array(df['label'])

X = preprocessing.scale(X)
# X = X[:-forecast_out+1]
df.dropna(inplace=True)
y = np.array(df['label'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)
