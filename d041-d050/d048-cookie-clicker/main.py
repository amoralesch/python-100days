# Cookie Clicker

# An app that plays the game of
# [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/)
# automatically for us
#
# Learn about [Selenium](https://www.selenium.dev/).

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

RUN_TIME = 5 * 60 # seconds
CHECK_GAP = 10 # seconds


def get_amount(text: str) -> int:
    return int(text.replace(',', ''))


def check_store(available_money: int) -> bool:
    store = driver.find_element(By.ID, 'store')
    items = store.find_elements(By.TAG_NAME, 'div')
    items.reverse()

    for item in items:
        if len(item.get_attribute('class')) != 0:
            continue

        price = get_amount(item.find_element(By.TAG_NAME, 'b').text.split('-')[1].strip())
        print(price)

        if price <= available_money:
            item.click()
            return True

    return False


# Keep browser running
options = webdriver.FirefoxOptions()
# options.set_preference('detach', True)

driver = webdriver.Firefox(options=options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

# find the cookie
cookie = driver.find_element(By.ID, 'cookie')

start = time.time()
timeout = time.time() + RUN_TIME

while time.time() < timeout:
    cookie.click()

    if time.time() > start + CHECK_GAP:
        start = time.time()

        money = get_amount(driver.find_element(By.ID, 'money').text)
        print(money)

        check_store(money)

money = get_amount(driver.find_element(By.ID, 'money').text)

print(f'After {RUN_TIME} seconds ({RUN_TIME // 60} minutes), your score is {money}.')

driver.quit()
