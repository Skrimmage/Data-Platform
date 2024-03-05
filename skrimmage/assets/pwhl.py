from dagster import asset
from pydantic import BaseModel

import json
import requests


class Team(BaseModel):
    id: str | int
    name: str
    nickname: str
    team_code: str
    division_id: str | int
    logo: str
    league: str = "PWHL"

class Standings(BaseModel):
    team_rank: str
    team: str
    team_code: str
    games_playe: str
    points: str
    wins: str
    non_reg_wins: str
    losses: str
    non_reg_losses: str
    goals_for: str
    goals_against: str
    games_remaining: str

URLS = {
    "teams": "https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=teamsForSeason&season=2&key=694cfeed58c932ee&client_code=pwhl&site_id=2",
    "standings_regular": "https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=teams&groupTeamsBy=league&context=overall&site_id=2&season=1&special=false&key=694cfeed58c932ee&client_code=pwhl&league_id=1&division=undefined&sort=points&lang=en",
    "standings_playoffs": "https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=teams&groupTeamsBy=league&context=overall&site_id=2&season=2&special=false&key=694cfeed58c932ee&client_code=pwhl&league_id=1&division=undefined&sort=points&lang=en",
}

@asset
def get_pwhl_teams():
    response = requests.get(URLS['teams'])

    team_text = response.text[:-1]
    team_text = team_text[1:]
    team_data = json.loads(team_text)['teams']

    teams = []
    for d in team_data:
        if d['id'] != -1:
            team = Team(**d)
            teams.append(team)

@asset
def get_standings():
    response = requests.get(URLS['standings_regular'])

    standings_text = response.text[:-1]
    standings_text = standings_text[1:]

    standings_data = json.loads(standings_text)[0]['sections'][0]['data']
    s_teams = []
    for t in standings_data:
        s_teams.append(Standings(**t['row']))

    s_teams[0]