# qiskit-bloch-sphere

Bell state circuit with Bloch sphere and Q-sphere visualization using Qiskit Statevector simulation.

## What This Shows

- Bell state |PHI+> = (|00> + |11>) / sqrt(2) built with H + CNOT
- - Bloch sphere for each qubit — entangled qubits land at the origin (mixed state)
  - - Q-sphere — global 2-qubit state view showing amplitudes at |00> and |11>
    - - 1000-shot measurement histogram — always ~50% |00>, ~50% |11>, never |01> or |10>
     
      - ## Key Insight
     
      - Once entangled, individual qubits cannot be described independently. The Bloch vector at the origin IS the visual proof of entanglement.
     
      - ## How to Run
     
      - ```bash
        pip install qiskit qiskit-aer matplotlib
        python bell_state_bloch.py
        ```

        Outputs: bell_state_bloch.png, bell_state_qsphere.png

        ## Tech Stack

        - Qiskit, Qiskit Statevector, Python 3.8+
       
        - ## Author
       
        - Built by [Vijaya Kumari](https://github.com/vijayarjun7) — quantum computing learning journey.
