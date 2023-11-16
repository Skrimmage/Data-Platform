from dagster import asset
from ..import constants
import pandas as pd

import glob
import shutil
import os

@asset(
    group_name="frontend",
    deps=["historical_nhl_schedule_file", "nhl_teams_file", "f1_csv_files"]
)
def frontend_build_folder():
    
    df = pd.read_parquet(constants.HISTORICAL_NHL_SCHEDULE_FILE_PATH)
    df.to_csv('frontend/sources/nhl/nhl_historical_schedule.csv')
    
    df = pd.read_parquet(constants.NHL_TEAMS_FILE_PATH)
    df.to_csv('frontend/sources/nhl/nhl_teams.csv')

    src_dir = constants.F1_CSVS_FOLDER_PATH
    dst_dir = constants.F1_CSVS_DEST_FOLDER_PATH
    for csv_file in glob.iglob(os.path.join(src_dir, "*.csv")):
        shutil.copy(csv_file, dst_dir)

