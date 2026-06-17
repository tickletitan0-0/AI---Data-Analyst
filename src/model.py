import pandas as pd
df = pd.read_csv("data/sample_sales.csv")

x = df.loc[df["Sales"].idxmax()]
z = df.loc[df["Sales"].idxmin()]
y = x["Product"]
p = z["Product"]
print("Total sales: ", df["Sales"].sum())
print("Average sales: ", df["Sales"].mean())
print("Best product: ",y)
print("Worst product: ",p)
