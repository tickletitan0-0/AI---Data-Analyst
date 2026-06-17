def generate_report(report):
    with open(
        "reports/summary.txt",
        "w"
    ) as file:

        file.write(
            f"Total Sales: {report.total_sales}\n"
        )

        file.write(
            f"Average Sales: {report.average_sales}\n"
        )

        file.write(
            f"Best Product: {report.best_product}\n"
        )

        file.write(
            f"Worst Product: {report.worst_product}\n"
        )