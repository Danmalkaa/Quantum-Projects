from qiskit import (execute ,Aer)

# Use Aer ’s qasm_simulator
simulator = Aer . get_backend ('qasm_simulator')
from qiskit import QuantumCircuit

# Q1
# Hadmard and Measure
circuit = QuantumCircuit(1, 1)
circuit.h(0)
circuit.measure(0,0)

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 0 and 1 are:",counts)

# Draw the circuit
circuit.draw()
print()