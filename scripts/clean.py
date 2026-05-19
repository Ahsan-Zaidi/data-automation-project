import pandas as pd

# Initialize data
df = pd.read_csv("data/titanic.csv")

# Display initial structure of dataset
print("Shape before cleaning:", df.shape)

# Delete the cabin column 
# REASON: Too many nulls not as useful
df = df.drop(columns=["Cabin"])
print("Dropped Cabin column")

# Replace age value with the median
# REASON: some age values are missing but many are still available
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)
print(f"Filled missing Age values with median: {median_age}")

# Fill missing Embarked values with the most common port
most_common_port = df["Embarked"].mode()[0]
df["Embarked"] = df["Embarked"].fillna(most_common_port)
print(f"Filled missing Embarked values with: {most_common_port}")

# Cast columns to their appropriate types
df["Survived"] = df["Survived"].astype("category")
df["Pclass"] = df["Pclass"].astype("category")
df["Sex"] = df["Sex"].astype("category")
df["Embarked"] = df["Embarked"].astype("category")
print("Cast Survived, Pclass, Sex, Embarked to category type")

# Drop any duplicates
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"Removed {before - after} duplicate rows")

# display the new structure
print("\nShape after cleaning:", df.shape)

# Verification / sum of null values discovered
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save cleaned data
df.to_csv("data/titanic_cleaned.csv", index=False)
print("\nCleaned data saved to data/titanic_cleaned.csv")