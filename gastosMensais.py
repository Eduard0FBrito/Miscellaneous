def total_gasto(lista):
    total = 0
    for valor in lista:
        total += valor
    return total

def calcular_percentual(lista, total):
    percentuais = []
    for i in range(len(lista)):
        percentuais.append((100 * lista[i]) // total)
    return percentuais

def maior_gasto(lista):
    indice = 0
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice = i
    return indice

def menor_gasto(lista):
    indice = 0
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice = i
    return indice

def saldo_mensal(total, salario):
    diferença = salario - total
    return diferença

def entradaCasa(valorCasa, economia):
    entrada = (valorCasa*10) / 100
    mensalidade = (entrada - economia) / 12
    return mensalidade

# main
gastos = [0, 0, 0, 0, 0]
nomeGastos = ["Contas Fixas","Alimentação","Lazer","Vestuario","Outros Gastos"]
valorCasa = float(input("Qual o valor da casa que deseja comprar? "))
salario = float(input("\nQual o seu salario mensal? "))
continuar = True

print("\nVamos começar a computar as contas, digite o valor depois o codigo numerico para informar o tipo de gasto.")
print("Ps: O programa para de computar ao digitar um valor negativo.")
while continuar:
    valor = int(input("\nQual o valor da conta? "))
    if valor < 0:
        print("Você digitou um numero negativo, deseja encerrar o programa? S/N")
        opcao = input()
        while opcao != 'S' and opcao != 'N':
            print("Opção invalida, tente novamente!")
            opcao = input()
        if opcao == 'S':
            total = total_gasto(gastos)
            print(f"O valor total de gastos no mês é de: R${total:.2f}")
            percentual = calcular_percentual(gastos, total)
            for i in range(len(percentual)):
                print(f"O tipo de gasto {nomeGastos[i]} equivale a {percentual[i]}% dos gastos mensais")
            maiorGasto = maior_gasto(gastos)
            print(f"A categoria com maior gasto no mês foi: {nomeGastos[maiorGasto]} com um total de R${gastos[maiorGasto]:.2f}")
            menorGasto = menor_gasto(gastos)
            print(f"A categoria com menor gasto no mês foi: {nomeGastos[menorGasto]} com um total de R${gastos[menorGasto]:.2f}")
            saldoMensal = saldo_mensal(total, salario)
            mensalidade = 0
            if saldoMensal < 0:
                print(f"Faltou R${saldoMensal*-1} para pagar todas as contas.")
                mensalidade = entradaCasa(valorCasa, 0)
            elif saldoMensal == 0:
                print("Você conseguiu pagar todas as contas")
                mensalidade = entradaCasa(valorCasa, 0)
            else:
                print(f"Você economizou R${saldoMensal} nesse mês.")
                mensalidade = entradaCasa(valorCasa, saldoMensal)
            print(f"Desta forma se você economizar R${mensalidade:.2f} por mês conseguira o dinheiro necessario para dar entrada na casa dos sonhos")
            continuar = False
        else:
            print("Vamos voltar a computador os gastos então.")
    else:
        print("\n1 - Contas Fixas\n2 - Alimentação\n3 - Lazer\n4 - Vestuario\n5 - Outros Gastos")
        tipo = input("A qual tipo de gasto se refere esse valor? ")
        while not tipo.isnumeric() or int(tipo) < 1 or int(tipo) > 5:
            print("Opção invalida, tente novamente!")
            tipo = input("A qual tipo de gasto se refere esse valor? ")
        tipo = int(tipo)
        gastos[tipo - 1] += valor