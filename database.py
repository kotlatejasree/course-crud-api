from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
Database_URL="mysql+pymysql://avnadmin:AVNS_36e8KzEiDkODfxHUC-V@tejasree2006-dbfastapicrud.f.aivencloud.com:19288/defaultdb?"
engine=create_engine(Database_URL)
sessionlocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)
Base=declarative_base()
