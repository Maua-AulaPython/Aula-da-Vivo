from math import *

def DistanciaEntrePontos (P1):
    dant = 0
    x1 = []
    y1 = []
    pts = []
    x=0
    y=0
    d=0
    for n in range(len(P1)):
        pts.append(P1[n].split(','))
        x1.append(float(pts[n][0]))
        y1.append(float(pts[n][1]))
    for n in range(len(P1)):
        for i in range (len(P1)):
            x = x1[n] - x1[i]
            y = y1[n] - y1[i]
            d =((x)**2+(y)**2)**0.5
            if (d>dant):
                dant = d
    return (dant)
    
P1 = []
aux = ''
while(aux!='fim'):
    aux = (raw_input("Digite as coordenadas do ponto no formato x,y(caso queira parar digite fim): "))
    if (aux == 'fim'): break
    P1.append(aux)
d = DistanciaEntrePontos(P1)
print ('A maior distancia eh {0}'.format(d))
