import os
import sys
from srce.dsprojects1.exception import CustomException
from srce.dsprojects1.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')

def raed_sql_data():
    logging.info("Reading SQL database started")
    try:
      mydb=pymysql.connect(
         host=host,
         user=user,
         password=password,
         db=db
      )
      logging.info("connection Establish",mydb)
      df=pd.read_sql_query('Select * from students',mydb)
      print(df.haed())

      return df
    except Exception as ex:
       raise CustomException(ex)
