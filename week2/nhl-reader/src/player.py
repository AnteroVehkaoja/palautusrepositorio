import requests
from rich.console import Console
from rich.table import Table


class Player:
    def __init__(self, dict1):
        self.name = dict1['name']
        self.nationality = dict1["nationality"]
        self.assists = dict1["assists"]
        self.goals = dict1["goals"]
        self.team = dict1["team"]
        self.games = dict1["games"]
        self.points = self.goals + self.assists
    def __str__(self):

        table = Table(title="stuff")

        table.add_column("name", justify="right", style="cyan", no_wrap=True)
        table.add_column("teams", justify="middle", style="red")
        table.add_column("points", justify="right", style="purple")
        table.add_row(self.name,str(self.team),str(self.goals))


        console = Console()
        console.print(table)
        return "how to fix"
class PlayerReader:
    def __init__(self,url):
        self.response = requests.get(url).json()
    def get_players(self):
        players = []
        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
        return players

class PlayerStats:
    def __init__(self,players):
        self.players = players


    def top_scores_by_nationality(self,nationality):


        players = []
        for player in self.players:
            if player.nationality == nationality:
                players.append(player)

        players.sort(key=lambda happy:happy.goals + happy.assists, reverse= True)
        return players

    def show_players(self,players):
        table = Table(title="stuff")

        table.add_column("name", justify="right", style="cyan", no_wrap=True)
        table.add_column("teams", justify="middle", style="red")
        table.add_column("points", justify="right", style="purple")
        for player in players:
            table.add_row(player.name,str(player.team),str(player.points))

        console = Console()
        return console.print(table)