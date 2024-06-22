# import numpy as np
# import matplotlib.pyplot as plt

# plt.subplot(2,1,1)
# width = [30, 10, 20, 50, 70]
# bars = ('6', '10', '8', '-2', '2')
# x_pos = np.arange(len(bars))
# plt.barh(x_pos, width, color=['gray', 'brown', 'blue', 'gray', 'brown'])
# plt.yticks(x_pos, bars)
# plt.title('Wykres górny')

# plt.subplot(2,1,2)
# N = 5
# left = (20, 10, 30, 10, 50)
# rigth = (25, 35, 15, 25, 25)
# ind = np.arange(N)
# height = 0.35

# plt.barh(ind, left, color=['gainsboro', 'slategrey', 'forestgreen', 'gray', 'palevioletred'])
# plt.barh(ind, rigth, left=left, color=['darkkhaki', 'darkkhaki', 'brown', 'cyan', 'red'])

# plt.title('Wykres dolny')
# plt.yticks(ind, ('A', 'B', 'C', 'D', 'E'))
# plt.xticks(np.arange(0, 101, 20))
# plt.tight_layout()
# #save
# plt.show()

# -------------------------------------

# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_excel('kina07.xlsx')
# miejskie = df[df["Gestor"] == "miejskie"]
# miejskie = miejskie[miejskie["Wykaz"] == "miejsca na widowni"]

# sizes = miejskie["Wartosc"]
# labels = miejskie["Rok"]
# colors = ['red', 'cyan', 'forestgreen']
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.0f%%', pctdistance=0.5, shadow=True, startangle=0)
# plt.title('Wykres kołowy')
# plt.annotate("XXXXXX",(1,-1))
# plt.axis('equal')
# plt.show()

# ------------------------------------

import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv('handel07.csv', sep=';', header=None).T
hipermar = dane[dane[0] == "hipermarkety"]
supermar = dane[dane[0] == "supermarkety"]
domtow = dane[dane[0] == "domy towarowe"]
plt.scatter(domtow[1], domtow[2], color='r', marker='o', s=100, label='Dom towarowy')
plt.scatter(hipermar[1], hipermar[2], color='g', marker='^', s=50, label=' Hipermarket')
plt.scatter(supermar[1], supermar[2], color='b', marker='>', s=25, label=' Supermarlet')
plt.xlabel('Wartość')
plt.ylabel('Rok')
plt.title('Cos')
plt.legend(title='Szkelpy', loc='lower center')
plt.show()
