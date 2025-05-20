import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_connection():
    return sqlite3.connect('car_sales.db')


# Create Tables 

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cars (
        car_id INTEGER PRIMARY KEY,
        make TEXT,
        model TEXT,
        year INTEGER,
        price REAL,
        category TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        region_id INTEGER
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sales (
        sale_id INTEGER PRIMARY KEY,
        car_id INTEGER,
        customer_id INTEGER,
        sale_date TEXT,
        price REAL,
        FOREIGN KEY (car_id) REFERENCES Cars(car_id),
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Regions (
        region_id INTEGER PRIMARY KEY,
        region_name TEXT
    )
    ''')
    conn.commit()


# Insterting Data

def insert_data(conn):
    cursor = conn.cursor()
    cars_data = [
        (1, 'Toyota', 'Camry', 2020, 24000, 'Sedan'),
        (2, 'Honda', 'Accord', 2019, 22000, 'Sedan'),
        (3, 'Ford', 'Mustang', 2018, 26000, 'Coupe'),
        (4, 'BMW', 'X5', 2021, 55000, 'SUV')
    ]
    customers_data = [
        (1, 'John', 'Doe', 'john.doe@example.com', 1),
        (2, 'Jane', 'Smith', 'jane.smith@example.com', 2),
        (3, 'Mike', 'Brown', 'mike.brown@example.com', 3),
        (4, 'Anna', 'Davis', 'anna.davis@example.com', 4)
    ]
    sales_data = [
        (1, 1, 1, '2024-08-01', 24000),
        (2, 1, 2, '2024-08-02', 24000),
        (3, 2, 2, '2024-08-03', 22000),
        (4, 2, 3, '2024-08-04', 22000),
        (5, 2, 4, '2024-08-05', 22000),
        (6, 3, 3, '2024-08-10', 26000),
        (7, 4, 4, '2024-08-12', 55000),
        (8, 4, 1, '2024-08-13', 55000),
        (9, 4, 2, '2024-08-14', 55000)
    ]
    regions_data = [
        (1, 'North'),
        (2, 'South'),
        (3, 'East'),
        (4, 'West')
    ]
    cursor.executemany('INSERT OR IGNORE INTO Cars VALUES (?, ?, ?, ?, ?, ?)', cars_data)
    cursor.executemany('INSERT OR IGNORE INTO Customers VALUES (?, ?, ?, ?, ?)', customers_data)
    cursor.executemany('INSERT OR IGNORE INTO Sales VALUES (?, ?, ?, ?, ?)', sales_data)
    cursor.executemany('INSERT OR IGNORE INTO Regions VALUES (?, ?)', regions_data)
    conn.commit()

#  Ananlysing and visualysing Top Selling Models 

def analyze_data(conn):
    # Top Selling Car Models
    top_models = pd.read_sql_query('''
        SELECT c.make, c.model, COUNT(s.sale_id) as total_sales
        FROM Sales s
        JOIN Cars c ON s.car_id = c.car_id
        GROUP BY c.make, c.model
        ORDER BY total_sales DESC
    ''', conn)
    print("\nTop Selling Car Models:")
    print(top_models)
    sns.barplot(x='model', y='total_sales', data=top_models)
    plt.title('Top Selling Car Models')
    plt.show()

#Analysing and visualysing Sales by Region

    # Sales by Region
    sales_by_region = pd.read_sql_query('''
        SELECT r.region_name, SUM(s.price) as total_sales
        FROM Sales s
        JOIN Customers cu ON s.customer_id = cu.customer_id
        JOIN Regions r ON cu.region_id = r.region_id
        GROUP BY r.region_name
        ORDER BY total_sales DESC
    ''', conn)
    print("\nSales by Region:")
    print(sales_by_region)
    sales_by_region.set_index('region_name').plot.pie(y='total_sales', autopct='%1.1f%%', legend=False)
    plt.ylabel('')
    plt.title('Sales by Region')
    plt.show()

#Analysing and visualysing Customer Spending 

    # Customer Spending
    spending = pd.read_sql_query('''
        SELECT cu.first_name || ' ' || cu.last_name AS customer_name, SUM(s.price) AS total_spent
        FROM Sales s
        JOIN Customers cu ON s.customer_id = cu.customer_id
        GROUP BY customer_name
        ORDER BY total_spent DESC
    ''', conn)
    print("\nCustomer Spending:")
    print(spending)
    sns.histplot(spending['total_spent'], bins=5, kde=True)
    plt.title('Customer Spending Distribution')
    plt.xlabel('Total Spent')
    plt.ylabel('Frequency')
    plt.show()

# Connecting to the databes and then closing it 

def main():
    conn = create_connection()
    create_tables(conn)
    insert_data(conn)
    analyze_data(conn)
    conn.close()

if __name__ == '__main__':
    main()

