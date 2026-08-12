# Projeto Luana
# Sistema de Gerenciamento de Biblioteca

Este projeto é um sistema de gerenciamento de biblioteca desenvolvido Python.

O programa permite cadastrar livros, registrar empréstimos e devoluções, listar livros, buscar livros pelo ISBN e ordenar os livros por título. Os dados dos livros também podem ser salvos e carregados por meio de um arquivo CSV.

## Como executar o programa
    1. Tenha o Python instalado no computador.
    2. Abra a pasta do projeto no VS Code.
    3. Abra o terminal na pasta do projeto.
    4. Execute o comando:

    ```bash
    python main.py
    Projeto desenvolvido Python.

Principais funcionalidades
    Cadastrar novos livros.
    Registrar empréstimos de livros.
    Registrar devoluções de livros.
    Listar todos os livros cadastrados.
    Buscar um livro pelo ISBN.
    Ordenar os livros pelo título.
    Salvar os dados dos livros em um arquivo CSV.
    Carregar os livros salvos ao iniciar o programa.
    Informar o status do livro: disponível ou emprestado.  

Requisitos técnicos aplicadosFunções 
    (def): o programa foi dividido em funções como adicionar_livro(), registrar_emprestimo(), registrar_devolucao(), listar_livros(), buscar_livro() e ordenar_livros().

    Listas: utilizada para armazenar os livros cadastrados.

    Dicionários: utilizados para guardar as informações de cada livro, como título, autor, ano, ISBN e status.

    Estruturas condicionais (if, elif e else): utilizadas para controlar as opções do menu e verificar as condições dos livros.

    Laços de repetição (for e while): utilizados para percorrer os livros e manter o menu funcionando até o usuário escolher sair.

    Entrada e saída de dados (input() e print()): utilizadas para receber informações do usuário e apresentar os resultados.

    Biblioteca csv: utilizada para salvar e carregar os dados dos livros em um arquivo CSV.
    Tratamento de exceções (try e except): utilizado para tratar a situação em que o arquivo CSV ainda não existe.
    
    Ordenação (sort()): utilizada para organizar os livros em ordem alfabética pelo título.
    Comentários no código: foram adicionados comentários nas principais partes da lógica para facilitar a compreensão do programa.