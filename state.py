class State:
    def __init__(self, name, id, description):
        self.name = name
        self.id = id
        self.description = description
    
    def getDetails(self):
        details =   "State name:"+self.name+" / "+"State id:"+ self.id +" / "+"State description:"+ self.description
        return details