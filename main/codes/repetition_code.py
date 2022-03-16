from main.Code import Code
from main.Qubit import Qubit
from main.Check import Check
from main.enums import Pauli, State


class RepetitionCode:
    def __init__(self, distance):

        self.data_qubits = {i*2: Qubit((i), State.Zero)
                            for i in range(distance)}
        self.init_checks(distance)

    def init_checks(self, distance):
        self.schedule = []
        for i in range(distance-1):
            operators = {self.data_qubits[2*i]: Pauli.Z,
                         self.data_qubits[2*(i+1)]: Pauli.Z}
            center = 2*i + 1
            ancilla = Qubit(center, State.Zero)
            new_check = Check(operators, ancilla, center)
            self.schedule.append(new_check)
