from qiskit import QuantumCircuit

from .csxdg import CSxdg
from .peres import Peres
from .tr import TR

QuantumCircuit.csxdg = lambda s, *x: s.append(CSxdg(), *x)
QuantumCircuit.peres = lambda s, *x: s.append(Peres(), *x)
QuantumCircuit.tr = lambda s, *x: s.append(TR(), *x)

