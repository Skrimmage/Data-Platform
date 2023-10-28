from dagster import Definitions, load_assets_from_modules

from .assets import f1, nhl, frontend
from . import metrics
from .resources import database_resource, ErgastDatabaseResource, NhlApiResource

all_assets = load_assets_from_modules([f1, nhl, metrics, frontend])

defs = Definitions(
    assets=all_assets,
    resources={
    	"database": database_resource,
        "nhl_api": NhlApiResource,
        "ergast_f1_api": ErgastDatabaseResource
    },
)
