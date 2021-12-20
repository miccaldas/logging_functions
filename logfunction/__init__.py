import functools
from loguru import logger


def logger_wraps(*, entry=True, exit=True, level="DEBUG"):

    def func_wrapper(func):
        """Function taken from the Loguru documentation.
           Creates a decorator that logs values going in
           and out of a function.
           https://tinyurl.com/y55kh9oa"""

        name = func.__name__

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            logger_ = logger.opt(depth=1)
            if entry:
                logger_.log(level, "Entering '{}' (args={}, kwargs={})", name, args, kwargs)   # noqa: E501
            result = func(*args, **kwargs)
            if exit:
                logger_.log(level, "Exiting '{}' (result={})", name, result)
            return result

        return wrapped

    return func_wrapper

    if __name__ == "__main__":
        func_wrapper()
