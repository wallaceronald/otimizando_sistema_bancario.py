import textwrap

def menu(): 
    menu = """

*------- BEM-VINDO AO BANCO BSB -------*

Escolha qual operação deseja fazer :

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo usuario
[5] Nova conta
[6] Listar contas
[7] Sair

=> """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += (f'\nDepósito: R$ {valor:.2f}')
            print('\n===Depósito  realizado com sucesso! ===')
                        
    else:
        print('\n @@@Operação falhou. Digite um valor válido! @@@' )

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

        
    if excedeu_saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
        
    elif excedeu_limite:
        print ('Operação falhou o valor do saque excede o limite.')
        
    elif excedeu_saques: 
        print('Operação falhou! Número máximo de saques excedido')
        
    elif valor > 0: 
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print('Saque realizado com sucesso!')
    else:
        print('Operação Falhou! O valor é inválido.')
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n----------EXTRATO --------------')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('----------------------------------')

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input("Informe a data de nascimento )dd-mm-aaaa: ")
    endereco = input("Informa o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
         
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato - sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            

        elif opcao == "6":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
