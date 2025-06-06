import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def smoke_detector_circuit():
    # Qubit 0: sensor de fumaça
    # Qubit 1: decisão de evacuação

    # Aplicar Hadamard ao sensor para simular superposição (estado incerto: fumaça ou não)
    qml.Hadamard(wires=0)

    # Porta CNOT: se sensor detectar fumaça (|1⟩), ativa evacuação (|1⟩ no qubit 1)
    qml.CNOT(wires=[0, 1])

    return qml.probs(wires=[0, 1])

probabilities = smoke_detector_circuit()
print("Probabilidades dos estados (00, 01, 10, 11):", probabilities)

num_shots = 1000
counts = {
    '00': int(probabilities[0] * num_shots),
    '01': int(probabilities[1] * num_shots),
    '10': int(probabilities[2] * num_shots),
    '11': int(probabilities[3] * num_shots),
}

plt.figure(figsize=(8, 6))
plt.bar(counts.keys(), counts.values(), color='skyblue')
plt.xlabel("Estados Quânticos (Qubit1Qubit0)")
plt.ylabel("Contagens")
plt.title("Simulação do Sensor de Fumaça Quântico com PennyLane")
plt.show()