from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HeaderPage:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def at_page(self):
        try:
            profile_logo_element = WebDriverWait(self.driver, 10) \
                .until(EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[3]/div/div[2]/div/a/span")))
            return profile_logo_element.is_displayed()
        except TimeoutException:
            return False