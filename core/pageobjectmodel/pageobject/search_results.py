from selenium.common.exceptions import TimeoutException
from core.pageobjectmodel.locators.search_results_locators import SearchResultsLocators
from core.pageobjectmodel.pageobject.base_page import BasePage
from core.pageobjectmodel.utils.wait import WaitForElement


class SearchResults(BasePage):
    """This class contains all methods specific to search results list"""

    def __init___(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_first_result(self):
        """Click first element in search result list"""
        self.click_list_item(SearchResultsLocators.RESULTS_LIST, 0)

    def get_results_list(self):
        """Return all results from search list"""
        try:
            WaitForElement.wait(self.driver, SearchResultsLocators.LAST_RESULT)
            return self.get_all_elements(SearchResultsLocators.RESULTS_LIST_ELEMENT)
        except TimeoutException:
            print('Not able to find results list')
