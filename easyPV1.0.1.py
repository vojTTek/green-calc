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
def taryfikatory():
    global taryfikator
    taryfikator = ('A21', 'A22', 'A23', 'B21', 'B22', 'B23','B11', 'C21', 'C22a', 'C23', 'C11', 'C12a', 'C13', 'G11', 'G12w', 'G13')
    global taryfikator2
    taryfikator2 = ('G12', 'G12as', 'C22b', 'C12b')
print('''

                       +================================+
                       |            EASYPV.PL           |
                       | Pomaga oszacować instalację PV |
                       |      versja 1.0.1 (08.2021)    |
                       +================================+
                                             by VojTTek
            Aplikacja jest projektem, który prowadzę w ramach nauki
            programowania w języku Python. Cel projektu to wsparcie
            wyceny instalacji fotowoltaicznej realizowanj w Polsce.
            - naukę Pythona rozpocząłem 27.07.2021 roku. 
    Wybierz:
1. Proste szacowanie instalacji PV.
2. Proste szacowanie instalacji PV.
   Wybierz inną liczbę aby zakończyć. 
''')
try:
    rozpocznij=int(input())
except ValueError:
    print('popraw dane')
    rozpocznij=int(input())
print(rozpocznij)
if rozpocznij==1:
    print('Jakiej wielkości instalacja  (kWp) fotowoltaiczna Cię interesuje?') 
    pros(systemPV)
    print('Podaj średnią stawkę za MWh')
    try:
        cena=float(input())
    except ValueError:
        print('popraw dane')
        cena=int(input())
    prosty=(systemPV*kWp) 
    ile_paneli=float(systemPV/(panel/1000))
    ile_miejsca=float(ile_paneli*1.7)
    dostepp=float(systemPV*prosument)
    mocowap=float(mocowa*dostepp*0.625)
    minicalc=float(dostepp*cena)
    roip=float(prosty/(mocowap+minicalc))
    print('Szacowany koszt instalacji fotowoltaicznej wynosi:', round(prosty, 2), 'zł')
    print('Szacunkowo twoja instalacja pozwoli Ci na wykorzystanie:', round(dostepp, 2), 'MWh')
    print('Szacunkowo twoja instalacja wymaga:', round(ile_paneli, 0), 'paneli')
    print('Szacunkowo twoja instalacja wymaga:', round(ile_miejsca, 1), 'm2')
    print('Szacunkowo twoja instalacja pozwoli Ci rocznie oszczędzić na zakupach energii:', round(minicalc, 2), 'zł')
    print('Szacunkowo twoja instalacja pozwoli Ci rocznie oszczędzić na opłacie mocowej:', round(mocowap, 2), 'zł')
    print('Szacunkowo twoja instalacja zwróci się po:', round(roip, 2), 'latach')
    if prosument<1:
        print('Wybudowanie twojej instalacji potrwa około 1 miesiąca')
    else:
        print('''Wybudowanie instalacji wymaga pozyskania:
        - warunków przyłączeniowych (120 dni).
        - przygotowania projektu (120 dni).
        - wybudowania instalacji (150 dni).
        - mogą pojawić się dodatkowe koszty, wykonaj szacunek zaawansowany.
        ''')
elif rozpocznij==2:
        taryfikatory()                                                                                                                                                                                                                                                                                                                                                                  
        print('Podaj taryfę. Pamiętaj, że oznaczenie zaczyna się dużą literą')
        taryfa=str(input())
        while True:
            if taryfa in taryfikator:
                strefa=int(taryfa[2])
                profil(strefa, 0)
                break
            elif taryfa in taryfikator2:
                strefa=int(taryfa[2])
                profil(strefa, 1)
                break
            else:
                print('Popraw taryfę.')
                taryfa=str(input())
                break
else:
    exit()
