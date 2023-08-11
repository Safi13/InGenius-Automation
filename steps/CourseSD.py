import time

from behave import given, when, then
import logging

from pages.CoursePage import CoursePage
from pages.LoginPage import LoginPage
from pages.TemplatePage import TemplatePage

logger = logging.getLogger(__name__)

template_page = TemplatePage()
course_page = CoursePage()
login_page = LoginPage()

@then('the course should be successfully created')
def step_impl(context):
    course_page.validate_alert_message("Course has been created successfully.")
    course_page.verify_current_page_is_courses_page()


@then('the Course should be updated successfully')
def step_impl(context):
    course_page.validate_alert_message("Course has been updated successfully.")
    course_page.verify_current_page_is_courses_page()

@when('the user adds a new course')
def step_impl(context):
    course_page.add_course_and_verify_that_course_is_opened()

@when('the user cancels the Courses form')
def step_impl(context):
    course_page.select_template_with_rate_type_and_its_validation("Single Student", "template rates")
    course_page.cancel_course()

@then('the user lands on current courses tab')
def step_impl(context):
    course_page.verify_current_page_is_courses_page()

@given('the current Course record should be present')
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()
    template_page.add_template_info(4)
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()
    template_page.validate_alert_message("Template has been created successfully.")
    template_page.verify_current_page_is_courses_page()

    course_page.add_course_and_verify_that_course_is_opened()
    course_page.select_template_with_rate_type_and_its_validation("Many Students", "template rates")
    course_page.add_many_students_course_data_without_rates()
    course_page.validate_alert_message("Course has been created successfully.")
    course_page.verify_current_page_is_courses_page()

@given('the upcoming Course record should be present')
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()
    template_page.add_template_info(4)
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()
    template_page.validate_alert_message("Template has been created successfully.")
    template_page.verify_current_page_is_courses_page()

    course_page.add_course_and_verify_that_course_is_opened()
    course_page.select_template_with_rate_type_and_its_validation("Many Students", "template rates",2)
    course_page.add_many_students_course_data_without_rates(2)
    course_page.validate_alert_message("Course has been created successfully.")
    course_page.verify_current_page_is_courses_page()

@given('the previous Course record should be present')
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()
    template_page.add_template_info(4)
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()
    template_page.validate_alert_message("Template has been created successfully.")
    template_page.verify_current_page_is_courses_page()

    course_page.add_course_and_verify_that_course_is_opened()
    course_page.select_template_with_rate_type_and_its_validation("Many Students", "template rates", 3)
    course_page.add_many_students_course_data_without_rates(3)
    course_page.validate_alert_message("Course has been created successfully.")
    course_page.verify_current_page_is_courses_page()

@when("the user select a single student template with template rates")
def step_impl(context):
    course_page.select_template_with_rate_type_and_its_validation("Single Student", "template rates")

@when("the user provides data for template with template rates in Course Details, Counselors and sets the rate for single student")
def step_impl(context):
    course_page.add_single_student_course_data_without_rates()

@when("the user provides data for template with course rates in Course Details, Counselors and sets the rate for single student")
def step_impl(context):
    course_page.add_single_student_course_data_with_rates()

@when("the user select a single student template with course rates")
def step_impl(context):
    course_page.select_template_with_rate_type_and_its_validation("Single Student", "course rates")

@when("the user select a many students template with template rates")
def step_impl(context):
    course_page.select_template_with_rate_type_and_its_validation("Many Students", "template rates")

@when("the user provides data for template with template rates in Course Details, Counselors and sets the rate for many students")
def step_impl(context):
    course_page.add_many_students_course_data_without_rates()

@when("the user provides data for template with course rates in Course Details, Counselors and sets the rate for many students")
def step_impl(context):
    course_page.add_many_students_course_data_with_rates()
@when("the user select a many students template with course rates")
def step_impl(context):
    course_page.select_template_with_rate_type_and_its_validation("Many Students", "course rates")

@when("the provides the Course Details, Counselors and sets the rate while validating the mandatory fields")
def step_impl(context):
    course_page.save_course()
    course_page.select_template_with_rate_type_and_its_validation("Many Students", "course rates")
    course_page.add_course_mandatory_fields_for_many_students_and_save_the_tab()

@given("that the single student Course record should be present")
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()
    template_page.add_template_info(2)
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()
    template_page.validate_alert_message("Template has been created successfully.")
    template_page.verify_current_page_is_courses_page()

    course_page.add_course_and_verify_that_course_is_opened()
    course_page.select_template_with_rate_type_and_its_validation("Single Student", "template rates")
    course_page.add_single_student_course_data_without_rates()
    course_page.validate_alert_message("Course has been created successfully.")
    course_page.verify_current_page_is_courses_page()
@when("the user search for the single student template course and edits the course record")
def step_impl(context):
    course_page.search_course_for_edit()
    course_page.verify_single_student_data_is_populating_on_course_fields_correctly()

@when("the user validates that only single student templates are populating in the templates")
def step_impl(context):
    course_page.validate_single_student_templates_in_dropdown()
    pass

@when("the user provides the updated Course Information for single student course")
def step_impl(context):
    course_page.save_course()

@given("that the many students Course record should be present")
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()
    template_page.add_template_info(4)
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()
    template_page.validate_alert_message("Template has been created successfully.")
    template_page.verify_current_page_is_courses_page()

    course_page.add_course_and_verify_that_course_is_opened()
    course_page.select_template_with_rate_type_and_its_validation("Many Students", "template rates")
    course_page.add_many_students_course_data_without_rates()
    course_page.validate_alert_message("Course has been created successfully.")
    course_page.verify_current_page_is_courses_page()

