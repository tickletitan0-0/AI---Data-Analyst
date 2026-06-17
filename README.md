# AI Data Analyst

An AI-powered sales analysis tool built with Python, Pandas, Pydantic, Matplotlib, and Groq.

The application analyzes sales data from a CSV file, generates summary statistics, creates visualizations, exports reports, and produces AI-generated business insights.

## Features

* Load sales data from CSV files
* Calculate summary statistics
* Identify best and worst performing products
* Generate category-wise sales visualizations
* Export analysis reports to text files
* Generate AI-powered executive summaries using Groq

## Tech Stack

* Python
* Pandas
* Pydantic
* Matplotlib
* Groq API
* Python Dotenv

## Project Structure

```text
AI-Data-Analyst/
│
├── data/
│   └── sample_sales.csv
│
├── reports/
│   ├── summary.txt
│   ├── ai_summary.txt
│   └── charts/
│       └── category_sales.png
│
├── src/
│   ├── analyzer.py
│   ├── ai_analyzer.py
│   ├── visualizer.py
│   ├── reporter.py
│   ├── models.py
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone <repo-url>
cd AI-Data-Analyst

pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

## Usage

```bash
python src/main.py
```

The program will:

1. Load sales data
2. Analyze performance metrics
3. Generate a sales visualization
4. Export a summary report
5. Generate AI-powered insights

## Sample Output

### Summary Report

```text
Total Sales: 1550
Average Sales: 310.0
Best Product: Laptop
Worst Product: Chair
```

### Generated Files

```text
reports/
├── summary.txt
├── ai_summary.txt
└── charts/
    └── category_sales.png
```

## What I Learned

* Data analysis with Pandas
* Data visualization with Matplotlib
* Structured data models using Pydantic
* Project modularization and architecture
* LLM integration using the Groq API
* Automated report generation

## Future Improvements

* Support for multiple dataset types
* Additional visualizations
* Interactive dashboard
* Advanced AI insights
* Automated anomaly detection
