from core.pageobjectmodel.utils.wait import WaitForElement
from selenium.webdriver.common.keys import Keys



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
        element.send_keys(Keys.ENTER)

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

    def switch_to_frame(self, locator):
        WaitForElement.wait(self.driver, locator)
        frame = self.driver.find_element(*locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def get_all_elements(self, locator):
        WaitForElement.wait(self.driver, locator)
        return  self.driver.find_elements(*locator)