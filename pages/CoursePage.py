import logging
import allure
from selenium.webdriver.common.by import By
from utils.Utilities import BrowserDriver
from api.requests.InGeniusApi import InGeniusApi
from utils.DatabaseConnection import DatabaseConnection
from utils.JsonReader import JsonReader
from utils.Utilities import WebDriverUtils
from utils.Config import Config


class CoursePage:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.config = Config()
        self.utilities = WebDriverUtils()
        self.json_reader = JsonReader()
        self.database_connection = DatabaseConnection()
        self.ingenius_api = InGeniusApi()
        self.courses_page_elements = {
            'course_counselor': (By.ID, "course_counselor"),
            'add_template': (By.XPATH, "//a[@href='https://qa-ingenious.folio3.com:5053/template/create']"),
            'add_course': (By.XPATH, "//a[@href='https://qa-ingenious.folio3.com:5053/course/create']"),
            'home_bread_crumb': (By.XPATH, "//ol//li[1]//a[text()='Home']"),
            'courses_bread_crumb': (By.XPATH, "//ol//li[2]//a[text()='Courses']"),
            'current_bread_crumb': (By.XPATH, "//li[@aria-current='page']"),
            'current': (By.XPATH, "//li//button[text()='Current']"),
            'upcoming': (By.XPATH, "//li//button[text()='Upcoming']"),
            'previous': (By.XPATH, "//li//button[text()='Previous']"),
            'edit_icon_first': (By.XPATH, "//table[@id='templateTable']//tr[1]//td[4]//i[@class='icon-edit']"),
            'current_search_icon': (By.XPATH, "//div[@id='currentCoursesData']//i"),
            'current_search_close_icon': (By.XPATH, "//div[@id='currentCoursesData']//i[2]"),
            'current_search_input': (By.XPATH, "//div[@id='currentCoursesData']//input"),
            'upcoming_search_icon': (By.XPATH, "//div[@id='upcomingCoursesData']//i"),
            'upcoming_search_close_icon': (By.XPATH, "//div[@id='upcomingCoursesData']//i[2]"),
            'upcoming_search_input': (By.XPATH, "//div[@id='upcomingCoursesData']//input"),
            'previous_search_icon': (By.XPATH, "//div[@id='previousCoursesData']//i"),
            'previous_search_close_icon': (By.XPATH, "//div[@id='previousCoursesData']//i[2]"),
            'previous_search_input': (By.XPATH, "//div[@id='previousCoursesData']//input"),
        }
        self.course_elements = {
            'templates': (By.ID, "selectCourseTemplate"),
            'template_type': (By.ID, "templateType"),
            'no_of_students': (By.ID, "allowedStudents"),
            'course_title': (By.ID, "courseTitle"),
            'frequency': (By.ID, "frequency"),
            'description': (By.ID, "templateDesc"),
            'start_date': (By.ID, "startDate"),
            'end_date': (By.ID, "endDate"),
            'fao_rate': (By.ID, "faoRate"),
            'gc_rate': (By.ID, "gcRate"),
            'fao_ta_click': (By.XPATH, "//label[text()='FAO/TA']//following-sibling::div//div"),
            'fao_ta_input': (By.XPATH, "//label[text()='FAO/TA']//following-sibling::div//input"),
            'fao_ta_value': (By.XPATH, "//label[text()='FAO/TA']//following-sibling::div//div[@class='choices__item choices__item--selectable']"),
            'gc_instructor_click': (By.XPATH, "//label[text()='GC/Instructor']//following-sibling::div//div"),
            'gc_instructor_input': (By.XPATH, "//label[text()='GC/Instructor']//following-sibling::div//input"),
            'gc_instructor_value': (By.XPATH, "//label[text()='GC/Instructor']//following-sibling::div//div[@class='choices__item choices__item--selectable']"),
            'pm_click': (By.XPATH, "//label[text()='PM']//following-sibling::div//div"),
            'pm_input': (By.XPATH, "//label[text()='PM']//following-sibling::div//input"),
            'pm_value': (By.XPATH, "//label[text()='PM']//following-sibling::div//div[@class='choices__item choices__item--selectable']"),
            'cm_click': (By.XPATH, "//label[text()='CM']//following-sibling::div//div"),
            'cm_input': (By.XPATH, "//label[text()='CM']//following-sibling::div//input"),
            'cm_value': (By.XPATH, "//label[text()='CM']//following-sibling::div//div[@class='choices__item choices__item--selectable']"),
            'other': (By.XPATH, "//select[@id='other']//following-sibling::input"),
            'other_index': (By.XPATH, "//select[@id='other']//following-sibling::div//div[index]"),
            'students': (By.XPATH, "//select[@id='multi-std']//following-sibling::input"),
            'students_index': (By.XPATH, "//select[@id='multi-std']//following-sibling::div//div[index]"),
            'students_click': (By.XPATH, "//select[@id='single-std']//parent::div"),
            'students_input': (By.XPATH, "//*[@id='single-student']//input"),
            'students_value': (By.XPATH, "//label[@for='single-std']//following-sibling::div//div[@class='choices__item choices__item--selectable']"),
            'save_information': (By.XPATH, "//button[text()='Save Information']"),
            'cancel': (By.XPATH, "//a[text()='Cancel']")

        }
        self.template_popup_elements = {
            'template_rate': (By.ID, "templateRate"),
            'course_rate': (By.ID, "courseRate"),
            'close': (By.XPATH, "//button[text()='Close']"),
        }
        self.alert = {
            'toast_body': (By.XPATH, "//div[@id='notification-sidebar']//following-sibling::div//div[@class='toast-body']"),
            'toast_error': (By.XPATH, "//div[@id='notification-sidebar']//following-sibling::div//div[@class='toast-body']//ul//li[rowValue]"),
            'close_toast': (By.XPATH, "//div[@id='notification-sidebar']//following-sibling::div//div[@class='toast-body']//following-sibling::button"),
        }
        self.course_table_records = {
            'course_name_col': (By.XPATH,"//table[@id='courseTable']//thead//th[1]"),
            'fao_ta_col': (By.XPATH, "//table[@id='courseTable']//thead//th[2]"),
            'gc_instructor_col': (By.XPATH, "//table[@id='courseTable']//thead//th[3]"),
            'pm_col': (By.XPATH, "//table[@id='courseTable']//thead//th[4]"),
            'cm_col': (By.XPATH, "//table[@id='courseTable']//thead//th[5]"),
            'action_col': (By.XPATH, "//table[@id='courseTable']//thead//th[6]"),
            'course_name': (By.XPATH, "//table[@id='courseTable']//tr[rowValue]//td[1]//a"),
            'fao_ta': (By.XPATH, "//table[@id='courseTable']//tr[rowValue]//td[2]"),
            'gc_instructor': (By.XPATH, "//table[@id='courseTable']//tr[rowValue]//td[3]"),
            'pm': (By.XPATH, "//table[@id='courseTable']//tr[rowValue]//td[4]"),
            'cm': (By.XPATH, "//table[@id='courseTable']//tr[rowValue]//td[5]"),
            'previous_course_name': (By.XPATH, "//div[@id='previousCoursesData']//table[@id='courseTable']//tr[rowValue]//td[1]//a"),
            'previous_fao_ta': (By.XPATH, "//div[@id='previousCoursesData']//table[@id='courseTable']//tr[rowValue]//td[2]"),
            'previous_gc_instructor': (By.XPATH, "//div[@id='previousCoursesData']//table[@id='courseTable']//tr[rowValue]//td[3]"),
            'previous_pm': (By.XPATH, "//div[@id='previousCoursesData']//table[@id='courseTable']//tr[rowValue]//td[4]"),
            'previous_cm': (By.XPATH, "//div[@id='previousCoursesData']//table[@id='courseTable']//tr[rowValue]//td[5]"),
            'upcoming_course_name': (By.XPATH, "//div[@id='upcomingCoursesData']//table[@id='courseTable']//tr[rowValue]//td[1]//a"),
            'upcoming_fao_ta': (By.XPATH, "//div[@id='upcomingCoursesData']//table[@id='courseTable']//tr[rowValue]//td[2]"),
            'upcoming_gc_instructor': (By.XPATH, "//div[@id='upcomingCoursesData']//table[@id='courseTable']//tr[rowValue]//td[3]"),
            'upcoming_pm': (By.XPATH, "//div[@id='upcomingCoursesData']//table[@id='courseTable']//tr[rowValue]//td[4]"),
            'upcoming_cm': (By.XPATH, "//div[@id='upcomingCoursesData']//table[@id='courseTable']//tr[rowValue]//td[5]"),
            'edit': (By.XPATH, "//table[@id='courseTable']//tr[rowValue]//td[6]//i"),
            'edit_first_row': (By.XPATH, "//table[@id='courseTable']//tr[1]//td[6]//i"),
            'reg_students_icon': (By.XPATH, "//table[@id='courseTable']//tr[rowValue]//td[6]//li[3]//i]")
        }

    def add_course_and_verify_that_course_is_opened(self):
        try:
            self.utilities.click_element(self.courses_page_elements['add_course'])
            self.utilities.validate_element_visible_and_present(self.courses_page_elements['home_bread_crumb'])
            self.utilities.validate_element_visible_and_present(self.courses_page_elements['courses_bread_crumb'])
            expected_bread_crumb_text = "Create Course"
            actual_bread_crumb_text = self.utilities.get_text(self.courses_page_elements['current_bread_crumb'])
            self.utilities.assert_result(expected_bread_crumb_text,actual_bread_crumb_text)
            self.logger.info("[ CoursePage ] add_course_and_verify_that_course_is_opened: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] add_course_and_verify_that_course_is_opened: FAIL - {str(e)}")
            raise

    def verify_current_page_is_courses_page(self):
        try:
            self.utilities.validate_element_visible_and_present(self.courses_page_elements['home_bread_crumb'])
            expected_bread_crumb_text = "Courses"
            actual_bread_crumb_text = self.utilities.get_text(self.courses_page_elements['current_bread_crumb'])
            self.utilities.assert_result(expected_bread_crumb_text,actual_bread_crumb_text)
            self.logger.info("[ CoursePage ] verify_current_page_is_courses_page: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] verify_current_page_is_courses_page: FAIL - {str(e)}")
            raise

    def verify_single_student_data_is_populating_on_course_fields_correctly(self, record_index = 0):
        try:
            templates = self.json_reader.get_single_student_data("Course Details", "Templates", record_index)
            types = self.json_reader.get_single_student_data("Course Details", "Type", record_index)
            no_of_student = self.json_reader.get_single_student_data("Course Details", "No. of Students", record_index)
            description = self.json_reader.get_single_student_data("Course Details", "Description", record_index)

            course_title = self.json_reader.get_single_student_data("Course Details", "Course Title", record_index)
            frequency_arr = self.json_reader.get_single_student_data("Course Details", "Frequency", record_index)
            frequency = frequency_arr[0]

            start_date = self.json_reader.get_single_student_data("Counselor", "Start Date", record_index)
            end_date = self.json_reader.get_single_student_data("Counselor", "End Date", record_index)
            start_date = self.utilities.get_date_in_yyyy_mm_dd_format(start_date)
            end_date = self.utilities.get_date_in_yyyy_mm_dd_format(end_date)

            fao_ta = self.json_reader.get_single_student_data("Counselor", "FAO/TA", record_index)
            gc_instructor = self.json_reader.get_single_student_data("Counselor", "GC/Instructor", record_index)
            pm = self.json_reader.get_single_student_data("Counselor", "PM", record_index)
            cm = self.json_reader.get_single_student_data("Counselor", "CM", record_index)
            other_arr = self.json_reader.get_single_student_data("Counselor", "Other", record_index)
            students = self.json_reader.get_single_student_data("Counselor", "Students", record_index)

            fao_rate = self.json_reader.get_single_student_data("Rate", "FAO Rate", record_index)
            gc_rate = self.json_reader.get_single_student_data("Rate", "GC Rate", record_index)

            self.utilities.assert_result(templates, self.utilities.get_value(self.course_elements['templates']))
            self.utilities.assert_result(types, self.utilities.get_value(self.course_elements['template_type']))
            self.utilities.assert_result(no_of_student, self.utilities.get_value(self.course_elements['no_of_students']))
            self.utilities.assert_result(description, self.utilities.get_value(self.course_elements['description']))

            self.utilities.assert_result(course_title, self.utilities.get_value(self.course_elements['course_title']))
            self.utilities.assert_result(frequency, self.utilities.get_value(self.course_elements['frequency']))

            self.utilities.assert_result(start_date, self.utilities.get_value(self.course_elements['start_date']))
            self.utilities.assert_result(end_date, self.utilities.get_value(self.course_elements['end_date']))

            self.utilities.assert_result(fao_rate, self.utilities.get_value(self.course_elements['fao_rate']))
            self.utilities.assert_result(gc_rate, self.utilities.get_value(self.course_elements['gc_rate']))

            fao_ta_value = self._process_string_for_counselor(self.utilities.get_text(self.course_elements['fao_ta_value']))
            gc_instructor_value = self._process_string_for_counselor(self.utilities.get_text((self.course_elements['gc_instructor_value'])))
            pm_value = self._process_string_for_counselor(self.utilities.get_text((self.course_elements['pm_value'])))
            cm_value = self._process_string_for_counselor(self.utilities.get_text((self.course_elements['cm_value'])))
            students_value = self._process_string_for_counselor(self.utilities.get_text((self.course_elements['students_value'])))

            self.utilities.assert_result(fao_ta, fao_ta_value)
            self.utilities.assert_result(gc_instructor, gc_instructor_value)
            self.utilities.assert_result(pm, pm_value)
            self.utilities.assert_result(cm, cm_value)
            self.utilities.assert_result(students, students_value)
            for index, other in enumerate(other_arr):
                other_locator = self.utilities.process_element(self.course_elements['other_index'], "index", str(index + 1))
                other_value = self._process_string_for_counselor(self.utilities.get_text(other_locator))
                self.utilities.assert_result(other, other_value)
            self.logger.info("[ CoursePage ] verify_single_student_data_is_populating_on_course_fields_correctly: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] verify_single_student_data_is_populating_on_course_fields_correctly: FAIL - {str(e)}")
            raise

    def verify_many_students_data_is_populating_on_course_fields_correctly(self, record_index = 0):
        try:
            templates = self.json_reader.get_many_students_data("Course Details", "Templates", record_index)
            types = self.json_reader.get_many_students_data("Course Details", "Type", record_index)
            no_of_student = self.json_reader.get_many_students_data("Course Details", "No. of Students", record_index)
            description = self.json_reader.get_many_students_data("Course Details", "Description", record_index)

            course_title = self.json_reader.get_many_students_data("Course Details", "Course Title", record_index)
            frequency_arr = self.json_reader.get_many_students_data("Course Details", "Frequency", record_index)
            frequency = frequency_arr[0]

            start_date = self.json_reader.get_many_students_data("Counselor", "Start Date", record_index)
            end_date = self.json_reader.get_many_students_data("Counselor", "End Date", record_index)
            start_date = self.utilities.get_date_in_yyyy_mm_dd_format(start_date)
            end_date = self.utilities.get_date_in_yyyy_mm_dd_format(end_date)

            fao_ta = self.json_reader.get_many_students_data("Counselor", "FAO/TA", record_index)
            gc_instructor = self.json_reader.get_many_students_data("Counselor", "GC/Instructor", record_index)
            pm = self.json_reader.get_many_students_data("Counselor", "PM", record_index)
            cm = self.json_reader.get_many_students_data("Counselor", "CM", record_index)
            other_arr = self.json_reader.get_many_students_data("Counselor", "Other", record_index)
            students_arr = self.json_reader.get_many_students_data("Counselor", "Students", record_index)

            fao_rate = self.json_reader.get_many_students_data("Rate", "FAO Rate", record_index)
            gc_rate = self.json_reader.get_many_students_data("Rate", "GC Rate", record_index)

            self.utilities.assert_result(templates, self.utilities.get_value(self.course_elements['templates']))
            self.utilities.assert_result(types, self.utilities.get_value(self.course_elements['template_type']))
            self.utilities.assert_result(no_of_student, self.utilities.get_value(self.course_elements['no_of_students']))
            self.utilities.assert_result(description, self.utilities.get_value(self.course_elements['description']))

            self.utilities.assert_result(course_title, self.utilities.get_value(self.course_elements['course_title']))
            self.utilities.assert_result(frequency, self.utilities.get_value(self.course_elements['frequency']))

            self.utilities.assert_result(start_date, self.utilities.get_value(self.course_elements['start_date']))
            self.utilities.assert_result(end_date, self.utilities.get_value(self.course_elements['end_date']))

            self.utilities.assert_result(fao_rate, self.utilities.get_value(self.course_elements['fao_rate']))
            self.utilities.assert_result(gc_rate, self.utilities.get_value(self.course_elements['gc_rate']))

            fao_ta_value = self._process_string_for_counselor(self.utilities.get_text(self.course_elements['fao_ta_value']))
            gc_instructor_value = self._process_string_for_counselor(self.utilities.get_text((self.course_elements['gc_instructor_value'])))
            pm_value = self._process_string_for_counselor(self.utilities.get_text((self.course_elements['pm_value'])))
            cm_value = self._process_string_for_counselor(self.utilities.get_text((self.course_elements['cm_value'])))

            self.utilities.assert_result(fao_ta, fao_ta_value)
            self.utilities.assert_result(gc_instructor, gc_instructor_value)
            self.utilities.assert_result(pm, pm_value)
            self.utilities.assert_result(cm, cm_value)
            for index, student in enumerate(students_arr):
                students_locator = self.utilities.process_element(self.course_elements['students_index'], "index", str(index + 1))
                students_value = self._process_string_for_counselor(self.utilities.get_text(students_locator))
                self.utilities.assert_result(student, students_value)
            for index, other in enumerate(other_arr):
                other_locator = self.utilities.process_element(self.course_elements['other_index'], "index", str(index + 1))
                other_value = self._process_string_for_counselor(self.utilities.get_text(other_locator))
                self.utilities.assert_result(other, other_value)
            self.logger.info("[ CoursePage ] verify_many_students_data_is_populating_on_course_fields_correctly: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] verify_many_students_data_is_populating_on_course_fields_correctly: FAIL - {str(e)}")
            raise

    def search_course_for_edit(self, template_type = "single student", record_index = 0, course_type= "current"):
        try:
            if template_type.lower() == "single student":
                course_title = self.json_reader.get_single_student_data("Course Details", "Course Title", record_index)
            elif template_type.lower() == "many students":
                course_title = self.json_reader.get_many_students_data("Course Details", "Course Title", record_index)

            if course_type == "upcoming":
                self.utilities.click_element(self.courses_page_elements['upcoming'])
                self.utilities.click_element(self.courses_page_elements['upcoming_search_icon'])
                self.utilities.send_text(self.courses_page_elements['upcoming_search_input'], course_title)
            elif course_type == "previous":
                self.utilities.click_element(self.courses_page_elements['previous'])
                self.utilities.click_element(self.courses_page_elements['previous_search_icon'])
                self.utilities.send_text(self.courses_page_elements['previous_search_input'], course_title)
            else:
                self.utilities.click_element(self.courses_page_elements['current_search_icon'])
                self.utilities.send_text(self.courses_page_elements['current_search_input'], course_title)

            self.verify_searched_course(course_title, course_type)
            self.utilities.click_element(self.course_table_records['edit_first_row'])
            self.logger.info("[ CoursePage ] search_course_for_edit: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] search_course_for_edit: FAIL - {str(e)}")
            raise

    def select_template_with_rate_type_and_its_validation(self, template_type, rate_type=None, record_index=0):
        try:
            if template_type.lower() == "single student":
                templates = self.json_reader.get_single_student_data("Course Details", "Templates", record_index)
                self.utilities.select_dropdown(self.course_elements['templates'], templates)
            elif template_type.lower() == "many students":
                templates = self.json_reader.get_many_students_data("Course Details", "Templates", record_index)
                self.utilities.select_dropdown(self.course_elements['templates'], templates)

            if rate_type is not None:
                if rate_type.lower() == "template rates" and template_type.lower() == "single student":
                    self.utilities.click_element(self.template_popup_elements['template_rate'])
                    fao_rate = self.json_reader.get_single_student_data("Rate", "FAO Rate", record_index)
                    gc_rate = self.json_reader.get_single_student_data("Rate", "GC Rate", record_index)
                    self.utilities.assert_result(fao_rate, self.utilities.get_value(self.course_elements['fao_rate']))
                    self.utilities.assert_result(gc_rate, self.utilities.get_value(self.course_elements['gc_rate']))
                elif rate_type.lower() == "template rates" and template_type.lower() == "many students":
                    self.utilities.click_element(self.template_popup_elements['template_rate'])
                    fao_rate = self.json_reader.get_many_students_data("Rate", "FAO Rate", record_index)
                    gc_rate = self.json_reader.get_many_students_data("Rate", "GC Rate", record_index)
                    self.utilities.assert_result(fao_rate, self.utilities.get_value(self.course_elements['fao_rate']))
                    self.utilities.assert_result(gc_rate, self.utilities.get_value(self.course_elements['gc_rate']))
                elif rate_type.lower() == "course rates":
                    self.utilities.click_element(self.template_popup_elements['course_rate'])
                    self.utilities.assert_field_empty(self.course_elements['fao_rate'])
                    self.utilities.assert_field_empty(self.course_elements['gc_rate'])
            else:
                self.utilities.click_element(self.template_popup_elements['close'])
                self.utilities.assert_field_empty(self.course_elements['templates'])
                self.utilities.assert_field_empty(self.course_elements['template_type'])
                self.utilities.assert_field_empty(self.course_elements['no_of_students'])
                self.utilities.assert_field_empty(self.course_elements['description'])
                self.utilities.assert_field_empty(self.course_elements['fao_rate'])
                self.utilities.assert_field_empty(self.course_elements['gc_rate'])

            if template_type.lower() == "single student":
                types = self.json_reader.get_single_student_data("Course Details", "Type", record_index)
                no_of_student = self.json_reader.get_single_student_data("Course Details", "No. of Students",record_index)
                description = self.json_reader.get_single_student_data("Course Details", "Description", record_index)
                self.utilities.assert_result(types, self.utilities.get_value(self.course_elements['template_type']))
                self.utilities.assert_result(no_of_student,self.utilities.get_value(self.course_elements['no_of_students']))
                self.utilities.assert_result(description, self.utilities.get_value(self.course_elements['description']))
            elif template_type.lower() == "many students":
                types = self.json_reader.get_many_students_data("Course Details", "Type", record_index)
                no_of_student = self.json_reader.get_many_students_data("Course Details", "No. of Students",record_index)
                description = self.json_reader.get_many_students_data("Course Details", "Description", record_index)
                self.utilities.assert_result(types, self.utilities.get_value(self.course_elements['template_type']))
                self.utilities.assert_result(no_of_student,self.utilities.get_value(self.course_elements['no_of_students']))
                self.utilities.assert_result(description, self.utilities.get_value(self.course_elements['description']))

            self.logger.info("[ CoursePage ] select_template_with_rate_type_and_its_validation: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] select_template_with_rate_type_and_its_validation: FAIL - {str(e)}")
            raise

    def _add_single_student_course_details(self, record_index = 0):
        try:
            course_title = self.json_reader.get_single_student_data("Course Details", "Course Title", record_index)
            frequency_arr = self.json_reader.get_single_student_data("Course Details", "Frequency", record_index)
            frequency = frequency_arr[0]
            self.utilities.send_text(self.course_elements['course_title'], course_title)
            self.utilities.select_dropdown(self.course_elements['frequency'], frequency)
            self.logger.info("[ CoursePage ] _add_single_student_course_details: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] _add_single_student_course_details: FAIL - {str(e)}")
            raise

    def _add_many_students_course_details(self, record_index = 0):
        try:
            course_title = self.json_reader.get_many_students_data("Course Details", "Course Title", record_index)
            frequency_arr = self.json_reader.get_many_students_data("Course Details", "Frequency", record_index)
            frequency = frequency_arr[0]
            self.utilities.send_text(self.course_elements['course_title'], course_title)
            self.utilities.select_dropdown(self.course_elements['frequency'], frequency)
            self.logger.info("[ CoursePage ] _add_many_students_course_details: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] _add_many_students_course_details: FAIL - {str(e)}")
            raise

    def _add_single_student_rate(self, record_index = 0):
        try:
            fao_rate = self.json_reader.get_single_student_data("Rate", "FAO Rate", record_index)
            gc_rate = self.json_reader.get_single_student_data("Rate", "GC Rate", record_index)
            self.utilities.send_text(self.course_elements['fao_rate'], fao_rate)
            self.utilities.send_text(self.course_elements['gc_rate'], gc_rate)
            self.logger.info("[ CoursePage ] _add_single_student_rate: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] _add_single_student_rate: FAIL - {str(e)}")
            raise

    def _add_many_students_rate(self, record_index = 0):
        try:
            fao_rate = self.json_reader.get_many_students_data("Rate", "FAO Rate", record_index)
            gc_rate = self.json_reader.get_many_students_data("Rate", "GC Rate", record_index)
            self.utilities.send_text(self.course_elements['fao_rate'], fao_rate)
            self.utilities.send_text(self.course_elements['gc_rate'], gc_rate)
            self.logger.info("[ CoursePage ] _add_many_students_rate: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] _add_many_students_rate: FAIL - {str(e)}")
            raise

    def _set_start_and_end_date_for_single_student(self, record_index = 0):
        try:
            start_date = self.json_reader.get_single_student_data("Counselor", "Start Date", record_index)
            end_date = self.json_reader.get_single_student_data("Counselor", "End Date", record_index)
            start_date = self.utilities.get_date_in_yyyy_mm_dd_format(start_date)
            end_date = self.utilities.get_date_in_yyyy_mm_dd_format(end_date)
            self.utilities.select_date(self.course_elements['start_date'],start_date)
            self.utilities.select_date(self.course_elements['end_date'], end_date)
            self.logger.info("[ CoursePage ] _set_start_and_end_date_for_single_student: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] _set_start_and_end_date_for_single_student: FAIL - {str(e)}")
            raise

    def _set_start_and_end_date_for_many_students(self, record_index = 0):
        try:
            start_date = self.json_reader.get_many_students_data("Counselor", "Start Date", record_index)
            end_date = self.json_reader.get_many_students_data("Counselor", "End Date", record_index)
            start_date = self.utilities.get_date_in_yyyy_mm_dd_format(start_date)
            end_date = self.utilities.get_date_in_yyyy_mm_dd_format(end_date)
            self.utilities.select_date(self.course_elements['start_date'],start_date)
            self.utilities.select_date(self.course_elements['end_date'], end_date)
            self.logger.info("[ CoursePage ] _set_start_and_end_date_for_many_students: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] _set_start_and_end_date_for_many_students: FAIL - {str(e)}")
            raise

    def _set_counselors_for_single_student(self, record_index = 0):
        try:
            fao_ta = self.json_reader.get_single_student_data("Counselor", "FAO/TA", record_index)
            gc_instructor = self.json_reader.get_single_student_data("Counselor", "GC/Instructor", record_index)
            pm = self.json_reader.get_single_student_data("Counselor", "PM", record_index)
            cm = self.json_reader.get_single_student_data("Counselor", "CM", record_index)
            other_arr = self.json_reader.get_single_student_data("Counselor", "Other", record_index)
            students = self.json_reader.get_single_student_data("Counselor", "Students", record_index)

            self.utilities.single_select_search_dropdown(self.course_elements['fao_ta_click'],self.course_elements['fao_ta_input'],fao_ta)
            self.utilities.single_select_search_dropdown(self.course_elements['gc_instructor_click'],self.course_elements['gc_instructor_input'], gc_instructor)
            self.utilities.single_select_search_dropdown(self.course_elements['pm_click'],self.course_elements['pm_input'], pm)
            self.utilities.single_select_search_dropdown(self.course_elements['cm_click'],self.course_elements['cm_input'], cm)
            self.utilities.multi_select_search_dropdown(self.course_elements['other'],other_arr)
            self.utilities.single_select_search_dropdown(self.course_elements['students_click'], self.course_elements['students_input'], students)
            self.logger.info("[ CoursePage ] _set_counselors_for_single_student: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] _set_counselors_for_single_student: FAIL - {str(e)}")
            raise

    def _set_counselors_for_many_students(self, record_index = 0):
        try:
            fao_ta = self.json_reader.get_many_students_data("Counselor", "FAO/TA", record_index)
            gc_instructor = self.json_reader.get_many_students_data("Counselor", "GC/Instructor", record_index)
            pm = self.json_reader.get_many_students_data("Counselor", "PM", record_index)
            cm = self.json_reader.get_many_students_data("Counselor", "CM", record_index)
            other_arr = self.json_reader.get_many_students_data("Counselor", "Other", record_index)
            students_arr = self.json_reader.get_many_students_data("Counselor", "Students", record_index)

            self.utilities.single_select_search_dropdown(self.course_elements['fao_ta_click'],self.course_elements['fao_ta_input'], fao_ta)
            self.utilities.single_select_search_dropdown(self.course_elements['gc_instructor_click'],self.course_elements['gc_instructor_input'], gc_instructor)
            self.utilities.single_select_search_dropdown(self.course_elements['pm_click'],self.course_elements['pm_input'], pm)
            self.utilities.single_select_search_dropdown(self.course_elements['cm_click'],self.course_elements['cm_input'], cm)
            self.utilities.multi_select_search_dropdown(self.course_elements['other'], other_arr)
            self.utilities.multi_select_search_dropdown(self.course_elements['students'], students_arr)

            self.logger.info("[ CoursePage ] _set_counselors_for_many_students: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] _set_counselors_for_many_students: FAIL - {str(e)}")
            raise
    def _add_single_student_counselor_data(self, record_index = 0):
        try:
            self._set_counselors_for_single_student(record_index)
            self._set_start_and_end_date_for_single_student(record_index)
            self.logger.info("[ CoursePage ] _add_single_student_counselor_data: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] _add_single_student_counselor_data: FAIL - {str(e)}")
            raise

    def _add_many_students_counselor_data(self, record_index=0):
        try:
            self._set_counselors_for_many_students(record_index)
            self._set_start_and_end_date_for_many_students(record_index)
            self.logger.info("[ CoursePage ] _add_many_students_counselor_data: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] _add_many_students_counselor_data: FAIL - {str(e)}")
            raise

    def add_single_student_course_data_with_rates(self, record_index = 0):
        try:
            self._add_single_student_course_details(record_index)
            self._add_single_student_counselor_data(record_index)
            self._add_single_student_rate(record_index)
            self.save_course()
            self.logger.info("[ CoursePage ] add_single_student_course_data_with_rates: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] add_single_student_course_data_with_rates: FAIL - {str(e)}")
            raise

    def add_single_student_course_data_without_rates(self, record_index = 0):
        try:
            self._add_single_student_course_details(record_index)
            self._add_single_student_counselor_data(record_index)
            self.save_course()
            self.logger.info("[ CoursePage ] add_single_student_course_data_without_rates: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] add_single_student_course_data_without_rates: FAIL - {str(e)}")
            raise

    def save_course(self):
        try:
            self.utilities.click_element(self.course_elements['save_information'])
            self.logger.info("[ CoursePage ] save_course: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] save_course: FAIL - {str(e)}")
            raise

    def cancel_course(self):
        try:
            self.utilities.click_element(self.course_elements['cancel'])
            self.logger.info("[ CoursePage ] cancel_course: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] cancel_course: FAIL - {str(e)}")
            raise


    def add_many_students_course_data_with_rates(self, record_index = 0):
        try:
            self._add_many_students_course_details(record_index)
            self._add_many_students_rate(record_index)
            self._add_many_students_counselor_data(record_index)
            self.save_course()
            self.logger.info("[ CoursePage ] add_many_students_course_data_with_rates: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] add_many_students_course_data_with_rates: FAIL - {str(e)}")
            raise

    def add_many_students_course_data_without_rates(self, record_index = 0):
        try:
            self._add_many_students_course_details(record_index)
            self._add_many_students_counselor_data(record_index)
            self.save_course()
            self.logger.info("[ CoursePage ] add_many_students_course_data_without_rates: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] add_many_students_course_data_without_rates: FAIL - {str(e)}")
            raise


    def validate_template_field_is_empty(self):
        try:
            self.utilities.assert_field_empty(self.course_elements['templates'])
            self.logger.info("[ CoursePage ] validate_template_field_is_empty: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] validate_template_field_is_empty: FAIL - {str(e)}")
            raise

    def search_and_validate_course_in_list(self, student_type = "single", search_type = "course_name", course_type = "current", record_index = 0):
        try:
            if search_type == "course_name" and student_type == "single":
                search_info = self.json_reader.get_single_student_data("Course Details", "Course Title", record_index)
            elif search_type == "course_name" and student_type == "many":
                search_info = self.json_reader.get_many_students_data("Course Details", "Course Title", record_index)
            elif search_type == "counselor" and student_type == "single":
                search_info = self.json_reader.get_single_student_data("Counselor", "FAO/TA", record_index)
            elif search_type == "counselor" and student_type == "many":
                search_info = self.json_reader.get_many_students_data("Counselor", "FAO/TA", record_index)

            if course_type == "upcoming":
                self.utilities.click_element(self.courses_page_elements['upcoming'])
                self.utilities.click_element(self.courses_page_elements['upcoming_search_icon'])
                self.utilities.send_text(self.courses_page_elements['upcoming_search_input'], search_info)
            elif course_type == "previous":
                self.utilities.click_element(self.courses_page_elements['previous'])
                self.utilities.click_element(self.courses_page_elements['previous_search_icon'])
                self.utilities.send_text(self.courses_page_elements['previous_search_input'], search_info)
            else:
                self.utilities.click_element(self.courses_page_elements['current_search_icon'])
                self.utilities.send_text(self.courses_page_elements['current_search_input'], search_info)
            self.verify_searched_course(search_info, course_type)
            web_driver = BrowserDriver.get_driver()
            web_driver.refresh()
            self.logger.info("[ CoursePage ] search_and_validate_course_in_list: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] search_and_validate_course_in_list: FAIL - {str(e)}")
            raise

    def verify_searched_course(self, searched_info, course_type = "current"):
        try:
            if course_type == "current":
                course_name_locator = self.utilities.process_element(self.course_table_records['course_name'], "rowValue", "1")
                fao_ta_locator = self.utilities.process_element(self.course_table_records['fao_ta'], "rowValue", "1")
                gc_instructor_locator = self.utilities.process_element(self.course_table_records['gc_instructor'], "rowValue", "1")
                pm_locator = self.utilities.process_element(self.course_table_records['pm'], "rowValue", "1")
                cm_locator = self.utilities.process_element(self.course_table_records['cm'], "rowValue", "1")
            elif course_type == "previous":
                course_name_locator = self.utilities.process_element(self.course_table_records['previous_course_name'], "rowValue", "1")
                fao_ta_locator = self.utilities.process_element(self.course_table_records['previous_fao_ta'], "rowValue", "1")
                gc_instructor_locator = self.utilities.process_element(self.course_table_records['previous_gc_instructor'], "rowValue", "1")
                pm_locator = self.utilities.process_element(self.course_table_records['previous_pm'], "rowValue", "1")
                cm_locator = self.utilities.process_element(self.course_table_records['previous_cm'], "rowValue", "1")
            elif course_type == "upcoming":
                course_name_locator = self.utilities.process_element(self.course_table_records['upcoming_course_name'], "rowValue", "1")
                fao_ta_locator = self.utilities.process_element(self.course_table_records['upcoming_fao_ta'], "rowValue", "1")
                gc_instructor_locator = self.utilities.process_element(self.course_table_records['upcoming_gc_instructor'], "rowValue", "1")
                pm_locator = self.utilities.process_element(self.course_table_records['upcoming_pm'], "rowValue", "1")
                cm_locator = self.utilities.process_element(self.course_table_records['upcoming_cm'], "rowValue", "1")

            course_name = self._get_text_after_first_space(self.utilities.get_text(course_name_locator))
            fao_ta = self._get_text_after_first_space(self.utilities.get_text(fao_ta_locator))
            gc_instructor = self._get_text_after_first_space(self.utilities.get_text(gc_instructor_locator))
            pm = self._get_text_after_first_space(self.utilities.get_text(pm_locator))
            cm = self._get_text_after_first_space(self.utilities.get_text(cm_locator))
            if course_name.startswith(searched_info) or fao_ta.startswith(searched_info) or gc_instructor.startswith(searched_info) or pm.startswith(searched_info) or cm.startswith(searched_info):
                if course_name.startswith(searched_info):
                    self.logger.info("Searched Course Name: " + str(course_name) + "| matched with list top element")
                    allure.attach("Searched Course Name: " + str(course_name) + "| matched with list top element", "Info")
                if fao_ta.startswith(searched_info):
                    self.logger.info("Searched FAO/TA: " + str(fao_ta) + "| matched with list top element:")
                    allure.attach("Searched FAO/TA: " + str(fao_ta) + "| matched with list top element:", "Info")
                if gc_instructor.startswith(searched_info):
                    self.logger.info("Searched GC/Instructor: " + str(gc_instructor) + "| matched with list top element")
                    allure.attach("Searched GC/Instructor: " + str(gc_instructor) + "| matched with list top element", "Info")
                if pm.startswith(searched_info):
                    self.logger.info("Searched PM: " + str(pm) + "| matched with list top element:")
                    allure.attach("Searched PM: " + str(pm) + "| matched with list top element:", "Info")
                if cm.startswith(searched_info):
                    self.logger.info("Searched CM: " + str(cm) + "| matched with list top element:")
                    allure.attach("Searched CM: " + str(cm) + "| matched with list top element:", "Info")
            else:
                self.logger.info("Search Results doesn't matched with the Expected Results")
                allure.attach("Search Results doesn't matched with the Expected Results", "Error")
                assert False, "Search Results doesn't matched with the Expected Results"

            self.logger.info("[ CoursePage ] search_for_template: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] search_for_template: FAIL - {str(e)}")
            raise

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

    def validate_alert_message(self, expected_message):
        try:
            self.utilities.verify_alert(self.alert['toast_body'], expected_message)
            self.utilities.click_with_js_executor(self.alert['close_toast'])
            self.logger.info("[ CoursePage ] validate_alert_message: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] validate_alert_message: FAIL - {str(e)}")
            raise

    def validate_alert_error(self, expected_message, row):
        try:
            alert_error_locator = self.utilities.process_element(self.alert['toast_error'], "rowValue", str(row))
            self.utilities.verify_alert(alert_error_locator, expected_message)
            self.utilities.click_with_js_executor(self.alert['close_toast'])
            self.logger.info("[ CoursePage ] validate_alert_error: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] validate_alert_error: FAIL - {str(e)}")
            raise

    def add_course_mandatory_fields_for_many_students_and_save_the_tab(self, record_index=0):
        try:
            course_title = self.json_reader.get_many_students_data("Course Details", "Course Title", record_index)
            frequency_arr = self.json_reader.get_many_students_data("Course Details", "Frequency", record_index)
            frequency = frequency_arr[0]
            fao_ta = self.json_reader.get_many_students_data("Counselor", "FAO/TA", record_index)
            gc_instructor = self.json_reader.get_many_students_data("Counselor", "GC/Instructor", record_index)
            pm = self.json_reader.get_many_students_data("Counselor", "PM", record_index)
            cm = self.json_reader.get_many_students_data("Counselor", "CM", record_index)
            students_arr = self.json_reader.get_many_students_data("Counselor", "Students", record_index)
            start_date = self.json_reader.get_many_students_data("Counselor", "Start Date", record_index)
            end_date = self.json_reader.get_many_students_data("Counselor", "End Date", record_index)
            start_date = self.utilities.get_date_in_yyyy_mm_dd_format(start_date)
            end_date = self.utilities.get_date_in_yyyy_mm_dd_format(end_date)
            fao_rate = self.json_reader.get_many_students_data("Rate", "FAO Rate", record_index)
            gc_rate = self.json_reader.get_many_students_data("Rate", "GC Rate", record_index)
            self.save_course()
            self.utilities.send_text(self.course_elements['course_title'], course_title)
            self.save_course()
            self.utilities.select_dropdown(self.course_elements['frequency'], frequency)
            self.save_course()
            for i in range(1,3):
                if i == 1:
                    self.utilities.select_date(self.course_elements['start_date'], start_date)
                    self.save_course()
                    self.utilities.select_date(self.course_elements['end_date'], "current-60")
                    self.save_course()
                else:
                    self.utilities.select_date(self.course_elements['end_date'], end_date)
                    self.save_course()
                error_list_1 = ["The FAO field is required.",
                              "The GC field is required.",
                              "The PM field is required.",
                              "The CM field is required.",
                              "The course end date is must be after course start date.",
                              "The FAO Rate field is required.",
                              "The GC Rate field is required."]
                error_list_2 = ["The FAO field is required.",
                              "The GC field is required.",
                              "The PM field is required.",
                              "The CM field is required.",
                              "The FAO Rate field is required.",
                              "The GC Rate field is required."]
                for index, error in enumerate(error_list_1):
                    if i == 1:
                        self.validate_alert_error(error, index + 1)
                        if index + 1 == len(error_list_1):
                            self.utilities.click_element(self.alert['close_toast'])
                for index, error in enumerate(error_list_2):
                    if i > 1:
                        self.validate_alert_error(error, index + 1)
                        if index + 1 == len(error_list_2):
                            self.utilities.click_element(self.alert['close_toast'])

            self.save_course()
            self._validate_error_msg(0)
            self.utilities.single_select_search_dropdown(self.course_elements['fao_ta_click'],self.course_elements['fao_ta_input'], fao_ta)
            self.save_course()
            self._validate_error_msg(1)
            self.utilities.single_select_search_dropdown(self.course_elements['gc_instructor_click'],self.course_elements['gc_instructor_input'], gc_instructor)
            self.save_course()
            self._validate_error_msg(2)
            self.utilities.single_select_search_dropdown(self.course_elements['pm_click'],self.course_elements['pm_input'], pm)
            self.save_course()
            self._validate_error_msg(3)
            self.utilities.single_select_search_dropdown(self.course_elements['cm_click'],self.course_elements['cm_input'], cm)
            self.save_course()
            self._validate_error_msg(4)
            self.utilities.send_text(self.course_elements['fao_rate'], fao_rate)
            self.save_course()
            self._validate_error_msg(5)
            self.utilities.send_text(self.course_elements['gc_rate'], gc_rate)
            self.save_course()
            self.validate_alert_error("The course students field is required.", 1)
            self.utilities.multi_select_search_dropdown(self.course_elements['students'], students_arr)
            self.save_course()
            self.logger.info("[ CoursePage ] add_course_mandatory_fields_for_many_students_and_save_the_tab: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] add_course_mandatory_fields_for_many_students_and_save_the_tab: FAIL - {str(e)}")
            raise
    def _validate_error_msg(self, start_index = 0):
        try:
            error_list = ["The FAO field is required.",
                            "The GC field is required.",
                            "The PM field is required.",
                            "The CM field is required.",
                            "The FAO Rate field is required.",
                            "The GC Rate field is required.",
                            ]
            iteration = 1
            for index, error in enumerate(error_list[start_index:], start=start_index):
                self.validate_alert_error(error, iteration)
                iteration = iteration + 1
                if index + 1 == len(error_list):
                    self.utilities.click_element(self.alert['close_toast'])

            self.logger.info("[ CoursePage ] _validate_error_msg: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] _validate_error_msg: FAIL - {str(e)}")
            raise

    def validate_single_student_templates_in_dropdown(self):
        try:
            data = self.database_connection.execute_select_query(self.utilities.read_db_query("get_single_student_templates"))
            single_student_templates = [item[0] for item in data]
            single_student_templates = sorted(single_student_templates)
            self.logger.info("single_student_templates")
            self.logger.info(str(len(single_student_templates)))
            self.logger.info(single_student_templates)
            template_dropdown = self.utilities.get_dropdown_options(self.course_elements['templates'])
            if template_dropdown and template_dropdown[0] == 'Select Template':
                template_dropdown.pop(0)
            template_dropdown = sorted(template_dropdown)
            self.logger.info("template_dropdown")
            self.logger.info(str(len(template_dropdown)))
            self.logger.info(template_dropdown)
            assert single_student_templates == template_dropdown, "Dropdown should have only single Student Template options"
            self.logger.info("Verified: Only Single User template options are present")
            allure.attach("Verified: Only Single User template options are present", "Info")
            self.logger.info("[ CoursePage ] validate_single_student_templates_in_dropdown: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] validate_single_student_templates_in_dropdown: FAIL - {str(e)}")
            raise

    def validate_many_students_templates_in_dropdown(self):
        try:
            data = self.database_connection.execute_select_query(self.utilities.read_db_query("get_many_students_templates"))
            single_student_templates = [item[0] for item in data]
            single_student_templates = sorted(single_student_templates)
            template_dropdown = self.utilities.get_dropdown_options(self.course_elements['templates'])
            if template_dropdown and template_dropdown[0] == 'Select Template':
                template_dropdown.pop(0)
            template_dropdown = sorted(template_dropdown)
            assert single_student_templates == template_dropdown, "Dropdown should have only single Student Template options"
            self.logger.info("Only Single User template options are present")
            allure.attach("Only Single User template options are present", "Info")
            self.logger.info("[ CoursePage ] validate_single_student_templates_in_dropdown: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] validate_single_student_templates_in_dropdown: FAIL - {str(e)}")
            raise

    def add_counselor_filter_and_search_with_validation(self, record_index = 0, course_type = "current"):
        try:
            course_title = self.json_reader.get_many_students_data("Course Details", "Course Title", record_index)
            fao_ta = self.json_reader.get_many_students_data("Counselor", "FAO/TA", record_index)
            gc_instructor = self.json_reader.get_many_students_data("Counselor", "GC/Instructor", record_index)
            pm = self.json_reader.get_many_students_data("Counselor", "PM", record_index)
            cm = self.json_reader.get_many_students_data("Counselor", "CM", record_index)
            other_arr = self.json_reader.get_many_students_data("Counselor", "Other", record_index)

            self._search_for_counselor_filter(course_title, fao_ta, course_type, "fao_ta")
            self._search_for_counselor_filter(course_title, gc_instructor, course_type, "gc_instructor", False)
            self._search_for_counselor_filter(course_title, pm, course_type, "pm", False)
            self._search_for_counselor_filter(course_title, cm, course_type, "cm", False)

            web_driver = BrowserDriver.get_driver()
            web_driver.refresh()
            self.utilities.select_dropdown(self.courses_page_elements['course_counselor'], fao_ta)
            self._search_for_counselor_filter(course_title, fao_ta, course_type,"fao_ta")

            web_driver.refresh()
            self.utilities.select_dropdown(self.courses_page_elements['course_counselor'], gc_instructor)
            self._search_for_counselor_filter(course_title, gc_instructor, course_type, "gc_instructor")

            web_driver.refresh()
            self.utilities.select_dropdown(self.courses_page_elements['course_counselor'], pm)
            self._search_for_counselor_filter(course_title, pm, course_type, "pm")

            web_driver.refresh()
            self.utilities.select_dropdown(self.courses_page_elements['course_counselor'], cm)
            self._search_for_counselor_filter(course_title, cm, course_type, "cm")

            for other in other_arr:
                web_driver.refresh()
                self.utilities.select_dropdown(self.courses_page_elements['course_counselor'], other)
                self._search_for_counselor_filter(course_title, other, course_type, "other")

            self.logger.info("[ CoursePage ] add_counselor_filter_and_search_with_validation: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] add_counselor_filter_and_search_with_validation: FAIL - {str(e)}")
            raise

    def _search_for_counselor_filter(self,course_title, expected_value, course_type = "current", column_type = "fao_ta", is_search: bool = True):
        try:
            if is_search is True:
                if course_type == "upcoming":
                    self.utilities.click_element(self.courses_page_elements['upcoming'])
                    self.utilities.click_element(self.courses_page_elements['upcoming_search_icon'])
                    self.utilities.send_text(self.courses_page_elements['upcoming_search_input'], course_title)
                elif course_type == "previous":
                    self.utilities.click_element(self.courses_page_elements['previous'])
                    self.utilities.click_element(self.courses_page_elements['previous_search_icon'])
                    self.utilities.send_text(self.courses_page_elements['previous_search_input'], course_title)
                else:
                    self.utilities.click_element(self.courses_page_elements['current_search_icon'])
                    self.utilities.send_text(self.courses_page_elements['current_search_input'], course_title)

            if course_type == "current":
                course_name_locator = self.utilities.process_element(self.course_table_records['course_name'], "rowValue", "1")
                fao_ta_locator = self.utilities.process_element(self.course_table_records['fao_ta'], "rowValue", "1")
                gc_instructor_locator = self.utilities.process_element(self.course_table_records['gc_instructor'], "rowValue", "1")
                pm_locator = self.utilities.process_element(self.course_table_records['pm'], "rowValue", "1")
                cm_locator = self.utilities.process_element(self.course_table_records['cm'], "rowValue", "1")
            elif course_type == "previous":
                course_name_locator = self.utilities.process_element(self.course_table_records['previous_course_name'], "rowValue", "1")
                fao_ta_locator = self.utilities.process_element(self.course_table_records['previous_fao_ta'], "rowValue", "1")
                gc_instructor_locator = self.utilities.process_element(self.course_table_records['previous_gc_instructor'], "rowValue", "1")
                pm_locator = self.utilities.process_element(self.course_table_records['previous_pm'], "rowValue", "1")
                cm_locator = self.utilities.process_element(self.course_table_records['previous_cm'], "rowValue", "1")
            elif course_type == "upcoming":
                course_name_locator = self.utilities.process_element(self.course_table_records['upcoming_course_name'], "rowValue", "1")
                fao_ta_locator = self.utilities.process_element(self.course_table_records['upcoming_fao_ta'], "rowValue", "1")
                gc_instructor_locator = self.utilities.process_element(self.course_table_records['upcoming_gc_instructor'], "rowValue", "1")
                pm_locator = self.utilities.process_element(self.course_table_records['upcoming_pm'], "rowValue", "1")
                cm_locator = self.utilities.process_element(self.course_table_records['upcoming_cm'], "rowValue", "1")

            course_name = self._get_text_after_first_space(self.utilities.get_text(course_name_locator))
            fao_ta = self._get_text_after_first_space(self.utilities.get_text(fao_ta_locator))
            gc_instructor = self._get_text_after_first_space(self.utilities.get_text(gc_instructor_locator))
            pm = self._get_text_after_first_space(self.utilities.get_text(pm_locator))
            cm = self._get_text_after_first_space(self.utilities.get_text(cm_locator))
            if course_name.startswith(course_title):
                self.logger.info("Searched Course Name: " + str(course_name) + "| matched with list top element")
                allure.attach("Searched Course Name: " + str(course_name) + "| matched with list top element", "Info")
                if column_type == "fao_ta":
                    if fao_ta.startswith(expected_value):
                        self.logger.info(expected_value + ": Does match with Search Results of: " + column_type)
                        allure.attach(expected_value + ": Does match with Search Results of: " + column_type, "Info")
                    else:
                        self.logger.error(expected_value + ": Does not match with Search Results of: " + column_type)
                        allure.attach(expected_value + ": Does not match with Search Results of: " + column_type, "Error")
                        assert False, f"Assertion failed: {expected_value} does not match with Search Results of {column_type}"
                elif column_type == "gc_instructor":
                    if gc_instructor.startswith(expected_value):
                        self.logger.info(expected_value + ": Does match with Search Results of: " + column_type)
                        allure.attach(expected_value + ": Does match with Search Results of: " + column_type, "Info")
                    else:
                        self.logger.error(expected_value + ": Does not match with Search Results of: " + column_type)
                        allure.attach(expected_value + ": Does not match with Search Results of: " + column_type, "Error")
                        assert False, f"Assertion failed: {expected_value} does not match with Search Results of {column_type}"
                elif column_type == "pm":
                    if pm.startswith(expected_value):
                        self.logger.info(expected_value + ": Does match with Search Results of: " + column_type)
                        allure.attach(expected_value + ": Does match with Search Results of: " + column_type, "Info")
                    else:
                        self.logger.error(expected_value + ": Does not match with Search Results of: " + column_type)
                        allure.attach(expected_value + ": Does not match with Search Results of: " + column_type, "Error")
                        assert False, f"Assertion failed: {expected_value} does not match with Search Results of {column_type}"
                elif column_type == "cm":
                    if cm.startswith(expected_value):
                        self.logger.info(expected_value + ": Does match with Search Results of: " + column_type)
                        allure.attach(expected_value + ": Does match with Search Results of: " + column_type, "Info")
                    else:
                        self.logger.error(expected_value + ": Does not match with Search Results of: " + column_type)
                        allure.attach(expected_value + ": Does not match with Search Results of: " + column_type, "Error")
                        assert False, f"Assertion failed: {expected_value} does not match with Search Results of {column_type}"
                elif column_type == "other":
                    self.logger.info("The course is present for others counselor filter")
                    allure.attach("The course is present for others counselor filter", "Info")
            else:
                self.logger.error("Searched Course Name: " + str(course_title) + "| doesn't matched with actual listed course: " + str(course_name))
                allure.attach("Searched Course Name: " + str(course_title) + " doesn't matched with actual listed course: " + str(course_name), "Error")
                assert False, "Assertion failed: Searched Course Name: " + str(course_title) + ", doesn't match with actual listed course: " + str(course_name)
            self.logger.info("[ CoursePage ] _search_for_counselor_filter: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] _search_for_counselor_filter: FAIL - {str(e)}")
            raise

    def execute_deletion_of_courses(self):
        try:
            token, cookies = self.ingenius_api.generate_login_token()
            response, cookies = self.ingenius_api.login_with_admin(token, cookies)
            course_ids = self.database_connection.execute_select_query(self.utilities.read_db_query("delete_course_id_to_delete"))
            for course_id in course_ids:
                cour_id = course_id[0]
                self.ingenius_api.delete_course(str(cour_id), token, cookies)

            template_ids = self.database_connection.execute_select_query(self.utilities.read_db_query("get_template_id_to_delete"))
            for template_id in template_ids:
                temp_id = template_id[0]
                self.ingenius_api.delete_template(str(temp_id), token, cookies)
            self.logger.info("[ CoursePage ] execute_deletion_of_courses: PASS")
        except Exception as e:
            self.logger.error(f"[ CoursePage ] execute_deletion_of_courses: FAIL - {str(e)}")
            raise

    def _get_text_after_first_space(self, input_text):
        try:
            words = input_text.split()
            if len(words) > 1:
                return ' '.join(words[1:])
            else:
                return ''
        except Exception as e:
            print(f"An error occurred: {e}")
            return ''

    def _process_string_for_counselor(self, input_string):
        cleaned_string = input_string.strip()
        cleaned_string = cleaned_string.replace('Remove item', '').strip()
        return cleaned_string