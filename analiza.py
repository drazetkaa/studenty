# PLIK Z ANALIZĄ DANYCH

# Import bibliotek
import pandas as pd
import numpy as np
import openpyxl as xl

# Wczytanie pliku z danymi
plik = 'PZ 2025 dane.xlsx'
df = pd.read_excel(plik)

# Obejrzenie zawartości pliku
print(df.info())

