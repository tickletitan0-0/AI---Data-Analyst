from analyzer import analyze_sales
import pandas as pd
from reporter import generate_report
df = pd.read_csv("data/sample_sales.csv")

report = analyze_sales(df)

generate_report(report)

print(report.model_dump())