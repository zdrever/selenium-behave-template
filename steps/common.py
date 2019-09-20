from behave import given, when, then
from context.config import settings
from context.driver import driver

"""Common hooks for any scenerio"""


@given(u'I load the website')
def load_website(context):
    driver.navigate(settings.url)
