
class BaseItem:
    def __init__(self, name="MissingName", path="MissingPath"):
        self.name = name
        self.path = path

    def print(self):
        print(self.name)
