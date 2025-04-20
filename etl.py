import os
import pandas as pd
from sqlalchemy import create_engine

file_path = 'AB_NYC_2019.csv' #'AB_NYC_2019.csv'
df = pd.read_csv(file_path)

missing_report = df.isnull().sum()
print("Missing Values Summary:\n", missing_report)
missing_report.to_csv("data engineering\EDA\missing_values_report.csv")

df["missing_flag"] = df.isnull().any(axis=1)

# Get environment variables

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "mydatabase")
DB_USER = os.getenv("DB_USER", "myuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "mypassword")
# dbname ='ab_nyc_db_2'
# user = 'postgres'
# password = 'admin'
# host = 'localhost'
# port = 5432
table_name = 'ab_nyc_2019'
table_name_2 = 'missing_values_report'
# Create a connection string
url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# url = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

engine = create_engine(url, echo = True)

try:
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    missing_report.to_sql(table_name_2, engine, if_exists='replace', index=False)
    # Test the connection
    print("Connection successful!")
    print(f"Data loaded into PostgreSQL table '{table_name}' successfully.")
except Exception as e:
    print(f"Error connecting to database: {e}")

def main():
    if __name__ == "__main__":
        main()