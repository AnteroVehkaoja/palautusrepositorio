import requests
from rich.console import Console
from rich.table import Table


class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict["nationality"]
        self.assists = dict["assists"]
        self.goals = dict["goals"]
        self.team = dict["team"]
        self.games = dict["games"]
        self.id = dict["id"]
        self.points = self.goals + self.assists
    
    def __str__(self):

        table = Table(title="stuff")

        table.add_column("name", justify="right", style="cyan", no_wrap=True)
        table.add_column("teams", justify="middle", style="red")
        table.add_column("points", justify="right", style="purple")
        table.add_row(self.name,str(self.team),str(self.goals))


        console = Console()
        return console.print(table)

class Player_reader:
    def __init__(self,url):
        self.response = requests.get(url).json()
        
        
    def get_players(self):

        players = []

        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
        return players

class Player_Stats:
    def __init__(self,players):
        self.players = players


    def top_scores_by_nationality(self,nationality):

        self.nationality = nationality

        players = []
        for player in self.players:
            if player.nationality == self.nationality:
                players.append(player)

        players.sort(key=lambda happy:happy.goals + happy.assists, reverse= True)
        return(players)

    def show_players(self,players):


        table = Table(title="stuff")

        table.add_column("name", justify="right", style="cyan", no_wrap=True)
        table.add_column("teams", justify="middle", style="red")
        table.add_column("points", justify="right", style="purple")
        for player in players:
            table.add_row(player.name,str(player.team),str(player.points))

        console = Console()
        return console.print(table)