from model import AnalysisReport

def analyze_sales(df):
    return AnalysisReport(
        total_sales=int(df["Sales"].sum()),
        average_sales=float(df["Sales"].mean()),
        best_product=df.loc[df["Sales"].idxmax()]["Product"],
        worst_product=df.loc[df["Sales"].idxmin()]["Product"]
    )