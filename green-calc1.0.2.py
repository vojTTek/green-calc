from subprocess import check_call #biblioteki
import sys
from tkinter.constants import X
import PySimpleGUI as sg
mocowa=float(76.20) #stałe
kWp=int(3600)
panel=int(450)
taryfy=('A', 'B', 'C', 'G')
def pros(systemPV): #prosumen2020
  global prosument
  if systemPV <=10:
    prosument=float(0.8)
#    window['wynik'+sg.WRITE_ONLY_KEY].print('Współczynnik rozliczenia 0,8\n')
  elif systemPV <=50:
    prosument=float(0.7)
#    window['wynik'+sg.WRITE_ONLY_KEY].print('Współczynnik rozliczenia 0,7\n')
  else:
    prosument=float(1)
#    window['wynik'+sg.WRITE_ONLY_KEY].print(''' Brak możliwości rozliczenia jako prosument,
#Wybudowanie instalacji wymaga pozyskania:
#- warunków przyłączeniowych (120 dni).
#- przygotowania projektu (120 dni).
#- wybudowania instalacji (150 dni).
#- mogą pojawić się dodatkowe koszty.''')
sg.theme('LightGreen3') #layout programu
dane_proste = [[sg.T('Metoda wstępna, bazuje na niewielkiej ilości danych. Jest ona mniej dokładna')],
          [sg.Text('Jaka wielkość instalacji fotowoltaicznej (kWp)?')],
          [sg.Input(key='-IN1-', enable_events=True)], 
          [sg.Text('Podaj średnią stawkę za MWh')],
          [sg.Input(key='-IN2-', enable_events=True)],
          [sg.Text('Podaj średnie zużycie energii')],
          [sg.Input(key='-IN3-', enable_events=True)]]
dane_zaawansowane = [[sg.T('Zostanie dodane w wersji 1.0.3')], 
          [sg.Text('Wybierz taryfę:')],
          [sg.InputCombo((taryfy), size=(20, 1))]]
ustawienia_aplikacji = [[sg.T('Zostanie dodane w wersji 1.0.3')]]
layout = [
          [sg.Frame(layout=[   
            [sg.Radio('Prosument', 'rozliczenie', key='prosument'), sg.Radio('Wytwórca','rozliczenie', key='wytwórca')]], title='Typ rozliczenia instalacji',title_color='green', relief=sg.RELIEF_SUNKEN)],  
          [sg.TabGroup([[sg.Tab('Prosta kalkulacja', dane_proste), sg.Tab('Zaawansowana kalkulacja', dane_zaawansowane), sg.Tab('Zmień dane startowe', ustawienia_aplikacji)]])],       
          [sg.Text('Efekty obliczeń:')],
          [sg.MLine(key='wynik'+sg.WRITE_ONLY_KEY, size=(40,8))],
          [sg.Button('Przelicz'), sg.Button('App info'), sg.Button('Wyjście')]
         ]
window = sg.Window('green-calc.tech 1.0.2', layout, margins=(100, 100), finalize=True)    #rozmiar okna
while True:                             #wydarzenia
    event, values = window.read()
    if event==sg.WIN_CLOSED or event=='Wyjście':
      break
    if event=='-IN1-' and values['-IN1-'] and values['-IN1-'][-1] not in ('0123456789.'):
      window['-IN1-'].update(values['-IN1-'][:-1])
    elif event=='-IN2-' and values['-IN2-'] and values['-IN2-'][-1] not in ('0123456789.'):
      window['-IN2-'].update(values['-IN2-'][:-1])
    elif event=='-IN3-' and values['-IN3-'] and values['-IN3-'][-1] not in ('0123456789.'):
      window['-IN3-'].update(values['-IN3-'][:-1])
    elif event=='Przelicz':
      systemPV=float(values['-IN1-'])
      cena=float(values['-IN2-'])
      zuzycie=float(values['-IN3-'])
      (pros(systemPV))
      prosty=(systemPV*kWp) 
      ile_paneli=float(systemPV/(panel/1000))
      ile_miejsca=float(ile_paneli*1.7)
      dostepp=float(systemPV*prosument)
      mocowap=float(mocowa*dostepp*0.625)
      minicalc=float(dostepp*cena)
      roip=float(prosty/(mocowap+minicalc))
      if values['prosument']==True:
        window['wynik'+sg.WRITE_ONLY_KEY].print('Rozliczenie jako prosument')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacowany koszt instalacji fotowoltaicznej wynosi:', round(prosty, 2), 'zł')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja pozwoli Ci na wykorzystanie:', round(dostepp, 2), 'MWh')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja wymaga:', round(ile_paneli, 0), 'paneli')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja wymaga:', round(ile_miejsca, 1), 'm2')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja pozwoli Ci rocznie oszczędzić na zakupach energii:', round(minicalc, 2), 'zł')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja pozwoli Ci rocznie oszczędzić na opłacie mocowej:', round(mocowap, 2), 'zł')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja zwróci się po:', round(roip, 2), 'latach')
      elif values['wytwórca']==True:
        window['wynik'+sg.WRITE_ONLY_KEY].print('zostanie dodane w wersji 1.0.3')
    elif event=='App info':
      sg.Popup((''' 
    green-calc.tech
    Pomaga oszacować instalację PV |
    versja 1.0.2 (08.2021) 
    by VojTTek
    Aplikacja jest projektem, który prowadzę w ramach nauki
    programowania w języku Python. Cel projektu to wsparcie
    wyceny instalacji fotowoltaicznej realizowanj w Polsce.
    - naukę Pythona rozpocząłem 27.07.2021 roku.'''))
window.close()