from selenium import webdriver

def test_title(selenium):
    # driver = webdriver.Chrome(service_args=["--verbose", "--log-path=test-reports/chrome.log"])

    selenium.get("https://9gag.com")

    selenium.implicitly_wait(0.5)

    print(selenium.title)

    assert selenium.title == "9GAG: Go Fun The World"

    selenium.quit()
