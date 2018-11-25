import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, ui
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from pages import Page


class Planner:

    driver = webdriver.Chrome()
    loginPage = Page.LoginPage(driver)
    loginPage.navigate()
    loginPage.setLogin('gerardkunze')
    loginPage.setPassword('123456')
    loginPage.submit()

    def wait_homePage(driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'employees-item')))

    wait_homePage(driver)

    #case 1: parental leave
    link = driver.find_element_by_xpath("//i[@class='dropdown__caret']")
    link.click()
    link = driver.find_element_by_xpath("//a[contains(text(),'TimeOff')]")
    link.click()
    timeOff = driver.find_element_by_xpath("//a[@class='btn btn-success js-vacation_add']")
    timeOff.click()
    type = driver.find_element_by_xpath("//select[@class='form-control js-type-select']")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@class='form-control js-type-select']")))
    dropdown = Select(type)
    dropdown.select_by_value("500")
    notify = driver.find_element_by_xpath("//input[@placeholder='QALead or DevLead, PM and Department Head']")
    notify.click()
    time.sleep(3)
    notify.send_keys("Abigale Rippin")
    wait = WebDriverWait(driver, 10)
    notifier = driver.find_element_by_xpath("//ul//li[contains(.,'Abigale Rippin')]")
    wait.until(EC.visibility_of(notifier)).click()
    driver.find_element_by_xpath("//form[@id='form']//button[@type='submit']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//div[@id='date-intersection-modal']//button[@type='submit']").click()
    time.sleep(3)

    homePage = Page.HomePage(driver)
    homePage.navigate()
    wait_homePage(driver)

    #case 2: find employee by name
    link = driver.find_element_by_xpath("//a[contains(text(),'Abraham Swift')]")
    link.click()
    link = driver.find_element_by_xpath("//a[@class='navbar-brand']")
    link.click()

    homePage.navigate()
    wait_homePage(driver)

    #case 3: click Working
    filter = driver.find_element_by_xpath("//span[contains(text(),'Working')]")
    filter.click()

    # case 5: click Skill
    filter = driver.find_element_by_xpath("//button[@class='btn btn-default js-toggle-skills']")
    filter.click()
    time.sleep(2)
    skills = driver.find_element_by_xpath("//input[@placeholder='Type to find skill']")
    skills.send_keys("A")
    driver.find_element_by_xpath("//div[@class='autocomplete-suggestions']//div[2]").click()
    driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[3]/button[1]").click()

    homePage.navigate()
    wait_homePage(driver)

    #case 4: click Department
    filter = driver.find_element_by_xpath("//button[@class='btn btn-default js-toggle-department']")
    filter.click()
    department = driver.find_element_by_xpath("//div[@class='checkbox-filter__options-list']//div[9]//div[1]//label[1]//i[1]")
    department.click()
    driver.find_element_by_xpath("//button[@class='btn btn-sm btn-primary js-apply']").click()

    homePage.navigate()
    wait_homePage(driver)

    #case 6: delete goal and undo
    link = driver.find_element_by_xpath("//i[@class='dropdown__caret']")
    link.click()
    goalsMenu = driver.find_element_by_xpath("//a[contains(text(),'Goals')]")
    goalsMenu.click()
    try:
        driver.find_element_by_xpath("//div[@class='goals-container js-goals-container js-inprogress-goals-container']//div[1]//div[3]//button[1]").click()
    except NoSuchElementException:
        print("Goals is empty")
    else:
        delete = driver.find_element_by_xpath("//div[@class='goal-actions open']//li[@title='Delete']//a")
        delete.click()
        time.sleep(2)
        undo = driver.find_element_by_xpath("//button[@class='dscrd-btn btn btn-primary js-goal-undo-delete-goal']")
        undo.click()

    driver.close()

