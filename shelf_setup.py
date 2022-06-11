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

with shelve.open('./vars_persist/vars', 'c') as shelf:
    # shelf['finals_game_dates'] = finals_game_dates
    # shelf['selected_year'] = selected_year
    # shelf['scoreboard_cache'] = scoreboard_cache
    # shelf['finals_team_1'] = 'Golden State Warriors'
    # shelf['finals_team_2'] = 'Boston Celtics'
    print(shelf['finals_team_1'], shelf['finals_team_2'])

shelf.close()