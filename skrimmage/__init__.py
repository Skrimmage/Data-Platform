from dagster import Definitions, AssetSelection, define_asset_job, load_assets_from_modules, ScheduleDefinition

from .assets import f1, nhl, frontend
from . import metrics
from .resources import database_resource, ErgastDatabaseResource, NhlApiResource

all_assets = load_assets_from_modules([f1, nhl, metrics, frontend])

daily_refresh_job = define_asset_job("daily_refresh_job", selection=AssetSelection.all())

daily_refresh_schedule = ScheduleDefinition(
    job=daily_refresh_job,
    cron_schedule="0 8 * * *"
)

defs = Definitions(
    assets=all_assets,
    jobs=[daily_refresh_job],
    resources={
    	"database": database_resource,
        "nhl_api": NhlApiResource,
        "ergast_f1_api": ErgastDatabaseResource
    },
    schedules=[daily_refresh_schedule],
)


