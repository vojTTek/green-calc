import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import PySimpleGUI as sg
import matplotlib.pyplot as plt
naslonecznienie=float(1050.00) #stałe
mocowa=float(76.20)
kWp=int(3600)
panel=int(450)
def pros(systemPV, zuzycie): #prosument2020
    overka=systemPV-zuzycie
    global nadprodukcja
    global prosument
    if systemPV <=10:
        prosument=float(0.8)
        if overka>0:
            nadprodukcja=overka*prosument
        else:
            nadprodukcja=0
    elif systemPV <=50:
        prosument=float(0.7)
        if overka>0:
            nadprodukcja=overka*prosument
        else:
            nadprodukcja=0
    else:
        prosument=float(1)
        if overka>0:
            nadprodukcja=overka*prosument
        else:
            nadprodukcja=0
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg
sg.theme('LightGreen3') #layout programu
dane_proste = [[sg.T('Program oblicza szacunkowe dane')],
          [sg.Text('Jaka wielkość instalacji fotowoltaicznej (kWp)?')],
          [sg.Input(key='-IN1-', enable_events=True)], 
          [sg.Text('Podaj średnią stawkę za MWh')],
          [sg.Input(key='-IN2-', enable_events=True)],
          [sg.Text('Podaj średnie roczne zużycie w MWh')],
          [sg.Input(key='-IN3-', enable_events=True)]]
layout = [
          [sg.Frame(layout=[   
          [sg.Radio('Prosument', 'rozliczenie', key='prosument'), sg.Radio('Wytwórca','rozliczenie', key='wytwórca')]], title='Typ rozliczenia instalacji',title_color='green', relief=sg.RELIEF_SUNKEN)],  
          [sg.TabGroup([[sg.Tab('Wprowadź dane kalkulacji', dane_proste)]])],        
          [sg.Text('Efekty obliczeń:')],
          [sg.MLine(key='wynik'+sg.WRITE_ONLY_KEY, size=(80,10))],
           [sg.Canvas(key="-CANVAS-")],#przemyśleć jak to przesunąć w inne miejsce
          [sg.Button('Przelicz'), sg.Button('App info'), sg.Button('Wyjście')]
         ]
window = sg.Window('green-calc.tech 1.0.2', layout)#, margins=(100, 100), finalize=True)    #rozmiar okna
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
      zuzycie=float(values['-IN3-'])
      cena=float(values['-IN2-'])
      pros(systemPV, zuzycie)
      prosty=(systemPV*kWp) 
      ile_paneli=float(systemPV/(panel/1000))
      ile_miejsca=float(ile_paneli*1.7)
      produkcja=systemPV*naslonecznienie/1000
      mocowap=float(mocowa*produkcja*0.625)
      dodo=float(nadprodukcja*247.50)
      minicalc=float(produkcja*cena)
      roip=float(prosty/(mocowap+minicalc))
      miesiecznie = [3.05, 4.74, 8.10, 10.57, 14.26, 13.49, 14.14, 12.69, 8.43, 5.26, 2.90, 2.37]
      Kalendarz = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
      wykres = []
      for i in range(len(miesiecznie)):
        wykres.append(miesiecznie[i]*systemPV/100)
      fig = matplotlib.figure.Figure(figsize=(4, 3), dpi=100)
      t = np.arange(0, 3, .01)
      fig.add_subplot(111).plot(Kalendarz, wykres)
      if values['prosument']==True:
        window['wynik'+sg.WRITE_ONLY_KEY].print('Rozliczenie jako prosument')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacowany koszt instalacji fotowoltaicznej wynosi:', round(prosty, 2), 'zł')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja pozwoli Ci na wykorzystanie:', round(produkcja, 2), 'MWh')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja wymaga:', round(ile_paneli, 0), 'paneli')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja wymaga:', round(ile_miejsca, 1), 'm2')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja pozwoli Ci rocznie oszczędzić na zakupach energii:', round(minicalc, 2), 'zł')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja pozwoli Ci rocznie oszczędzić na opłacie mocowej:', round(mocowap, 2), 'zł')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja zwróci się po:', round(roip, 2), 'latach')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowa nadprodukcja energii wynosi', round(nadprodukcja, 2), 'MWh')
        draw_figure(window["-CANVAS-"].TKCanvas, fig)
      elif values['wytwórca']==True:
        window['wynik'+sg.WRITE_ONLY_KEY].print('Rozliczenie jako wytwórca')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacowany koszt instalacji fotowoltaicznej wynosi:', round(prosty, 2), 'zł')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja pozwoli Ci na wykorzystanie:', round(produkcja, 2), 'MWh')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja wymaga:', round(ile_paneli, 0), 'paneli')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja wymaga:', round(ile_miejsca, 1), 'm2')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja pozwoli Ci rocznie oszczędzić na zakupach energii:', round(minicalc, 2), 'zł')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja pozwoli Ci rocznie oszczędzić na opłacie mocowej:', round(mocowap, 2), 'zł')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowo twoja instalacja zwróci się po:', round(roip, 2), 'latach')
        window['wynik'+sg.WRITE_ONLY_KEY].print('Szacunkowa sprzedaż nadprodukcji energii wygeneruje', round(dodo, 2), 'zł')
        draw_figure(window["-CANVAS-"].TKCanvas, fig)
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
