import shelve

with shelve.open('./vars_persist/vars', 'c') as shelf:
    shelf['finals_team_1'] = 'Golden State Warriors'
    shelf['finals_team_2'] = 'Boston Celtics'

with shelve.open('./vars_persist/shelf-example', 'r') as shelf:
    for key in shelf.keys():
        print(repr(key), repr(shelf[key]))

with shelve.open('./vars_persist/vars', 'c') as shelf:
    shelf['finals_team_1'] = 'Not a team'

with shelve.open('./vars_persist/shelf-example', 'r') as shelf:
    print(shelf['finals_team_1'])

shelf.close()