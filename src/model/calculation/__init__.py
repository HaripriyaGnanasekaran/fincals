from .preprocess import Preprocess
from .nodes.var_monte_carlo import VARMonteCarlo, VARMonteCarloYearSweep


class Calculation:
    @staticmethod
    def execute():
        Preprocess.execute()
        VARMonteCarlo.execute()
