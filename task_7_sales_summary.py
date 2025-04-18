
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# connect to the SQLite database
conn = sqlite3.connect('sales_data.db')

# SQL query to summarize sales by product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
"""

# run query and load into pandas DataFrame
df = pd.read_sql_query(query, conn)

# print the result
print("Sales Summary:")
print(df)

# create a bar chart of revenue by product
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.xlabel("Product")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# close the database connection
conn.close()