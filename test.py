import sys
import pathlib
import unittest

sys.path.append(pathlib.Path(__file__).parents[0])

import unicodedata

loader = unittest.TestLoader()
tests =loader.discover('.')
testRunner = unittest.runner.TextTestRunner()


if __name__ == '__main__':
    testRunner.run(tests)
