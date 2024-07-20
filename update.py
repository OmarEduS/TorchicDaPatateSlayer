from typing import List

from actions import Action, create_build_barricade_action, create_build_factory_action, create_demolish_action, create_move_action
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
                if pipe.first() in player_terrains_index:
                    orders.append(create_build_factory_action(terrains[pipe.first()].id()))
                    print("FACTORY")
                        
                #if pipe.second() not in player_terrains_index and (terrains[pipe.second()].type != 0 or terrains[pipe.second()].type != 3):
                 #   orders.append(create_move_action(terrains[pipe.first()].id(), terrains[pipe.second()].id(), 1 ))
                  #  print("1 to 2")
                        # si le deuxieme et le premier path ne sont pas à nous
                #if terrains[pipe.first()].number_of_soldier() > terrains[pipe.second()].number_of_soldier()*2 + 6:
                #    orders.append(create_move_action(terrains[pipe.first()].id(), terrains[pipe.second()].id(), terrains[pipe.first()].number_of_soldier()))
                #    orders.append(create_demolish_action(terrains[pipe.second()].id()))
                #    orders.append(create_build_barricade_action(terrains[pipe.second()].id()))
                #    print("DEMOLISH")
                    
                if pipe.second() not in player_terrains_index and (terrains[pipe.second()].type != 0 or terrains[pipe.second()].type != 3) and terrains[pipe.first()].number_of_soldier() > 0:
                    orders.append(create_move_action(terrains[pipe.first()].id(), terrains[pipe.second()].id(), 1))
                    print("-")
                if pipe.second() in player_terrains_index:
                    orders.append(create_build_barricade_action(terrains[pipe.second()].id()))
                    print("barricade")
                
            return orders
        return []
    
    

