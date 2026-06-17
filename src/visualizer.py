import matplotlib.pyplot as plt
from model import pqr

pqr.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()