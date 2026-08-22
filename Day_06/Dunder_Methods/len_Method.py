"""


class Team:
    def __init__(self,players):
        self.players = players

team = Team(["P1", "P2", "P3", "P4", "P5"])
#print(len(team))                               # Returns an error


"""





class Team:
    def __init__(self,players):
        self.players = players

    def __len__(self):                     # Returns len for user created classes
        return len(self.players)

team = Team(["P1", "P2", "P3", "P4", "P5"])
print(len(team))