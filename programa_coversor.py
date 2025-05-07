import pandas as pd


def cm_a_pulgadas(cm):
    return cm / 2.24


# Leer el archivo excel:
df = pd.read_excel("muebres_medidas.xlsx")

# Añadir una columna al dataframe en un archivo excel

df["Pulgadas"] = df["Centimetros "].apply(cm_a_pulgadas)

df.to_excel("mueble_medidas_convertidas.xlsx", index=False)

print(
    "Conversion completada y guarda en un nuevo archivo llamada 'mueble_medidas_convertidas.xlsx'"
)