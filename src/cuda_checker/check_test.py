import logging
import unittest

from cuda_checker.check import (
    get_pytorch_properties,
    get_tensorflow_properties,
)

_LOGGING_FORMAT = "%(asctime)s %(levelname)s %(pathname)s %(message)s"
logging.basicConfig(
    format=_LOGGING_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S%z",
    handlers=[logging.StreamHandler()],
    level=logging.DEBUG,
)


class Test(unittest.TestCase):
    def test_check(self) -> None:
        logging
        _LOGGING_FORMAT = "%(asctime)s %(levelname)s %(pathname)s %(message)s"
        logging.basicConfig(
            format=_LOGGING_FORMAT,
            datefmt="%Y-%m-%d %H:%M:%S%z",
            handlers=[logging.StreamHandler()],
            level=logging.DEBUG,
        )

        get_pytorch_properties()
        get_tensorflow_properties()


if __name__ == "__main__":
    unittest.main()
