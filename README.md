# Flash Cards REST API

### Tecnologias
<section align="left">
    <img alt="Static Badge" src="https://img.shields.io/badge/Python-grey?style=flat&logo=Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/Unittest-grey?style=flat&logo=Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/Marshmallow-grey?style=flat&logo=Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/Flask-grey?style=flat&logo=Flask">
    <img alt="Static Badge" src="https://img.shields.io/badge/SQLALchemy-grey?style=flat&logo=SQLAlchemy">
    <img alt="Static Badge" src="https://img.shields.io/badge/Docker-grey?style=flat&logo=Docker">
    <img alt="Static Badge" src="https://img.shields.io/badge/PostgreSQL-grey?style=flat&logo=PostgreSQL">
    <img alt="Static Badge" src="https://img.shields.io/badge/PgAdmin-grey?style=flat&logo=PostgreSQL">
    <img alt="Static Badge" src="https://img.shields.io/badge/Postman-grey?style=flat&logo=Postman">
</section>

## Instalação

```bash
# Clone o repositório já trazendo o submódulo templates
git clone --recurse-submodules https://github.com/TechAbraao/flash-cards-rest-api.git

# Acesse o diretório do projeto
cd flash-cards-rest-api

# (Opcional) Se esqueceu do --recurse-submodules, inicialize o submódulo manualmente
git submodule update --init --recursive

# Crie o ambiente virtual
python3 -m venv .venv

# Ative o ambiente virtual (Linux ou Mac)
source .venv/bin/activate

# Ou, se estiver no Windows
# .venv\Scripts\activate

# Instale as dependências do projeto
pip install -r src/requirements.txt

# Acesse a pasta de código-fonte
cd src

# Rode a aplicação Flask
flask run
```
## Atualizando o submódulo templates (quando houver alterações)
```bash
# Acesse a pasta do submódulo
cd src/app/templates

# Busque as últimas alterações do repositório de templates
git pull origin main  # ou a branch correta

# Volte para o repositório principal
cd ../../../..

# Adicione e commite a atualização do submódulo
git add src/app/templates
git commit -m "Atualiza submódulo templates"
git push origin main
```

## Contrato e Definições da API
### Endpoints
#### Decks

| Método | URL                   | Descrição                      |
| ------ | --------------------- | ------------------------------- |
| GET   | `/api/decks`           | Listar todos os decks          |
| POST  | `/api/decks`           | Criar um novo deck             |
| GET   | `/api/decks/<id>`      | Obter detalhes de um deck      |
| PUT   | `/api/decks/<id>`      | Atualizar informações de um deck |

##### Exemplo de Payload para Decks

```json
{
  "title": "História - Revolução Francesa Atualizado",
  "description": "Deck atualizado com mais flashcards sobre a Revolução Francesa.",
  "tags": ["história", "revolução", "frança"]
}
```

#### Flashcards

| Método | URL                                 | Descrição                           |
| ------ | ----------------------------------- | ----------------------------------- |
| POST  | `/api/decks/<deck_id>/cards`        | Adicionar flashcard ao deck         |
| GET   | `/api/decks/<deck_id>/cards/random` | Buscar flashcard aleatório do deck  |
| GET   | `/api/cards/<card_id>`              | Buscar flashcard específico         |
| PUT   | `/api/cards/<card_id>`              | Atualizar flashcard específico      |
| DELETE| `/api/cards/<card_id>`              | Remover flashcard                   |

#### Exemplo de Payload para Flashcards

```json
{
  "question": "Quando ocorreu a Revolução Francesa?",
  "answer": "Em 1789.",
  "tags": ["história", "datas", "revolução"]
}
```

#### Formato das Respostas da API:
Todas as respostas da API seguem o seguinte padrão:

- Sucesso
```json
{
  "success": true,
  "message": "Mensagem descritiva da operação",
  "data": { /* objeto ou lista retornada */ }
}
```

- Erro
```json
{
  "success": false,
  "message": "Mensagem de erro",
  "error": { /* objeto ou lista de erros */ }
}
```
> **Observações:**  
> - O campo `data` contém os dados retornados pela operação ou `null` em caso de erro.  
> - O campo `message` descreve o resultado da operação ou o motivo do erro.



