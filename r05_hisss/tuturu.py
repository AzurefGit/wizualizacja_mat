# import matplotlib.pyplot as plt


# labels = ['a', 'b', 'c', 'd', 'e']
# colors = ['grey', 'brown', 'cyan', 'violet', 'orange']
# fig, (ax1, ax2)= plt.subplots(2, 1)
# ax1.pie([10.80, 32.22, 29.99, 17.19, 9.80], explode=(0, 0, 0.2, 0, 0), labels=labels, colors=colors, autopct='%1.2f%%', startangle=45)
# plt.axis('equal')


# ax2.pie([13.5, 23.7, 28.8, 23.1, 10.9], explode=(0, 0, 0.4, 0, 0.1), labels=labels, colors=colors, autopct='%1.1f%%', startangle=30)
# plt.axis('equal')
# plt.savefig('mbappe.webp')
# plt.show()
# --------------------------------

# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_excel('ceny5.xlsx')
# pstrag = df[df["Rodzaje produktów"]=="pstrąg świeży niepatroszony - za 1 kg"]
# filet = df[df["Rodzaje produktów"] == "filety z morszczuka mrożone - za 1kg"]
# sledz = df[df["Rodzaje produktów"] == "śledź solony, niepatroszony - za 1kg"] 

# plt.scatter(pstrag["Rok"], pstrag["Wartosc"], color='r', marker='*', label='pstrąg', s=200)
# plt.scatter(filet["Rok"], filet["Wartosc"], color='forestgreen', marker='p', label='filet', s=50)
# plt.scatter(sledz["Rok"], sledz["Wartosc"], color='cyan', marker='o', label='śledź', s=300)
# plt.grid()
# plt.xlabel('Rok')
# plt.ylabel('Wartość')
# plt.title("Wykres z cenami ryb")
# plt.text(2015,15.3,"XXXXXX")
# plt.legend(title='Ceny ryb')
# plt.savefig('skot.png')
# plt.show()

# --------------------------------

# import matplotlib.pyplot as plt
# import pandas as pd

# dane = pd.read_csv('cechy5.csv', sep=';')
# dane = dane.replace(',','.',regex=True).astype(float)
# cecha1 = dane["Cecha1"]
# plt.hist(cecha1, bins=6, color='cyan')
# plt.xlabel("Wartość cechy")
# plt.ylabel("Liczba obserwacji")
# plt.grid()
# plt.legend(['Pierwsza cecha'])
# plt.title('Histogram')
# # plt.savefig('smutek.jpg')
# plt.show()