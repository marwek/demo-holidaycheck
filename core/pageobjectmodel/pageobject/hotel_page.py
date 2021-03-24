from selenium.common.exceptions import TimeoutException
from core.pageobjectmodel.locators.hotel_list_locators import HotelListLocators
from core.pageobjectmodel.pageobject.base_page import BasePage
from core.pageobjectmodel.utils.wait import WaitForElement



class HotelPage(BasePage):
        """This class contains all methods specific to hotel results list"""

        def select_first_hotel(self):
            """Select first available hotel"""
            self.click_list_item(HotelListLocators.HOTEL_LIST_ITEM, 0)

        def select_hotel(self, position: int):
            """Select hotel from given position"""
            self.click_list_item(HotelListLocators.HOTEL_LIST_ITEM, position)

        def get_hotel_address(self):
            """Get selected hotel address"""
            addrr = self.__get__(HotelListLocators.HOTEL_ADDRESS)
            return addrr
