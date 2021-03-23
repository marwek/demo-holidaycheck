from selenium.webdriver.common.by import By


class CommonPageLocators:
    """This class contains all common ID's for all pages"""

    SEARCH = (By.ID, 'search-input')
    MENU = (By.CSS_SELECTOR, 'a[data-testid="burgerMenu"]')
