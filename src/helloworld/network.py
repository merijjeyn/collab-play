from .game import Game


class SingletonMeta(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Network(metaclass=SingletonMeta):
    def set_game_instance(self, game: Game):
        self.game = game
        pass

    def start_host_connection():
        # Can be an endless loop on a different thread
        pass

    def start_player_connection():
        # setup the socket 
        pass

    def get_players_in_room():
        pass

    def make_action():
        # use the socket to send action
        pass

    def __del__():
        # destroy the player socket
        pass