from dagster import Definitions, load_assets_from_modules

from . import assets
from . import metrics
from .resources import database_resource

all_assets = load_assets_from_modules([assets, metrics])

defs = Definitions(
    assets=all_assets,
    resources={
    	"database": database_resource,
    },
)
