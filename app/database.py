from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL") # NEEDS TO BE CHANGED - issue with .env file
DATABASE_URL = "mssql+pyodbc://localhost\\SQLEXPRESS/test8?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes&TrustServerCertificate=yes"


# Set up the database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Test the database connection
try:
    with engine.connect() as connection:
        print("Dabase Connection successful.")
except Exception as e:
    print(f"Dabase Connection failed: {e}")
