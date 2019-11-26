
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    LOGIN_INPUT = (By.ID, "userEmail")
    PASSWORD_INPUT = (By.ID, "userPass")
    LOGIN_BUTTON = (By.ID, "se_userLogin")
    driver = None

    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def login_to_olx(self):
        self.driver.find_element(*self.LOGIN_INPUT).clear()
        self.driver.find_element(*self.LOGIN_INPUT).send_keys("testingsergosend3@gmail.com")
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys("testingsergosend123")
        self.driver.find_element(*self.LOGIN_BUTTON).submit()

    @allure.step
    def enter_name(self, user_name):
        self.driver.find_element(*self.LOGIN_INPUT).clear()
        self.driver.find_element(*self.LOGIN_INPUT).send_keys(user_name)

    @allure.step
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    @allure.step
    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_BUTTON)).click()

    def at_page(self):
        return "Объявления" in self.driver.title

    @allure.step
    def open(self):
        self.driver.get("https://www.olx.ua/myaccount/#login")
        return self

    @allure.step
    def wait_for_text_to_appear(self, text):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/header/div[1]/div/ul/li[2]/div/a/div/i" + text + "')]")))
