import pandas as pd

# Data frame es la información basica con el nombre de las piezas y centrimetros para poder armar el excel

data = {
    "Piezas: " : ["Pata", "Tablero", "Puerta", "Estante", "Panel lateral"],
    "Centimetros ": [40,120,60,30,180],
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo de excel

df.to_excel("muebres_medidas.xlsx", index=False)