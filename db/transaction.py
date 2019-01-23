import functools

from db.scoped_session import Session


def transaction(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        Session.close()

        func(*args, **kwargs)

        try:
            Session.commit()
        except Exception:
            Session.rollback()
            raise
        finally:
            Session.close()

    return wrapper
