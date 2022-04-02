from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=service)

driver.get("https://pinball.etrash.pro")

driver.implicitly_wait(0.5)

assert "Pinball Leaderboard" in driver.title

driver.quit()