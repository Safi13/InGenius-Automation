from selenium import webdriver
from utils.Config import Config
from selenium.webdriver.chrome.options import Options
import logging


class BrowserDriver:
    driver = None
    logger = logging.getLogger(__name__)

    @classmethod
    def initialize_driver(cls):
        if cls.driver is None:
            config = Config()
            browser = config.browser
            url = config.web_url
            is_headless = config.is_headless
            is_detachable = config.is_detachable

            if browser.lower() == 'chrome':
                if is_headless.lower() == 'true':
                    chrome_options = Options()
                    chrome_options.add_argument("--headless")
                    cls.driver = webdriver.Chrome(options=chrome_options)
                    cls.logger.info("Chrome Browser on Headless mode Initialized")
                elif is_detachable.lower() == 'true':
                    chrome_options = Options()
                    chrome_options.add_experimental_option("detach", True)
                    cls.driver = webdriver.Chrome(chrome_options=chrome_options)
                else:
                    cls.driver = webdriver.Chrome()
                    cls.logger.info("Chrome Browser Initialized")
            elif browser.lower() == 'edge':
                cls.driver = webdriver.Edge()
                cls.logger.info("Edge Browser Initialized")
            elif browser.lower() == 'firefox':
                cls.driver = webdriver.Firefox()
                cls.logger.info("Firefox Browser Initialized")
            if cls.driver is not None:
                cls.driver.maximize_window()
                cls.logger.info("Browser window maximized")
                cls.driver.get(url)
                cls.logger.info("Navigating to the URL: " + url)

    @classmethod
    def get_driver(cls):
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.logger.info("Explicitly closing the browser")
            cls.driver = None
