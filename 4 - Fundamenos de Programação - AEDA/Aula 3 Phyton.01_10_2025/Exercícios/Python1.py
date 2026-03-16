
cont1 = cont2 = 0

for x in range (10):
    quant = int(input("Informe a sua quantidade de filhos: "))

    if (quant<=2):
        cont1=cont1+1
    else:
        cont2=cont2+2

print("Maior igual a 2 filhos", cont1)
print("Maior que Dois filhos", cont2)

