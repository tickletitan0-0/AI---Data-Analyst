import pandas as pd

from analyzer import analyze_sales
from visualizer import create_bar_chart
from reporter import generate_report, save_ai_summary
from ai_analyzer import generate_ai_summary

df = pd.read_csv("data/sample_sales.csv")

report = analyze_sales(df)

create_bar_chart(df)

generate_report(report)
airep = generate_ai_summary(report)

save_ai_summary(airep)

print(report)