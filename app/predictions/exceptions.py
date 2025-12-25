class CouldNotCreatePrediction(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    @classmethod
    def becauseGameDoesNotExist(cls):
        return cls()
