# Data Automation & Analysis Pipeline

A Python data pipeline project that ingests, cleans, and analyzes the Titanic dataset using Pandas.

## Project Structure

```
data-automation-project/
├── data/
│ ├── titanic.csv
│ └── titanic_cleaned.csv
├── scripts/
│ ├── ingest.py
│ ├── clean.py
│ └── report.py
├── reports/
│ └── summary_report.txt
├── requirements.txt
└── README.md
```

## Scripts

- **ingest.py** - Loads the raw Titanic CSV data and explores the dataset structure. data types, and missing values
- **clean.py** - Handles all null values, cast columns to their appropriate types, and removes any duplicates
- **report.py** - Generates descriptive statistics and surfaces insights from the cleaned data

## Key Insights from the Data

- Overall survival rate was **38.4%**
- Female survival rate was **74.2%** vs male at **18.9%**
- 1st class passengers survived at **63%** vs 3rd class at **24.2%**
- Fare data was heavily skewed — median fare was $14.50 but max was $512.33

## How to Run

**1. Clone the repository:**

```bash
git clone https://github.com/Ahsan-Zaidi/data-automation-project.git
cd data-automation-project
```

**2. Create and activate a virtual environment:**

```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

**4. Run the scripts in order:**

```bash
python scripts/ingest.py
python scripts/clean.py
python scripts/report.py
```

## Tools & Libraries

- Python
- Pandas
- CSV / txt file I/O
