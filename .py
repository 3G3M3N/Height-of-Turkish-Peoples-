import pandas as pd 
df = pd.read_csv("heightofworld")

df.sort_values("Male Height in Cm")
df.loc[(df["Country Name"]=="Turkey")]

df.sort_values("Female Height in Cm")
df.loc[(df["Country Name"]=="Turkey")]
