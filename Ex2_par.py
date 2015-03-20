def Par(N):
	if (N%2==0):
		return('par')
	else:
		return('impar')

N = int(raw_input('Digite o numero a ser testado: '))
print(Par(N))
