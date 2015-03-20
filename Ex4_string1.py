str = raw_input("Digite a palavra: ")
resp=""
for i in range(len(str)):
  resp+=str[-(i+1)]
print resp
