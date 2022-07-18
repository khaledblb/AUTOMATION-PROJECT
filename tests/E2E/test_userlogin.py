import time
from selenium.webdriver.common.by import By


def test_userlogin(driver):
    driver.get("http://localhost:8000/")
    time.sleep(3)

    driver.set_window_size(1440, 900)

    driver.implicitly_wait(3)
    driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1)").click()
    time.sleep(1)
    driver.find_element(By.ID, "email").click()
    time.sleep(1)

    driver.find_element(By.ID, "email").send_keys("khaledblb@gmaill.com")
    driver.find_element(By.ID, "password").click()
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("Aa123456")
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
    actualName = driver.find_element(By.XPATH,'//*[@id="username"]')
    time.sleep(2)
    assert actualName.text == "KHALED"
  
