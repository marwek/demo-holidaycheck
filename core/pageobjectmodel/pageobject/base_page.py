from appium.webdriver.common.touch_action import TouchAction
from core.pageobjectmodel.utils.wait import WaitForElement


class BasePage:
    """Basic class, contains all common operations."""

    def __init__(self, driver):
        self.driver = driver

    def __set__(self, locator, value):
        """Set the supplied text to the specified object"""
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def __get__(self, locator):
        """Gets the text of the specified object"""
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_element(*locator)
        return element.get_attribute("text")

    def click(self, locator):
        """Click element"""
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_element(*locator)
        element.click()

    def click_list_item(self, locator, pos):
        """Click element on a position from available list"""
        WaitForElement.wait(self.driver, locator)
        element = self.driver.find_elements(*locator)[pos]
        element.click()