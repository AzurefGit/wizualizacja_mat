# import matplotlib.pyplot as plt

# sizes = [10, 25, 7, 14, 14, 30]
# labels = ['A', 'B', 'C', 'D', 'E', 'F']
# colors = ['olive', 'forestgreen', 'gainsboro', 'navajowhite', 'purple', 'orange']
# explode = (0.2, 0, 0, 0, 0, 0)

# plt.pie(sizes, explode=explode, labels=labels, colors=colors, startangle=45)
# plt.axis('equal')
# circle = plt.Circle((0, 0), 0.6, color='white')
# p = plt.gcf()
# p.gca().add_artist(circle)
# plt.annotate("ABCDE", (-0.15,0))
# # plt.savefig
# plt.show()

# ------------------------------------------------------------------ #

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_excel('ceny06.xlsx')

# cytryny = df[df["Rodzaje towarów i usług"] == "cytryny - za 1 kg"]
# marchew = df[df["Rodzaje towarów i usług"] == "marchew - za 1 kg"]

# plt.scatter(cytryny['Miesiące'], cytryny['Wartosc'], color='cyan', marker='o', s=100, label='cytryny')
# plt.scatter(marchew['Miesiące'], marchew['Wartosc'], color='blue', marker='^', s=50, label='marchewki')
# plt.xlabel('Miesiące')
# plt.xticks(rotation=45)
# plt.ylabel('Cena')
# plt.title('Wartość marchewek i cytryn w poszczególnych miesiącach')
# plt.grid()
# plt.annotate("",('grudzień', 1.59),('październik',4),arrowprops=dict(facecolor='lightgreen'))
# plt.legend()
# plt.tight_layout()
# plt.show()

# ------------------------------------------------------------------ #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv('wynagrodzenia06.csv',sep=';', header=None)
headers = dane[0]
dane = dane.T
dane = dane[1:]
dane.columns = headers
dane["Wartosc"] = dane["Wartosc"].str.replace(',', '.', regex=True).astype(float)

slazk = dane[dane["Nazwa"] == "ŚLĄSKIE"]
podkarpacie = dane[dane["Nazwa"] == "PODKARPACKIE"]


Y = np.arange(3)

plt.barh(Y - 0.125, slazk["Wartosc"].T, color='b', height=0.25, label="ŚLĄSKIE")
plt.barh(Y + 0.125, podkarpacie["Wartosc"].T, color='g', height=0.25, label="PODKARPACKIE")
plt.yticks(Y + 0.00, slazk["Rok"])
plt.title('HCWD')
plt.legend()
plt.tight_layout()
plt.show()