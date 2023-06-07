import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython import display

display.set_matplotlib_formats('svg')

data = pd.read_feather('./house_sales.ftr')
print(data.shape)
null_sum = data.isnull().sum()
print(data.columns[null_sum < len(data) * 0.3])  # columns will keep
data.drop(columns=data.columns[null_sum > len(data) * 0.3], inplace=True)
currency = ['Sold Price', 'Listed Price', 'Tax assessed value', 'Annual tax amount']
for c in currency:
    data[c] = data[c].replace(
        r'[$,-]', '', regex=True).replace(
        r'^\s*$', np.nan, regex=True).astype(float)

areas = ['Total interior livable area', 'Lot size']
for c in areas:
    acres = data[c].str.contains('Acres') == True
    col = data[c].replace(r'\b sqft\b|\b Acres\b|\b,\b', '', regex=True).astype(float)
    col[acres] *= 43560
    data[c] = col

abnormal = (data[areas[1]] < 10) | (data[areas[1]] > 1e4)
data = data[~abnormal]
sum(abnormal)

ax = sns.histplot(np.log10(data['Sold Price']))
ax.set_xlim([3, 8])
ax.set_xticks(range(3, 9))
ax.set_xticklabels(['%.0e' % a for a in 10 ** ax.get_xticks()])

print(data['Type'].value_counts()[0:20])
types = data['Type'].isin(['SingleFamily', 'Condo', 'MultiFamily', 'Townhouse'])
sns.displot(pd.DataFrame({'Sold Price': np.log10(data[types]['Sold Price']),
                          'Type': data[types]['Type']}),
            x='Sold Price', hue='Type', kind='kde')
