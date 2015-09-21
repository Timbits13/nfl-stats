"""
A demo app that will print stats from this week's games.
"""
import datetime

from pynfl import schedule
from pynfl import stats
from pynfl import utils

l = schedule.Load()
l.read_data()

if len(l.games) == 0:
    l.get_data()
    l.write_data()
    l.read_data()

d = datetime.date.today()

week = utils.get_game_week(d)

week_games = []

for game in l.games:
    if int(game.week) == int(week['week']):
        week_games.append(game)

for game in week_games:
    g = stats.Load(game_id=game.id)
    g.get_data()
    g.write_data()
    try:
        print g.game_obj.__dict__
    except:
        pass