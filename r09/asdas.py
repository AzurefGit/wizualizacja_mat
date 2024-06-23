import numpy as np
import matplotlib.pyplot as plt

data = [[78, 82, 65, 67, 37],
        [19, 24, 85, 35, 85],
        [62, 90, 63, 72, 23]]
X = np.arange(5)

plt.bar(X + 0.00, data[0], color='burlywood', width=0.25, label="A")
plt.bar(X + 0.25, data[1], color='navy', width=0.25, label="B")
plt.bar(X + 0.50, data[2], color='yellowgreen', width=0.25, label="C")
labelsbar = np.arange(0, 5)
plt.xticks(X + 0.25, labelsbar)
plt.xlabel('Podpis osi x')
plt.ylabel('Podpis osi y')
plt.title('Wykres')
handles, labels = plt.gca().get_legend_handles_labels()
order = [1,2,0]
plt.grid(axis='y')
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc='upper left')
# plt.savefig(...)
plt.show()

# -------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('praca09.xlsx')
nowe = df[df["Miejsca pracy"] == "liczba nowo utworzonych miejsc pracy"]
zlikwidowane = df[df["Miejsca pracy"] == "liczba zlikwidowanych miejsc pracy"]

X = np.arange(5)

plt.bar(X - 0.125, nowe["Wartosc"], color='b', width=0.25, label="A")
plt.bar(X + 0.125, zlikwidowane["Wartosc"], color='g', width=0.25, label="B")
plt.xticks(X, nowe["Rok"])
plt.legend()
plt.show()

# ----------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv('kurs09.csv', sep=';')
dane = dane.replace(',','.', regex=True).astype(float)
parzyste = dane[dane['Dzień'] % 2 == 0]['Dzień']
kurs_czk_parzyste = dane[dane['Dzień'] % 2 == 0]['Kurs CZK']
plt.plot(parzyste, kurs_czk_parzyste)
plt.show()