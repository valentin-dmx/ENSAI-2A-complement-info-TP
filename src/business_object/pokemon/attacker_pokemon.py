from src.business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.statistic import Statistic


class Attacker(AbstractPokemon):
    def __init__(
        self,
        stat_max=None, 
        stat_current=None, 
        level=0, 
        name=None):

        super().__init__(self, stat_max=None, stat_current=None, level=0, name=None)

    def get_pokemon_attack_coef(self):
        return 1 + (self.speed_current + self.attack_current) / 200