@when("the user search for the many students template course and edits the course record")
def step_impl(context):
    course_page.search_course_for_edit("many students")
    course_page.verify_many_students_data_is_populating_on_course_fields_correctly()

@when("the user validates that only many students templates are populating in the templates")
def step_impl(context):
    course_page.validate_many_students_templates_in_dropdown()

@when("provides the updated Course Information for many students course")
def step_impl(context):
    course_page.save_course()

@given("that a single record of a single student template should be present")
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()
    template_page.add_template_info(2)
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()
    template_page.validate_alert_message("Template has been created successfully.")
    template_page.verify_current_page_is_courses_page()

@given("that a single record of many students template should be present")
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()
    template_page.add_template_info(4)
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()
    template_page.validate_alert_message("Template has been created successfully.")
    template_page.verify_current_page_is_courses_page()

@given("that the single student template record should be present")
def step_impl(context):
    record_index = [2,3]
    for record in record_index:
        template_page.add_template_and_verify_that_template_page_is_opened()
        template_page.add_template_info(record)
        template_page.next_step_after_template_info()
        template_page.add_progress_checklist()
        template_page.save_template()
        template_page.validate_alert_message("Template has been created successfully.")
        template_page.verify_current_page_is_courses_page()


@then("the user reselect a single student template with template rates and updated template rates should populate on respective fields")
def step_impl(context):
    time.sleep(1)
    course_page.select_template_with_rate_type_and_its_validation("Single Student", "template rates", 1)

@then("the user reselect a single student template with course rates and the rates should be empty")
def step_impl(context):
    time.sleep(1)
    course_page.select_template_with_rate_type_and_its_validation("Single Student", "course rates", 1)

@given("that the template record should be present")
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()
    template_page.add_template_info()
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()
    template_page.validate_alert_message("Template has been created successfully.")
    template_page.verify_current_page_is_courses_page()

@when("the user select a template with course and close the template popup")
def step_impl(context):
    course_page.select_template_with_rate_type_and_its_validation("Single Student")

@then("the template should not be selected in the create course form")
def step_impl(context):
    course_page.validate_template_field_is_empty()

@then("the user search for the single student course and its correctly visible in the current course list")
def step_impl(context):
    time.sleep(2)
    course_page.search_and_validate_course_in_list("single","course_name","current")
    course_page.search_and_validate_course_in_list("single","counselor","current")

@then("the user search for the single student course and its correctly visible in the upcoming course list")
def step_impl(context):
    time.sleep(2)
    course_page.search_and_validate_course_in_list("single", "course_name", "upcoming")
    course_page.search_and_validate_course_in_list("single", "counselor", "upcoming")

@then("the user search for the single student course and its correctly visible in the previous course list")
def step_impl(context):
    time.sleep(2)
    course_page.search_and_validate_course_in_list("single", "course_name", "previous")
    course_page.search_and_validate_course_in_list("single", "counselor", "previous")

@then("the user search for many students course and its correctly visible in the current course list")
def step_impl(context):
    time.sleep(2)
    course_page.search_and_validate_course_in_list("many","course_name","current")
    course_page.search_and_validate_course_in_list("many","counselor","current")

@then("the user search for many students course and its correctly visible in the upcoming course list")
def step_impl(context):
    time.sleep(2)
    course_page.search_and_validate_course_in_list("many", "course_name", "upcoming",2)
    course_page.search_and_validate_course_in_list("many", "counselor", "upcoming",2)

@then("the user search for many students course and its correctly visible in the previous course list")
def step_impl(context):
    time.sleep(2)
    course_page.search_and_validate_course_in_list("many", "course_name", "previous",3)
    course_page.search_and_validate_course_in_list("many", "counselor", "previous",3)


@given("the counselor linked current Course record should be present")
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()
    template_page.add_template_info(4)
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()
    template_page.validate_alert_message("Template has been created successfully.")
    template_page.verify_current_page_is_courses_page()

    course_page.add_course_and_verify_that_course_is_opened()
    course_page.select_template_with_rate_type_and_its_validation("Many Students", "template rates", 5)
    course_page.add_many_students_course_data_without_rates(5)
    course_page.validate_alert_message("Course has been created successfully.")
    course_page.verify_current_page_is_courses_page()

@given("the counselor linked previous Course record should be present")
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()
    template_page.add_template_info(4)
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()
    template_page.validate_alert_message("Template has been created successfully.")
    template_page.verify_current_page_is_courses_page()

    course_page.add_course_and_verify_that_course_is_opened()
    course_page.select_template_with_rate_type_and_its_validation("Many Students", "template rates", 4)
    course_page.add_many_students_course_data_without_rates(4)
    course_page.validate_alert_message("Course has been created successfully.")
    course_page.verify_current_page_is_courses_page()


@given("the counselor linked upcoming Course record should be present")
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()
    template_page.add_template_info(4)
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()
    template_page.validate_alert_message("Template has been created successfully.")
    template_page.verify_current_page_is_courses_page()

    course_page.add_course_and_verify_that_course_is_opened()
    course_page.select_template_with_rate_type_and_its_validation("Many Students", "template rates", 6)
    course_page.add_many_students_course_data_without_rates(6)
    course_page.validate_alert_message("Course has been created successfully.")
    course_page.verify_current_page_is_courses_page()

@when("the user filter for the counselor and validate the course is in the current course list")
def step_impl(context):
    course_page.add_counselor_filter_and_search_with_validation(5, "current")

@when("the user filter for the counselor and validate the course is in the previous course list")
def step_impl(context):
    course_page.add_counselor_filter_and_search_with_validation(4, "previous")

@when("the user filter for the counselor and validate the course is in the upcoming course list")
def step_impl(context):
    course_page.add_counselor_filter_and_search_with_validation(6, "upcoming")