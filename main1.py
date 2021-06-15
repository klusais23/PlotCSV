import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
if os.path.exists("log.csv"):
  os.remove("log.csv")
  print("file is delited")
else:
  print("The file does not exist")

programmruning = True

data_toPlot = list()

def get_data_by_nr(keyss):
    count = 0
    for key in keyss:
        print(f"{count}: {key}")
        count = count + 1
    nr = int(input("select number to show: "))
    return nr


delimiter = "," #input("delimeer_ simbol: ")

data = pd.read_csv("log2.csv", delimiter=delimiter)
keyss = data.keys()
index = data.index
number_of_rows = len(index)



