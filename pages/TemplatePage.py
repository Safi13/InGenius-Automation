import logging
import time
import allure
from selenium.webdriver.common.by import By

from api.requests.InGeniusApi import InGeniusApi
from utils.DatabaseConnection import DatabaseConnection
from utils.JsonReader import JsonReader
from utils.Utilities import WebDriverUtils
from utils.Config import Config


class TemplatePage:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.config = Config()
        self.utilities = WebDriverUtils()
        self.json_reader = JsonReader()
        self.database_connection = DatabaseConnection()
        self.ingenius_api = InGeniusApi()
        self.courses_page_elements = {
            'add_template': (By.XPATH, "//a[@href='https://qa-ingenious.folio3.com:5053/template/create']"),
            'home_bread_crumb': (By.XPATH, "//ol//li[1]//a[text()='Home']"),
            'courses_bread_crumb': (By.XPATH, "//ol//li[2]//a[text()='Courses']"),
            'current_bread_crumb': (By.XPATH, "//li[@aria-current='page']"),
            'template_search_icon': (By.XPATH, "//div[@id='template']//i[@class='icon-magnifying-glass']"),
            'template_search': (By.XPATH, "//div[@id='template']//input[@type='search']"),
            'current': (By.XPATH, "//li//button[text()='Current']"),
            'upcoming': (By.XPATH, "//li//button[text()='Upcoming']"),
            'previous': (By.XPATH, "//li//button[text()='Previous']"),
            'template': (By.XPATH, "//li//button[text()='Template']"),
            'edit_icon_first': (By.XPATH, "//table[@id='templateTable']//tr[1]//td[4]//i[@class='icon-edit']")
        }
        self.template_table_records = {
            'template_name_col': (By.XPATH,"//table[@id='templateTable']//thead//th[1]"),
            'course_classification_col': (By.XPATH, "//table[@id='templateTable']//thead//th[2]"),
            'checklist_items_col': (By.XPATH, "//table[@id='templateTable']//thead//th[3]"),
            'actions_col': (By.XPATH, "//table[@id='templateTable']//thead//th[4]"),
            'template_name': (By.XPATH, "//table[@id='templateTable']//tr[rowValue]//td[1]"),
            'course_classification': (By.XPATH, "//table[@id='templateTable']//tr[rowValue]//td[2]"),
            'checklist_items': (By.XPATH, "//table[@id='templateTable']//tr[rowValue]//td[3]")
        }
        self.template_info_tab_elements = {
            'template_type': (By.ID, "type"),
            'no_of_allowed_student': (By.ID, "allowed_students"),
            'template': (By.ID, "TemplateName"),
            'course_classification': (By.ID, "classification"),
            'frequency': (By.ID, "frequency"),
            'country': (By.ID, "country"),
            'template_description': (By.XPATH, "//*[@name='template[description]']"),
            'FAO/TA_payment': (By.ID, "FormerAdmissionsOfficerPayment"),
            'GC/instructor_payment': (By.ID, "GraduateCoachPayment"),
            'upload_course_image': (By.ID, "task_document")
        }
        self.progress_checklist_tab_elements = {
            'task_group': (By.XPATH, "//*[text()='Task Group']//following-sibling::input[@name='group[GROUP_SEQ]']"),
            'assigned_to': (By.XPATH, "//*[text()='Assigned To']//following-sibling::select[@name='assigned_to[GROUP_SEQ]']"),
            'role_completion_percentage': (By.XPATH, "//*[text()='Role Completion Percentage']//following-sibling::input[@name='role_completion_percentage[GROUP_SEQ]']"),
            'due_date': (By.XPATH, "//*[text()='Due Date']//following-sibling::input[@name='due_date[GROUP_SEQ]']"),
            'checklist_item': (By.XPATH, "//div[@id='groupItem-GROUP_SEQ']//div[@class='row'][ITEM_SEQ]//input[@placeholder='Checklist Item Title']"),
            'checklist_item_description': (By.XPATH, "//div[@id='groupItem-GROUP_SEQ']//div[@class='row'][ITEM_SEQ]//*[@placeholder='Checklist Item Description']"),
            'add_group': (By.XPATH, "//button[text()='Add Group']"),
            'delete_group': (By.XPATH, "//button[@id='groupId-GROUP_SEQ']"),
            'add_item': (By.XPATH, "//*[@id='groupItem-GROUP_SEQ']//button"),
            'remove_item': (By.XPATH, "//div[@id='groupItem-GROUP_SEQ']//div[@class='row'][ITEM_SEQ]//button[text()='Remove Item']")
        }
        self.template_transition_elements = {
            'cancel': (By.XPATH, "//*[text()='Cancel']"),
            'previous_step': (By.XPATH, "//*[text()='Previous Step']"),
            'next_step': (By.XPATH, "//*[text()='Next Step']"),
            'save_template': (By.XPATH, "//*[text()='Save Template']")
        }
        self.alert = {
            'toast_body': (By.XPATH, "//div[@id='ajax-response-msg']//div[@class='toast-body']"),
            'invalid_file_msg': (By.XPATH, "//div[@class='toast-body']//ul//li"),
            'close_toast': (By.XPATH, "//div[@id='ajax-response-msg']//button[@aria-label='Close']"),
            'close_invalid_file_toast': (By.XPATH, "//ul//parent::div[@class='toast-body']//following-sibling::button[@aria-label='Close']")
        }


    def verify_current_page_is_courses_page(self):
        try:
            self.utilities.validate_element_visible_and_present(self.courses_page_elements['home_bread_crumb'])
            expected_bread_crumb_text = "Courses"
            actual_bread_crumb_text = self.utilities.get_text(self.courses_page_elements['current_bread_crumb'])
            self.utilities.assert_result(expected_bread_crumb_text,actual_bread_crumb_text)
            self.logger.info("[ TemplatePage ] verify_current_page_is_courses_page: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] verify_current_page_is_courses_page: FAIL - {str(e)}")
            raise

    def add_template_and_verify_that_template_page_is_opened(self):
        try:
            self.utilities.click_element(self.courses_page_elements['add_template'])
            self.utilities.validate_element_visible_and_present(self.courses_page_elements['home_bread_crumb'])
            self.utilities.validate_element_visible_and_present(self.courses_page_elements['courses_bread_crumb'])
            expected_bread_crumb_text = "Templates"
            actual_bread_crumb_text = self.utilities.get_text(self.courses_page_elements['current_bread_crumb'])
            self.utilities.assert_result(expected_bread_crumb_text,actual_bread_crumb_text)
            self.logger.info("[ TemplatePage ] add_template_and_verify_that_template_page_is_opened: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] add_template_and_verify_that_template_page_is_opened: FAIL - {str(e)}")
            raise

    def _add_template_details_in_template_info(self, record_index = 0):
        try:
            template_type_arr = self.json_reader.get_template_info_tab_data("Template Details","Template Type",record_index)
            template_type = template_type_arr[0]
            no_of_allowed_student_arr = self.json_reader.get_template_info_tab_data("Template Details", "Number Of Allowed Student", record_index)
            no_of_allowed_student = no_of_allowed_student_arr[0]
            template = self.json_reader.get_template_info_tab_data("Template Details", "Template", record_index)
            course_classification_arr = self.json_reader.get_template_info_tab_data("Template Details", "Course Classification", record_index)
            course_classification = course_classification_arr[0]
            frequency_arr = self.json_reader.get_template_info_tab_data("Template Details", "Frequency", record_index)
            frequency = frequency_arr[0]
            country_arr = self.json_reader.get_template_info_tab_data("Template Details", "Country", record_index)
            country = country_arr[0]
            template_description = self.json_reader.get_template_info_tab_data("Template Details", "Template Description (Optional)", record_index)

            self.utilities.select_dropdown(self.template_info_tab_elements['template_type'], template_type)
            self.utilities.select_dropdown(self.template_info_tab_elements['no_of_allowed_student'], no_of_allowed_student)
            self.utilities.send_text(self.template_info_tab_elements['template'], template)
            self.utilities.select_dropdown(self.template_info_tab_elements['course_classification'], course_classification)
            self.utilities.select_dropdown(self.template_info_tab_elements['frequency'], frequency)
            self.utilities.select_dropdown(self.template_info_tab_elements['country'], country)
            self.utilities.send_text(self.template_info_tab_elements['template_description'], template_description)

            self.logger.info("[ TemplatePage ] _add_template_details_in_template_info: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] _add_template_details_in_template_info: FAIL - {str(e)}")
            raise

    def verify_template_info_fields_not_empty(self):
        try:
            self.utilities.assert_field_not_empty(self.template_info_tab_elements['template_type'])
            self.utilities.assert_field_not_empty(self.template_info_tab_elements['no_of_allowed_student'])
            self.utilities.assert_field_not_empty(self.template_info_tab_elements['template'])
            self.utilities.assert_field_not_empty(self.template_info_tab_elements['course_classification'])
            self.utilities.assert_field_not_empty(self.template_info_tab_elements['frequency'])
            self.utilities.assert_field_not_empty(self.template_info_tab_elements['country'])
            self.utilities.assert_field_not_empty(self.template_info_tab_elements['template_description'])
            self.utilities.assert_field_not_empty(self.template_info_tab_elements['FAO/TA_payment'])
            self.utilities.assert_field_not_empty(self.template_info_tab_elements['GC/instructor_payment'])
            self.utilities.assert_field_not_empty(self.template_info_tab_elements['upload_course_image'])
            self.logger.info("[ TemplatePage ] verify_template_info_fields_not_empty: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] verify_template_info_fields_not_empty: FAIL - {str(e)}")
            raise

    def verify_progress_checklist_fields_not_empty(self, record_index = 0):
        try:
            groups = self.json_reader.get_progress_checklist_tab_data_group_count(record_index)
            for i in range(1, groups+1):
                task_group_locator = self.utilities.process_element(self.progress_checklist_tab_elements['task_group'],"GROUP_SEQ", str(i))
                assigned_to_locator = self.utilities.process_element(self.progress_checklist_tab_elements['assigned_to'], "GROUP_SEQ", str(i))
                role_completion_percentage_locator = self.utilities.process_element(self.progress_checklist_tab_elements['role_completion_percentage'], "GROUP_SEQ", str(i))
                due_date_locator = self.utilities.process_element(self.progress_checklist_tab_elements['due_date'],"GROUP_SEQ", str(i))
                self.utilities.assert_field_not_empty(task_group_locator)
                self.utilities.assert_field_not_empty(assigned_to_locator)
                self.utilities.assert_field_not_empty(role_completion_percentage_locator)
                self.utilities.assert_field_not_empty(due_date_locator)
                items = self.json_reader.get_progress_checklist_tab_data_group_item_count(record_index,groups-1)
                for j in range(1, items+1):
                    checklist_item_loc = self.utilities.process_element(self.progress_checklist_tab_elements['checklist_item'], "GROUP_SEQ", str(i))
                    checklist_item_locator = self.utilities.process_element(checklist_item_loc, "ITEM_SEQ", str(j))
                    checklist_item_description_loc = self.utilities.process_element(self.progress_checklist_tab_elements['checklist_item_description'], "GROUP_SEQ", str(i))
                    checklist_item_description_locator = self.utilities.process_element(checklist_item_description_loc,"ITEM_SEQ", str(j))
                    self.utilities.assert_field_not_empty(checklist_item_locator)
                    self.utilities.assert_field_not_empty(checklist_item_description_locator)

            self.logger.info("[ TemplatePage ] verify_progress_checklist_fields_not_empty: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] verify_progress_checklist_fields_not_empty: FAIL - {str(e)}")
            raise

    def add_mandatory_fields_in_template_info(self, record_index = 0):
        try:
            template_type_arr = self.json_reader.get_template_info_tab_data("Template Details","Template Type",record_index)
            template_type = template_type_arr[0]
            no_of_allowed_student_arr = self.json_reader.get_template_info_tab_data("Template Details", "Number Of Allowed Student")
            no_of_allowed_student = no_of_allowed_student_arr[0]
            template = self.json_reader.get_template_info_tab_data("Template Details", "Template")
            course_classification_arr = self.json_reader.get_template_info_tab_data("Template Details", "Course Classification")
            course_classification = course_classification_arr[0]
            frequency_arr = self.json_reader.get_template_info_tab_data("Template Details", "Frequency")
            frequency = frequency_arr[0]
            country_arr = self.json_reader.get_template_info_tab_data("Template Details", "Country")
            country = country_arr[0]
            fao_ta_payment = self.json_reader.get_template_info_tab_data("Payments", "FAO/TA Payment", record_index)
            gc_instructor_payment = self.json_reader.get_template_info_tab_data("Payments", "GC/Instructor Payment")

            self.utilities.assert_disabled(self.template_transition_elements['next_step'])
            self.utilities.select_dropdown(self.template_info_tab_elements['template_type'], template_type)
            self.utilities.assert_disabled(self.template_transition_elements['next_step'])
            self.utilities.select_dropdown(self.template_info_tab_elements['no_of_allowed_student'], no_of_allowed_student)
            self.utilities.assert_disabled(self.template_transition_elements['next_step'])
            self.utilities.send_text(self.template_info_tab_elements['template'], template)
            self.utilities.assert_disabled(self.template_transition_elements['next_step'])
            self.utilities.select_dropdown(self.template_info_tab_elements['course_classification'], course_classification)
            self.utilities.assert_disabled(self.template_transition_elements['next_step'])
            self.utilities.select_dropdown(self.template_info_tab_elements['frequency'], frequency)
            self.utilities.assert_disabled(self.template_transition_elements['next_step'])
            self.utilities.select_dropdown(self.template_info_tab_elements['country'], country)
            self.utilities.assert_disabled(self.template_transition_elements['next_step'])
            self.utilities.send_text(self.template_info_tab_elements['FAO/TA_payment'], fao_ta_payment)
            self.utilities.assert_disabled(self.template_transition_elements['next_step'])
            self.utilities.send_text(self.template_info_tab_elements['GC/instructor_payment'], gc_instructor_payment)
            self.utilities.assert_enabled(self.template_transition_elements['next_step'])

            self.logger.info("[ TemplatePage ] add_mandatory_fields_in_template_info: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] add_mandatory_fields_in_template_info: FAIL - {str(e)}")
            raise

    def _add_payments_in_template_info(self, record_index = 0):
        try:
            fao_ta_payment = self.json_reader.get_template_info_tab_data("Payments", "FAO/TA Payment", record_index)
            gc_instructor_payment = self.json_reader.get_template_info_tab_data("Payments", "GC/Instructor Payment")
            self.utilities.send_text(self.template_info_tab_elements['FAO/TA_payment'],fao_ta_payment)
            self.utilities.send_text(self.template_info_tab_elements['GC/instructor_payment'],gc_instructor_payment)
            self.logger.info("[ TemplatePage ] _add_payments_in_template_info: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] _add_payments_in_template_info: FAIL - {str(e)}")
            raise

    def _upload_course_image_in_template_info(self):
        try:
            filename = "upload-course.png"
            self.utilities.upload_file(self.template_info_tab_elements['upload_course_image'], filename)
            self.logger.info("[ TemplatePage ] _upload_course_image_in_template_info: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] _upload_course_image_in_template_info: FAIL - {str(e)}")
            raise

    def upload_invalid_course_image_in_template_info(self):
        try:
            filename = "upload-course.bmp"
            self.utilities.upload_file(self.template_info_tab_elements['upload_course_image'], filename)
            self.logger.info("[ TemplatePage ] upload_invalid_course_image_in_template_info: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] upload_invalid_course_image_in_template_info: FAIL - {str(e)}")
            raise

    def add_template_info(self, record_index = 0):
        try:
            self._add_template_details_in_template_info(record_index)
            self._add_payments_in_template_info()
            self._upload_course_image_in_template_info()
            self.logger.info("[ TemplatePage ] add_template_info: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] add_template_info: FAIL - {str(e)}")
            raise

    def next_step_after_template_info(self):
        try:
            self.utilities.click_with_js_executor(self.template_transition_elements['next_step'])
            self.logger.info("[ TemplatePage ] next_step_after_template_info: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] next_step_after_template_info: FAIL - {str(e)}")
            raise

    def cancel_template_form(self):
        try:
            self.utilities.click_element(self.template_transition_elements['cancel'])
            self.logger.info("[ TemplatePage ] cancel_template_form: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] cancel_template_form: FAIL - {str(e)}")
            raise

    def previous_step_after_progress_checklist(self):
        try:
            self.utilities.click_element(self.template_transition_elements['previous_step'])
            self.logger.info("[ TemplatePage ] previous_step_after_progress_checklist: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] previous_step_after_progress_checklist: FAIL - {str(e)}")
            raise

    def save_template(self):
        try:
            self.utilities.click_element(self.template_transition_elements['save_template'])
            self.logger.info("[ TemplatePage ] save_template: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] save_template: FAIL - {str(e)}")
            raise

    def navigate_to_template_list(self):
        try:
            self.utilities.click_element(self.courses_page_elements['template'])
            self.logger.info("[ TemplatePage ] navigate_to_template_list: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] navigate_to_template_list: FAIL - {str(e)}")
            raise

    def validate_template_list_columns(self):
        try:
            self.utilities.assert_result("Template Name",self.utilities.get_text(self.template_table_records['template_name_col']))
            self.utilities.assert_result("Course Classification",self.utilities.get_text(self.template_table_records['course_classification_col']))
            self.utilities.assert_result("Checklist Items",self.utilities.get_text(self.template_table_records['checklist_items_col']))
            self.utilities.assert_result("Actions",self.utilities.get_text(self.template_table_records['actions_col']))

            self.logger.info("[ TemplatePage ] validate_template_list_columns: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] validate_template_list_columns: FAIL - {str(e)}")
            raise

    def add_progress_checklist(self, record_index = 0):
        try:
            progress_checklist_group_count = self.json_reader.get_progress_checklist_tab_data_group_count(record_index)
            for i in range (1, progress_checklist_group_count + 1):
                self._add_group(i, record_index)
            self.logger.info("[ TemplatePage ] add_progress_checklist: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] add_progress_checklist: FAIL - {str(e)}")
            raise

    def _add_group(self, group_index, record_index = 0):
        try:
            task_group_locator = self.utilities.process_element(self.progress_checklist_tab_elements['task_group'],"GROUP_SEQ", str(group_index))
            assigned_to_locator = self.utilities.process_element(self.progress_checklist_tab_elements['assigned_to'],"GROUP_SEQ", str(group_index))
            role_completion_percentage_locator = self.utilities.process_element(self.progress_checklist_tab_elements['role_completion_percentage'],"GROUP_SEQ", str(group_index))
            due_date_locator = self.utilities.process_element(self.progress_checklist_tab_elements['due_date'],"GROUP_SEQ", str(group_index))

            task_group = self.json_reader.get_progress_checklist_tab_data("Group", "Task Group", record_index, group_index - 1)
            assigned_to_arr = self.json_reader.get_progress_checklist_tab_data("Group", "Assigned To", record_index, group_index - 1)
            assigned_to = assigned_to_arr[0]
            role_completion_percentage = self.json_reader.get_progress_checklist_tab_data("Group", "Role Completion Percentage", record_index, group_index - 1)
            due_date = self.json_reader.get_progress_checklist_tab_data("Group", "Due Date", record_index, group_index - 1)
            due_date = self.utilities.get_current_or_future_date_in_yyyy_mm_dd_format(due_date)
            if group_index > 1 :
                self.utilities.click_element(self.progress_checklist_tab_elements['add_group'])
            self.utilities.send_text(task_group_locator, task_group)
            self.utilities.select_dropdown(assigned_to_locator, assigned_to)
            self.utilities.send_text(role_completion_percentage_locator, role_completion_percentage)
            self.utilities.select_date(due_date_locator, due_date)

            progress_checklist_group_item_count = self.json_reader.get_progress_checklist_tab_data_group_item_count(record_index, group_index - 1)
            self.logger.info(str(progress_checklist_group_item_count))
            for i in range(1, progress_checklist_group_item_count + 1):
                self._add_item_in_group(group_index, i, record_index)
            self.logger.info("[ TemplatePage ] _add_group: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] _add_group: FAIL - {str(e)}")
            raise

    def _add_item_in_group(self, group_index, item_index, record_index = 0):
        try:
            item_in_group = self.json_reader.get_progress_checklist_tab_data("Group", "Item", record_index, group_index - 1)
            item_in_group = item_in_group[item_index - 1]
            checklist_item = item_in_group.get("Checklist Item")
            checklist_item_description = item_in_group.get("Checklist Item Description")
            checklist_item_loc = self.utilities.process_element(self.progress_checklist_tab_elements['checklist_item'],"GROUP_SEQ", str(group_index))
            checklist_item_locator = self.utilities.process_element(checklist_item_loc,"ITEM_SEQ", str(item_index))
            checklist_item_description_loc = self.utilities.process_element(self.progress_checklist_tab_elements['checklist_item_description'],"GROUP_SEQ", str(group_index))
            checklist_item_description_locator = self.utilities.process_element(checklist_item_description_loc, "ITEM_SEQ", str(item_index))
            if item_index > 1 :
                add_item_locator = self.utilities.process_element(self.progress_checklist_tab_elements['add_item'],"GROUP_SEQ", str(group_index))
                self.utilities.click_element(add_item_locator)
            self.utilities.send_text(checklist_item_locator, checklist_item)
            self.utilities.send_text(checklist_item_description_locator, checklist_item_description)

            self.logger.info("[ TemplatePage ] _add_item_in_group: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] _add_item_in_group: FAIL - {str(e)}")
            raise

    def add_groups_with_items(self, no_of_groups, no_of_items):
        try:
            for i in range(1,no_of_groups + 1):
                if i > 1:
                    self.utilities.click_element(self.progress_checklist_tab_elements['add_group'])
                for j in range(1,no_of_items[i-1] + 1):
                    add_item_locator = self.utilities.process_element(self.progress_checklist_tab_elements['add_item'],"GROUP_SEQ", str(i))
                    if j > 1:
                        self.utilities.click_element(add_item_locator)

            for i in range(1,no_of_groups + 1):
                task_group = self.json_reader.get_progress_checklist_verification_data("Task Group")
                assigned_to = self.json_reader.get_progress_checklist_verification_data("Assigned To")
                role_completion_percentage = self.json_reader.get_progress_checklist_verification_data("Role Completion Percentage")
                due_date = self.utilities.get_date_in_yyyy_mm_dd_format(self.json_reader.get_progress_checklist_verification_data("Due Date"))
                task_group_locator = self.utilities.process_element(self.progress_checklist_tab_elements['task_group'], "GROUP_SEQ", str(i))
                assigned_to_locator = self.utilities.process_element(self.progress_checklist_tab_elements['assigned_to'],"GROUP_SEQ", str(i))
                role_completion_percentage_locator = self.utilities.process_element(self.progress_checklist_tab_elements['role_completion_percentage'],"GROUP_SEQ", str(i))
                due_date_locator = self.utilities.process_element(self.progress_checklist_tab_elements['due_date'],"GROUP_SEQ", str(i))
                self.utilities.send_text(task_group_locator, task_group)
                self.utilities.select_dropdown(assigned_to_locator, assigned_to)
                self.utilities.send_text(role_completion_percentage_locator, role_completion_percentage)
                self.utilities.select_date(due_date_locator, due_date)
                for j in range(1,no_of_items[i-1] + 1):
                    checklist_item = self.json_reader.get_progress_checklist_verification_data("Checklist Item")
                    checklist_item_description = self.json_reader.get_progress_checklist_verification_data("Checklist Item Description")
                    checklist_item_loc = self.utilities.process_element(self.progress_checklist_tab_elements['checklist_item'], "GROUP_SEQ", str(i))
                    checklist_item_locator = self.utilities.process_element(checklist_item_loc, "ITEM_SEQ", str(j))
                    checklist_item_description_loc = self.utilities.process_element(self.progress_checklist_tab_elements['checklist_item_description'], "GROUP_SEQ", str(i))
                    checklist_item_description_locator = self.utilities.process_element(checklist_item_description_loc,"ITEM_SEQ", str(j))
                    self.utilities.send_text(checklist_item_locator, checklist_item)
                    self.utilities.send_text(checklist_item_description_locator, checklist_item_description)

            self.logger.info("[ TemplatePage ] add_groups_with_items: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] add_groups_with_items: FAIL - {str(e)}")
            raise

    def delete_group_with_its_items_and_verify_its_deletion(self, no_of_groups, no_of_items):
        try:
            for i in range(no_of_groups, 0, -1):
                delete_group_locator = self.utilities.process_element(self.progress_checklist_tab_elements['delete_group'], "GROUP_SEQ", str(i))
                task_group_locator = self.utilities.process_element(self.progress_checklist_tab_elements['task_group'],"GROUP_SEQ", str(i))
                assigned_to_locator = self.utilities.process_element(self.progress_checklist_tab_elements['assigned_to'], "GROUP_SEQ", str(i))
                role_completion_percentage_locator = self.utilities.process_element(self.progress_checklist_tab_elements['role_completion_percentage'], "GROUP_SEQ", str(i))
                due_date_locator = self.utilities.process_element(self.progress_checklist_tab_elements['due_date'],"GROUP_SEQ", str(i))

                task_group = self.json_reader.get_progress_checklist_verification_data("Task Group")
                assigned_to = self.json_reader.get_progress_checklist_verification_data("Assigned To")
                role_completion_percentage = self.json_reader.get_progress_checklist_verification_data("Role Completion Percentage")
                due_date = self.utilities.get_date_in_yyyy_mm_dd_format(self.json_reader.get_progress_checklist_verification_data("Due Date"))

                self.utilities.assert_result(task_group, self.utilities.get_value(task_group_locator))
                self.utilities.assert_result(assigned_to, self.utilities.get_value(assigned_to_locator))
                self.utilities.assert_result(role_completion_percentage,self.utilities.get_value(role_completion_percentage_locator))
                self.utilities.assert_result(due_date, self.utilities.get_value(due_date_locator))

                for j in range(no_of_items[i-1], 0, -1):
                    remove_item_loc = self.utilities.process_element(self.progress_checklist_tab_elements['remove_item'],"GROUP_SEQ", str(i))
                    remove_item_locator = self.utilities.process_element(remove_item_loc, "ITEM_SEQ", str(j))

                    checklist_item_loc = self.utilities.process_element(self.progress_checklist_tab_elements['checklist_item'], "GROUP_SEQ", str(i))
                    checklist_item_locator = self.utilities.process_element(checklist_item_loc, "ITEM_SEQ", str(j))
                    checklist_item_description_loc = self.utilities.process_element(self.progress_checklist_tab_elements['checklist_item_description'], "GROUP_SEQ", str(i))
                    checklist_item_description_locator = self.utilities.process_element(checklist_item_description_loc,"ITEM_SEQ", str(j))

                    checklist_item = self.json_reader.get_progress_checklist_verification_data("Checklist Item")
                    checklist_item_description = self.json_reader.get_progress_checklist_verification_data("Checklist Item Description")

                    self.utilities.assert_result(checklist_item, self.utilities.get_value(checklist_item_locator))
                    self.utilities.assert_result(checklist_item_description, self.utilities.get_value(checklist_item_description_locator))

                    if j > 1:
                        self.utilities.click_element(remove_item_locator)
                    elif i > 1 and j == 1:
                        self.utilities.click_element(delete_group_locator)
            self.logger.info("[ TemplatePage ] delete_group_with_its_items_and_verify_its_deletion: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] delete_group_with_its_items_and_verify_its_deletion: FAIL - {str(e)}")
            raise

    def verify_added_groups_and_items_with_their_values(self, no_of_groups, no_of_items):
        try:
            for i in range(no_of_groups, 0, -1):
                task_group_locator = self.utilities.process_element(self.progress_checklist_tab_elements['task_group'],"GROUP_SEQ", str(i))
                assigned_to_locator = self.utilities.process_element(self.progress_checklist_tab_elements['assigned_to'], "GROUP_SEQ", str(i))
                role_completion_percentage_locator = self.utilities.process_element(self.progress_checklist_tab_elements['role_completion_percentage'], "GROUP_SEQ", str(i))
                due_date_locator = self.utilities.process_element(self.progress_checklist_tab_elements['due_date'],"GROUP_SEQ", str(i))

                task_group = self.json_reader.get_progress_checklist_verification_data("Task Group")
                assigned_to = self.json_reader.get_progress_checklist_verification_data("Assigned To")
                role_completion_percentage = self.json_reader.get_progress_checklist_verification_data("Role Completion Percentage")
                due_date = self.utilities.get_date_in_yyyy_mm_dd_format(self.json_reader.get_progress_checklist_verification_data("Due Date"))

                self.utilities.assert_result(task_group, self.utilities.get_value(task_group_locator))
                self.utilities.assert_result(assigned_to, self.utilities.get_value(assigned_to_locator))
                self.utilities.assert_result(role_completion_percentage,self.utilities.get_value(role_completion_percentage_locator))
                self.utilities.assert_result(due_date, self.utilities.get_value(due_date_locator))

                for j in range(no_of_items[i-1], 0, -1):
                    checklist_item_loc = self.utilities.process_element(self.progress_checklist_tab_elements['checklist_item'], "GROUP_SEQ", str(i))
                    checklist_item_locator = self.utilities.process_element(checklist_item_loc, "ITEM_SEQ", str(j))
                    checklist_item_description_loc = self.utilities.process_element(self.progress_checklist_tab_elements['checklist_item_description'], "GROUP_SEQ", str(i))
                    checklist_item_description_locator = self.utilities.process_element(checklist_item_description_loc,"ITEM_SEQ", str(j))

                    checklist_item = self.json_reader.get_progress_checklist_verification_data("Checklist Item")
                    checklist_item_description = self.json_reader.get_progress_checklist_verification_data("Checklist Item Description")

                    self.utilities.assert_result(checklist_item, self.utilities.get_value(checklist_item_locator))
                    self.utilities.assert_result(checklist_item_description, self.utilities.get_value(checklist_item_description_locator))
            self.logger.info("[ TemplatePage ] verify_added_groups_and_items_with_their_values: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] verify_added_groups_and_items_with_their_values: FAIL - {str(e)}")
            raise

    def validate_default_progress_checklist_open_only(self):
        try:
            task_group_locator = self.utilities.process_element(self.progress_checklist_tab_elements['task_group'], "GROUP_SEQ", str(2))
            self.utilities.validate_element_not_present_or_visible(task_group_locator)
            self.logger.info("[ TemplatePage ] validate_default_progress_checklist_open_only: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] validate_default_progress_checklist_open_only: FAIL - {str(e)}")
            raise

    def validate_progress_checklist_fields_are_mandatory(self):
        try:
            for i in range(1, 5):
                if i > 1:
                    self.utilities.click_element(self.progress_checklist_tab_elements['add_group'])
                task_group_locator = self.utilities.process_element(self.progress_checklist_tab_elements['task_group'], "GROUP_SEQ", str(i))
                assigned_to_locator = self.utilities.process_element(self.progress_checklist_tab_elements['assigned_to'],"GROUP_SEQ", str(i))
                role_completion_percentage_locator = self.utilities.process_element(self.progress_checklist_tab_elements['role_completion_percentage'],"GROUP_SEQ", str(i))
                due_date_locator = self.utilities.process_element(self.progress_checklist_tab_elements['due_date'],"GROUP_SEQ", str(i))

                self._validate_submission_not_occur()
                self.utilities.send_text(task_group_locator, "Task Group")

                self._validate_submission_not_occur()
                self.utilities.select_dropdown(assigned_to_locator, "PM")

                self._validate_submission_not_occur()
                self.utilities.send_text(role_completion_percentage_locator, "10.00")

                self._validate_submission_not_occur()
                due_date = self.utilities.get_current_or_future_date_in_yyyy_mm_dd_format("current+30")
                self.utilities.send_text(due_date_locator, due_date)

                for j in range(1,5):
                    checklist_item_loc = self.utilities.process_element(self.progress_checklist_tab_elements['checklist_item'], "GROUP_SEQ", str(i))
                    checklist_item_locator = self.utilities.process_element(checklist_item_loc, "ITEM_SEQ", str(j))
                    checklist_item_description_loc = self.utilities.process_element(self.progress_checklist_tab_elements['checklist_item_description'], "GROUP_SEQ", str(i))
                    checklist_item_description_locator = self.utilities.process_element(checklist_item_description_loc,"ITEM_SEQ", str(j))

                    add_item_locator = self.utilities.process_element(self.progress_checklist_tab_elements['add_item'],"GROUP_SEQ", str(i))
                    if j == 1:
                        self._validate_submission_not_occur()
                        self.utilities.send_text(checklist_item_locator, "Item 1")

                        self._validate_submission_not_occur()
                        self.utilities.send_text(checklist_item_description_locator, "Item 1 Description")
                    if j > 1:
                        self.utilities.click_element(add_item_locator)
                        self._validate_submission_not_occur()
                        self.utilities.send_text(checklist_item_locator, "Item 2")

                        self._validate_submission_not_occur()
                        self.utilities.send_text(checklist_item_description_locator, "Item 2 Description")
            self._validate_submission_not_occur()
            self.logger.info("[ TemplatePage ] validate_progress_checklist_fields_are_mandatory: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] validate_progress_checklist_fields_are_mandatory: FAIL - {str(e)}")
            raise
    def validate_alert_message(self, expected_message):
        try:
            self.utilities.verify_alert(self.alert['toast_body'], expected_message)
            self.utilities.click_with_js_executor(self.alert['close_toast'])
            self.logger.info("[ TemplatePage ] validate_alert_message: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] validate_alert_message: FAIL - {str(e)}")
            raise

    def _validate_submission_not_occur(self):
        try:
            self.utilities.click_with_js_executor(self.template_transition_elements['save_template'])
            self.logger.info("[ TemplatePage ] _validate_submission_not_occur: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] _validate_submission_not_occur: FAIL - {str(e)}")
            raise

    def validate_invalid_file_message(self, expected_message):
        try:
            self.utilities.verify_alert(self.alert['invalid_file_msg'], expected_message)
            self.utilities.click_with_js_executor(self.alert['close_invalid_file_toast'])
            self.logger.info("[ TemplatePage ] validate_alert_message: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] validate_alert_message: FAIL - {str(e)}")
            raise

    def search_for_template_and_edits_top_record(self, record_index = 0):
        try:
            self.search_for_template(record_index)
            self.utilities.click_element(self.courses_page_elements['edit_icon_first'])

            self.logger.info("[ TemplatePage ] search_for_template_and_edits_top_record: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] search_for_template_and_edits_top_record: FAIL - {str(e)}")
            raise

    def edit_top_record(self):
        try:
            self.utilities.click_element(self.courses_page_elements['edit_icon_first'])
            self.logger.info("[ TemplatePage ] edit_top_record: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] edit_top_record: FAIL - {str(e)}")
            raise

    def click_next_step(self):
        try:
            self.utilities.click_element(self.template_transition_elements['next_step'])
            self.logger.info("[ TemplatePage ] click_next_step: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] click_next_step: FAIL - {str(e)}")
            raise

    def verify_template_info_data_populating(self, record_index = 0):
        try:
            template_type_arr = self.json_reader.get_template_info_tab_data("Template Details", "Template Type",record_index)
            template_type = template_type_arr[0]
            no_of_allowed_student_arr = self.json_reader.get_template_info_tab_data("Template Details","Number Of Allowed Student",record_index)
            no_of_allowed_student = no_of_allowed_student_arr[0]
            template = self.json_reader.get_template_info_tab_data("Template Details", "Template", record_index)
            course_classification_arr = self.json_reader.get_template_info_tab_data("Template Details","Course Classification",record_index)
            course_classification = course_classification_arr[0]
            frequency_arr = self.json_reader.get_template_info_tab_data("Template Details", "Frequency", record_index)
            frequency = frequency_arr[0]
            country_arr = self.json_reader.get_template_info_tab_data("Template Details", "Country", record_index)
            country = country_arr[0]
            template_description = self.json_reader.get_template_info_tab_data("Template Details","Template Description (Optional)",record_index)
            fao_ta_payment = self.json_reader.get_template_info_tab_data("Payments", "FAO/TA Payment", record_index)
            gc_instructor_payment = self.json_reader.get_template_info_tab_data("Payments", "GC/Instructor Payment")

            actual_template_type =  self.utilities.get_value(self.template_info_tab_elements['template_type'])
            actual_no_of_allowed_student = self.utilities.get_value(self.template_info_tab_elements['no_of_allowed_student'])
            actual_template = self.utilities.get_value(self.template_info_tab_elements['template'])
            actual_course_classification = self.utilities.get_value(self.template_info_tab_elements['course_classification'])
            actual_frequency = self.utilities.get_value(self.template_info_tab_elements['frequency'])
            actual_country = self.utilities.get_value(self.template_info_tab_elements['country'])
            actual_template_description = self.utilities.get_value(self.template_info_tab_elements['template_description'])
            actual_fao_ta_payment = self.utilities.get_value(self.template_info_tab_elements['FAO/TA_payment'])
            actual_gc_instructor_payment = self.utilities.get_value(self.template_info_tab_elements['GC/instructor_payment'])

            self.utilities.assert_result(template_type,actual_template_type)
            self.utilities.assert_result(no_of_allowed_student,actual_no_of_allowed_student)
            self.utilities.assert_result(template,actual_template)
            self.utilities.assert_result(course_classification, actual_course_classification)
            self.utilities.assert_result(frequency,actual_frequency)
            self.utilities.assert_result(country,actual_country)
            self.utilities.assert_result(template_description,actual_template_description)
            self.utilities.assert_result(fao_ta_payment,actual_fao_ta_payment)
            self.utilities.assert_result(gc_instructor_payment,actual_gc_instructor_payment)

            self.logger.info("[ TemplatePage ] verify_template_info_data_populating: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] verify_template_info_data_populating: FAIL - {str(e)}")
            raise

    def open_search_option_in_template(self):
        try:
            self.utilities.click_element(self.courses_page_elements['template'])
            self.utilities.click_element(self.courses_page_elements['template_search_icon'])
            self.logger.info("[ TemplatePage ] open_search_option_in_template: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] open_search_option_in_template: FAIL - {str(e)}")
            raise
    def search_for_template(self,search_type = "name", record_index = 0):
        try:
            self.utilities.click_element(self.courses_page_elements['template'])
            self.utilities.click_element(self.courses_page_elements['template_search_icon'])
            if search_type == "name":
                template = self.json_reader.get_template_info_tab_data("Template Details", "Template", record_index)
                self.utilities.send_text(self.courses_page_elements['template_search'],template)
            elif search_type == "course_classification":
                course_classification_arr = self.json_reader.get_template_info_tab_data("Template Details", "Course Classification", record_index)
                course_classification = course_classification_arr[0]
                self.utilities.send_text(self.courses_page_elements['template_search'],course_classification)
            elif search_type == "checklist_items":
                groups = self.json_reader.get_progress_checklist_tab_data_group_count(record_index)
                total_items = 0
                for i in range(0, groups):
                    items = self.json_reader.get_progress_checklist_tab_data_group_item_count(record_index, i)
                    total_items = total_items + items
                self.utilities.send_text(self.courses_page_elements['template_search'], str(total_items))
            self.logger.info("[ TemplatePage ] search_for_template: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] search_for_template: FAIL - {str(e)}")
            raise

    def search_and_verify_template_with_dynamic_groups_and_items(self, record_index = 0):
        try:
            self.utilities.click_element(self.courses_page_elements['template'])
            self.utilities.click_element(self.courses_page_elements['template_search_icon'])
            template = self.json_reader.get_template_info_tab_data("Template Details", "Template", record_index)
            self.utilities.send_text(self.courses_page_elements['template_search'],template)
            course_classification_arr = self.json_reader.get_template_info_tab_data("Template Details","Course Classification",record_index)
            course_classification = course_classification_arr[0]
            checklist_items_arr = self.json_reader.get_progress_checklist_verification_data("Number of Items")
            checklist_items = sum(checklist_items_arr)

            template_name_locator = self.utilities.process_element(self.template_table_records['template_name'],"rowValue", "1")
            course_classification_locator = self.utilities.process_element(self.template_table_records['course_classification'], "rowValue", "1")
            checklist_items_locator = self.utilities.process_element(self.template_table_records['checklist_items'],"rowValue", "1")
            self.utilities.assert_result(template, self.utilities.get_text(template_name_locator))
            self.utilities.assert_result(course_classification, self.utilities.get_text(course_classification_locator))
            self.utilities.assert_result(checklist_items, self.utilities.get_text(checklist_items_locator))

            self.logger.info("[ TemplatePage ] search_for_template: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] search_for_template: FAIL - {str(e)}")
            raise

    def verify_searched_template(self):
        try:
            searched_info = self.utilities.get_value(self.courses_page_elements['template_search'])
            template_name_locator = self.utilities.process_element(self.template_table_records['template_name'], "rowValue", "1")
            course_classification_locator = self.utilities.process_element(self.template_table_records['course_classification'], "rowValue", "1")
            checklist_items_locator = self.utilities.process_element(self.template_table_records['checklist_items'], "rowValue", "1")
            template_name = self.utilities.get_text(template_name_locator)
            course_classification = self.utilities.get_text(course_classification_locator)
            checklist_items = self.utilities.get_text(checklist_items_locator)

            if template_name.startswith(searched_info) or course_classification.startswith(searched_info) or checklist_items.startswith(searched_info):
                if template_name.startswith(searched_info):
                    self.logger.info("Searched Template Name: " + str(template_name) + "| matched with list top element")
                    allure.attach("Searched Template Name: " + str(template_name) + "| matched with list top element", "Info")
                if course_classification.startswith(searched_info):
                    self.logger.info("Searched Course Classification: " + str(course_classification) + "| matched with list top element:")
                    allure.attach("Searched Course Classification: " + str(course_classification) + "| matched with list top element:", "Info")
                if checklist_items.startswith(searched_info):
                    self.logger.info("Searched Checklist Items count: " + str(checklist_items) + "| matched with list top element")
                    allure.attach("Searched Checklist Items count: " + str(checklist_items) + "| matched with list top element", "Info")
            else:
                self.logger.info("Search Results doesn't matched with the Expected Results")
                allure.attach("Search Results doesn't matched with the Expected Results", "Info")

            self.logger.info("[ TemplatePage ] search_for_template: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] search_for_template: FAIL - {str(e)}")
            raise

    def execute_deletion_of_templates(self):
        try:
            token, cookies = self.ingenius_api.generate_login_token()
            response, cookies = self.ingenius_api.login_with_admin(token, cookies)
            template_ids = self.database_connection.execute_select_query(self.utilities.read_db_query("get_template_id_to_delete"))
            for template_id in template_ids:
                temp_id = template_id[0]
                self.ingenius_api.delete_template(str(temp_id), token, cookies)
            self.logger.info("[ TemplatePage ] execute_deletion_of_templates: PASS")
        except Exception as e:
            self.logger.error(f"[ TemplatePage ] execute_deletion_of_templates: FAIL - {str(e)}")
            raise