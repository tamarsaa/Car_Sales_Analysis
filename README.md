# Car Sales Analysis

### Introduction
This project presents a hands-on data analysis of car sales using Python and SQLite, focusing on real-world business performance metrics. It involves structured data modeling, querying with SQL, and delivering insights through clear visualizations using `matplotlib` and `seaborn`. The goal is to practice turning raw data into business-relevant stories using clean, reproducible code.

### Motivation
The project was designed as a practical exercise to deepen understanding of business analytics, with an emphasis on key performance indicators (KPIs) such as product performance, regional revenue distribution, and customer spending trends. It also provided experience in building complete analysis pipelines independently using standard tools.

### Project Structure
- **`car_sales_analysis.py`**: The main file for setting up the database, populating data, analyzing trends, and visualizing findings.
  - `create_connection()`: Initializes the SQLite connection.
  - `create_tables()`: Creates relational tables for cars, customers, sales, and regions.
  - `insert_data()`: Adds predefined test data into all tables.
  - `analyze_data()`: Runs SQL queries and visualizations for:
    - Top-selling car models
    - Sales by region
    - Customer spending patterns

- **`test_sales_analysis.py`**: A suite of unit tests validating SQL query logic and data consistency using `unittest`.

### Problems and Solutions
- **Table Dependencies**:
  - *Challenge*: Ensuring referential integrity across multiple foreign keys during table creation.
  - *Solution*: Used explicit schema definition with `FOREIGN KEY` constraints and controlled insertion order for smooth initialization.

- **Insight Extraction**:
  - *Challenge*: Writing concise SQL queries that reflect real-world KPIs.
  - *Solution*: Structured joins and grouping logic to pull out customer behavior, sales performance by region, and best-performing models.

### Personal Experience
This project allowed me to apply my SQL and Python skills in a meaningful business context. It reinforced my ability to think relationally, build repeatable processes, and translate queries into actionable insights. From writing queries to visualizing results, I practiced full-cycle analysis—valuable preparation for junior data analyst roles.

### Dependencies
To run this project, install the following:
- pandas
- matplotlib
- seaborn
- sqlite3 (included with Python)
- unittest (included with Python)

Install them using:
```
pip install -r requirements.txt
```

### How to Run:
1. Clone the repository:
```
git clone https://github.com/tamarsaa/car_sales_data_analysis.git
cd car_sales_data_analysis
```

2. Run the analysis:
```
python car_sales_analysis.py
```

### How to Test:
1. (Optional) Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run unit tests:
```
python -m unittest test_sales_analysis.py
```
