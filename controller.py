# Tutorial:
# https://www.playingnumbers.com/2019/12/how-to-get-nba-data-using-the-nba_api-python-module-beginner/
# NBA API library documentation
# https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md

from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog, teamplayerdashboard
import pandas as pd 
from nba_api.stats.static import teams 
import numpy as np



teams = teams.get_teams()
team_input_name = 'Golden State Warriors'
# GSW = [x for x in teams if x['full_name'] == team_input_name][0]
# GSW_id = GSW['id']


player_input_name = 'Stephen Curry' 
selected_year = '2021'
finals_team_1 = 'Golden State Warriors'
finals_team_2 = 'Dallas Mavericks'

finals_game_dates = ['MAY 18, 2022', 'MAY 20, 2022', 'MAY 13, 2022']

user_list = ['Andrew', 'Chris', 'Jake', 'Todd']

user_selection_1 = ['Stephen Curry', 'MAY 18, 2022', 'Chris', 1]
user_selection_2 = ['Luka Doncic', 'MAY 18, 2022', 'Andrew', 1]
user_selection_3 = ['Klay Thompson', 'MAY 18, 2022', 'Todd', 1]

all_user_selections = [user_selection_1, user_selection_2, user_selection_3]

def get_player_id(player_name):
    player_dict = players.get_players()
    selected_player = [player for player in player_dict if player['full_name'] == f'{player_name}'][0]
    selected_player_id = selected_player['id']
    return selected_player_id

def get_team_abrv(full_team_name):
    selected_team = [x for x in teams if x['full_name'] == full_team_name][0]
    selected_team_abrv = selected_team['abbreviation']
    return selected_team_abrv

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
        team1 = get_team_abrv(finals_team_1)
        team2 = get_team_abrv(finals_team_2)
        if team1 in game and team2 in game:
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

            player_game_stats = {
                'Player Name': player_name,
                'PTS': player_pts,
                'REB': player_reb,
                'AST': player_ast,
                'STL': player_stl,
                'BLK': player_blk,
                'TOT': player_tot,
                'Date': game_day
            }
            player_playoff_stats.append(player_game_stats)
    return player_playoff_stats

def get_team_players(team_name):
    
    selected_team = [x for x in teams if x['full_name'] == team_name][0]
    selected_team_id = selected_team['id']
    player_dict = players.get_players()
    team_roster = []
    players_on_team = teamplayerdashboard.TeamPlayerDashboard(
                                                                team_id=f'{selected_team_id}',
                                                                season_type_all_star='Playoffs'
                                                                )
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
    finals_players = [
                        {'Team Name': team1, 'Roster': team1_roster},
                        {'Team Name': team2, 'Roster': team2_roster}
                    ]
    return finals_players

finals_roster = get_finals_players(finals_team_1, finals_team_2)

def scoreboard():
    user_choices = all_user_selections
    game_data = []
    for choice in user_choices:
        selected_player = get_player_finals_stats(choice[0])
        selected_date = choice[1]
        for player_game in selected_player:
            if selected_date == player_game['Date']:
                player_game.update({'User': choice[2]})
                game_data.append(player_game)
    return game_data

# for player in finals_roster:
#     print(f"Player: {player['full_name']} ID: {player['id']} ")
# for team in teams:
#     print(team)