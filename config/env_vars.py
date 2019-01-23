import os

from str2bool import str2bool


def get_env(key: str, default: str) -> str:
    """ Returns default even if env var is empty string """
    env = os.getenv(key)
    return env if env else default


POSTGRES_HOST: str = get_env(key='POSTGRES_HOST', default='localhost')
POSTGRES_PORT: int = int(get_env(key='POSTGRES_PORT', default='5432'))
POSTGRES_DB: str = get_env(key='POSTGRES_DB', default='al_data')
POSTGRES_USER: str = get_env(key='POSTGRES_USER', default='postgres')
POSTGRES_PASSWORD: str = get_env(key='POSTGRES_PASSWORD', default='postgres')

LOGGING_LEVEL: str = get_env(key='LOGGING_LEVEL', default='info')

DEBUG: bool = str2bool(get_env(key='DEBUG', default='False'))
