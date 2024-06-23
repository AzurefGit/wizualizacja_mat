import numpy as np
import matplotlib.pyplot as plt

N = 5

a = (49, 60, 65, 60, 55)
b = (51, 55, 45, 42, 50)
ind = np.arange(N)
width = 0.8

colors_a = ['violet', 'sienna', 'green', '#854700', 'lightyellow']
colors_b = ['darkviolet','darkviolet','blue','gray','blueviolet']

plt.bar(ind, a, width, label="A", color=colors_a)
plt.bar(ind, b, width, bottom=a, label="B", color=colors_b)

plt.ylabel('Wartość')
plt.title('Wykres słupkowy pogrupowany')
plt.xticks(ind, ('Olsztyn', 'Gdańsk', 'Toruń', 'Warszawa', 'Kraków'))
plt.yticks(np.arange(0, 151, 10))
plt.legend()
plt.show()
plt.savefig('wykres1.webp')

#-------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("parki01.xlsx")
lodzkie = df[df["Nazwa"] == "ŁÓDZKIE"]
slaskie = df[df["Nazwa"] == "ŚLĄSKIE"]
podkarpackie = df[df["Nazwa"] == "PODKARPACKIE"]
plt.plot(lodzkie['Rok'], lodzkie['Wartosc'],linestyle='solid',linewidth=3,color='cyan',label='łodzkie')
plt.plot(slaskie['Rok'], slaskie['Wartosc'],linestyle='-.',linewidth=2,color='yellow',label='śląskie')
plt.plot(podkarpackie['Rok'], podkarpackie['Wartosc'],linestyle=':',linewidth=2,color='lightgreen',label='podkarpackie')
plt.xlabel("Rok")
plt.ylabel("Wartość")
plt.xticks(np.arange(2015, 2018))
plt.title('Wykres rok-wartość')
plt.legend()
plt.grid()
plt.tight_layout()
plt.text(1,1,'19.06.2024',transform=plt.gcf().transFigure,va='top',ha='right')
plt.show()
plt.savefig('wykres2.svg', format='svg')

#-------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('medale01.csv', sep=';')

df_letni = df[df["Rodzaj"] == "Letnie"]
df_zimowy = df[df["Rodzaj"] == "Zimowe"]

plt.subplot(1, 2, 1)
plt.pie(df_letni["Brązowe"], autopct='%1.1f%%', labels = df_letni["Rok"])
plt.title('Olimpiady letnie')

plt.subplot(1, 2, 2)
plt.pie(df_zimowy["Brązowe"], autopct='%1.1f%%', labels = df_zimowy["Rok"])
plt.title('Olimpiady zimowe')
plt.tight_layout()
plt.show()
plt.savefig('wykres3.png')