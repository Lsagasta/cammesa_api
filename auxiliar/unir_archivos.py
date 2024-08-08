import pandas as pd
import glob
import os

# Ruta a los archivos CSV
path = 'csvs/'  # Carpeta donde se encuentran tus archivos CSV
all_files = glob.glob(os.path.join(path, "*.csv"))

# Lista para almacenar los dataframes
dataframes = []

# Leer y concatenar todos los archivos CSV
for filename in all_files:
    df = pd.read_csv(filename)
    dataframes.append(df)

# Concatenar todos los dataframes en uno solo
combined_df = pd.concat(dataframes, ignore_index=True)

combined_df.drop_duplicates(inplace=True)

# Guardar el dataframe combinado en un nuevo archivo CSV
combined_df.to_csv('archivo_unificado.csv', index=False)

print("Todos los archivos CSV se han unificado en 'archivo_unificado.csv'")
