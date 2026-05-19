import pandas as pd

# Load CSV into mainframe
df = pd.read_csv("data/titanic.csv")

# Confirm size of the dataset
print("Shape:", df.shape)

# What is in the columns
print("\nColumns:", df.columns.tolist())

# Structure of the data
print("\nFirst 5 rows:")
print(df.head())

# What data types are in each column
print("\nData types:")
print(df.dtypes)

# What are the missing values
print("\nMissing values per column:")
print(df.isnull().sum())