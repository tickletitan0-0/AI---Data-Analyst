import pandas as pd
df = pd.read_csv("data/sample_sales.csv")

x = df.loc[df["Sales"].idxmax()]
z = df.loc[df["Sales"].idxmin()]
y = x["Product"]
p = z["Product"]

print(df[df["Sales"]>300])
print(df[df["Sales"]<400])

print(df.groupby("Category")["Sales"].sum())