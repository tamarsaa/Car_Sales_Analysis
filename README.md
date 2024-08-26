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
```bash
pip install -r requirements.txt

How to Run

Clone the repository:
git clone https://github.com/tamarsaa/car_sales_data_analysis.git
cd car_sales_data_analysis


Install the dependencies:

pip install -r requirements.txt


Run the analysis:

python car_sales_analysis.py


How to Test
Set Up Virtual Environment (Optional but recommended):
Create and activate a virtual environment to isolate the testing environment.

python -m venv venv
source venv/bin/activate
Or On Windows:
venv\Scripts\activate


Install Dependencies:

pip install -r requirements.txt


Run the tests:

python -m unittest test_sales_analysis.py


### Future Improvements
Looking ahead, potential improvements include expanding the dataset to include more comprehensive sales data, integrating additional analysis functions to explore different aspects of the sales process, and enhancing the visualizations with more interactive elements. Additionally, exploring the use of machine learning models to predict sales trends based on historical data could add significant value to the project.


