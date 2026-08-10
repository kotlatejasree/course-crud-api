from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
load_dotenv()
Database_URL=os.getenv("DATABASE_URL")
print(os.getenv("DATABASE_URL"))
engine=create_engine(Database_URL)
sessionlocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)
Base=declarative_base()