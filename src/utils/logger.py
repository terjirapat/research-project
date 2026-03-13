import time
import logging
from functools import wraps
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)


def log_execution_time(func):
    """Decorator that logs start time, end time, and execution duration."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_perf = time.perf_counter()
        start_dt = datetime.now()

        logger.info("Start function '%s' at %s", func.__name__, start_dt)

        result = func(*args, **kwargs)

        end_perf = time.perf_counter()
        end_dt = datetime.now()

        elapsed = end_perf - start_perf

        logger.info(
            "End function '%s' at %s | elapsed %.4f seconds",
            func.__name__,
            end_dt,
            elapsed
        )

        return result

    return wrapper