from selenium_main import start_selenium, get_color, selenium_close, get_ref
import datetime
import time
import os
import config


def cls():
    os.system('cls')


start_selenium("https://gamdom.com/roulette")

presupuesto_inicial = config.presupuesto_inicial
apuesta_inicial = config.apuesta_inicial
color_apuesta = config.color_apuesta
presupuesto = config.presupuesto_inicial
apuesta = config.apuesta_inicial
ultima_ref = get_ref()
win = 0
lose = 0
hora_inicio = datetime.datetime.now()
h = 0
m = 0
s = 0

while True:
    cls()
    print('Dinero Inicial: '+str(presupuesto_inicial)+'€')
    print('Dinero Actual: '+str(round(presupuesto,2))+'€')
    print('\nApuesta Inicial: '+str(apuesta_inicial)+'€')
    print('Apuesta Actual: '+str(round(apuesta,2))+'€')
    print('\nÚltimo color: '+str(get_color()))
    print('Color al que se apuesta: '+color_apuesta)
    print('\nApuestas: '+str(win+lose))
    print('Victorias: '+str(win))
    print('Derrotas: '+str(lose))
    print('\nHora Inicio: '+str(hora_inicio))
    print('Tiempo transcurrido: '+str(h)+":"+str(m)+":"+str(s))

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
    if (apuesta > presupuesto):
        print('\nHas perdido, pringao, has tardado '+str(win+lose)+' tiradas')
        break
        # print('Te has quedado con '+str(presupuesto)+'€')

    time.sleep(3)

    s += 3

    if s >= 60:
        s -= 60
        m += 1
    if m >= 60:
        m -= 60
        h += 1
