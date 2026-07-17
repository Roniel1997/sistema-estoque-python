lista_produtos = []

def cadastrar_produtos():
    qtd_produto = 0

    while True:
        print("====== CADASTRAR PRODUTOS ======")
        print("Digite 'sair' para voltar ao menu principal\n")

        while True:
            produto = input("Digite o nome do produto (ou 'sair' para voltar): ").strip()

            if produto.lower() == "sair":
                print(f"Foram cadastrados {qtd_produto} produto(s).\n")
                print("Voltando ao menu principal...")
                return

            if produto == "":
                print("ERRO, o nome do produto não pode ficar vazio...")
                continue

            if produto.isdigit():
                print("ERRO, o nome do produto não pode conter apenas números...")
                continue

            break

        while True:
            try:
                preco = float(input("Digite o valor do produto: ").strip().replace(",", "."))

                if preco < 0:
                    print("ERRO, preço menor que 0!")
                    continue

                break

            except ValueError:
                print("ERRO, digite apenas números...")

        while True:
            try:
                quantidade = int(input("Digite a quantidade de produtos: ").strip())

                if quantidade < 0:
                    print("ERRO, quantidade menor que 0!")
                    continue

                break

            except ValueError:
                print("ERRO, digite apenas números...")

        dicionario_produto = {
            "nome": produto,
            "preco": preco,
            "quantidade": quantidade
        }

        lista_produtos.append(dicionario_produto)
        qtd_produto += 1

        print(f"{produto} foi cadastrado com sucesso!\n")
        print(f"{qtd_produto} produto(s) cadastrado(s).\n")


def vender_produtos():
    while True:
        if len(lista_produtos) == 0:
            print("❌❌ Lista vazia ❌❌\n")
            return
        else:
            print("=== Realizar Venda ===\n")
            for indice, produto in enumerate(lista_produtos):
                print(f"{indice + 1} - {produto['nome']}")

            while True:
                try:
                    busca_indice = int(input("Digite um numero de busca: ").strip()) - 1
                    if busca_indice < 0 or busca_indice >= len(lista_produtos):
                        print("Valor de busca não encontrado. Digite um novo valor de busca.")
                    else:
                        produto_encontrado = lista_produtos[busca_indice]
                        print("\n✅ Produto selecionado!\n")
                        print(f"Produto: {produto_encontrado['nome']}")
                        print(f"Preço: {produto_encontrado['preco']}")
                        print(f"Quantidade: {produto_encontrado['quantidade']}\n")

                        while True:
                            try:
                                qtd_venda = int(input("\nDigite o numero de venda do produto: ").strip())
                                if qtd_venda > 0 and qtd_venda <= produto_encontrado["quantidade"]:
                                    produto_encontrado["quantidade"] -= qtd_venda
                                    print("\n✅ Venda realizada com sucesso!")
                                    print(f"📦 Estoque restante: {produto_encontrado['quantidade']}")

                                    return
                                else:
                                    print("ERRO! Quantidade menor que estoque ou maior que o estoque.")
                                    continue
                            except ValueError:
                                print("Aconteceu algum erro, tente novamente...")



                    break
                except ValueError:
                    print("ERRO, digite apenas numeros inteiros.")




def consultar_produto():

    if len(lista_produtos) == 0:
        print("❌ Nenhum produto cadastrado ❌\n")
        return

    print("=== Produtos Cadastrados ===")
    print(f"Foram encontrados {len(lista_produtos)} produto(s).")

    for indice, produto in enumerate(lista_produtos):
        print(f"{indice + 1} - {produto['nome']}")

    while True:
        try:
            buscar_indice = int(input("\nDigite o índice do produto: ").strip()) - 1

            if buscar_indice < 0 or buscar_indice >= len(lista_produtos):
                print("Produto não encontrado! Digite um número válido.")
                continue

            produto_encontrado = lista_produtos[buscar_indice]

            print("\nBusca realizada com sucesso!")
            print(f"📦 Nome: {produto_encontrado['nome']}")
            print(f"💵 Preço: R$ {produto_encontrado['preco']:.2f}")
            print(f"🔢 Estoque: {produto_encontrado['quantidade']} unidades\n")
            break

        except ValueError:
            print("ERRO, digite apenas números inteiros para o índice...")


def sair_produto():
    print("Sistema finalizado.\n")


while True:

    print("====== MENU ======")
    print("1 - Cadastrar produtos 🛒")
    print("2 - Vender produtos 🖥️")
    print("3 - Consultar produtos 🔍")
    print("4 - ❌ Sair" )

    try:
        opcao = int(input("\nDigite a opção escolhida: "))

        if opcao == 1:
            cadastrar_produtos()

        elif opcao == 2:
            vender_produtos()

        elif opcao == 3:
            consultar_produto()

        elif opcao == 4:
            sair_produto()
            break

        else:
            print("ERRO, opção inválida! Escolha uma opção do menu.\n")

    except ValueError:
        print("ERRO, digite apenas números inteiros.\n")