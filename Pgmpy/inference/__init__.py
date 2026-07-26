from .base import Inference
from .ExactInference import BeliefPropagation
from .ExactInference import VariableElimination
from .ExactInference import VariableEliminationJIT

__all__ = [
    "Inference",
    "VariableElimination",
    "BeliefPropagation",
    "VariableEliminationJIT",
]

try:
    from .ExactInferenceTorch import VariableEliminationJIT_torch
except ImportError:
    VariableEliminationJIT_torch = None
else:
    __all__.append("VariableEliminationJIT_torch")
