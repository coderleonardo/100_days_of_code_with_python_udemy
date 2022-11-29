class HandsInitializer():
    def __init__(self, person_name: str) -> None:
        self.name = person_name
        self.cards = []
        self.score = 0

    def update_score(self):
        if self.cards:
            self.score = sum(self.cards)
            return self.score
        return self.score

    def __repr__(self):
            return f"{self.name}'s cards: {self.cards}. Current score: {self.score}"

    def first_card_infos(self):
        print(f"{self.name}'s cards: {self.cards[0]}. Current score: {self.score}")
