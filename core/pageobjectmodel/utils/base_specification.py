import unittest

import core.pageobjectmodel.utils.desired_capabilities as desired_capabilities
from appium import webdriver
from core.pageobjectmodel.utils.driver import Driver


class BaseSpecification(unittest.TestCase):
    """
    This class is responsible for creating driver connection with appium server
    """

    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.base = Driver(self.driver)

    def tearDown(self):
        self.driver.quit()
