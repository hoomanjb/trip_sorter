class BoardingPass:
    """
    Each boarding card contains information about seat assignment, and means of
    transportation (such as flight number, bus number etc)
    """
    def __init__(self, transportation, origin, destination, seat_assignment=None, gate=None):
        self.transportation = transportation
        self.origin = origin
        self.destination = destination
        self.seat_assignment = seat_assignment
        self.gate = gate

    def __str__(self):
        details = f"{self.transportation} from {self.origin} to {self.destination}."
        if self.seat_assignment:
            details += f" Sit in seat {self.seat_assignment}."
        if self.gate:
            details += f" Gate {self.gate}."
        return details
