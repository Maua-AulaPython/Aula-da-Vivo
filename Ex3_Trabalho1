from math import *

def Polares(P1, P2):
    P1 = P1.split(',')
    P2 = P2.split(',')
    x1 = float(P1[0])
    y1 = float(P1[1])
    x2 = float(P2[0])
    y2 = float(P2[1])
    mod1 = (x1**2+y1**2)**0.5
    mod2 = (x2**2+y2**2)**0.5
    teta1 = atan2(y1,x1)*180/pi
    teta2 = atan2(y2,x2)*180/pi
    print '''O primeiro ponto eh {0}|{1}
O segundo ponto eh {2}|{3}'''.format(mod1, teta1, mod2, teta2)

P1 = raw_input("Digite as coordenadas do primeiro ponto no formato x,y: ")
P2 = raw_input("Digite as coordenadas do segundo ponto no formato x,y: ")
Polares(P1, P2)
