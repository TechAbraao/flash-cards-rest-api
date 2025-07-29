## Project Progress

### Decks API

- [x] List all decks (`GET /api/decks`)

- [x] Create a new deck (`POST /api/decks`)
  - [ ] Validate `title` is required and not empty
  - [ ] Validate `tags` are list of strings (optional)
  - [ ] Validate `description` max length 500 chars

- [x] Get deck details (`GET /api/decks/<id>`)
  - [ ] Validate UUID format for `<id>`

- [x] Update deck information (`PUT /api/decks/<id>`)
  - [ ] Validate fields if present (partial update)
  - [ ] Validate title uniqueness (optional)

- [x] Delete a deck (`DELETE /api/decks/<id>`)
  - [ ] Validate UUID format for `<id>`

---

### Cards API

- [ ] Add card to deck (`POST /api/decks/<deck_id>/cards`)
  - [ ] Validate `question` is required and not empty
  - [ ] Validate `answer` is required
  - [ ] Validate `tags` are list of strings (optional)
  - [ ] Validate `deck_id` is valid UUID and exists

- [ ] Search all cards in a deck (`GET /api/decks/<deck_id>/cards`)
  - [ ] Validate UUID format for `<deck_id>`

- [ ] Search for random card (`GET /api/decks/<deck_id>/cards/random`)
  - [ ] Validate UUID format for `<deck_id>`

- [ ] Search specific card (`GET /api/cards/<card_id>`)
  - [ ] Validate UUID format for `<card_id>`

- [ ] Update card (`PUT /api/cards/<card_id>`)
  - [ ] Validate fields if present
  - [ ] Validate question uniqueness (optional)

- [ ] Remove card (`DELETE /api/cards/<card_id>`)
  - [ ] Validate UUID format for `<card_id>`

---

### Testing

- [ ] Unit tests for Decks endpoints
- [ ] Unit tests for Cards endpoints
