# Flash Cards REST API - Backend for Flashcard Management

### Technologies
<section align="left">
    <img alt="Static Badge" src="https://img.shields.io/badge/Python-grey?style=flat&logo=Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/Unittest-grey?style=flat&logo=Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/PyTest-grey?style=flat&logo=PyTest">
    <img alt="Static Badge" src="https://img.shields.io/badge/Marshmallow-grey?style=flat&logo=Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/Flask-grey?style=flat&logo=Flask">
    <img alt="Static Badge" src="https://img.shields.io/badge/SQLALchemy-grey?style=flat&logo=SQLAlchemy">
    <img alt="Static Badge" src="https://img.shields.io/badge/Docker-grey?style=flat&logo=Docker">
    <img alt="Static Badge" src="https://img.shields.io/badge/PostgreSQL-grey?style=flat&logo=PostgreSQL">
    <img alt="Static Badge" src="https://img.shields.io/badge/PgAdmin-grey?style=flat&logo=PostgreSQL">
    <img alt="Static Badge" src="https://img.shields.io/badge/Github Actions-grey?style=flat&logo=Github Actions">
    <img alt="Static Badge" src="https://img.shields.io/badge/Postman-grey?style=flat&logo=Postman">
</section>

### Features
- __Deck Management:__ create, list, update, delete, and view deck details.  
- __Card Management:__ create cards, associate them with decks, search randomly or individually, update, and delete cards.

## Installation Guide
#### 1. Clone the repository and initialize submodules
```bash
git clone --recurse-submodules https://github.com/TechAbraao/flash-cards-rest-api.git
cd flash-cards-rest-api

# (Optional) If you forgot --recurse-submodules, initialize the submodule manually
git submodule update --init --recursive
```

#### 2. Create and activate the virtual environment
```bash
python3 -m venv .venv

# Activate the virtual environment (Linux or Mac)
source .venv/bin/activate

# Or, if you're on Windows
# .venv\Scripts\activate
```
#### 3. Install dependencies
```bash
pip install -r src/requirements.txt
```
#### 4. Configure environment variables
- Rename the .env.example file to .env and edit the variables accordingly:
```bash
# Default Flask app configurations
FLASK_APP=src.app:create_app
FLASK_ENV=development
FLASK_DEBUG=1
PYTHONPATH=.

# Database configurations
DATABASE_HOST=
DATABASE_PORT=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_NAME=
```
#### 5. Run the Flask application
```bash
flask run
```
#### 6. Access and test the API
```bash
# Use Postman or any HTTP client to test the available endpoints. Access:
http://<host>:<port> to start using the API.
```

## Templates submodule update (for updates or experimental front-end)
```bash
# Enter the submodule folder
cd src/app/templates

# Fetch the latest changes from the templates repository
git pull origin main  # or the correct branch

# Go back to the main repository
cd ../../../..

# Add and commit the submodule update
git add src/app/templates
git commit -m "Update templates submodule"
git push origin main
```

## API Reference
### Endpoints
#### Decks

| Method | URL | Description |
| ------ | --------------------- | ------------------------------- |
| GET | `/api/decks` | List all decks |
| POST | `/api/decks` | Create a new deck |
| GET | `/api/decks/<id>` | Get deck details |
| PUT | `/api/decks/<id>` | Update deck information |
| DELETE | `/api/decks/<id>` | Delete a deck |

- Example Payload for Decks

```json
{
"title": "History - French Revolution Updated",
"description": "Deck updated with more flashcards about the French Revolution.",
"tags": ["history", "revolution", "france"]
}
```

#### Cards

| Method | URL | Description |
| ------ | ----------------------------------- | ----------------------------------- |
| POST | `/api/decks/<deck_id>/cards` | Add card to deck |
| GET | `/api/decks/<deck_id>/cards` | Search for all cards in a deck |
| GET | `/api/decks/<deck_id>/cards/random` | Search for a random card in the deck |
| GET | `/api/cards/<card_id>` | Search for a specific card |
| PUT | `/api/cards/<card_id>` | Update a specific card |
| DELETE | `/api/cards/<card_id>` | Remove card |

- Example Payload for Cards

```json
{
"question": "When did the French Revolution occur?",
"answer": "In 1789.",
"tags": ["history", "dates", "revolution"]
}
```

#### API Response Format:
All API responses follow the following pattern:

- Success
```json
{
"success": true,
"message": "Message describing the operation",
"data": { /* object or list returned */ }
}
```

- Error
```json
{
"success": false,
"message": "Error message",
"error": { /* object or list of errors */ }
}
```
> **Notes:**
> - The `error` field contains the error object or list of errors.
> - The `message` field describes the result of the operation or the reason for the error.