# Flash Cards REST API

```css
 _______  _        _______  _______                  _______  _______  _______  ______   _______         _______  _______  _______ _________     _______  _______ _________
(  ____ \( \      (  ___  )(  ____ \|\     /|       (  ____ \(  ___  )(  ____ )(  __  \ (  ____ \       (  ____ )(  ____ \(  ____ \\__   __/    (  ___  )(  ____ )\__   __/
| (    \/| (      | (   ) || (    \/| )   ( |       | (    \/| (   ) || (    )|| (  \  )| (    \/       | (    )|| (    \/| (    \/   ) (       | (   ) || (    )|   ) (   
| (__    | |      | (___) || (_____ | (___) | _____ | |      | (___) || (____)|| |   ) || (_____  _____ | (____)|| (__    | (_____    | | _____ | (___) || (____)|   | |   
|  __)   | |      |  ___  |(_____  )|  ___  |(_____)| |      |  ___  ||     __)| |   | |(_____  )(_____)|     __)|  __)   (_____  )   | |(_____)|  ___  ||  _____)   | |   
| (      | |      | (   ) |      ) || (   ) |       | |      | (   ) || (\ (   | |   ) |      ) |       | (\ (   | (            ) |   | |       | (   ) || (         | |   
| )      | (____/\| )   ( |/\____) || )   ( |       | (____/\| )   ( || ) \ \__| (__/  )/\____) |       | ) \ \__| (____/\/\____) |   | |       | )   ( || )      ___) (___
|/       (_______/|/     \|\_______)|/     \|       (_______/|/     \||/   \__/(______/ \_______)       |/   \__/(_______/\_______)   )_(       |/     \||/       \_______/
```

### Tecnologias
<section align="left">
    <img alt="Static Badge" src="https://img.shields.io/badge/Python-grey?style=flat&logo=Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/Unittest-grey?style=flat&logo=Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/Flask-grey?style=flat&logo=Flask">
    <img alt="Static Badge" src="https://img.shields.io/badge/SQLALchemy-grey?style=flat&logo=SQLAlchemy">
    <img alt="Static Badge" src="https://img.shields.io/badge/Docker-grey?style=flat&logo=Docker">
    <img alt="Static Badge" src="https://img.shields.io/badge/MySQL-grey?style=flat&logo=MySQL">
    <img alt="Static Badge" src="https://img.shields.io/badge/MySQL Workbench-grey?style=flat&logo=MySQL">
    <img alt="Static Badge" src="https://img.shields.io/badge/Postman-grey?style=flat&logo=Postman">
    <img alt="Static Badge" src="https://img.shields.io/badge/Yaml-grey?style=flat&logo=yaml">
</section>

## Instalação

```bash
# Clone o repositório
git clone https://github.com/TechAbraao/flash-cards-rest-api.git

# Acesse o projeto
cd flash-cards-rest-api

# Crie o ambiente virtual
python3 -m venv .venv

# Ative o ambiente virtual (Linux)
source .venv/bin/activate  # Ou .venv\Scripts\activate no Windows

# Instale as dependências
pip install -r src/requirements.txt

# Execute o projeto
flask run
```

## Contrato da API
### Endpoints
#### Decks

| Método | URL                   | Descrição                      |
| ------ | --------------------- | ------------------------------- |
| GET   | `/api/decks`           | Listar todos os decks          |
| POST  | `/api/decks`           | Criar um novo deck             |
| GET   | `/api/decks/<id>`      | Obter detalhes de um deck      |
| PUT   | `/api/decks/<id>`      | Atualizar informações de um deck |

#### Flashcards

| Método | URL                                 | Descrição                           |
| ------ | ----------------------------------- | ----------------------------------- |
| POST  | `/api/decks/<deck_id>/cards`        | Adicionar flashcard ao deck         |
| GET   | `/api/decks/<deck_id>/cards/random` | Buscar flashcard aleatório do deck  |
| GET   | `/api/cards/<card_id>`              | Buscar flashcard específico         |
| PUT   | `/api/cards/<card_id>`              | Atualizar flashcard específico      |
| DELETE| `/api/cards/<card_id>`              | Remover flashcard                   |

