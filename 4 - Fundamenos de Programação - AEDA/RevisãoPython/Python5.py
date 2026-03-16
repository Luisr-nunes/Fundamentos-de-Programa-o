horasDeExercicio = float(input("Informe a quantidade de horas exercitadas no mês: "))

if horasDeExercicio < 10:
    print(f"Seus pontos totais foram: {horasDeExercicio * 2}")
elif horasDeExercicio < 20:
    print(f"Seus pontos totais foram: {horasDeExercicio * 5}")
else:
    print(f"Seus pontos totais foram: {horasDeExercicio * 10}")

