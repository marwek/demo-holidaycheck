from core.pageobjectmodel.locators.search_results_locators import SearchResultsLocators
from core.pageobjectmodel.pageobject.base_page import BasePage


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
        return self.driver.find_elements(SearchResultsLocators.RESULTS_LIST)
