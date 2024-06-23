import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
arr = np.array(["Pn", "Wt", "Śr", "Czw", "Pt", "So", "Nd"])
np.random.seed(123)
wartosci = [[0.78, 0.75, 0.15],
            [0.49,  0.13, 0.6],
            [0.52, 0.5, 0.5],
            [0.76, 0.15, 0.5],
            [0.22, 0.15, 0.7],
            [0.78, 0.76, 0.23],
            [0.03, 0.08, 0.69]]

df = pd.DataFrame(wartosci,arr, columns=['Olsztyn', 'Toruń', 'Gdańsk'])
df.plot.area()
plt.xticks(rotation=315)
plt.yticks(np.arange(0,1.76, 0.25))
plt.grid(axis='y')
plt.show()

# -----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('handel10.xlsx')
sklepy = df[df["Wyszczególnienie"] == "sklepy"]
stacje_paliw = df[df["Wyszczególnienie"] == "stacje paliw"]
plt.scatter(sklepy["Rok"], sklepy["Wartosc"], color='b', marker='p', s=200, label='szklep')
plt.scatter(stacje_paliw["Rok"], stacje_paliw["Wartosc"], color='r', marker='*', s=50, label='Stacje_paliw')
plt.xlabel('Rok')
plt.ylabel('Wartość')
plt.title('Wykres wartości sklepów i stacji paliw')
plt.tight_layout()
plt.xticks(stacje_paliw["Rok"])
plt.annotate("",xytext=(2015,340000),xy=(2016,367011),arrowprops=dict(facecolor='cyan'))
plt.show()

#-------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_csv('wyksz10.csv', sep=',')
lata13_19 = dane[dane["Wiek"] == "13-19"]
lata20_24 = dane[dane["Wiek"] == "20-24"]
lata25_29 = dane[dane["Wiek"] == "25-29"]

X = np.arange(6)

plt.bar(X + 0.00, lata13_19["Liczebność"], color='b', width=0.25, label="13-19")
plt.bar(X + 0.25, lata20_24["Liczebność"], color='g', width=0.25, label="20-24")
plt.bar(X + 0.50, lata25_29["Liczebność"], color='r', width=0.25, label="25-29")

plt.xticks(X + 0.25, lata13_19["Wykształcenie"])
plt.title('Wykres roczników do wykształceń')
plt.xlabel('Wykształcenie')
plt.ylabel('Liczebność')
plt.legend(title='Lata')
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()