from player import PlayerReader, PlayerStats

def main(nationality):
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    nhl = PlayerReader(url)
    all_players = nhl.get_players()
    stats = PlayerStats(all_players)

    nationality_players = stats.top_scores_by_nationality(str(nationality))

    stats.show_players(nationality_players)




if __name__ == "__main__":
    nationality2 = input("Nationality: USA/FIN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS:  ")
    main(nationality2)
