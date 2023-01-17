import os

from str2bool import str2bool

POSTGRES_HOST: str = os.getenv(key='POSTGRES_HOST', default='localhost')
POSTGRES_PORT: int = int(os.getenv(key='POSTGRES_PORT', default='5432'))
POSTGRES_DB: str = os.getenv(key='POSTGRES_DB', default='al_data')
POSTGRES_USER: str = os.getenv(key='POSTGRES_USER', default='postgres')
POSTGRES_PASSWORD: str = os.getenv(key='POSTGRES_PASSWORD', default='postgres')

LOGGING_LEVEL: str = os.getenv(key='LOGGING_LEVEL', default='info')

DEBUG: bool = str2bool(os.getenv(key='DEBUG', default='False'))
