import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_log_attendance():
    try:
        options = Options()
        options.add_argument("--window-size=1440,768")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--no-sandbox")  # Bypass OS security model
        options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        options.headless = True
        driver = webdriver.Chrome(options=options,executable_path="chromedriver.exe")
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
        time.sleep(10)
        eles = driver.find_elements_by_xpath("//a[text()='May be Later']")
        if len(eles)>0:
            eles[0].click()
        time.sleep(3)
        element = driver.find_element_by_xpath("//div[contains(@class,'p-dialog-content')]//a[@class='btnclose']")
        driver.execute_script("arguments[0].click()", element)
        time.sleep(2)
        driver.find_element_by_xpath("//button[text()='MARK ATTENDANCE']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[text()=' Mark attendance ']").click()
        print("Passed")
        send_sms("Attendance logged successfully")

    except Exception as e:
        print("failed" + str(e))
        send_sms("Attendance log failed")
        driver.quit()
        assert False


def send_sms(message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    querystring = {"authorization": "F9ZR78D0iBqpEIw2UCszkAfcrKlNdOojvJh5LHeMn3XG6mbQWPOSIok7AWdhj58FJmrEq9XaRexpMLw3",
                   "message": message, "language": "english",
                   "route": "q", "numbers": "9849909905"}
    headers = {
        'cache-control': "no-cache"
    }
    requests.request("GET", url, headers=headers, params=querystring)
