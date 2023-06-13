"""
Deposito
Saque
Extrato

Valores positivos

Depositos armazenados em uma variável para serem exibidos no Extrato

3 saques diarios com limite de R$500,00 por saque
"""
saldo = 2000.00

LIMITE_SAQUE = 501.00
LIMITE_SAQUES_NO_DIA = 2
count = 0

while True:
    opcao = input("Escolha a operação desejada: \n[1]Saque: \n[2]Depósito: \n[3]Extrato: \n[4]Sair: \n")
    opcao = float(opcao)

    if opcao == 1:
        saque = input("Digite um valor a ser retirado:")
        saque = float(saque)

        if saque >= LIMITE_SAQUE:
            print("Limite de saque ultrapassado!")
        elif count > LIMITE_SAQUES_NO_DIA:
            print('Não é possível fazer novos saques. Tente novamente amanhã.')
        elif saque <= saldo and count <= LIMITE_SAQUES_NO_DIA:
            print("Saque realizado com sucesso, retire seu dinheiro abaixo!")
            count = count + 1
            saldo = saldo - saque
        else:
            print("Saldo insuficiente para o valor digitado!")
   
    elif opcao == 2:
        deposito = input("Digite o valor a ser depositado:")
        deposito = float(deposito)

        saldo = saldo + deposito

        if deposito <= 0:
            print("Valor impossivel de ser depositado!")

    elif opcao == 3:
        extrato = print(saldo)

    elif opcao == 4:
        print("Obrigado por utilizar nossos serviços!")
        break
