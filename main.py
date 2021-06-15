
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

data = pd.read_csv("log4.csv", delimiter=delimiter)
keyss = data.keys()
index = data.index
number_of_rows = len(index)

while(programmruning):

    comand = input("Comand: ")
    if comand == "exit":
        break


    deataPoints_lenght =range(0, number_of_rows, 1)
    plt.figure()

    addData = True
    while addData:
        datNr = get_data_by_nr(keyss=keyss)
        if datNr == -1:
            break

        plt.plot(deataPoints_lenght, data[keyss[datNr]], linewidth=1, linestyle="-", label = keyss[datNr])

    plt.grid()
    plt.xlim([0, number_of_rows*1.1])

    #plt.ylim(C.min()*1.1,C.max()*1.1)
    #plt.yticks(ticks= range(0,6500,100),)

    plt.legend()
    plt.show()

