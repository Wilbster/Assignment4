class OutOfTheRealmError(Exception):

    def __init__(self, message="You have reached the world's edge. "
                               "None but dragons play past here. You should turn back."):
        self.message = message
        super().__init__(self.message)
