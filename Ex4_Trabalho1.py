def Verifica(A, B, C):
    if (C**2 == A**2+B**2):
        print 'A area vale {0}!'.format(A*B/2)
    else:
        print 'Os valores A = {0}, B = {1}, C = {2} nao formam um triangulo retangulo!'.format(A, B, C)

A = int(raw_input('Digite o primeiro cateto: '))
B = int(raw_input('Digite o segundo cateto: '))
C = int(raw_input('Digite a hipotenusa: '))
if (C>A+B):
    print('Nao eh um triangulo!')
else:
    Verifica(A, B, C)

# Nota: 0.5
# Algoritmo incorreto na função
