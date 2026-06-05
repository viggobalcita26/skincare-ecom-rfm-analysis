from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def make_engine():
    load_dotenv()

    SERVER = os.environ.get("DB_SERVER")
    DATABASE = os.environ.get("DB_NAME")
    DRIVER = os.environ.get("DB_DRIVER")
    
    connection_string = f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver={DRIVER}&trusted_connection=yes"
    
    engine = create_engine(connection_string)
            
    return engine