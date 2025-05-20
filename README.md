# Car Sales Data Analysis

### Introduction
This project is a comprehensive data analysis of car sales using Python and SQLite. It involves creating a database, performing SQL queries to extract meaningful insights, and visualizing the results using Python's `matplotlib` and `seaborn` libraries. The analysis focuses on identifying top-selling car models, understanding sales performance across different regions, and analyzing customer spending patterns. The project also includes unit tests to ensure the reliability and accuracy of the analysis functions.

### Motivation
The motivation behind this project is to demonstrate proficiency in SQL and Python for data analysis, particularly within the context of a car sales business. The project aims to provide a clear understanding of sales dynamics and customer behavior, which are critical for business decision-making. By working on this project, I enhanced my skills in database management, data analysis, and data visualization, and gained experience in developing robust, testable code.

### Project Structure

- **`car_sales_analysis.py`**: Contains the main logic for database creation, data insertion, analysis, and visualization.
  - `create_database()`: Creates the SQLite database and tables.
  - `insert_data()`: Inserts sample data into the tables.
  - `analyze_top_selling_models()`: Analyzes and identifies the top-selling car models.
  - `analyze_sales_by_region()`: Analyzes sales performance across different regions.
  - `analyze_customer_spending()`: Analyzes customer spending patterns.
  - `visualize_results()`: Generates visualizations based on the analysis.

- **`test_sales_analysis.py`**: Contains unit tests for the core analysis functions.
  - `test_analyze_top_selling_models()`: Tests the analysis of top-selling car models.
  - `test_analyze_sales_by_region()`: Tests the sales performance analysis by region.
  - `test_analyze_customer_spending()`: Tests the analysis of customer spending.

### Problems and Solutions

1. **Database Initialization**:
   - **Problem**: Ensuring that the SQLite database and tables are correctly initialized and populated.
   - **Solution**: Implemented a `create_database()` function that sets up the database schema and an `insert_data()` function to handle data insertion, with error handling to ensure robustness.

2. **Data Analysis Queries**:
   - **Problem**: Extracting accurate and meaningful insights from the database using SQL queries.
   - **Solution**: Carefully constructed SQL queries in functions like `analyze_top_selling_models()` to ensure that the results are accurate and reflect the business needs.

3. **Data Visualization**:
   - **Problem**: Visualizing the results in an informative and aesthetically pleasing manner.
   - **Solution**: Utilized `matplotlib` and `seaborn` to create clear and informative bar charts, pie charts, and histograms, ensuring that the visualizations accurately represent the data.

### Personal Experience
This project provided valuable experience in integrating SQL and Python for data analysis, as well as in writing testable, maintainable code. By focusing on a real-world application like car sales, I was able to create a meaningful project that demonstrates the ability to extract insights from data and present them effectively. Testing the analysis functions also reinforced the importance of code reliability and correctness, especially when dealing with business-critical data.

### Dependencies
To run this project, you need:
- pandas
- matplotlib
- seaborn
- sqlite3 (built-in with Python)
- unittest (built-in with Python)

Install them using:
# pip install -r requirements.txt

### How to Run:
Clone the repository:
# git clone https://github.com/tamarsaa/car_sales_data_analysis.git
# cd car_sales_data_analysis

### Install the dependencies:
# pip install -r requirements.txt

### Run the analysis:
# python car_sales_analysis.py

### How to Test:
Set Up Virtual Environment (Optional but recommended):
Create and activate a virtual environment to isolate the testing environment.
# python -m venv venv
# source venv/bin/activate
Or On Windows:
# venv\Scripts\activate

### Install Dependencies:
# pip install -r requirements.txt

### Run the tests:
# python -m unittest test_sales_analysis.py



-----------------------------



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
