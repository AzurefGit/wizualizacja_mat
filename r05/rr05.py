# import matplotlib.pyplot as plt

# sizes_1 = [10.8, 32.22, 29.99, 17.19, 9.8]
# sizes_2 = [13.5, 23.7, 28.8, 23.1, 10.9]
# labels = ['a', 'b', 'c', 'd', 'e']
# colors = ['gray', 'brown', 'cyan', 'purple', 'orange']
# plt.subplot(2,1,1)
# plt.pie(sizes_1, explode=(0, 0, 0.2, 0, 0), labels=labels, colors=colors, autopct='%1.2f%%', startangle=30)
# plt.subplot(2,1,2)
# plt.pie(sizes_2, explode=(0, 0, 0.2, 0, 0.05), labels=labels, colors=colors, autopct='%1.1f%%', startangle=30)
# plt.axis('equal')
# # plt.savefig
# plt.show()

# ------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_excel('ceny5.xlsx')
# pstrag = df[df["Rodzaje produktów"] == "pstrąg świeży niepatroszony - za 1 kg"]
# morszczuk = df[df["Rodzaje produktów"] =="filety z morszczuka mrożone - za 1kg"]
# sledz = df[df["Rodzaje produktów"] == "śledź solony, niepatroszony - za 1kg"]
# plt.scatter(pstrag["Wartosc"], pstrag["Rok"], color='r', marker='o', label='pstrag')
# plt.scatter(morszczuk["Wartosc"], morszczuk["Rok"], color='g', marker='*', label='morszczuk') 
# plt.scatter(sledz["Wartosc"], sledz["Rok"], color='b', marker='x', label='sledz') 
# plt.xlabel('Wartosc')
# plt.ylabel('Rok')
# plt.grid()
# plt.title('Ceny ryb')
# plt.annotate("175271",(14.5,2016.1))
# plt.legend()
# plt.show()

# ------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv('cechy5.csv', sep=';')
dane = dane.replace(',','.', regex=True)
print(dane)
dane["Cecha1"] = dane["Cecha1"].astype(float)
plt.hist(dane["Cecha1"], edgecolor='black', bins=6)
plt.title("Histogram pierwszej cechy podzielonej na 6 koszyków")
plt.xlabel("Wartość cechy")
plt.ylabel("Liczba obserwacji")
plt.grid()
plt.legend(['Pierwsza cecha'])
plt.show()
