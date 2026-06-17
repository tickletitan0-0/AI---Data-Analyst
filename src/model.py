from pydantic import BaseModel

class AnalysisReport(BaseModel):
    total_sales: int
    average_sales: float
    best_product: str
    worst_product: str