# Tutorial:
# https://www.playingnumbers.com/2019/12/how-to-get-nba-data-using-the-nba_api-python-module-beginner/
# NBA API library documentation
# https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md

from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog, teamplayerdashboard
from nba_api.stats.static import teams 
from models import User, Selection
from __init__ import db
import time

# teams = []
player_dict = []
teams = teams.get_teams()
# player_dict = players.get_players()

scoreboard_cache = {
    'scoreboard_save': None,
    'current_timestamp': None
}

selected_year = '2021'
finals_team_1 = 'Golden State Warriors'
finals_team_2 = 'Boston Celtics'

finals_game_dates = [
                        'JUN 02, 2022',
                        'JUN 05, 2022',
                        'JUN 08, 2022',
                        'JUN 10, 2022',
                        'JUN 13, 2022',
                        'JUN 16, 2022',
                        'JUN 19, 2022'
                        ]


def user_list():
    users = []
    all_db_users = User.query.all()
    for user in all_db_users:
        user_dict = {'username': user.username, 'id': user.id}
        users.append(user_dict)
    sortedByName = sorted(users, key=lambda x: x['username'])
    return sortedByName


def all_user_selections():
    user_selections = []
    all_db_selections = Selection.query.all()
    for selection in all_db_selections:
        selection_username = db.session.query(User).get(selection.id).username
        selection_arr = [
                            selection.selected_player,
                            selection.game_date,
                            selection_username,
                            selection.selection_id
                            ]
        user_selections.append(selection_arr)
    return user_selections


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

# finals_roster = get_finals_players(finals_team_1, finals_team_2)
finals_roster = []

def scoreboard():
    return scoreboard_cache['scoreboard_save']

    # if scoreboard_cache['current_timestamp'] == None or time.time() - scoreboard_cache['current_timestamp'] > 120:
    #     user_choices = all_user_selections()
    #     game_data = []
    #     user_scores = []
    #     current_users_list = user_list()
    #     for list_user in current_users_list:
    #         user_for_board = {
    #                             'Username': list_user['username'],
    #                             'Score': 0
    #                             }
    #         user_scores.append(user_for_board)
    #     for choice in user_choices:
    #         choice_count = 0
    #         selected_player = get_player_finals_stats(choice[0])
    #         selected_date = choice[1]
    #         selected_user = choice[2]
    #         seleted_id = choice[3]
    #         for player_game in selected_player:
    #             if selected_date == player_game['Date']:
    #                 player_game.update({'User': selected_user})
    #                 player_game.update({'Selection_id': seleted_id})
    #                 game_data.append(player_game)
    #                 choice_count += 1
    #                 for board_user in user_scores:
    #                     if board_user['Username'] == player_game['User']:
    #                         board_user['Score'] += int(player_game['TOT'])
    #         if choice_count == 0:
    #             player_game = {
    #                 'Player Name': choice[0],
    #                 'PTS': 0,
    #                 'REB': 0,
    #                 'AST': 0,
    #                 'STL': 0,
    #                 'BLK': 0,
    #                 'TOT': 0,
    #                 'Date': selected_date,
    #                 'User': selected_user,
    #                 'Selection_id': seleted_id
    #             }
    #             game_data.append(player_game)
    #     scoreboard_cache['scoreboard_save'] = [game_data, user_scores]
    #     scoreboard_cache['current_timestamp'] = time.time()
    #     return scoreboard_cache['scoreboard_save']
    # else:
    #     return scoreboard_cache['scoreboard_save']

def clear_scoreboard_cache():
    scoreboard_cache['current_timestamp'] = None


if __name__ == "__main__":
    print(player_dict)
    print(teams)