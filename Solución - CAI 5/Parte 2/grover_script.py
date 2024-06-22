from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import numpy as np
 
QiskitRuntimeService(channel="ibm_quantum", token="token")
service = QiskitRuntimeService()
#backend = service.backend(name="ibm_brisbane")

# Definir el número de qubits
n = 3
# Crear un circuito cuántico con n qubits
qc = QuantumCircuit(n)
# Aplicar la transformada de Hadamard a todos los qubits
qc.h(range(n))
# Aplicar la función de oráculo (en este caso, buscar el estado '101')
qc.z(2)
qc.cx(0, 1)
qc.cx(1, 2)
# Aplicar la transformada de Grover
qc.h(range(n))
qc.z(range(n))
qc.h(range(n))
# Medir los qubits
qc.measure_all()
# Ejecutar el circuito en un simulador de IBM
backend = Aer.get_backend('ibmq_qasm_simulator')
job = execute(qc, backend, shots=1024)
result = job.result()
# Obtener la distribución de probabilidad de los resultados
counts = result.get_counts(qc)
# Mostrar la distribución de probabilidad
plot_histogram(counts)