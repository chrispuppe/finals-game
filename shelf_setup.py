import shelve

finals_game_dates = [
                        'JUN 02, 2022',
                        'JUN 05, 2022',
                        'JUN 08, 2022',
                        'JUN 10, 2022',
                        'JUN 13, 2022',
                        'JUN 16, 2022',
                        'JUN 19, 2022'
                        ]

selected_year = '2021'
scoreboard_cache = {
    'scoreboard_save': None,
    'current_timestamp': None
}

finals_roster_cache = {
    'finals_roster_save': None,
    'current_timestamp': None
}


with shelve.open('./vars_persist/vars', 'c') as shelf:
    # shelf['finals_game_dates'] = finals_game_dates
    # shelf['selected_year'] = selected_year
    # shelf['scoreboard_cache'] = scoreboard_cache
    # shelf['finals_team_1'] = 'Golden State Warriors'
    # shelf['finals_team_2'] = 'Boston Celtics'
    # shelf['finals_roster_cache'] = finals_roster_cache
    print(shelf['player_cache'])

    # print(shelf['finals_roster_cache'])
    # for key in shelf.keys():
    #     print(repr(key), repr(shelf[key]))

    shelf.close()