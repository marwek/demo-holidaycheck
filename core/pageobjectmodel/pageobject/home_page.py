from core.pageobjectmodel.locators.common_page_locators import CommonPageLocators
from core.pageobjectmodel.pageobject.base_page import BasePage


class HomePage(BasePage):
    """This class contains all common method for home page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def input_search(self, text):
        self.__set__(CommonPageLocators.SEARCH, text)

    def click_menu(self):
        self.click(CommonPageLocators.MENU)