import time

from selenium import webdriver
import os

def test_log_attendance():
    try:
        driver_path = (r"/chromedriver.exe")
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.maximize_window()
        driver.set_page_load_timeout(60)
        driver.get("https://app.hrone.cloud/login")
        time.sleep(2)
        driver.find_element_by_id("hrone-username").send_keys("9849909905")
        driver.find_element_by_css_selector(".btn-login").click()
        time.sleep(2)
        driver.find_element_by_id("hrone-password").send_keys("#Moneyheist@789")
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()=' LOG IN ']").click()
        time.sleep(5)
        eles = driver.find_elements_by_xpath("//a[text()='May be Later']")
        if len(eles)>0:
            eles[0].click()
        time.sleep(3)
        element = driver.find_element_by_xpath("//div[contains(@class,'p-dialog-content')]//a[@class='btnclose']")
        driver.execute_script("arguments[0].click()", element)
        time.sleep(2)
        driver.find_element_by_xpath("//button[text()='MARK ATTENDANCE']").click()
        # driver.find_element_by_xpath("//span[text()=' Mark attendance ']").click()
        # test

    except Exception as e:
        driver.quit()

