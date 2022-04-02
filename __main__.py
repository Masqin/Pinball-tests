from selenium import webdriver

driver = webdriver.Chrome(service_args=["--verbose", "--log-path=test-reports/chrome.log"])

driver.get("https://pinball.etrash.pro")

driver.implicitly_wait(0.5)

print(driver.title)

assert driver.title == "Pinball Leaderboard"

driver.quit()
