from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base



# DB_URL = 'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}'.format(db_user='keonlee', db_password='Tldhdlrtm6@3(', db_host='183.101.143.204', db_port='13306', db_database='dordor_test')
DB_URL = engine.URL.create(
  drivername="mysql",
  username='keonlee',
  password='Tldhdlrtm6@3(',
  host='183.101.143.204',
  port='13306',
  database='dordor_test', 
)

# Base = declarative_base()
engine = create_engine(DB_URL, pool_recycle = 500)

class MysqlDB:

  def __init__(self):
    ...
    # self.engine = create_engine(DB_URL, pool_recycle = 500)

  def sessionmaker():
    Session = sessionmaker(bind=engine)
    session = Session()
    # Base.metadata.create_all(bind=self.engine)
    return session

  def connection():
    conn = engine.connect()
    return conn
