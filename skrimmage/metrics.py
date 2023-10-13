from dagster import asset

import plotly.express as px
import plotly.io as pio

import duckdb
import os

from . import constants
from dagster_duckdb import DuckDBResource


@asset(
  deps=["nhl_games_basic"],
  group_name="Charts"
)
def goal_scoring_historical_stat_graph(database: DuckDBResource):
    """
        Bar Chart - The number of games with X number of total goals.
    """

    query = """
        select
            count(*) as games,
            (homeScore + visitingScore) as total
        from raw_nhl_games as g
        group by total
        having total < 20
    """

    results = None
    with database.get_connection() as conn:
        results = conn.execute(query).fetch_df()

    fig = px.bar(results, x='total', y='games')
    fig.write_image(constants.HISTORICAL_TOTAL_GOALS_BAR_CHART_PATH)

@asset(
  deps=["nhl_games_basic", "nhl_teams_basic"],
  group_name="Charts"
)
def team_total_goals_bar_chart(database: DuckDBResource):
    """
       Bar Chart - Top 10 Teams With the Most Wins 
    """

    query = """
        WITH home_games AS (
            select 
                id,
                homeTeamId as teamId,
                homeScore as teamScore,
                visitingScore as opponentScore,
                CASE
                    WHEN homeScore > visitingScore THEN 'win'
                    WHEN homeScore < visitingScore THEN 'loss'
                    ELSE 'tie'
                END AS result
            from raw_nhl_games
            ),
        away_games AS (
            select
                id,
                visitingTeamId as teamId,
                homeScore as opponentScore,
                visitingScore as teamScore,
                CASE
                    WHEN visitingScore > homeScore THEN 'win'
                    WHEN visitingScore < homeScore THEN 'loss'
                    ELSE 'tie'
                END AS result
            from raw_nhl_games),
        games as (
            select id, teamId, teamScore, opponentScore, result from home_games
            UNION ALL
            select id, teamId, teamScore, opponentScore, result from away_games)

        select 
            games.teamId,
            ANY_VALUE(teams.fullName) as name,
            count(CASE WHEN games.result = 'win' THEN games.id END) as wins
        from games
        LEFT JOIN raw_nhl_teams as teams
        ON games.teamId = teams.id
        group by games.teamId
        order by wins desc
        limit 10
    """

    results = None
    with database.get_connection() as conn:
        results = conn.execute(query).fetch_df()

    fig = px.bar(results, x='name', y='wins', title="Top 10 Teams With the Most Wins")
    fig.write_image(constants.HISTORICAL_TOP_10_TEAMS_IN_WINS_BAR_CHART_PATH)
