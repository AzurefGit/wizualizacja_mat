# import matplotlib.pyplot as plt
# import numpy as np
 
# plt.scatter([11, 12, 13, 15, 36, 40], [30, 13, 3, 5, 8, 28], s=100, color='red', marker='p', label='pięciokąty')  
# plt.scatter([11, 12, 13, 15, 36, 40], [25, 47, 42, 26, 39, 32], s=100, color='blue', marker='x', label='krzyżyki')  

# plt.grid()
# plt.title('Wykres punktowy - 2 x 6 punktów')
# plt.xticks(np.arange(10,45,5))
# plt.yticks(np.arange(0,50,10))
# plt.ylim(1,50)
# plt.legend()
# plt.savefig('wykres1.tiff')
# plt.show()

#----------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# df = pd.read_excel('sprzedaz03.xlsx')
# jablka = df[df["Produkt"] == "Jabłka"]
# gruszki = df[df["Produkt"] == "Gruszki"]
# morele = df[df["Produkt"] == "Morele"]

# Y = np.arange(3)
# plt.barh(Y, jablka['Sprzedaż'], color='r', height=0.25, label='Jabłka')
# plt.barh(Y + 0.25, gruszki['Sprzedaż'], color='lightgreen', height=0.25, label='Gruszki')
# plt.barh(Y + 0.50, morele['Sprzedaż'], color='orange', height=0.25, label='Morele')
# labelsbar = np.arange(2015, 2018)
# plt.yticks(Y + 0.25, labelsbar)
# plt.xlabel('Sprzedaż')
# plt.ylabel('Rok')
# plt.title('Sprzedaż za lata 2015-2017')
# plt.grid()
# plt.annotate("", xy=(1781, 0), xytext=(1951, 1),arrowprops=dict(facecolor='cyan'))
# plt.legend()
# plt.savefig("wykres2.pdf")
# plt.show()

#---------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel('sady03.xlsx', header=None).T
rok = df[1].astype(int)
wartosci = df[3].astype(int)

colors = ['red', 'blue', 'lightgreen', 'yellow', 'cyan', 'gold']
explode = (0.2, 0, 0, 0, 0, 0)
plt.pie(wartosci, explode=explode, colors=colors, pctdistance=0.85, autopct='%1.1f%%', shadow=True, startangle=15)
circle = plt.Circle((0, 0), 0.7, color='white')
p = plt.gcf()
p.gca().add_artist(circle)
plt.title('Wykres pierścieniowy')
plt.axis('equal')
plt.legend(rok, title="Rok")
plt.show()