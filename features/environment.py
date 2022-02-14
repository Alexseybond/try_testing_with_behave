from selenium import webdriver

def browser_init(context):
    context.driver = webdriver.Chrome()
    # context.browser = webdriver.Firefox()
    # context.browser = webdriver.Safari()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    context.driver.execute_script("return document.readyState == 'complete';")
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
