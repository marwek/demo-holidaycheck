from selenium.webdriver.common.by import By


class SearchResultsLocators:
    """This class contains all common ID's of home page"""

    RESULTS_LIST = (By.CSS_SELECTOR, "ul li[data-testid='regular-item']")
    LAST_RESULT = (By.CSS_SELECTOR, "a[data-testid='results-last-element']")
    RESULT_ELEMENT = (By.CSS_SELECTOR, "div[data-testid='name-description']")
