from typing import List

from actions import Action, create_build_barricade_action, create_build_factory_action, create_move_action
from server import Game

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Agent:
    def __init__(self):
        pass
    
    def pr(mess: str):
        print(f"{bcolors.FAIL}-----------------------------------------------{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}TEST:: {mess}{bcolors.ENDC}")
        print(f"{bcolors.FAIL}-----------------------------------------------{bcolors.ENDC}")

    def update(self, game: Game) -> List[Action]:
        player_name = 'TorchicDaPatateSlayer'
        terrains = game.terrains()
        players = game.players()
        pipes = game.pipes()
        player = [index for index in range(len(players)) if players[index].name() == player_name]
        if len(player) == 1:
            player_index = player[0]
            player_terrains = [(index, terrains[index]) for index in range(len(terrains)) if terrains[index].owner_index() == player_index]
            player_terrains_index = [terrain[0] for terrain in player_terrains]
            orders = []
            
            
            for pipe in pipes: 
                # si le premier path est à nous, mais pas le deuxieme et on a au moins 1 soldat
                if pipe.first() in player_terrains_index and terrains[pipe.first()].type == 2:
                    #si on a un espace vide et pas beaucoup de soldats, on build une factory
                    orders.append(create_build_factory_action(terrains[pipe.first()].id()))
                    # sinon, si c'Est un espace vide et qu'on a beaucoup de sodlats, on build une barriere
                        
                if pipe.second() not in player_terrains_index and terrains[pipe.second()].type != 0:
                        # on bouge des soldat du premier au deuxieme path
                    orders.append(create_move_action(terrains[pipe.second()].id(), terrains[pipe.second()].id(), 1 ))
                        # si le deuxieme et le premier path ne sont pas à nous
            return orders
        return []
    
    

