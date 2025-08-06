import textwrap
#variavel de visualização
def menu():

    menu ="""
     
        "[1]--DEPOSITAR--"
        "[2]--SACAR--"
        "[3]--EXTRATO--"
        "[4]--Criar Conta--"
        "[5]--Listar Contas--"
        "[6]--Novo usuário--"
        "[7]--SAIR--"

    """
    # Exibe o menu e solicita a opção do usuário
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato, /):
    if valor >0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print("\n Depósito realizado com sucesso!")
    else:
        print("Operação falhou! Valor informado inválido!")
    
    return saldo, extrato

#parametros nomeados
#usando o * para indicar que os parametros devem ser nomeados
def sacar(*, saldo,valor,extrato, limite, numero_saques, limite_saques,limite_saque):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saque
            
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente!")    
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite!")         
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido!") 
    
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print("\n Saque realizado com sucesso!")
    else:
        print("Operação falhou! Valor informado inválido!") 
    
    return saldo, extrato

def exibir_extrato(saldo, /,*, extrato):

    
    print("---Extrato---")
    print("Não foram feitas movimentações." if not extrato else extrato)
    print(f'Seu saldo é de: R$:{saldo}')
    print("--------------------")

def criar_user(usuarios):

    cpf = input("Informe o CPF(SOMENTE NÚMEROS): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe o endereço (Rua, Número - Bairro - Cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })  
    print("Usuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
          print("*\n Conta criada com sucesso!")
          return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    print("Usuário não encontrado! Conta não criada.")

def filtrar_usuarios(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_contas(contas):
      for conta in contas:
          linha = f"""
          Agência: {conta['agencia']}
          Número da Conta: {conta['numero_conta']}
          Usuário: {conta['usuario']['nome']}
          """
          print("=" * 100)
          print(textwrap.dedent(linha)) 


def main():

    #constantes
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    #variavel de saldo
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    contas = []
    usuarios = []

    #condiçoes

    while True:

        opcao = menu()

        if opcao == '1':
            valor = float(input("Quanto você quer depositar? "))
            saldo, extrato = depositar(valor,saldo, extrato) 
        elif opcao == '2':

            saque = float(input("Quanto você quer sacar? "))

            #passagem de argumnetos da funçao sacar
            saldo,extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
                
            )
        
        elif opcao == '3':

            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == '4':
            
            criar_user(usuarios)
        
        elif opcao == '5':
            numero_conta = len(conta) + 1
            conta = criar_conta( AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '6':
            listar_contas(contas)
        elif opcao == '7':
            print("Obrigado por usar nosso sistema!")
            break
        else:
            print("Operação inválida, tente novamente!")


main()
#chamada da função- main