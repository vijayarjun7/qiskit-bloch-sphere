from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_state_qsphere
import matplotlib.pyplot as plt

# 1. Build the Bell state circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

print("Bell State Circuit:")
print(qc.draw("text"))

# 2. Simulate statevector
sv = Statevector.from_instruction(qc)
print("\nStatevector:", sv)

# 3. Bloch sphere - entangled qubits land at origin (mixed state)
fig_bloch = plot_bloch_multivector(sv)
fig_bloch.suptitle("Bloch Spheres: Bell State - Entangled qubits at origin", fontsize=11)
plt.savefig("bell_state_bloch.png", dpi=150, bbox_inches="tight")
print("Saved: bell_state_bloch.png")

# 4. Q-sphere - full 2-qubit state view
fig_q = plot_state_qsphere(sv)
fig_q.suptitle("Q-Sphere: Bell State", fontsize=11)
plt.savefig("bell_state_qsphere.png", dpi=150, bbox_inches="tight")
print("Saved: bell_state_qsphere.png")

plt.show()

# 5. Sample 1000 measurements
print("\n1000-shot measurement (expect ~50% |00>, ~50% |11>):")
counts = sv.sample_counts(shots=1000)
for state, count in sorted(counts.items()):
      bar = "#" * (count // 20)
      print(f"  |{state}> {count:4d}  {bar}")
