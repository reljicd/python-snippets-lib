from decorator import contextmanager
from sqlalchemy.orm import Session

from db.scoped_session import session_factory


@contextmanager
def session_scope() -> Session:
    """Provide a transactional scope around a series of operations."""
    session = session_factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
