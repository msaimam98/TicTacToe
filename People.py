class Player:
    """
    Initialize a new User

    """
    def __init__(self, name: str, token: int) ->  None:

        self.name = name
        self.tracking_num = token

    def give_name(self) -> str:
        """Gives the name of the player"""
