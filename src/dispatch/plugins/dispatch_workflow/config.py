from starlette.datastructures import URL

from dispatch.config import config, Secret

CAMUNDA_API_URL=config("CAMUNDA_API_URL", cast=URL)
