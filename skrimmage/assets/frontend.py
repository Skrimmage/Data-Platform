from dagster import asset
from ..import constants
import pandas as pd

@asset(
    group_name="frontend",
    deps=["historical_nhl_schedule_file", "nhl_teams_file"]
)
def frontend_build_folder():
    
    df = pd.read_parquet(constants.HISTORICAL_NHL_SCHEDULE_FILE_PATH)
    df.to_csv('skrimmage-frontend/data/nhl_historical_schedule.csv')
    
    df = pd.read_parquet(constants.NHL_TEAMS_FILE_PATH)
    df.to_csv('skrimmage-frontend/data/nhl_teams.csv')

