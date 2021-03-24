import unittest

from core.pageobjectmodel.utils.base_specification import BaseSpecification
import time
import pytest


WEB_PAGE = "https://www.holidaycheck.de"
TEXT_SEARCH = 'Berlin'

class TestSearchResults(BaseSpecification):

    def test_search_results_list(self):
        self.base.load(WEB_PAGE)
        self.base.home_page.accept_cookies()
        self.base.home_page.input_search(TEXT_SEARCH)
        
        results = self.base.search_results.get_results_list()
        for result in results:
            assert TEXT_SEARCH.lower() in result.text.lower()
        
        self.base.search_results.click_first_result()
        self.base.hotel_page.select_first_hotel()

        address = self.base.hotel_page.get_hotel_address()
        assert TEXT_SEARCH.lower() in address.lower()