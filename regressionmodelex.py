import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
import pandas

df = sm.datasets.get_rdataset("Guerry", "HistData").data
df = df[['Lottery', 'Literacy', 'Wealth', 'Region']].dropna()

mod = smf.ols(formula='Lottery ~ Literacy + Wealth + Region', data=df)
res = mod.fit()

print(res.summary())
