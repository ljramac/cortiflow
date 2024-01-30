class APIVersionError(Exception):
    def __init__(self):
        self.message = "API Version not implemented"
