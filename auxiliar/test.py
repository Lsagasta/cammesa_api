import pandas as pd
from decouple import config
from functions import conection



#df = pd.read_csv("csvs/generacion-electrica-2024-07-31.csv")


#df['fecha'] = pd.to_datetime(df['timestamp']).dt.date
#df["hora"] = pd.to_datetime(df["timestamp"]).dt.strftime('%H:%M:%S')



con = conection()

cursor = con.cursor()
cursor.execute("SELECT * FROM cammesa")
resultado = cursor.fetchall()
print(resultado)




