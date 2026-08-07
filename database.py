from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
Database_URL="mysql://avnadmin:AVNS_36e8KzEiDkODfxHUC-V@tejasree2006-dbfastapicrud.f.aivencloud.com:19288/defaultdb?ssl-mode=REQUIRED"
#Database_URL="mysql+pymysql://root:Tejasree%402006@localhost:3306/student_db"
engine=create_engine(Database_URL)
sessionlocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)
Base=declarative_base()
