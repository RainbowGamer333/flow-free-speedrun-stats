import srcomapi, srcomapi.datatypes as dt

base_src_api = "https://www.speedrun.com/api"
api = srcomapi.SpeedrunCom(user_agent='RainbowGamer333/v0')
api.debug = 1

flow_games = {
    'flow_free': '46woj31r',
    'flow_bridges': '369px8l1',
    'flow_hexes': 'pdvzq246',
    'flow_warps': 'pd0wvq01',
    'flow_shapes': 'k6qpnzxd'
}

def get_game_runs(gameID):
    runs = {}
    game = dt.Game(api, data=api.get(f"games/{gameID}"))
    no_hints_category = next((cat for cat in game.categories if cat.name == 'No Hints'), None)
    for level in game.levels:
        leaderboard = dt.Leaderboard(api, data=api.get(
            f"leaderboards/{game.id}/level/{level.id}/{no_hints_category.id}"))
        runs.update({level.name: leaderboard.runs})
        print(level.name + " - added")
    return runs

def get_all_games_runs():
    for game, id in flow_games.items():
        _ = get_game_runs(id)


if __name__ == '__main__':
    get_all_games_runs()