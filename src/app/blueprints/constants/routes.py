DECKS = {
    "get_all_decks": {
        "method": "GET",
        "URI": "/api/decks"
    },
    "create_deck": {
        "method": "POST",
        "URI": "/api/decks"
    },
    "get_deck": {
        "method": "GET",
        "URI": "/api/decks/<string:deck_id>",
    },
    "update_deck": {
        "method": "PUT",
        "URI": "/api/decks/<string:deck_id>"
    },
    "delete_deck": {
        "method": "DELETE",
        "URI": "/api/decks/<string:deck_id>"
    }
}

CARDS = {
    ...
}