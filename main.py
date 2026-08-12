import csv

# def - cria uma função para salvar os livros
def salvar_livros(livros):
    with open("livros.csv", "w", newline="", encoding="utf-8") as arquivo:
        campos = ["titulo", "autor", "ano", "isbn", "status"]

   # csv.DictWriter - permite escrever os dados dos livros no arquivo CSV
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=campos,
            delimiter=";"
        )

   # writeheader - escreve o cabeçalho do arquivo
        escritor.writeheader()
   # writerows - escreve todos os livros no arquivo
        escritor.writerows(livros)

   # return - retorna um resultado para indicar que a função terminou
    return True

   # def - cria uma função para carregar os livros salvos
def carregar_livros():
    livros = []

    # try - tenta executar o código abaixo
    try:
        with open("livros.csv", "r", encoding="utf-8") as arquivo:

    # DictReader - lê os dados do arquivo como dicionários
            leitor = csv.DictReader(arquivo, delimiter=";")

    # for - percorre cada livro encontrado no arquivo
            for livro in leitor:
                livros.append(livro)

    # except - trata o erro caso o arquivo ainda não exista
    except FileNotFoundError:
        pass

    return livros

    # def - cria uma função para cadastrar um novo livro
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

    # append - adiciona o novo livro à lista
    livros.append(livro)

    print(f"Livro '{titulo}' adicionado com sucesso!")
    # def - cria uma função para registrar um empréstimo
def registrar_emprestimo(livros, isbn):

    # for - procura o livro dentro da lista
    for livro in livros:

        # if - verifica se o ISBN informado pertence ao livro
        if livro["isbn"] == isbn:

            # if - verifica se o livro está disponível
            if livro["status"] == "disponível":
                livro["status"] = "emprestado"

        # return True - informa que o empréstimo foi realizado
                return True
            return False

    return False

        # def - cria uma função para registrar uma devolução
def registrar_devolucao(livros, isbn):

        # for - procura o livro pelo ISBN
    for livro in livros:

        # if - verifica se o ISBN informado pertence ao livro
        if livro["isbn"] == isbn:

        # if - verifica se o livro está emprestado
            if livro["status"] == "emprestado":
                livro["status"] = "disponível"

        # return True - informa que a devolução foi realizada
                return True
            return False

    return False

        # def - cria uma função para listar os livros
def listar_livros(livros):

    # if - verifica se não existem livros cadastrados
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    print("\n=== LIVROS CADASTRADOS ===")

    # for - percorre todos os livros para mostrar suas informações
    for livro in livros:
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Status: {livro['status']}")
        print("------------------------")

    # def - cria uma função para buscar um livro
def buscar_livro(livros):
    isbn = input("Digite o ISBN do livro: ")

    # for - procura o livro dentro da lista
    for livro in livros:

    # if - verifica se o ISBN corresponde ao livro
        if livro["isbn"] == isbn:
            print("\n=== LIVRO ENCONTRADO ===")
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"ISBN: {livro['isbn']}")
            print(f"Status: {livro['status']}")

    # return - encerra a função depois de encontrar o livro    
            return

    print("Livro não encontrado.")

    # def - cria uma função para ordenar os livros
def ordenar_livros(livros):

    # if - verifica se existem livros para ordenar
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    # sort - organiza os livros em ordem alfabética pelo título
    livros.sort(key=lambda livro: livro["titulo"].lower())

    print("Livros ordenados pelo título:")

    # for - mostra os livros depois da ordenação
    for livro in livros:
        print(f"- {livro['titulo']}")

    # função - carrega os livros salvos antes de iniciar o programa
livros = carregar_livros()

    # while - mantém o menu funcionando até o usuário escolher sair
while True:
    print("\nBem-vindo à biblioteca!")
    print("1: Adicionar livro")
    print("2: Registrar empréstimo")
    print("3: Registrar devolução")
    print("4: Listar os livros")
    print("5: Buscar um livro")
    print("6: Ordenar a listagem de livros")
    print("7: Sair")

    # input - recebe a opção escolhida pelo usuário
    opcao = input("Escolha uma opção: ")

    # if - verifica se o usuário escolheu adicionar livro
    if opcao == "1":
        adicionar_livro(livros)

    # elif - verifica se o usuário escolheu registrar empréstimo
    elif opcao == "2":
        isbn = input("Digite o ISBN do livro: ")

        if registrar_emprestimo(livros, isbn):
            print("Empréstimo registrado com sucesso!")
        else:
            print("Não foi possível registrar o empréstimo.")

    # elif - verifica se o usuário escolheu registrar devolução
    elif opcao == "3":
        isbn = input("Digite o ISBN do livro: ")

        if registrar_devolucao(livros, isbn):
            print("Devolução registrada com sucesso!")
        else:
            print("Não foi possível registrar a devolução.")

    # elif - verifica se o usuário escolheu listar os livros
    elif opcao == "4":
        print("Listando os livros cadastrados...")
        print(livros)
        listar_livros(livros)

    # elif - verifica se o usuário escolheu buscar um livro
    elif opcao == "5":
        buscar_livro(livros)

    # elif - verifica se o usuário escolheu ordenar os livros
    elif opcao == "6":
        ordenar_livros(livros)

    # elif - verifica se o usuário escolheu sair
    elif opcao == "7":
        print("Saindo do programa...")

    # break - encerra o while e finaliza o programa
        break

    # else - executa quando a opção digitada não existe
    else:
        print("Opção inválida. Tente novamente.")