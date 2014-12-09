__author__ = 'a04316'

import unittest
import logging
import logging.config

class TestConfigurationTool(unittest.TestCase):

    def test_logging(self):
        logging.config.fileConfig('logging.conf')
        logging.info("test info mess")
        logging.warn("test warn mess")
        logging.error("test error mess")

if __name__ == '__main__':
    unittest.main()