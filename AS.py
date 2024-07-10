#adicionado menu em 03 07 10 horas
#implementado menu com pass, pronto para ser codado
#adicionando opção de excluir conta no menu as 11:00 horas 03/07/2024
#alteração na ordem das funções as 19:10 horas 03/07

# Dicionário para armazenar usuários
usuarios = {}

# Dicionário para armazenar contas correntes
contas = {}

def cadastrar_usuario(nome, cpf): #alteramos a função, retiramos o if e o else, deixando apenas a função por si só
        usuarios[cpf] = {"nome": nome, "cpf": cpf}
        contas[cpf] = {"saldo": 0.0, "extrato": []}
        print(f"Usuário {nome} cadastrado com sucesso.")

def depositar(cpf, valor):
        if cpf in contas:
            contas[cpf]["saldo"] += valor
            contas[cpf]["extrato"].append(f"Depósito: +R${valor:.2f}")
        else:
            print("Usuário não encontrado.")

def sacar(cpf, valor):
    if cpf in contas:
        if valor > contas[cpf]["saldo"]:
            print("Saldo insuficiente.")
        else:
            contas[cpf]["saldo"] -= valor
            contas[cpf]["extrato"].append(f"Saque: -R${valor:.2f}")
    else:
        print("Usuário não encontrado.")

def transferir(cpf_origem, cpf_destino, valor):
    if cpf_origem in contas and cpf_destino in contas:
        if valor > contas[cpf_origem]["saldo"]:
            print("Saldo insuficiente para transferência.")
        else:
            contas[cpf_origem]["saldo"] -= valor
            contas[cpf_destino]["saldo"] += valor
            contas[cpf_origem]["extrato"].append(f"Transferência enviada: -R${valor:.2f} para {usuarios[cpf_destino]['nome']}")
            contas[cpf_destino]["extrato"].append(f"Transferência recebida: +R${valor:.2f} de {usuarios[cpf_origem]['nome']}")
    else:
        print("Usuário de origem ou destino não encontrado.")

def gerar_extrato(cpf):
    if cpf in contas:
        print(f"Extrato da conta de {usuarios[cpf]['nome']} (CPF: {usuarios[cpf]['cpf']}):")
        for item in contas[cpf]["extrato"]:
            print(item)
        print(f"Saldo atual: R${contas[cpf]['saldo']:.2f}")
    else:
        print("Usuário não encontrado.")

def editar_usuario(cpf):
    if cpf in usuarios:
        novo_nome = input("Digite o novo nome: ").strip()
        usuarios[cpf]['nome'] = novo_nome
        print(f"Dados do usuário {cpf} atualizados para: {usuarios[cpf]}")
    else:
        print("Usuário não encontrado.")

# Adicione a função fechar_conta aqui
# Adicione a função consultar_saldo aqui
while True:
    print('Menu Principal')
    print('1. Criar Conta')
    print('2. Depositar')
    print('3. Sacar')
    print('4. Consultar Saldo')
    print('5. Excluir conta')
    print('6. Sair')
    
    opcao = int(input('Escolha uma opção: '))


    
    if opcao == 1: #validamos a opção 1 de criar o usuário.
             
            print("Opção Criar Conta selecionada.")
            while True:
                    nome = input("Digite o nome do usuário a ser cadastrado: ") 
                    if nome.isdigit() > 0:
                        print("Utilize apenas letras no nome do usuário!")
                        continue
                    else:
                         break

            while True:
                    
                    cpf = (input("Digite o CPF do usuário: "))
                    if cpf in usuarios:
                        print("CPF já cadastrado.")
                        continue

                    elif cpf.isdigit() and len(cpf) == 11:
                        cadastrar_usuario(nome,cpf)
                        break

                    else:
                        print("Digite um CPF válido!")
                        continue
                        

    elif opcao == 2: #validamos a opção 2 para depositar
        print("Opção Depositar selecionada.")
        while True:
            cpf = input("Digite o CPF do usuário: ")
            if not cpf in contas:
                print("Digite um CPF existente.")
                continue
            else:
                 break
        valor = float(input("Digite o valor a ser depositado:"))
        depositar(cpf, valor)
 
    elif opcao == 3:
        print("Opção Sacar selecionada.")
        pass 
    elif opcao == 4:
        print("Opção Consultar Saldo selecionada.")
        print(usuarios)
        print(contas)
        pass  
    elif opcao == 5:
        print("Opção excluir conta selecionada.")
        pass
    elif opcao == 6:
        print("Sair...")
        break
    else:
        print("Opção inválida. Tente novamente.")


# Cadastro de usuários (exemplo)
cadastrar_usuario("João", "12345678900")
cadastrar_usuario("Maria", "09876543211")

# Realizar algumas operações (exemplo)
depositar("12345678900", 1000.0)
sacar("12345678900", 200.0)
transferir("12345678900", "09876543211", 300.0)

# Gerar extratos (exemplo)
gerar_extrato("12345678900")
print()
gerar_extrato("09876543211")