entradaPassos = input()
entradaPassos = int(entradaPassos)
if(entradaPassos<1):
    print("Nenhum passo dado na floresta.")
else:
    for i in range(1,entradaPassos + 1):
       if(i == 1):
           print(f"Explorador: {i} passo")
       else:
           print(f"Explorador: {i} passos")