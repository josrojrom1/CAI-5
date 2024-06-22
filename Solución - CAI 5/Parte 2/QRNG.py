from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

service = QiskitRuntimeService(channel="ibm_quantum", token="token")
backend = service.backend("ibm_brisbane")

q = QuantumRegister(16,'q')
c = ClassicalRegister(16,'c')
circuit = QuantumCircuit(q,c)
circuit.h(q) # Applies hadamard gate to all qubits
circuit.measure(q,c) # Measures all qubits 

job = backend.run(circuit, shots = 5)
                               
print('Ejecutando...\n')                 
result = job.result()
counts = result.get_counts(circuit)

for i in counts.keys():
    counts[i] = int(i, 2)
    
print('Resultados: ',counts,'\n')