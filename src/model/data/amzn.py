import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the cash flow statement page for Amazon
url = "https://www.macrotrends.net/stocks/charts/AMZN/amazon/cash-flow-statement"

# Use requests library to retrieve the HTML content of the page
response = requests.get(url, verify=False)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the cash flow statement table by looking for the table with class "historical_data_table table"
table = soup.find("table", class_="historical_data_table table")

# Extract the column names from the table header
headers = table.find_all("th")
column_names = [header.text.strip() for header in headers]

# Extract the data rows from the table body
rows = table.find_all("tr")[
    1:
]  # Exclude the first row since it only contains the column names
data = []
for row in rows:
    cells = row.find_all("td")
    row_data = [cell.text.strip() for cell in cells]
    data.append(row_data)

# Create a pandas DataFrame from the extracted data and column names
df = pd.DataFrame(data, columns=column_names)

# Print the resulting DataFrame
print(df)
