# Tutorial:
# https://www.playingnumbers.com/2019/12/how-to-get-nba-data-using-the-nba_api-python-module-beginner/
# NBA API library documentation
# https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md

from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog, commonallplayers
import pandas as pd 
from nba_api.stats.static import teams 
from nba_api.stats.library.parameters import SeasonAll
import numpy as np

player_dict = players.get_players()

# print(player_dict)
# Use ternary operator or write function 
# Names are case sensitive
# bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
# bron_id = bron['id']

player_input_name = 'Stephen Curry'
selected_player = [player for player in player_dict if player['full_name'] == f'{player_input_name}'][0]
selected_player_id = selected_player['id']
# print(selected_player_id)
# print(bron['full_name'] + ' Player ID: ' + str(bron_id))

# find team Ids

teams = teams.get_teams()
team_input_name = 'Golden State Warriors'
# print(teams)
GSW = [x for x in teams if x['full_name'] == team_input_name][0]
GSW_id = GSW['id']

# print(GSW['full_name'] + ' Team ID: ' + str(GSW_id))

#Call the API endpoint passing in lebron's ID & which season
 
selected_year = '2021'
  
gamelog_player_input = playergamelog.PlayerGameLog(player_id=f'{selected_player_id}', season_type_all_star='Playoffs', season=selected_year)


# # print(gamelog_player_input.DataSet.player_game_log)
# #Converts gamelog object into a pandas dataframe
# #can also convert to JSON or dictionary  

df_player_input = gamelog_player_input.get_data_frames()[0]

finals_team_1 = 'GSW'
finals_team_2 = 'DEN'

number_of_games = len(df_player_input)
for i in range(0, number_of_games):
    game = df_player_input.loc[i,'MATCHUP']
    if finals_team_1 in game and finals_team_2 in game:
        if df_player_input.loc[i,'WL'] == 'W':
            results = 'won'
        else:
            results = 'lost'
        player_score = df_player_input.loc[i,'PTS']
        game_day = df_player_input.loc[i,'GAME_DATE']
        print(f'On {game_day} the {game} and the {team_input_name} {results}, {player_input_name} had {player_score}pts.')


# labels = []
# for game in df_player_input:
#     labels.append(game)
# df = pd.DataFrame(df_player_input, index=labels)

# print("Select specific columns:")
# print(df[['GAME_DATE', 'MATCHUP']])
# print(df.loc[[0]])
# If you want all seasons, you must import the SeasonAll parameter 


# gamelog_player_input_all = playergamelog.PlayerGameLog(player_id='2544', season = SeasonAll.all)

# df_bron_games_all = gamelog_player_input_all.get_data_frames()

# for item in gamelog_player_input:
#     print(item)

#### Find players on specified team ####
# all_teams = commonallplayers.CommonAllPlayers('TEAM_ID'==1610612744)
# print(all_teams)