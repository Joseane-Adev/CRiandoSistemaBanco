#variavel de visualização

menu ="""
"[1]--DEPOSITAR--"
"[2]--SACAR--"
"[3]--EXTRATO--"
"[4]--SAIR--"

"""

#variavel de saldo
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#condiçoes

while True:

    opcao = input("Escolha uma opção: " + menu)

    if opcao == '1':
        valor = float(input("Quanto você quer depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"Seu depósito é de: R$ {valor:.2f} - Depósito realizado com sucesso!\n"
        else:print('Digite um valor válido!')  

    elif opcao == '2':

        saque = float(input("Quanto você quer sacar? "))

        excedeu_saque = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >+ LIMITE_SAQUES
    
        if excedeu_saque:
            print("Você não tem saldo suficiente!")
        elif excedeu_limite:
            print("Você não excedeu o limite de saque!")
        elif excedeu_saque:
            print("Você atingiu o limite de saque por dia!")
        
        elif valor > 0:
            #diminui no saldo atual
            saldo -= saque
            #acrescenta saque no extrato
            extrato += f'Seu saque é de: R$: {saque}'
            #contar o numeo de saques
            numero_saques += 1
        else:
            print("Digite um valor válido para saque!")
        

    elif opcao == '3':

        print("---Extrato---")
        print("Não foram feitas movimentações." if not extrato else extrato)
        print(f'Seu saldo é de: R$:{saldo}')
        print("--------------------")
       
    elif opcao == '4':
        
        print("Obrigada por acessar nosso banco. Volte sempre!")
        break
    else:
        print('OPÇÃO INVÁLIDA!')



