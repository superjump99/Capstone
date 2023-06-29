import pandas as pd
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

df = pd.read_csv('MergeDate.csv', index_col='Order Date')
print(df.__len__())

exit()
#### 상관분석
columns = list(df.keys())
target = columns[0]
keys = columns[1:]


Y = df[target].values
for key in keys:
    print(key)
    X = df[key].values
    print('Covariance : {:.2f}'.format(np.cov(X,Y)[0,1]))
    print('Correlation : {:.2f}'.format(stats.pearsonr(X,Y)[0]))
    print('P-value : : {:.5f}'.format(stats.pearsonr(X,Y)[1]))
    print('\n')