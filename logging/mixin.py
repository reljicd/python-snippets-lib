import logging
import sys


class LoggingMixin(object):
    """ Convenience super-class to have a logger
    configured with the class name """

    @property
    def log(self) -> logging.Logger:
        try:
            return self._log
        except AttributeError:
            self._log = logging.getLogger(
                self.__class__.__module__ + '.' + self.__class__.__name__
            )

            formatter = logging.Formatter(
                '%(asctime)s %(name)-12s %(levelname)s: %(message)s')

            stdout_handler = logging.StreamHandler(sys.stdout)
            stdout_handler.setFormatter(formatter)
            stdout_handler.setLevel(logging.DEBUG)

            stderr_handler = logging.StreamHandler(sys.stderr)
            stderr_handler.setFormatter(formatter)
            stderr_handler.setLevel(logging.WARNING)

            self._log.addHandler(stdout_handler)
            self._log.addHandler(stderr_handler)
            self._log.setLevel(level=logging.INFO)  # type: ignore

            return self._log
