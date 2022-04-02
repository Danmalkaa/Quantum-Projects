from qiskit import (execute ,Aer)

# Use Aer ’s qasm_simulator
simulator = Aer . get_backend (’ qasm_simulator ’)
from qiskit import QuantumCircuit
circuit = QuantumCircuit ( qbits , cbits )
circuit .h (3)
# Hadamard gate
circuit .h( qubit_number )

# X gate
circuit .x( qubit_number )

# Z gate
circuit .z( qubit_number )

# CNOT gate with control qubit control_qubit and target qubit target_qubit
circuit . cx ( control_qubit , target_qubit )

# Measure the qubits in qibits_subset and store the result in the classical bits cbits_subset .
# Note that we do not have to measure all of the qubits , but only the subset we choose .
circuit . measure ( qubits_subset , cbits_subset )

# Draw the circuit
circuit . draw ( output =’mpl ’, filename =’my_circuit . png ’)

# Execute the circuit on the IBM simulator
# The simulator will run 1000 simulations of the circuit and will collect the
measurement results .
job = execute ( circuit , simulator , shots =1000)

# Grab results from the job
result = job . result ()

# Returns counts of the number of occurences of each eigenstate of the
computational basis
counts = result . get_counts ( circuit )
print ( counts )