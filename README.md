# Sistema de Gerenciamento de Biblioteca

## Descrição

Sistema desenvolvido em Python para gerenciar uma biblioteca. O programa permite cadastrar livros, registrar empréstimos e devoluções, listar, buscar e ordenar os livros. Os dados são salvos em um arquivo CSV.

## Como executar o programa

1. Abra a pasta do projeto no Visual Studio Code.
2. Abra o terminal.
3. Execute:

```bash
python main.py
```

4. Escolha uma opção no menu de 1 a 7.
5. Para encerrar, escolha a opção 7.

## Principais funcionalidades

- Cadastrar livros com título, autor, ano, ISBN e status.
- Registrar empréstimos.
- Registrar devoluções.
- Listar todos os livros cadastrados.
- Buscar livros por título ou autor.
- Ordenar livros por título, autor ou ano.
- Salvar e carregar os livros pelo arquivo `livros.csv`.

## Requisitos técnicos aplicados

- **if/elif/else:** utilizado no menu principal para controlar as opções.
- **while:** mantém o menu funcionando até o usuário escolher sair.
- **Funções:** o programa foi dividido em funções como `adicionar_livro()`, `registrar_emprestimo()`, `registrar_devolucao()`, `listar_livros()`, `buscar_livro()` e `ordenar_livros()`.
- **Lista de dicionários:** os livros são armazenados na lista `livros`.
- **Arquivo CSV:** `salvar_livros()` salva os dados e `carregar_livros()` recupera os dados quando o programa é aberto.
- **Biblioteca padrão:** foi utilizado o módulo `csv`, sem instalação de pacotes externos.