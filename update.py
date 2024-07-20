from typing import List

from actions import Action, create_build_barricade_action, create_build_factory_action, create_move_action
from server import Game


class Agent:
    def __init__(self):
        pass

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
                if pipe.first() in player_terrains_index and pipe.first().type == 2:
                    #si on a un espace vide et pas beaucoup de soldats, on build une factory
                    if terrains[pipe.first()].number_of_soldier() < 5:
                        orders.append(create_build_factory_action(terrains[pipe.first()].id()))
                    # sinon, si c'Est un espace vide et qu'on a beaucoup de sodlats, on build une barriere
                    else:
                        orders.append(create_build_barricade_action(terrains[pipe.first()].id()))
                        
                if pipe.second() not in player_terrains_index and terrains[pipe.first()].number_of_soldier() > 5:
                        # on bouge des soldat du premier au deuxieme path
                        orders.append(create_move_action(terrains[pipe.first()].id(), terrains[pipe.second()].id(), 2))
                        # si le deuxieme et le premier path ne sont pas à nous
                        if pipe.second() in player_terrains_index and pipe.first() not in player_terrains_index and terrains[pipe.second()].number_of_soldier() > 0:
                            # on ramene le soldat
                            orders.append(create_move_action(terrains[pipe.second()].id(), terrains[pipe.first()].id(), 2))

            return orders
        return []
    
    

