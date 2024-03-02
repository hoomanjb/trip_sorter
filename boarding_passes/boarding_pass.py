class BoardingPass:
    """
    Each boarding card contains information about seat assignment, and means of
    transportation (such as flight number, bus number etc)
    """
    def __init__(self, transport_type: str, origin: str, destination: str,
                 transport_id: str | None = None, seat_assignment: str | None = None,
                 gate: str | None = None, extra: dict | None = None):
        self.transport_type = transport_type
        self.origin = origin
        self.destination = destination
        self.transport_id = transport_id
        self.seat_assignment = seat_assignment
        self.gate = gate
        self.extra = extra  # For additional info like baggage drop

    def __str__(self):
        details = f"{self.transport_type} from {self.origin} to {self.destination}."
        if self.transport_id:
            details += f" Transport Id is {self.transport_id}."
        if self.seat_assignment:
            details += f" Sit in seat {self.seat_assignment}."
        if self.gate:
            details += f" Gate {self.gate}."
        if self.extra:
            details += f" Extra Data is {self.gate}."
        return details
