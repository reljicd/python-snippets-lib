from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import (Session as AlchemySession, scoped_session,
                            sessionmaker)

from config.env_vars import (LOGGING_LEVEL, POSTGRES_DB, POSTGRES_HOST,
                             POSTGRES_PASSWORD, POSTGRES_PORT,
                             POSTGRES_USER)

engine: Engine = create_engine(
    f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@'
    f'{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}',
    # poolclass=NullPool,
    echo=True if LOGGING_LEVEL == 'debug' else False)
session_factory: Callable[..., AlchemySession] = sessionmaker(bind=engine)

Session: AlchemySession = scoped_session(session_factory)
