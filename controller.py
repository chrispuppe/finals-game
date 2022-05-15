# Tutorial:
# https://www.playingnumbers.com/2019/12/how-to-get-nba-data-using-the-nba_api-python-module-beginner/
# NBA API library documentation
# https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md

from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog, playerprofilev2, teamplayerdashboard
import pandas as pd 
from nba_api.stats.static import teams 
from nba_api.stats.library.parameters import SeasonAll
import numpy as np



teams = teams.get_teams()
team_input_name = 'Golden State Warriors'
# GSW = [x for x in teams if x['full_name'] == team_input_name][0]
# GSW_id = GSW['id']


player_input_name = 'Stephen Curry' 
selected_year = '2021'
finals_team_1 = 'GSW'
finals_team_2 = 'MEM'

finals_game_dates = ['APR 27, 2022', 'APR 24, 2022', 'APR 21, 2022 	']

def get_player_id(player_name):
    player_dict = players.get_players()
    selected_player = [player for player in player_dict if player['full_name'] == f'{player_name}'][0]
    selected_player_id = selected_player['id']
    return selected_player_id


def get_player_finals_stats(player_name):
    selected_player_id = get_player_id(player_name)
    gamelog_player_input = playergamelog.PlayerGameLog(
                                                        player_id=f'{selected_player_id}', 
                                                        season_type_all_star='Playoffs', 
                                                        season=selected_year)
    df_player_input = gamelog_player_input.get_data_frames()[0]
    number_of_games = len(df_player_input)
    player_playoff_stats = []
    for i in range(0, number_of_games):
        game = df_player_input.loc[i,'MATCHUP']
        if finals_team_1 in game and finals_team_2 in game:
            player_pts = df_player_input.loc[i,'PTS']
            player_reb = df_player_input.loc[i,'REB']
            player_ast = df_player_input.loc[i,'AST']
            player_stl = df_player_input.loc[i,'STL']
            player_blk = df_player_input.loc[i,'BLK']
            player_tot = (
                player_pts
                + player_reb * 2
                + player_ast * 2
                + player_stl * 3
                + player_blk * 3
            )
            game_day = df_player_input.loc[i,'GAME_DATE']

            player_game_stats = [
                player_name,
                player_pts,
                player_reb,
                player_ast,
                player_stl,
                player_blk,
                player_tot,
                game_day
            ]
            player_playoff_stats.append(player_game_stats)
    return player_playoff_stats

def get_team_players(team_name):
    
    selected_team = [x for x in teams if x['abbreviation'] == team_name][0]
    selected_team_id = selected_team['id']
    player_dict = players.get_players()
    team_roster = []
    players_on_team = teamplayerdashboard.TeamPlayerDashboard(team_id=f'{selected_team_id}')
    df_players_on_team = players_on_team.get_data_frames()[1]
    number_of_players = len(df_players_on_team)

    for i in range(0, number_of_players):
        for player in player_dict:
            if player['id'] == df_players_on_team.loc[i,'PLAYER_ID']:
                team_roster.append(player)
    return team_roster

def get_finals_players(team1, team2):
    team1_roster = get_team_players(team1)
    team2_roster = get_team_players(team2)
    finals_players = team1_roster + team2_roster
    return finals_players

finals_roster = get_finals_players(finals_team_1, finals_team_2)

# for player in finals_roster:
#     print(f"Player: {player['full_name']} ID: {player['id']} ")