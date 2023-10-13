import sqlite3
import requests
import pyarrow.parquet as pq
import pandas as pd
import pyarrow as pa

from . import constants
from dagster import asset
from dagster_duckdb import DuckDBResource


@asset(
    group_name="Extract"
)
def historical_nhl_schedule_file():
    """
        Input: The raw JSON file for every NHL game in history, up until the last regular season of the current season.
        Output: Creates a parquet file with every game
    """
    raw_games = requests.get(
        "https://api.nhle.com/stats/rest/en/game"
    )

    data = raw_games.json()['data']

    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, constants.HISTORICAL_NHL_SCHEDULE_FILE_PATH)


@asset(
    deps=["historical_nhl_schedule_file"],
    group_name="Load"
)
def nhl_games_basic(database: DuckDBResource):
    """
        Input: parquet file with every game
        Output: writes to raw_nhl_games in a DuckDB instance
    """

    sql_query = f"""
		create or replace table raw_nhl_games as (
            select
                id,
                easternStartTime,
                gameDate,
                gameNumber,
                gameScheduleStateId,
                gameStateId,
                gameType,
                homeScore,
                homeTeamId,
                period,
                season,
                visitingScore,
                visitingTeamId
            from '{constants.HISTORICAL_NHL_SCHEDULE_FILE_PATH}'
        );
	"""

    with database.get_connection() as conn:
	    conn.execute(sql_query)

@asset(
    group_name="Extract"
)
def nhl_teams_file():
    """
        Write parquet file of NHL Teams, pulled from NHL API
    """

    raw_teams = requests.get(
        'https://api.nhle.com/stats/rest/en/team'
    )

    data = raw_teams.json()['data']

    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, constants.NHL_TEAMS_FILE_PATH)

@asset(
    deps=["nhl_teams_file"],
    group_name="Load"
)
def nhl_teams_basic(database: DuckDBResource):
    """
        Load DuckDB with basic team information
    """

    sql_query = f"""
		create or replace table raw_nhl_teams as (
            select
                id,
                franchiseId, 
                fullName, 
                leagueId, 
                rawTricode, 
                triCode
            from '{constants.NHL_TEAMS_FILE_PATH}'
        );
	"""

    with database.get_connection() as conn:
	    conn.execute(sql_query)