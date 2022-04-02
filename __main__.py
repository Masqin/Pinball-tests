from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://pinball.etrash.pro")

driver.implicitly_wait(0.5)

print(driver.title)

assert driver.title == "Pinball Leaderboard"

driver.quit()