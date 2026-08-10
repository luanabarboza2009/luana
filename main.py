livros = []

def adicionar_livro(livros):
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação do livro: ")
    isbn = input("Digite o ISBN do livro: ")

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponível"
    }

    livros.append(livro)

    print(f"Livro '{titulo}' adicionado com sucesso!")

def registrar_emprestimo(livros, isbn):
    for livro in livros:
        if livro["isbn"] == isbn:
            if livro["status"] == "disponível":
                livro["status"] = "emprestado"
                return True
            return False

    return False

def registrar_devolucao(livros, isbn):
    for livro in livros:
        if livro["isbn"] == isbn:
            if livro["status"] == "emprestado":
                livro["status"] = "disponível"
                return True
            return False

    return False

while True:
    print("\nBem-vindo à biblioteca!")
    print("1: Adicionar livro")
    print("2: Registrar empréstimo")
    print("3: Registrar devolução")
    print("4: Listar os livros")
    print("5: Buscar um livro")
    print("6: Ordenar a listagem de livros")
    print("7: Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_livro(livros)

    elif opcao == "2":
        isbn = input("Digite o ISBN do livro: ")

        if registrar_emprestimo(livros, isbn):
            print("Empréstimo registrado com sucesso!")
        else:
            print("Não foi possível registrar o empréstimo.")

    elif opcao == "3":
        isbn = input("Digite o ISBN do livro: ")

        if registrar_devolucao(livros, isbn):
            print("Devolução registrada com sucesso!")
        else:
            print("Não foi possível registrar a devolução.")
            
    elif opcao == "4":
       "Listar os livros"

    elif opcao == "5":
        "Buscar um livro"

    elif opcao == "6":
        "Ordenar a listagem de livros"

    elif opcao == "7":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")