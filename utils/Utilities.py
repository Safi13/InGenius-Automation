import os
from telnetlib import EC
import allure
import logging
from selenium.webdriver.common.keys import Keys
from selenium.common import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.BrowserDriver import BrowserDriver
from utils.Config import Config
from datetime import datetime, timedelta, date
from selenium.webdriver.common.keys import Keys
import configparser
import datetime



class WebDriverUtils:
    config = Config()
    logger = logging.getLogger(__name__)

    @classmethod
    def send_text(cls, locator, text_input):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator) and EC.visibility_of_element_located(locator))
            element = web_driver.find_element(*locator)
            element.send_keys(Keys.BACKSPACE * len(element.get_attribute("value")))
            element.send_keys(text_input)
            cls.logger.info(
                text_input + " : is entered correctly on the textbox | textarea on locator Type: " + locator_type + " and Value: " + locator_value)
            allure.attach(
                text_input + " : is entered correctly on the textbox | textarea on locator Type: " + locator_type + " and Value: " + locator_value,
                "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the element to be located.")
            allure.attach("Timeout occurred while waiting for the element to be located.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Textbox | Textarea Element not found.")
            allure.attach("Textbox | Textarea Element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: " + str(e))
            allure.attach("An error occurred: " + str(e), "Error")
            raise


    @classmethod
    def press_enter_key(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator) and EC.visibility_of_element_located(locator))
            element = web_driver.find_element(*locator)
            element.send_keys(Keys.RETURN)
            cls.logger.info(
                "Keys.RETURN : is entered correctly on the textbox | textarea on locator Type: " + locator_type + " and Value: " + locator_value)
            allure.attach(
                "Keys.RETURN : is entered correctly on the textbox | textarea on locator Type: " + locator_type + " and Value: " + locator_value,
                "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the element to be located.")
            allure.attach("Timeout occurred while waiting for the element to be located.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Textbox | Textarea Element not found.")
            allure.attach("Textbox | Textarea Element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def select_dropdown(cls, locator, option_text):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator) and EC.visibility_of_element_located(locator))
            dropdown = Select(web_driver.find_element(*locator))
            dropdown.select_by_visible_text(option_text)
            cls.logger.info(
                option_text + " : option is selected correctly in the dropdown on locator Type: " + locator_type + " and Value: " + locator_value)
            allure.attach(
                option_text + " : option is selected correctly in the dropdown on locator Type: " + locator_type + " and Value: " + locator_value,
                "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the dropdown element to be located.")
            allure.attach("Timeout occurred while waiting for the dropdown element to be located.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Dropdown element not found.")
            allure.attach("Dropdown element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def single_select_search_dropdown(cls, click_locator, input_locator, option_text):
        try:
            locator_type, locator_value = input_locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(click_locator) and EC.visibility_of_element_located(click_locator))
            element = web_driver.find_element(*click_locator)
            element.click()
            WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(input_locator) and EC.visibility_of_element_located(input_locator))
            element = web_driver.find_element(*input_locator)
            element.send_keys(option_text)
            element.send_keys(Keys.RETURN)
            cls.logger.info(
                option_text + " : option is selected correctly in the dropdown on locator Type: " + locator_type + " and Value: " + locator_value)
            allure.attach(
                option_text + " : option is selected correctly in the dropdown on locator Type: " + locator_type + " and Value: " + locator_value,
                "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the dropdown element to be located.")
            allure.attach("Timeout occurred while waiting for the dropdown element to be located.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Dropdown element not found.")
            allure.attach("Dropdown element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def multi_select_search_dropdown(cls, locator, option_texts):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator) and EC.visibility_of_element_located(locator))
            element = web_driver.find_element(*locator)
            for option_text in option_texts:
                element.send_keys(option_text)
                element.send_keys(Keys.RETURN)
                cls.logger.info(
                    option_text + " : option is selected correctly in the dropdown on locator Type: " + locator_type + " and Value: " + locator_value)
                allure.attach(
                    option_text + " : option is selected correctly in the dropdown on locator Type: " + locator_type + " and Value: " + locator_value,
                    "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the dropdown element to be located.")
            allure.attach("Timeout occurred while waiting for the dropdown element to be located.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Dropdown element not found.")
            allure.attach("Dropdown element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise


    @classmethod
    def select_checkbox(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator) and EC.visibility_of_element_located(locator))
            checkbox = web_driver.find_element(*locator)
            if not checkbox.is_selected():
                checkbox.click()
                cls.logger.info("Checkbox is marked on locator Type: " + locator_type + " and Value: " + locator_value)
                allure.attach("Checkbox is marked on locator Type: " + locator_type + " and Value: " + locator_value,
                              "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the checkbox element to be located.")
            allure.attach("Timeout occurred while waiting for the checkbox element to be located.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Checkbox element not found.")
            allure.attach("Checkbox element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def deselect_checkbox(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator) and EC.visibility_of_element_located(locator))
            checkbox = web_driver.find_element(*locator)
            if checkbox.is_selected():
                checkbox.click()
                cls.logger.info(
                    "Checkbox is un-marked on locator Type: " + locator_type + " and Value: " + locator_value)
                allure.attach("Checkbox is un-marked on locator Type: " + locator_type + " and Value: " + locator_value,
                              "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the checkbox element to be located.")
            allure.attach("Timeout occurred while waiting for the checkbox element to be located.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Checkbox element not found.")
            allure.attach("Checkbox element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def select_radio_button(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator) and EC.visibility_of_element_located(locator))
            radio_button = web_driver.find_element(*locator)
            if not radio_button.is_selected():
                radio_button.click()
                cls.logger.info(
                    "Radiobutton is marked on locator Type: " + locator_type + " and Value: " + locator_value)
                allure.attach("Radiobutton is marked on locator Type: " + locator_type + " and Value: " + locator_value,
                              "Info")

        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the radio button element to be located.")
            allure.attach("Timeout occurred while waiting for the radio button element to be located.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Radio button element not found.")
            allure.attach("Radio button element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def select_date(cls, locator, date):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator) and EC.visibility_of_element_located(locator))
            date_field = web_driver.find_element(*locator)
            date_field.clear()
            date_field.send_keys(date)
            cls.logger.info(
                date + " : is entered correctly on the date picker on locator Type: " + locator_type + " and Value: " + locator_value)
            allure.attach(
                date + " : is entered correctly on the date picker on locator Type: " + locator_type + " and Value: " + locator_value,
                "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the date picker element to be located.")
            allure.attach("Timeout occurred while waiting for the date picker element to be located.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Date picker element not found.")
            allure.attach("Date picker element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise


    @classmethod
    def get_text(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator) and EC.visibility_of_element_located(locator))
            element = web_driver.find_element(*locator)
            text = element.text
            cls.logger.info(
                text + " : text is fetched from locator Type: " + locator_type + " and Value: " + locator_value)
            allure.attach(
                text + " : text is fetched from locator Type: " + locator_type + " and Value: " + locator_value, "Info")
            return text
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the element to be located. Element: "+ locator_value)
            allure.attach("Timeout occurred while waiting for the element to be located.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Element not found.")
            allure.attach("Element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def get_value(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator) and EC.visibility_of_element_located(locator))
            element = web_driver.find_element(*locator)
            element_value = element.get_attribute("value")
            cls.logger.info(
                element_value + " : is fetched from locator Type: " + locator_type + " and Value: " + locator_value)
            allure.attach(
                element_value + " : is fetched from locator Type: " + locator_type + " and Value: " + locator_value,
                "Info")
            return element_value
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the element to be located.")
            allure.attach("Timeout occurred while waiting for the element to be located.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Element not found.")
            allure.attach("Element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def switch_to_window(cls, window_index):
        try:
            web_driver = BrowserDriver.get_driver()
            web_driver.switch_to.window(web_driver.window_handles[window_index])
            cls.logger.info(f"Switched control to window index {window_index}")
            allure.attach(f"Switched control to window index {window_index}", "Info")
        except Exception as e:
            cls.logger.error("An error occurred while switching window: %s" % str(e), exc_info=True)
            allure.attach("An error occurred while switching window: " + str(e), "Error")
            raise

    @classmethod
    def click_element(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until(EC.element_to_be_clickable(locator))
            element = web_driver.find_element(*locator)
            element.click()
            cls.logger.info(
                "Clicked on element with locator Type: " + locator_type + " and Value: " + locator_value)
            allure.attach(
                "Clicked on element with locator Type: " + locator_type + " and Value: " + locator_value, "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the element to be clickable: " + str(locator_value))
            allure.attach("Timeout occurred while waiting for the element to be clickable:"  + str(locator_value), "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Element not found.")
            allure.attach("Element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error(str(locator_value) + ": An error occurred: %s" % str(e), exc_info=True)
            allure.attach(str(locator_value) + ": An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def click_with_js_executor(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            element = web_driver.find_element(*locator)
            web_driver.execute_script("arguments[0].click();", element)
            cls.logger.info("Clicked on element with locator Type: " + locator_type + " and Value: " + locator_value)
            allure.attach("Clicked on element with locator Type: " + locator_type + " and Value: " + locator_value,
                          "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the element to be clickable.")
            allure.attach("Timeout occurred while waiting for the element to be clickable.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Element not found.")
            allure.attach("Element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def validate_element_visible_and_present(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator) and EC.visibility_of_element_located(locator))
            cls.logger.info(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is present and visible")
            allure.attach(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is present and visible",
                "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the element to be visible.")
            allure.attach("Timeout occurred while waiting for the element to be visible.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Element not found.")
            allure.attach("Element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def validate_element_not_present_or_visible(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            WebDriverWait(web_driver, cls.config.exp_wait).until_not(
                EC.presence_of_element_located(locator) or EC.visibility_of_element_located(locator))
            cls.logger.info(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is not present and not visible")
            allure.attach(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is not present and not visible",
                "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the element to be not visible.")
            allure.attach("Timeout occurred while waiting for the element to be not visible.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Element not found.")
            allure.attach("Element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise


    @classmethod
    def add_to_local_storage(cls, key, value):
        try:
            web_driver = BrowserDriver.get_driver()
            web_driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")
        except Exception as e:
            cls.logger.error("An error occurred while adding to local storage: %s" % str(e), exc_info=True)
            allure.attach("An error occurred while adding to local storage: " + str(e), "Error")
            raise

    @classmethod
    def refresh_page(cls):
        try:
            web_driver = BrowserDriver.get_driver()
            web_driver.refresh()
        except Exception as e:
            cls.logger.error("An error occurred while refreshing the page: %s" % str(e), exc_info=True)
            allure.attach("An error occurred while refreshing the page: " + str(e), "Error")
            raise


    @classmethod
    def assert_result(cls, expected, actual):
        try:
            assert expected == actual
            response = "Pass"
            cls.logger.info(f"Assertion: Expected = {expected}, Actual = {actual} - Passed")
        except AssertionError:
            response = "Fail"
            cls.logger.error(f"Assertion: Expected = {expected}, Actual = {actual} - Failed")
        except Exception as e:
            response = f"Error: {str(e)}"
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
        return response

    @classmethod
    def verify_alert(cls,alert_message_locator, alert_expected_message):
        try:
            alert_message = cls.get_text(alert_message_locator)
            cls.assert_result(alert_expected_message, alert_message)
        except Exception as e:
            cls.logger.error("An error occurred while verifying alert: %s" % str(e), exc_info=True)
            allure.attach("An error occurred while verifying alert: " + str(e), "Error")
            raise


    @classmethod
    def is_textbox_empty(cls, locator):
        locator_type, locator_value = locator
        try:
            cls.assert_result("", cls.get_value(locator))
            cls.logger.info("Textbox element : " + locator_value + "is cleared.")
        except Exception as e:
            cls.logger.error(f"Textbox element : {locator_value} is not empty: %s" % str(e), exc_info=True)
            allure.attach(f"Textbox element : {locator_value} is not empty: " + str(e), "Error")
            raise

    @classmethod
    def validate_text_content(cls, locator, expected_text):
        try:
            cls.assert_result(expected_text, cls.get_text(locator))
            cls.logger.info("Text contents are matched")
        except Exception as e:
            cls.logger.error("Text content are mismatched: %s" % str(e), exc_info=True)
            raise


    @classmethod
    def validate_field_value(cls, locator, expected_value):
        try:
            cls.assert_result(expected_value, cls.get_value(locator))
            cls.logger.info("Field values are matched")
        except Exception as e:
            cls.logger.error("Field values are mismatched: %s" % str(e), exc_info=True)
            raise

    @classmethod
    def process_element(cls, locator, replace_text, replace_value):
        try:
            locator_type, locator_value = locator
            locator_value = locator_value.replace(replace_text, replace_value)
            locator = (locator_type, locator_value)
            return locator
        except Exception as e:
            cls.logger.error("Error occurred while processing element: %s" % str(e), exc_info=True)
            raise

    @classmethod
    def read_db_query(cls, key):
        filepath = "./resources/db-queries.ini"
        config = configparser.ConfigParser()
        try:
            config.read(filepath)
            response = config.get('db_queries', key)
            return response
        except configparser.Error as e:
            cls.logger.error("An error occurred while reading the .ini file: %s" % str(e), exc_info=True)
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)

    @classmethod
    def scroll_vertical(cls, pixels):
        try:
            web_driver = BrowserDriver.get_driver()
            web_driver.implicitly_wait(cls.config.imp_wait)
            initial_scroll_position = web_driver.execute_script("return window.pageYOffset;")
            web_driver.execute_script(f"window.scrollBy(0, {pixels});")
            new_scroll_position = web_driver.execute_script("return window.pageYOffset;")
            if new_scroll_position != initial_scroll_position:
                cls.logger.info("Vertical scroll performed successfully.")
                allure.attach("Vertical scroll performed successfully.", "Info")
                return True
            cls.logger.error("Vertical scroll failed.")
            allure.attach("Vertical scroll failed.", "Error")
            return False

        except Exception as e:
            allure.attach("An error occurred while scrolling vertically: " + str(e), "Error")
            cls.logger.error("An error occurred while scrolling vertically: %s" % str(e), exc_info=True)
            return False

    @classmethod
    def upload_file(cls, locator, file_name):
        try:
            current_path = os.getcwd()
            file_path = os.path.join(current_path, 'resources', file_name)
            web_driver = BrowserDriver.get_driver()
            file_input = web_driver.find_element(*locator)
            file_input.clear()
            file_input.send_keys(file_path)
        except NoSuchElementException:
            allure.attach("File input element not found.")
            cls.logger.error("File input element not found.")
        except Exception as e:
            allure.attach("An error occurred while selecting file: " + str(e), "Error")
            cls.logger.error("An error occurred while selecting file: %s" % str(e), exc_info=True)
            raise

    @classmethod
    def get_current_or_future_date_in_yyyy_mm_dd_format(cls, date_arg):
        try:
            if date_arg == "current":
                current_date = date.today()
            elif date_arg.startswith("current+"):
                days_to_add = int(date_arg.split("+")[1])
                current_date = date.today() + timedelta(days=days_to_add)
            else:
                raise ValueError("Invalid date argument")

            formatted_date = current_date.strftime("%Y-%m-%d")
            return formatted_date
        except Exception as e:
            allure.attach("Error occurred while getting current date: " + str(e), "Error")
            cls.logger.error("Error occurred while getting current date: %s" % str(e), exc_info=True)
            raise

    @classmethod
    def get_current_or_previous_date_in_yyyy_mm_dd_format(cls, date_arg):
        try:
            if date_arg == "current":
                current_date = date.today()
            elif date_arg.startswith("current-"):
                days_to_subtract = int(date_arg.split("-")[1])
                current_date = date.today() - timedelta(days=days_to_subtract)
            else:
                raise ValueError("Invalid date argument")

            formatted_date = current_date.strftime("%Y-%m-%d")
            return formatted_date
        except Exception as e:
            allure.attach("Error occurred while getting current date: " + str(e), "Error")
            cls.logger.error("Error occurred while getting current date: %s" % str(e), exc_info=True)
            raise

    @classmethod
    def get_date_in_yyyy_mm_dd_format(cls, date_arg):
        cls.logger.info("Date ARG: " +str(date_arg))
        try:
            if date_arg == "current":
                current_date = date.today()
            elif date_arg.startswith("current+"):
                days_to_add = int(date_arg.split("+")[1])
                current_date = date.today() + timedelta(days=days_to_add)
            elif date_arg.startswith("current-"):
                days_to_subtract = int(date_arg.split("-")[1])
                current_date = date.today() - timedelta(days=days_to_subtract)
            else:
                raise ValueError("Invalid date argument")

            formatted_date = current_date.strftime("%Y-%m-%d")
            return formatted_date
        except Exception as e:
            allure.attach("Error occurred while getting the date: " + str(e), "Error")
            cls.logger.error("Error occurred while getting the date: %s" % str(e), exc_info=True)
            raise


    @classmethod
    def assert_enabled(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            element = WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator))
            cls.logger.info(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is present.")
            allure.attach(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is present.",
                "Info")
            assert not element.get_attribute('disabled'), "Element with locator Type: {} and Value: {} is disabled.".format(locator_type, locator_value)
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the element to be present.")
            allure.attach("Timeout occurred while waiting for the element to be present.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Element not found.")
            allure.attach("Element not found.", "Error")
            raise
        except AssertionError as e:
            cls.logger.error(str(e))
            allure.attach(str(e), "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def assert_disabled(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            element = WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator))
            cls.logger.info(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is present.")
            allure.attach(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is present.",
                "Info")
            assert element.get_attribute('disabled'), "Element with locator Type: {} and Value: {} is enabled.".format(locator_type, locator_value)
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the element to be present.")
            allure.attach("Timeout occurred while waiting for the element to be present.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Element not found.")
            allure.attach("Element not found.", "Error")
            raise
        except AssertionError as e:
            cls.logger.error(str(e))
            allure.attach(str(e), "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def assert_field_not_empty(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            element = WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator))
            cls.logger.info(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is present.")
            allure.attach(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is present.",
                "Info")
            field_value = element.get_attribute("value").strip()
            assert field_value, "Field with locator Type: {} and Value: {} is empty.".format(locator_type, locator_value)
            cls.logger.info("Field is not empty.")
            allure.attach("Field is not empty.", "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the element to be present.")
            allure.attach("Timeout occurred while waiting for the element to be present.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Element not found.")
            allure.attach("Element not found.", "Error")
            raise
        except AssertionError as e:
            cls.logger.error(str(e))
            allure.attach(str(e), "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def assert_field_empty(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            element = WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator))
            cls.logger.info(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is present.")
            allure.attach(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is present.",
                "Info")
            field_value = element.get_attribute("value").strip()
            assert not field_value, "Field with locator Type: {} and Value: {} is not empty.".format(locator_type,
                                                                                                     locator_value)
            cls.logger.info("Field is empty.")
            allure.attach("Field is empty.", "Info")
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the element to be present.")
            allure.attach("Timeout occurred while waiting for the element to be present.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Element not found.")
            allure.attach("Element not found.", "Error")
            raise
        except AssertionError as e:
            cls.logger.error(str(e))
            allure.attach(str(e), "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise

    @classmethod
    def get_dropdown_options(cls, locator):
        try:
            locator_type, locator_value = locator
            web_driver = BrowserDriver.get_driver()
            element = WebDriverWait(web_driver, cls.config.exp_wait).until(
                EC.presence_of_element_located(locator))
            cls.logger.info(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is present.")
            allure.attach(
                "Element with locator Type: " + locator_type + " and Value: " + locator_value + " is present.",
                "Info")
            dropdown = Select(element)
            options = [option.text for option in dropdown.options]
            return options
        except TimeoutException:
            cls.logger.error("Timeout occurred while waiting for the element to be present.")
            allure.attach("Timeout occurred while waiting for the element to be present.", "Error")
            raise
        except NoSuchElementException:
            cls.logger.error("Element not found.")
            allure.attach("Element not found.", "Error")
            raise
        except Exception as e:
            cls.logger.error("An error occurred: %s" % str(e), exc_info=True)
            allure.attach("An error occurred: " + str(e), "Error")
            raise