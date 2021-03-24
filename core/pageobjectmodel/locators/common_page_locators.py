from selenium.webdriver.common.by import By


class CommonPageLocators:
    """This class contains all common ID's for all pages"""

    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="search-input"]')
    SEARCH = (By.CSS_SELECTOR, 'input[data-testid="autosuggest-input"]')
    HOME = (By.CSS_SELECTOR, '#home')
    MENU = (By.CSS_SELECTOR, 'a[data-testid="burgerMenu"]')
    COOKIES_CONTAINER = (By.XPATH, './/iframe[@title="SP Consent Message"]')
    COOKIES_BUTTONS = (By.XPATH, '//div[@class="message-component message-row button-container"]/button')
