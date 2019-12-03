#%%
import pandas
from pandas import DataFrame, Series
import numpy as np 
import matplotlib.pyplot as pyplot

#%%
df = DataFrame([[1,2,5,6,7],[10,20,30,40]]
,columns=['c1', 'c2', 'c3', 'c4',]
, index=['11','22'])

print(df)
#%%