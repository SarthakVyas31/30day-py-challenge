class TempConv:
    def __init__(self, value: float, from_unit: str, to_unit: str, result: float=None):
        self.value = value
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.result = result
    
    def __repr__(self):
        return f"{self.value} {self.from_unit} = {self.result} {self.to_unit}"