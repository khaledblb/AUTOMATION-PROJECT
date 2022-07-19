import string
import time
import namegenerator
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_buyE2EPRODUCT(driver):
    name = namegenerator.gen()
    password = ''.join(random.choice(string.printable) for i in range(8))
    paymentData ={
        "cardNumber":"4929095603577545",
        "expDate":"03/29",
        "cvs":"436"
    }

    driver.get("http://localhost:8000/#/")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(1)
    driver.find_element(By.ID, "name").click()
    time.sleep(1)
    driver.find_element(By.ID, "name").send_keys(name)
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys(name+"@test.com")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, "passwordConfirm").send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, "passwordConfirm").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".col-xl-3:nth-child(1) strong").click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,198)")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".w-100").click()
    driver.execute_script("window.scrollTo(0,178)")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".active > img").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".col-xl-3:nth-child(6) .card-img").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".w-100").click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,178)")
    driver.find_element(By.CSS_SELECTOR, ".w-100").click()
    driver.find_element(By.ID, "address").click()
    time.sleep(1)
    driver.find_element(By.ID, "address").send_keys("7054, 9107001")
    driver.find_element(By.ID, "city").send_keys("Jerusalem")
    driver.find_element(By.ID, "postalCode").send_keys("7054")
    driver.find_element(By.ID, "country").send_keys("Israel")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".my-3").click()
    time.sleep(4)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/div/form/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div[2]/div[2]/div/div/div[7]/button').click()
    time.sleep(12)
    # TODO: getting payment button selector
    # driver.find_element(By.CSS_SELECTOR,"#buttons-container > div > div.paypal-button-row.paypal-button-number-1.paypal-button-layout-vertical.paypal-button-shape-rect.paypal-button-number-multiple.paypal-button-env-sandbox.paypal-button-color-black.paypal-button-text-color-white.paypal-logo-color-white > div > div.paypal-button-label-container > span.paypal-button-text.true").click()
    # driver.find_element(By.XPATH,'// *[ @ id = "buttons-container"] / div / div[2]').click()
    # driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div.col-md-4 > buttons-container > div > div.paypal-button-row.paypal-button-number-1.paypal-button-layout-vertical.paypal-button-shape-rect.paypal-button-number-multiple.paypal-button-env-sandbox.paypal-button-color-black.paypal-button-text-color-white.paypal-logo-color-white > div").click()
    # time.sleep(3)
    # driver.find_element(By.XPATH,'//*[@id="credit-card-number"]').send_keys(paymentData.cardNumber)
    # time.sleep(1)
    # driver.find_element(By.XPATH,'//*[@id="root"]/div/div/form/div/div[3]').send_keys(paymentData.expDate)
    # driver.find_element(By.XPATH,'//*[@id="root"]/div/div/form/div/div[3]/div[3]/div[1]').send_keys(paymentData.cvs)
    # time.sleep(5)

    orderSummaryElement = driver.find_element(By.CSS_SELECTOR,".card > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1)")

    assert orderSummaryElement.text == "ORDER SUMMARY"

