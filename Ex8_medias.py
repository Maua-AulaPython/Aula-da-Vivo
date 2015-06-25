import sys
nota=0
tot=0
num=0
j = []
notam = 0
notalist = []
while(nota>=0):
    while True:
        try:
              nota=float(raw_input("digite a nota (para sair digite um numero negativo): "))
              break
        except:
            print '\nNao foi um numero valido\n'
    if(nota>=0):
        notalist.append(nota)
        num+=1
for i in range(num):
    if notam < notalist[i]:
        j=[]
        notam = notalist[i]
        j.append(i+1)
    elif notam == notalist[i]:
        j.append(i+1)
    tot+=notalist[i]

if num != 0:
    print "\nO(s) aluno(s) {1} obteve a maior nota: {0}, e a media da sala foi: {2}\n".format(notam, j, round(tot/num, 2))
else:
    print '\nVoce nao digitou nenhuma nota\n'

#Nota: 1.0
#Comentario: **
