import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 400)

y1 = x**2 + 3
y2 = (np.e**x)-1

fig, ax1 = plt.subplots()

ax1.plot(x, y1, color='red')
ax1.set_ylabel(r'$y = x^2 + 3$')

ax2 = ax1.twinx()
ax2.plot(x, y2)
ax2.set_ylabel(r'$y = e^x - 1$')

plt.title("Dwa wykresy")
plt.tight_layout()
plt.savefig('wykres.tiff')
plt.show()

# --------------------------

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('ceny08.xlsx')
r2014 = df[df["Rok"] == 2014]
r2015 = df[df["Rok"] == 2015]
plt.plot(r2014["Miesiące"], r2014["Wartosc"], label='2014', linestyle='dashed', color='gold', linewidth=9)
plt.plot(r2015["Miesiące"], r2015["Wartosc"], label='2015', linestyle='dotted', color='cyan', linewidth=3)
plt.xlabel('Miesiące')
plt.ylabel('Wartości')
plt.title("Wykres cen do miesięcy")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()

# -----------------------

import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_excel('przewozy08.xlsx')

dane = dane.melt(["Nazwa"], var_name="Rok", value_name="Liczba")
slazk = dane[dane["Nazwa"] == "ŚLĄSKIE"]
mazowsze = dane[dane["Nazwa"] == "MAZOWIECKIE"]
labels = slazk["Rok"]
plt.subplot(1,2,1)
plt.pie(slazk["Liczba"], labels=labels, colors=['red', 'blue', 'green', 'yellow'], autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Wykres 1.')
plt.axis('equal')

plt.subplot(1,2,2)
plt.pie(mazowsze["Liczba"], labels=labels, colors=['gold', 'forestgreen', 'cyan', 'grey'], autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Wykres 2.')
plt.axis('equal')
plt.show()