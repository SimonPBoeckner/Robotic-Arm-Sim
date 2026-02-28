from config.config import Config

class Plotter():
    def __init__(self, config: Config = None):
        if config == None:
            self.config = Config()
        else:
            self.config = config

    def polarToCartesian(self):
        pass