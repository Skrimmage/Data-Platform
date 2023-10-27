from dagster import asset
from ..resources import ErgastDatabaseResource
from .. import constants

@asset(
    group_name="Extract",s
    key_prefix="f1"
)
def f1_csv_files(ergast_f1_api: ErgastDatabaseResource):
    zip = ergast_f1_api().fetch_csv_zip()
    zip.extractall(constants.F1_CSVS_FOLDER_PATH)
    