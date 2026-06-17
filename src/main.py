from analyzer import analyze_sales
import pandas as pd
df = pd.read_csv("data/sample_sales.csv")

report = analyze_sales(df)

print(report.model_dump())