from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

def generate_ai_summary(report):

    prompt = f"""
    Analyze this sales report:

    Total Sales: {report.total_sales}
    Average Sales: {report.average_sales}
    Best Product: {report.best_product}
    Worst Product: {report.worst_product}

    Provide:
    1. Executive Summary
    2. Key Insight
    3. Recommendation
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content