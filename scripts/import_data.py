import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path

# get database info for connnection string
load_dotenv()
SERVER = os.environ.get("DB_SERVER")
DATABASE = os.environ.get("DB_NAME")
DRIVER = os.environ.get("DB_DRIVER")

# create engine 
connection_string = f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver={DRIVER}&trusted_connection=yes"
engine = create_engine(connection_string)

# import the data into SQL server
files_to_import = {
    "customers": "Customers.csv", 
    "order_items": "Order_Items.csv",
    "orders": "Orders.csv",
    "products": "Products.csv",
    "returns": "Returns.csv",
    "reviews": "Reviews.csv" 
}

BASE_DIR = Path(__file__).resolve().parent.parent

for table, csv_file in files_to_import.items():
    try:
        csv_path = BASE_DIR / "data" / csv_file
        df = pd.read_csv(csv_path)
        df.to_sql(table, con=engine, if_exists="replace", index=False, chunksize=1000)
    except Exception as e:
        print(f"Caught an exception: {e}")

print("Datasets have been successfully imported!")