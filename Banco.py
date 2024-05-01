extrato = " "
saldo = 0
limite_deposito = 10000
limite_sacar = 500
numero_saques = 0
LIMITE_SAQUE = 3

print("----------------------")
print(" \n Bem Vindo ao Banco \n")
print("----------------------")

while True:
    opcao=int(input("\n Escolha uma opção\n \n 1)Depositar \n 2)Sacar \n 3)Ver extrato \n 0) Sair \n "))
    
        #Depositar

    if opcao ==1:
        valor = float(input("Quanto voce quer depositar ?\n"))
        excedeu_limite_deposito = valor > limite_deposito

        if excedeu_limite_deposito:
            print("O valor limite do depósito é %d "%(limite_deposito))

        elif valor > 0:
            saldo += valor
            extrato +=  f"Depósito: R${valor:.2f}\n"      
        
        else:
            print("\n Operação falhou, valor inválido")    



        #Sacar

    elif opcao == 2:
        print("Sacar")

        valor = float(input("Quanto voce deseja sacar ?\n "))

        excedeu_saldo= valor > saldo

        excedeu_limite= valor > limite_sacar
        
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("\n Saldo insuficiente")

        elif excedeu_limite:
            print("\n Limite maximo para o saque R$%d"%(limite_sacar))

        elif excedeu_saques:
            print("\n Máximo de saques possivel")
        
        elif valor > 0:
            saldo -= valor
            extrato +=  f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("\n O valor informado é inválaido")
        

        #Ver extrato

    elif opcao == 3:
        
        print("----EXTRATO----")
        print("Não houve movimentação na conta " if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("---------------")

        #Sair

    elif opcao == 0:
        print("\nSaindo... \nObrigado pela preferência!\n")
        break

    else:
        print("Opção inválida, por favor tente novamente.")