import pandas as pd

# Load cleaned Titanic data
df = pd.read_csv("data/titanic_cleaned.csv")

# Header
print("-" * 50)
print("TITANIC DATASET | SUMMARY REPORT")
print("-" * 50)

# Overall survival rate
survival_rate = df["Survived"].astype(int).mean() * 100
print(f"\nOverall Survival Rate: {survival_rate:.1f}%")

# Survival rate by gender
print("\nSurvival Rate by Gender:")
gender_survival = df.groupby("Sex")["Survived"].apply(lambda x: x.astype(int).mean() * 100)
print(gender_survival.round(1))

# Survival rate by passenger class
print("\nSurvival Rate by Passenger Class:")
class_survival = df.groupby("Pclass")["Survived"].apply(lambda x: x.astype(int).mean() * 100)
print(class_survival.round(1))

# Age statistics
print("\nAge Statistics:")
print(df["Age"].describe().round(1))

# Fare statistics
print("\nFare Statistics:")
print(df["Fare"].describe().round(1))

# Average Fare by Passenger Class
print("\nAverage Fare by Passenger Class:")
fare_by_class = df.groupby("Pclass")["Fare"].mean()
print(fare_by_class.round(2))

# Calculate average Fare by passenger class
print("\nPassenger Count by Port Embarked:")
print(df["Embarked"].value_counts())

# Save report to file
with open("reports/summary_report.txt", "w") as f:
    f.write("TITANIC DATASET - SUMMARY REPORT\n")
    f.write("-" * 50 + "\n\n")
    f.write(f"Overall Survival Rate: {survival_rate:.1f}%\n\n")
    f.write("Survival Rate by Gender:\n")
    f.write(str(gender_survival.round(1)) + "\n\n")
    f.write("Survival Rate by Passenger Class:\n")
    f.write(str(class_survival.round(1)) + "\n\n")
    f.write("Average Fare by Passenger Class:\n")
    f.write(str(fare_by_class.round(2)) + "\n\n")
    f.write("Passenger Count by Port Embarked:\n")
    f.write(str(df["Embarked"].value_counts()) + "\n\n")

print("\nReport saved to reports/summary_report.txt")