class Magnitude:

    symbolist = [("y", "yotta"), "banana", "cherry"]

    def __init__(self, unit, submultiples, symbols):
        self.unit = unit
        self.submultiples = submultiples
        self.symbols = symbols

magnitud = Magnitude(36, "k", "g")
print(magnitud.magnitude)
