from selenium_main import start_selenium, get_color, selenium_close, get_ref
import time
import os

def cls():
    os.system('cls')

start_selenium("https://gamdom.com/roulette")

presupuesto_inicial = 10
presupuesto = presupuesto_inicial
color_apuesta = 'red'
apuesta_inicial = 0.5
apuesta = apuesta_inicial
ultima_ref = get_ref()
win = 0
lose = 0

while True:
    cls()
    print('Dinero Inicial: '+str(presupuesto_inicial)+'€')    
    print('Dinero Actual: '+str(presupuesto)+'€')
    print('Apuesta Inicial: '+str(apuesta_inicial)+'€')
    print('Apuesta Actual: '+str(apuesta)+'€')
    print('\nÚltimo color: '+str(get_color()))
    print('Color al que se apuesta: '+color_apuesta)
    print('\nVictorias: '+str(win))
    print('Derrotas: '+str(lose))

    ref = get_ref()
    
    if (ref != ultima_ref):
        if get_color() == color_apuesta:
            presupuesto += apuesta
            win += 1
            apuesta = apuesta_inicial
        else:
            presupuesto -= apuesta
            apuesta *= 2
            lose += 1
        ultima_ref = ref
    if (apuesta > presupuesto_inicial):
        print('\nHas perdido, pringao, has tardado '+str(win+lose)+' tiradas')
        print('Te has quedado con '+presupuesto+'€')
    time.sleep(3)