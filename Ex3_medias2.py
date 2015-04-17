nota=0
tot=0
num=0
while(nota>=0):
  nota=int(raw_input("digite a nota: "))
  if(nota>=0):
    notalist.append(nota)
    num+=1
for i in range(num):
  tot+=notalist[i]
tot=tot/num
ptint("a media do aluno e: {0}".format(tot))


# Nota: 0
# Comentario: programa nao executa
