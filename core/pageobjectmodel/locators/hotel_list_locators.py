from selenium.webdriver.common.by import By


class HotelListLocators:
    HOTEL_LIST_MAIN = (By.ID, 'hotel-list')
    HOTEL_LIST_ITEM = (By.CSS_SELECTOR, '#hotel-list div.hotel-list-items div.hotel-list-item')
    HOTEL_ADDRESS = (By.CSS_SELECTOR, 'div.hotel-address a')