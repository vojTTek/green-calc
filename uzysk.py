import matplotlib.pyplot as plt
naslonecznienie=float(950.00)
def pros(x):
    global prosument
    if x <=10:
        prosument=float(0.8)
    elif x <=50:
        prosument=float(0.7)
    else:
        prosument=float(1)
print('Prosty Generator uzysku PV')
print('Podaj wielkość instalacji w kWp')
wielkosc=float(input())
produkcja=wielkosc*naslonecznienie/1000
pros(produkcja)
system=wielkosc*prosument
print('mozliwy uzysk:', produkcja, ' MWh' )
print('Dla prosumenta do wykorzystania zostanie:', system, ' MWh/rok' )
miesiecznie = [3.05, 4.74, 8.10, 10.57, 14.26, 13.49, 14.14, 12.69, 8.43, 5.26, 2.90, 2.37]
Kalendarz = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']
wykres=[]
print(wykres)
for i in range(len(miesiecznie)):
    wykres.append(miesiecznie[i]*system/100)
print(wykres)
plt.scatter(Kalendarz, wykres)
plt.show()
