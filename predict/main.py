import pandas as pd
from prophet import Prophet
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

user = 'myuser'
password = 'mypass'
host = '127.0.0.1'
port = 3307
database = 'DATA'

def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )

def __main__(): 
  con = get_connection()
  df = pd.read_sql_query("SELECT CONCAT(\"01-\", DATE_FORMAT(Cle_Temps,\"\%m-%Y\")) as ds,COUNT(*)AS y FROM Ventes GROUP BY ds ORDER BY ds ASC;", con)
  m = Prophet()
  m.fit(df)
  future = m.make_future_dataframe(periods=365)
  forecast = m.predict(future)
  fig1 = m.plot(forecast)
  plt.show()

if __name__ == '__main__':
  __main__()
