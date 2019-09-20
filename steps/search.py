from behave import given, when, then
from pages.search import search_page

"""Hooks for interacting with google search"""


@when(u'I search for "{search_term}"')
def search(context, search_term):
    search_page.search(search_term)


@then(u'I should see "{url}" in the results')
def results(context, url):
    search_page.verify_search_results(url)
