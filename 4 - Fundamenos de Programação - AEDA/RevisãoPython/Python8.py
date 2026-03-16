
diasproduzidos = float(input("Informe a quantidade de dias produzidos: "))
qntproduzida = float(input("Informe a produção dos dias: "))

mediaproducaodia = qntproduzida / diasproduzidos

if mediaproducaodia < 1000:
    print(f"Sua média de produção no periodo foi de: {mediaproducaodia}, isso é uma BAIXA PRODUÇÃO")
elif mediaproducaodia < 2000:
    print(f"Sua média de produção no periodo foi de: {mediaproducaodia}, isso é uma PRODUÇÃO SATISFATÓRIA")
else:
    print(f"Sua média de produção no periodo foi de: {mediaproducaodia}, isso é uma PRODUÇÃO EXCELENTE")
