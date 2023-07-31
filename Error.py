class MyError(Exception):
    def __init__(self, massage) -> None:
        self.text = massage
    
    def __str__(self) -> str:
        return self.text
