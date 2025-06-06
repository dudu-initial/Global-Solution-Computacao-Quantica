# Global-Solution-Computacao-Quantica
Simulador de Sensor de Fumaça Quântico
Este projeto demonstra um conceito básico de computação quântica utilizando o Qiskit para simular um "sensor de fumaça quântico" e um sistema de decisão de evacuação. Ele ilustra como as propriedades quânticas, como superposição e emaranhamento, podem ser aplicadas em um cenário simples.

# Como Funciona?
O circuito quântico é composto por dois qubits:

Qubit 0 (Sensor de Fumaça): Este qubit representa o sensor. Ele é colocado em um estado de superposição (usando uma porta Hadamard), o que significa que ele existe simultaneamente em dois estados: "sem fumaça" (∣0⟩) e "com fumaça" (∣1⟩). Isso simula a incerteza ou a capacidade de detectar ambos os estados.
Qubit 1 (Decisão de Evacuação): Este qubit representa a decisão de evacuação. Ele é emaranhado com o Qubit 0 através de uma porta CNOT (Controlled-NOT). A porta CNOT garante que:
Se o Qubit 0 estiver em ∣0⟩ (sem fumaça), o Qubit 1 permanecerá em ∣0⟩ (sem evacuação).
Se o Qubit 0 estiver em ∣1⟩ (com fumaça), o Qubit 1 será invertido para ∣1⟩ (evacuação ativada).
O resultado é que o estado do Qubit 1 está diretamente correlacionado com o estado do Qubit 0 devido ao emaranhamento. Quando o sistema é medido, observamos os estados de ambos os qubits, revelando se a "fumaça" foi detectada e se a "evacuação" foi acionada.

# Estados Esperados
Devido à superposição inicial no Qubit 0 e o emaranhamento pela porta CNOT, os únicos resultados possíveis após a medição serão:

∣00⟩: (Sensor: sem fumaça, Evacuação: não) - Ocorre em aproximadamente 50% das vezes.
∣11⟩: (Sensor: com fumaça, Evacuação: sim) - Ocorre em aproximadamente 50% das vezes.
Os estados ∣01⟩ e ∣10⟩ não são observados, demonstrando a correlação criada pelo emaranhamento.

# Requisitos
Para rodar este código, você precisará ter o Python e o Qiskit instalados.

Python 3.x

Qiskit: Você pode instalar o Qiskit usando pip:



pip install qiskit
pip install matplotlib # Para plotar o histograma
Como Rodar
Crie um arquivo chamado smoke_detector_quantum.py.

Copie e cole o seguinte código no arquivo:



from qiskit import QuantumCircuit
from qiskit.primitives import Sampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Criar o circuito com 2 qubits
# Qubit 0: sensor de fumaça
# Qubit 1: decisão de evacuação
circuit = QuantumCircuit(2)

# Aplicar Hadamard ao sensor para simular superposição (estado incerto: fumaça ou não)
circuit.h(0)

# Porta CNOT: se sensor detectar fumaça (|1⟩), ativa evacuação (|1⟩ no qubit 1)
circuit.cx(0, 1)

# Medição de todos os qubits
circuit.measure_all()

# Mostrar o circuito (opcional)
print(circuit.draw('text'))

# Simulação com Sampler (sem Aer)
sampler = Sampler()
job = sampler.run(circuit)
result = job.result()

# Obter os resultados
counts = result.quasi_dists[0]
print("Resultados da simulação:", counts)

# Plotar o histograma
plot_histogram(counts)
plt.show()
Salve o arquivo.

Abra seu terminal ou prompt de comando.

Navegue até o diretório onde o arquivo smoke_detector_quantum.py está salvo.

Execute o script Python:


python smoke_detector_quantum.py
Saída do Programa
Ao executar o script, você verá:

O diagrama do circuito quântico em formato de texto, mostrando as portas aplicadas aos qubits.
Os resultados da simulação, que mostram a frequência com que cada estado final (por exemplo, 00, 11) foi observado.
Um histograma visualizando essas contagens, mostrando a distribuição dos resultados.
