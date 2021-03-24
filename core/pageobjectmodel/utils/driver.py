from core.pageobjectmodel.pageobject.home_page import HomePage
from core.pageobjectmodel.pageobject.search_results import SearchResults
from core.pageobjectmodel.pageobject.hotel_page import HotelPage


class Driver:
    """
    This class will be responsible for creating a instance of page object
    """
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.search_results = SearchResults(driver)
        self.hotel_page = HotelPage(driver)

    def load(self, url):
        """Loads a web page"""
        self.driver.get(url)
