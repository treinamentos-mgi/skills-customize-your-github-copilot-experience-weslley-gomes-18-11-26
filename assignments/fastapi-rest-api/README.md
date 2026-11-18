# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma API REST com FastAPI, organizar endpoints HTTP e validar dados com modelos Pydantic. Ao final, você terá construído uma API CRUD simples para um catálogo de livros.

## 📝 Tasks

### 🛠️ Listar Livros

#### Descrição
Explore o app FastAPI inicial e implemente o endpoint para consultar os livros cadastrados. Inicie o servidor local e teste a API pela documentação interativa.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI chamada `app` no arquivo `starter-code.py`.
- Implementar `GET /books` para retornar a lista de livros em formato JSON.
- Iniciar o servidor com `uvicorn starter-code:app --reload`.
- Permitir que os endpoints sejam explorados em `http://127.0.0.1:8000/docs`.

### 🛠️ Cadastrar Livros

#### Descrição
Adicione um endpoint para cadastrar um livro. Use um modelo Pydantic para validar os dados enviados pelo cliente.

#### Requisitos
O programa concluído deve:

- Definir um modelo de entrada com os campos `title` e `author`, ambos obrigatórios e não vazios.
- Implementar `POST /books` para receber os dados do livro em JSON.
- Atribuir um identificador único ao novo livro e adicioná-lo à lista em memória.
- Retornar o livro criado com status HTTP `201 Created`.

Exemplo de corpo da requisição:

```json
{
  "title": "Dune",
  "author": "Frank Herbert"
}
```

### 🛠️ Consultar, Atualizar e Remover Livros

#### Descrição
Complete a API permitindo que um cliente consulte, atualize ou remova um livro específico pelo identificador.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` para retornar um livro específico.
- Implementar `PUT /books/{book_id}` para atualizar o título e o autor de um livro.
- Implementar `DELETE /books/{book_id}` para remover um livro.
- Retornar status HTTP `404 Not Found` quando o identificador não corresponder a um livro existente.
- Verificar as operações e os respectivos códigos de resposta na documentação interativa do FastAPI.
