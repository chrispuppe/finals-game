# Tutorial:
# https://www.playingnumbers.com/2019/12/how-to-get-nba-data-using-the-nba_api-python-module-beginner/
# NBA API library documentation
# https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md

from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog, playerprofilev2
import pandas as pd 
from nba_api.stats.static import teams 
from nba_api.stats.library.parameters import SeasonAll
import numpy as np



# print(player_dict)
# Use ternary operator or write function 
# Names are case sensitive
# bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
# bron_id = bron['id']



# print(selected_player_id)
# print(bron['full_name'] + ' Player ID: ' + str(bron_id))

# find team Ids

teams = teams.get_teams()
team_input_name = 'Golden State Warriors'
# for team in teams:
#     print(team['full_name'])
GSW = [x for x in teams if x['full_name'] == team_input_name][0]
GSW_id = GSW['id']

# print(GSW['full_name'] + ' Team ID: ' + str(GSW_id))

#Call the API endpoint passing in lebron's ID & which season

player_input_name = 'Stephen Curry' 
selected_year = '2021'
finals_team_1 = 'GSW'
finals_team_2 = 'DEN'

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

# print(get_player_finals_stats(player_input_name))

def get_team_players(team_name):
    selected_team = [x for x in teams if x['full_name'] == team_name][0]
    selected_team_id = selected_team['id']
    team_roster = []
    player_dict = players.get_players()
    for player in player_dict:
        selected_player_id = player['id']
        player_next_game = playerprofilev2.PlayerProfileV2(player_id=f'{selected_player_id}')
        df_player_next_game = player_next_game.get_data_frames()[14]
        try:
            if df_player_next_game.loc[0, 'PLAYER_TEAM_ID'] == selected_team_id:
                team_roster.append(player)
        except KeyError:
            print(player)

    return team_roster

    #     if 
    # [player for player in player_dict if player['full_name'] == f'{player_name}'][0]
    # [x for x in teams if x['full_name'] == team_input_name][0]
    # playerprofilev2.NextGame(player_id=f'{player}')
    # df_player_input = gamelog_player_input.get_data_frames()[0]

get_team_players(team_input_name)