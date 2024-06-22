# import matplotlib.pyplot as plt

# sizes = [27.2, 8.8, 28.1, 21.1, 14.9]
# sizes2 = [25.7, 21.2, 13.4, 12.8, 26.8]
# labels = ['A', 'B', 'C', 'D', 'E']
# colors = ['gray', 'lightyellow', 'yellow', 'red', 'green']
# colors2 = ['cyan', 'orange', 'brown', 'green', 'red']
# explode = (0, 0.1, 0, 0, 0)

# plt.subplot(2,1,1)
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=15)
# plt.title('Tytuł 1')
# plt.axis('equal')

# plt.subplot(2,1,2)
# plt.pie(sizes2, explode=explode, labels=labels, colors=colors2, autopct='%1.1f%%', shadow=True, startangle=30)
# plt.title('Tytuł 2')
# plt.axis('equal')
# plt.show()
# plt.savefig('wykres1.svg', format='svg')

#---------------------------------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_excel('ceny02.xlsx')
# jablka = df[df["Rodzaje towarów i usług"] == "jabłka - za 1kg"]
# cytryny = df[df["Rodzaje towarów i usług"] == "cytryny - za 1 kg"]

# plt.plot(jablka['Miesiące'], jablka['Wartosc'], linewidth=3, linestyle='dotted', color='cyan', label='jabłka')

# plt.plot(cytryny['Miesiące'], cytryny['Wartosc'], linewidth=3, linestyle='solid', color='gold', label='cytryny')

# plt.xlabel('Miesiące')
# plt.ylabel('Cena (w zł)')
# plt.xticks(rotation=45)
# plt.title('Cenny jabłek i cytryn w dawnych miesiącach')
# plt.tight_layout()
# plt.annotate('Najwyższy punkt', ('sierpień', 14), xytext=(4, 8), arrowprops=dict(facecolor = 'blue'))
# plt.legend()
# plt.show()
# plt.savefig('wykres2.webp', format='webp')

#---------------------------------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_excel('samochody02.xlsx', header=None).T
# df[1] = df[1].astype(int)
# df[2] = df[2].astype(int)
# pogroup = df.groupby([0, 1])[2].sum().unstack()
# pogroup.plot(kind='bar')
# plt.xticks(rotation=45)
# plt.xlabel('Typ pojazdu')
# plt.ylabel('Ilość')
# plt.title("Wykres słupkowy ilości pojazdów w latach 2017 i 2018")
# plt.tight_layout()
# plt.legend()
# plt.show()
# plt.savefig("wykres3.png")