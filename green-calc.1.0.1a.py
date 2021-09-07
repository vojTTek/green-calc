import matplotlib.pyplot as plt
naslonecznienie=float(1050.00)
mocowa=float(76.20)
kWp=int(3600)
panel=int(450)
def pros(systemPV):
    global prosument
    if systemPV <=10:
        prosument=float(0.8)
    elif systemPV <=50:
        prosument=float(0.7)
    else:
        prosument=float(1) 
print('''

                       +================================+
                       |            green-calc.TECH     |
                       | Pomaga oszacować instalację PV |
                       |      versja 1.0.1a (09.2021)   |
                       +================================+
                                             by VojTTek
            Aplikacja jest projektem, który prowadzę w ramach nauki
            programowania w języku Python. Cel projektu to wsparcie
            wyceny instalacji fotowoltaicznej realizowanj w Polsce.
            - naukę Pythona rozpocząłem 27.07.2021 roku. 
    ''')
print('wybierz 1 by rozpocząć')
while True:
    try:
        rozpocznij=int(input())
        break
    except ValueError:
        print('popraw dane')
if rozpocznij==1:
    print('Jakiej wielkości instalacja  (kWp) fotowoltaiczna Cię interesuje?') 
    while True:
        try:
            systemPV=int(input())
            break
        except ValueError:
            print('popraw dane')
    pros(systemPV)
    print('Podaj średnią stawkę za MWh')
    while True:
        try:
            cena=float(input())
            break
        except ValueError:
            print('popraw dane')
    prosty=(systemPV*kWp) 
    ile_paneli=float(systemPV/(panel/1000))
    ile_miejsca=float(ile_paneli*1.7)
    produkcja=systemPV*naslonecznienie/1000
    dostepp=float(produkcja*prosument)
    mocowap=float(mocowa*dostepp*0.625)
    minicalc=float(dostepp*cena)
    roip=float(prosty/(mocowap+minicalc))
    miesiecznie = [3.05, 4.74, 8.10, 10.57, 14.26, 13.49, 14.14, 12.69, 8.43, 5.26, 2.90, 2.37]
    Kalendarz = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    wykres=[]
    for i in range(len(miesiecznie)):
        wykres.append(miesiecznie[i]*systemPV/100)
    print('Szacowany koszt instalacji fotowoltaicznej wynosi:', round(prosty, 2), 'zł')
    print('Szacunkowo twoja instalacja pozwoli Ci na wykorzystanie:', round(dostepp, 2), 'MWh')
    print('Szacunkowo twoja instalacja wymaga:', round(ile_paneli, 0), 'paneli')
    print('Szacunkowo twoja instalacja wymaga:', round(ile_miejsca, 1), 'm2')
    print('Szacunkowo twoja instalacja pozwoli Ci rocznie oszczędzić na zakupach energii:', round(minicalc, 2), 'zł')
    print('Szacunkowo twoja instalacja pozwoli Ci rocznie oszczędzić na opłacie mocowej:', round(mocowap, 2), 'zł')
    print('Szacunkowo twoja instalacja zwróci się po:', round(roip, 2), 'latach')
    plt.bar(Kalendarz, wykres, color='purple')
    plt.title('Wykres produkcji miesięcznej')
    plt.xlabel('miesiące')
    plt.ylabel('produkcja (MWh)')
    plt.show()
    if prosument<1:
        print('Wybudowanie twojej instalacji potrwa około 1 miesiąca')
    else:
        print('''Wybudowanie instalacji wymaga pozyskania:
        - warunków przyłączeniowych (120 dni).
        - przygotowania projektu (120 dni).
        - wybudowania instalacji (150 dni).
        - mogą pojawić się dodatkowe koszty, wykonaj szacunek zaawansowany.
        ''')
else:
    exit()
