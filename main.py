# Importa o módulo csv, que permite trabalhar com arquivos CSV
import csv

def salvar_livros(livros):
    with open("livros.csv", "w", newline="", encoding="utf-8") as arquivo:
        campos = ["titulo", "autor", "ano", "isbn", "status"]

        escritor = csv.DictWriter(
            arquivo,
            fieldnames=campos,
            delimiter=";"
        )

        escritor.writeheader()
        escritor.writerows(livros)

    return True

def carregar_livros():
    livros = []

    try:
        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo, delimiter=";")

            for livro in leitor:
                livros.append(livro)

    except FileNotFoundError:
        pass

    return livros

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

def listar_livros(livros):
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    print("\n=== LIVROS CADASTRADOS ===")

    for livro in livros:
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Status: {livro['status']}")
        print("------------------------")

def buscar_livro(livros):
    busca = input("Digite o título ou autor do livro: ")

    for livro in livros:
        if livro["titulo"] == busca or livro["autor"] == busca:
            print("\n=== LIVRO ENCONTRADO ===")
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"ISBN: {livro['isbn']}")
            print(f"Status: {livro['status']}")
            return True

    print("Livro não encontrado.")
    return False
    
def ordenar_livros(livros):
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    livros.sort(key=lambda livro: livro["titulo"].lower())

    print("Livros ordenados pelo título:")
    
    for livro in livros:
        print(f"- {livro['titulo']}")

livros = carregar_livros()

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
        salvar_livros(livros)

    elif opcao == "2":
        isbn = input("Digite o ISBN do livro: ")

        if registrar_emprestimo(livros, isbn):
            salvar_livros(livros)
            print("Empréstimo registrado com sucesso!")
        else:
            print("Não foi possível registrar o empréstimo.")

    elif opcao == "3":
        isbn = input("Digite o ISBN do livro: ")

        if registrar_devolucao(livros, isbn):
            salvar_livros(livros)
            print("Devolução registrada com sucesso!")
        else:
            print("Não foi possível registrar a devolução.")
            
    elif opcao == "4":
        print("Listando os livros cadastrados...")
        listar_livros(livros)

    elif opcao == "5":
        buscar_livro(livros)

    elif opcao == "6":
        ordenar_livros(livros)

    elif opcao == "7":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")