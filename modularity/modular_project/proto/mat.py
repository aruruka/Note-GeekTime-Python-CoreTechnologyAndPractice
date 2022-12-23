class Matrix(object):
    def __init__(self, data) -> None:
        self.data = data
        self.n = len(data)
        self.m = len(data[0])
