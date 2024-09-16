
entrada = input().split()
capacidade_atual = int(entrada[0])
aumento_percentual = int(entrada[1])


nova_capacidade = capacidade_atual * (1 + aumento_percentual / 100)



print(int(nova_capacidade))
