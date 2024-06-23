import matplotlib.pyplot as plt
import numpy as np

x_pos = [5,1,22,40,38,25]
x_neg = [-45,-40,-47,-29,-25,-50]
bars = ('Czerwiec', 'Maj', 'Kwiecień', 'Marzec', 'Luty', 'Styczeń')
y = np.arange(len(bars))
plt.barh(y, x_pos[::-1], color='pink')
plt.barh(y, x_neg[::-1], color='cyan')
plt.yticks(y, bars, rotation=30)
plt.savefig('wykres1.tiff')
plt.title('Bla bla')
plt.show()

# --------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('linieautobusowe4.xlsx')

rok = df["Rok"]
wartosc = df["Wartosc"]
explode = (0.2, 0, 0, 0, 0)
colors = ['r','g','b','cyan','magenta']
plt.pie(wartosc, explode=explode, colors=colors, autopct="%1.1f%%", pctdistance=1.2)
circle = plt.Circle((0, 0), 0.7, color='white')
p = plt.gcf()
p.gca().add_artist(circle)
plt.title('Wykres pierścieniowy')
plt.annotate("",(0.7,0.6),(0.2,0.5),arrowprops=dict(facecolor='violet'))
plt.legend(title='Rok',labels=rok, bbox_to_anchor=(-0.05, 0.5),loc='right')
plt.show()

# -------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dane = pd.read_csv('hotele4.csv', sep='#')
print(dane)
dane = dane.melt(["Nazwa"], var_name="Rok", value_name="Liczba")

kujawy = dane[dane["Nazwa"] == "KUJAWSKO-POMORSKIE"]

lubelskie = dane[dane["Nazwa"] == "LUBELSKIE"]
lubuskie = dane[dane["Nazwa"] == "LUBUSKIE"]
lodzkie = dane[dane["Nazwa"] == "ŁÓDZKIE"]
pomorskie = dane[dane["Nazwa"] == "POMORSKIE"]

plt.scatter(kujawy["Rok"], kujawy["Liczba"], color='r', marker='o', label='Kujawy') 
plt.scatter(lubelskie["Rok"], lubelskie["Liczba"], color='lightgreen', marker='x', label='Lubelaki') 
plt.scatter(lubuskie["Rok"], lubuskie["Liczba"], color='b', marker='>', label='Lubaki') 
plt.scatter(lodzkie["Rok"], lodzkie["Liczba"], color='magenta', marker='^', label='Łudki') 
plt.scatter(pomorskie["Rok"], pomorskie["Liczba"], color='cyan', marker='p', label='PoMorsk') 

plt.ylabel('Śmieszne cyferki')
plt.xlabel('Rok')
plt.title('Bruh')
plt.legend(title='Legenda',loc='upper right')
plt.tight_layout()
plt.show()
