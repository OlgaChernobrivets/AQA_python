class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def fill_form_by_css(self, form_css, value):
        elem = self.driver.find_element_by_css_selector(form_css)
        elem.send_keys(value)

    def fill_form_by_id(self, form_element_id, value):
        return self.fill_form_by_css('#%s' % form_element_id, value)

    def navigate(self):
        self.driver.get(self.url)


class LoginPage(BasePage):
    url = "https://planner-sandbox.dev.thumbtack.net"

    def setLogin(self, login):
        self.fill_form_by_id("id_username", login)

    def setPassword(self, password):
        self.fill_form_by_id("id_password",password)

    def submit(self):
        self.driver.find_element_by_tag_name('button').click()

class HomePage(BasePage):
    url = "https://planner-sandbox.dev.thumbtack.net/employees/"
