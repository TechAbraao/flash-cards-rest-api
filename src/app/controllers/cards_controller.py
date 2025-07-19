
class CardsController:
    def __init__(self, service, validator):
        self.service = service
        self.validator = validator
        
    def get_cards_by_deck(self, id):
        return f"Your UUID is: {id}"