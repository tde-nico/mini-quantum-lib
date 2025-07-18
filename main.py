from qiskit import QuantumCircuit, QuantumRegister
from mqt import ddsim
from qlib import *

a = QuantumRegister(4, "A")
b = QuantumRegister(4, "B")

circ = QuantumCircuit(a, b)

# circ.append(Peres(), [a[0], a[1], a[2]])
circ.peres([a[0], a[1], a[2]])
circ.tr([b[0], b[1], b[2]])
circ.x(0)
# circ.measure_all()

print(circ.draw())

# backend = ddsim.DDSIMProvider().get_backend("qasm_simulator")

# job = backend.run(circ)
# result = job.result()

# out = result.get_counts(circ)

# print(out)
