from dataclasses import dataclass

from utils.basic_utils import format_with_spaces


@dataclass
class OptimSolvers:
    gurobi: str = 'gurobi'
    highs: str = 'highs'


@dataclass
class OptimPbTypes:
    lp: str = 'lp'
    milp: str = 'milp'
    qp: str = 'qp'
    miqp: str = 'miqp'


@dataclass
class OptimPbCharacteristics:
    type: str = 'LP'
    n_variables: int = None
    n_int_variables: int = None
    n_constraints: int = None

    def __repr__(self) -> str:
        repr_str = f'{self.type.upper()} optimisation pb with:'
        repr_str += f'\n* {format_with_spaces(number=self.n_variables)} variables'
        if self.n_int_variables is not None:
            repr_str += f' (including {format_with_spaces(number=self.n_int_variables)} integer ones)'
        repr_str += f'\n* {format_with_spaces(number=self.n_constraints)} constraints'
        return repr_str


@dataclass
class OptimResolStatus:
    optimal: str = 'optimal'
    infeasible: str = 'infeasible'
    

OPTIM_RESOL_STATUS = OptimResolStatus()


@dataclass
class SolverParams:
    name: str = 'highs'
    license_file: str = None


DEFAULT_OPTIM_SOLVER_PARAMS = SolverParams(name=OptimSolvers.highs)
