import logging

from selenium.webdriver.common.by import By
from utils.Utilities import WebDriverUtils
from utils.Config import Config


class LoginPage:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.config = Config()
        self.utilities = WebDriverUtils()
        self.login_elements = {
            'email': (By.XPATH, "//input[@name='email']"),
            'password': (By.XPATH, "//input[@name='password']"),
            'login_to_continue': (By.XPATH, "//button[@type='submit']//div")
        }

    def _enter_credentials(self, email, password):
        try:
            self.utilities.send_text(self.login_elements['email'], email)
            self.utilities.send_text(self.login_elements['password'], password)
            self.utilities.click_element(self.login_elements['login_to_continue'])
            self.logger.info("[ LoginPage ] _enter_credentials: PASS")
        except Exception as e:
            self.logger.error(f"[ LoginPage ] _enter_credentials: FAIL - {str(e)}")
            raise


    def admin_login_with_valid_credentials(self):
        try:
            email = self.config.admin_email
            password = self.config.admin_password
            self._enter_credentials(email,password)
            self.logger.info("[ LoginPage ] admin_login_with_valid_credentials: PASS")
        except Exception as e:
            self.logger.error(f"[ LoginPage ] admin_login_with_valid_credentials: FAIL - {str(e)}")
            raise