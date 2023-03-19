import numpy as np
import pandas as pd
df=pd.read_csv('/home/mush/Downloads/txn.txt',sep=',',header=None)
#if header is none type header is equal to none
print(df)
df.columns=['id1','id2','id3','id4','id5','id6','id7','id8','id9']
print(df)