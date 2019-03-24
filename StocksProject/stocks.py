import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from pandas.plotting import register_matplotlib_converters

data = pd.read_csv("data_csv.csv")

#Drops unnecceary Columns
to_drop =['PE10', 'Real Price', 'Real Dividend']
data.drop(to_drop, inplace=True, axis=1)

#Convert str to Datetime
data['Date'] = pd.to_datetime(data['Date'])
#Remove unnecceary dates < 2010-1-1
time = datetime.datetime(2010, 1, 1)
new_datarange = data.loc[data['Date'] >= time]
new_data = pd.DataFrame(new_datarange)


#print(new_datarange)

#scatter plot of SP500 Preformance
g = plt.figure(1)
plt.scatter(new_data['Date'], new_data['SP500'], c='black')
plt.title('SP500 over the years')
plt.xlabel('Date')
plt.ylabel('SP500 Preformance')

g.show()


input()
