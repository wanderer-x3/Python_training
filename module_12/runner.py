class Runner:
    def __init__(self, name) -> None:
        self.name: str = name
        self.distance: int = 0

    def run(self) -> None:
        self.distance += 10

    def walk(self) -> None:
        self.distance += 5

    def __str__(self):
        return self.name
