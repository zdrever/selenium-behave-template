from context.driver import driver

def after_all(context):
    driver.stop_instance()

def before_scenario(context, scenario):
    driver.clear_cookies()
    