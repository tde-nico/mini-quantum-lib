from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit import Gate
from .csxdg import CSxdg

class TR(Gate):
	def __init__(self):
		super().__init__('TR', 3, [], label='TR')
	
	def _define(self):
		a = QuantumRegister(1, 'A')
		b = QuantumRegister(1, 'B')
		c = QuantumRegister(1, 'C')

		qc = QuantumCircuit(a, b, c, name=self.name)

		qc.append(CSxdg, [b, c])
		qc.cx(a, b)
		qc.csx(a, c)
		qc.csx(b, c)

		self.definition = qc
