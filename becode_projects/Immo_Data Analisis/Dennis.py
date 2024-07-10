import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

immo_Dennis = pd.read_csv(r'C:\Users\admin\Documents\becode_projects\Immo_Data Analisis\Dennis.csv')
#print(immo_Dennis.head)
#print(immo_Dennis.columns.tolist())

#print(immo_Dennis.head())
#print(immo_Dennis.info())
#remove duplicates

immo_Dennis_unique= immo_Dennis.drop_duplicates(subset= "Url")

#print(immo_Dennis_unique)

#delete Url
del immo_Dennis_unique["Url"]

print(immo_Dennis_unique)


