from algorithms.CRM import CRM, lightCRM
from algorithms.random_strategy import random_strategy
from algorithms.opt_espgain_strategy import opt_espgain_strategy

class Strategy:
    def __init__(self, arbre):
        self.arbre = arbre

class lightCRM_model(Strategy):

    def __init__(self, arbre):
        super().__init__(arbre = arbre)
    
    def run(self, simulations = 1):
        model = lightCRM(self.arbre)
        model.run(simulations)
        model.compute_equilibre_nash()
        return model.information_set_equilibre_nash

class CRM_model(Strategy):

    def __init__(self, arbre):
        super().__init__(arbre = arbre)
    
    def run(self, simulations = 1):
        model = CRM(self.arbre)
        model.run(simulations)
        model.compute_equilibre_nash()
        return model.information_set_equilibre_nash

class random_model(Strategy):

    def __init__(self, arbre):
        super().__init__(arbre = arbre)

    def run(self):
        return random_strategy(self.arbre)

class opt_espgain_model(Strategy):

    def __init__(self, arbre):
        super().__init__(arbre = arbre)

    def run(self):
        return opt_espgain_strategy(self.arbre)
