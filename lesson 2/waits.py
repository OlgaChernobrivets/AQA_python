from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Waits:
    def __init__(self, driver):
        self.driver = driver

    def wait_homePage(self, selector):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, selector)))