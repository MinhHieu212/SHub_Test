import pandas as pd

# URL of the Excel file
url = "https://go.microsoft.com/fwlink/?LinkID=521962"

# Read data from the URL
df = pd.read_excel(url)

# Print column names
print(df.columns)

# Filter rows with values in the "Sales" column > 50,000
filtered_df = df[df[' Sales'] > 50000]

# Create a new Excel file from the filtered DataFrame
filtered_df.to_excel("filtered_sales.xlsx", index=False)

print("New Excel file has been created and saved successfully.")
