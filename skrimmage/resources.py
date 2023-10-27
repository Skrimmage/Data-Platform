# Resources for re-usability https://docs.dagster.io/concepts/resources#defining-a-resource

from dagster import EnvVar, ConfigurableResource
from dagster_duckdb import DuckDBResource
import requests, zipfile, io
from requests import Response

# DuckDB, most configuration is within the DuckDBResource

database_resource = DuckDBResource(
    database=EnvVar("DUCKDB_DATABASE")      # replaced with environment variable
)


class NhlApiResource(ConfigurableResource):
    """
        NHL API Resource
    """
    def __init__(self):
        pass

    def _api_request(self, endpoint: str) -> Response:
        return requests.get(
            f"https://api.nhle.com/{endpoint}",
            headers={"user-agent": "dagster"},
        )

    def fetch_historical_nhl_schedule(self):
        """
            Input: The raw JSON file for every NHL game in history, up until the last regular season of the current season.
            Output: Creates a parquet file with every game
        """
        raw_games = self._api_request(
            "stats/rest/en/game"
        )

        return raw_games.json()['data']
    
    def get_historical_nhl_teams(self):
        """
            Input: The raw JSON file for every NHL game in history, up until the last regular season of the current season.
            Output: Creates a parquet file with every game
        """
        raw_games = self._api_request(
            "stats/rest/en/team"
        )

        return raw_games.json()['data']


class ErgastDatabaseResource(ConfigurableResource):
    def fetch_csv_zip(self):
        """
            Get CSV zips
        """

        r = requests.get("http://ergast.com/downloads/f1db_csv.zip")
        return zipfile.ZipFile(io.BytesIO(r.content))
        