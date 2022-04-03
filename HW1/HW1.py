import numpy as np
from qiskit.visualization import plot_histogram
from qiskit import (execute ,Aer, QuantumRegister,ClassicalRegister)

# Use Aer ’s qasm_simulator
simulator = Aer . get_backend ('qasm_simulator')
from qiskit import QuantumCircuit

def run_plot(circ, shots=1000, print_total=True, state_to_print=None):
    # Execute the circuit on the qasm simulator
    job = execute(circ, simulator, shots=shots)

    # Grab results from the job
    result = job.result()

    # Returns counts
    counts = result.get_counts(circ)
    if print_total:
        print("\nTotal count are:", counts)
    if state_to_print:
        print(f"\nState {state_to_print} count is:", counts[state_to_print])
    # Draw the circuit
    print(circ.draw())
    plot_histogram(counts)

# Q1_a
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
print(circuit.draw())
plot_histogram(counts)

# Q1_b
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0,1)
circuit.measure(0,0)
circuit.measure(1,1)
run_plot(circuit)

# Q2
circuit = QuantumCircuit(6, 6)
for i in range(6):
    circuit.h(i)
for i in range(6):
    circuit.measure(i, i)

run_plot(circuit, shots=(2**6)*1000, print_total=False, state_to_print='011111')

# Q3
circuit = QuantumCircuit(5, 5)
circuit.h(0)
for i in range(1, 5):
    circuit.cx(0,i)
for i in range(5):
    circuit.measure(i, i)

run_plot(circuit, shots=1000)

# Q4
aliceQubits = QuantumRegister(2, 'a')
aliceCBits = ClassicalRegister(2, 'ac')
bobQubits = QuantumRegister(1, 'b')
bobCBits = ClassicalRegister(1 , 'bc')
circuit = QuantumCircuit ( aliceQubits , bobQubits , aliceCBits ,bobCBits )

circuit.u(np.pi/2, np.pi/2, 0, aliceQubits[0]) # rotate by theta and phi
# entangle 2 qbits to bell state 00
circuit.h(aliceQubits[1])
circuit.cx(aliceQubits[1],bobQubits[0])

circuit.cx(aliceQubits[0],aliceQubits[1])
circuit.h(aliceQubits[0])
circuit.measure(aliceQubits,aliceCBits)

# case 01
circuit.x(bobQubits[0],bobCBits[0]).c_if(aliceCBits,1)

# case 10
circuit.z(bobQubits,bobCBits).c_if(aliceCBits,2)

# case 11
circuit.z(bobQubits,bobCBits).c_if(aliceCBits,3)
circuit.x(bobQubits,bobCBits).c_if(aliceCBits,3)


circuit.measure(bobQubits,bobCBits)

run_plot(circuit, shots=1000)
print()
