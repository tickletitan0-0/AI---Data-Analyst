import matplotlib.pyplot as plt

def create_bar_chart(df):

    grouped = (
        df.groupby("Category")["Sales"]
        .sum()
    )

    grouped.plot(kind="bar")

    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig(
        "reports/charts/category_sales.png"
    )

    plt.close()