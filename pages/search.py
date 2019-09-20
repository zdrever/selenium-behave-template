from context.driver import driver
from pages.locators import SearchPageLocators
from pages.page import Page
from selenium.webdriver.common.keys import Keys


class SearchPage(Page):
    """Object to represent the google search splash page"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = SearchPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def search(self, search_term):
        element = super().get_element(SearchPageLocators.SEARCH_BAR)
        element.clear()
        element.send_keys(search_term)
        element.send_keys(Keys.ENTER)

    def verify_search_results(self, url):
        SearchPageLocators.SEARCH_RESULT.parameterize(url)
        assert super().element_exists(SearchPageLocators.SEARCH_RESULT) is True, (
            "Expected search result was not found on the search page"
        )


search_page = SearchPage.get_instance()
