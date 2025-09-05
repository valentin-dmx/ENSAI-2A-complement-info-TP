from abstract_ pokemon import AbstractPokemon

class Attacker(AbstractPokemon):
    def __init__(self):
        super().__init__(self, stat_max=None, stat_current=None)

    def get_pokemon_attack_coef(self):
        return 1 + (self.speed_current + self.attack_current) / 200