import json

class Configurator:

    def __init__ (self):
        with open('config.json') as json_data_file:
            self.data = json.load(json_data_file)
    
    def getConfigData(self):
        return self.data
