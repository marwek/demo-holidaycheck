import unittest

import core.pageobjectmodel.utils.desired_capabilities as desired_capabilities
from appium import webdriver


class BaseSpecification(unittest.TestCase):
    """
    This class is responsible for creating driver connection with appium server
    """

    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities()
        self.driver = webdriver.Remote('http://localhost:8000/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
