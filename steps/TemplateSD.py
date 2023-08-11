import time

from behave import given, when, then
import logging

from pages.LoginPage import LoginPage
from pages.TemplatePage import TemplatePage
from utils.JsonReader import JsonReader

logger = logging.getLogger(__name__)

template_page = TemplatePage()
login_page = LoginPage()
json_reader = JsonReader()

@given("the admin user is logged in to InGenius Prep")
def step_impl(context):
    login_page.admin_login_with_valid_credentials()

@given('the user is on the Courses tab')
def step_impl(context):
    template_page.verify_current_page_is_courses_page()

@when('the user adds a new template')
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()

@when('the user provides the Template Info and Progress Checklist details')
def step_impl(context):
    template_page.add_template_info()
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()

@then('the template should be successfully created')
def step_impl(context):
    template_page.validate_alert_message("Template has been created successfully.")
    template_page.verify_current_page_is_courses_page()

@given('the Template record should be present')
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()
    template_page.verify_current_page_is_courses_page()
    template_page.add_template_info()
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()
    template_page.verify_current_page_is_courses_page()

@when('the user search for the template and edits the template record')
def step_impl(context):
    template_page.search_for_template_and_edits_top_record()

@when('provides the updated Template Info and Progress Checklist details')
def step_impl(context):
    template_page.add_template_info(1)
    template_page.next_step_after_template_info()
    template_page.save_template()

@then('the template should be updated successfully')
def step_impl(context):
    template_page.validate_alert_message("Template has been updated successfully.")


@when('the user adds a new template and adds Template Info')
def step_impl(context):
    template_page.add_template_and_verify_that_template_page_is_opened()
    template_page.add_template_info()

@when('the user moves to next step and adds Progress checklist details')
def step_impl(context):
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist(1)

@when('the user cancels the Template form')
def step_impl(context):
    template_page.cancel_template_form()

@when('the user searches for the template by template name')
def step_impl(context):
    template_page.open_search_option_in_template()
    template_page.search_for_template("name")

@when('the user searches for the template by course classification')
def step_impl(context):
    template_page.search_for_template("course_classification")

@when('the user searches for the template by checklist items')
def step_impl(context):
    template_page.search_for_template("checklist_items")

@then('the searched template information should be listed in the template tab')
def step_impl(context):
    template_page.verify_searched_template()

@then('the searched course classification should be listed in the template tab')
def step_impl(context):
    template_page.verify_searched_template()

@then('the searched course template items should be listed in the template tab')
def step_impl(context):
    template_page.verify_searched_template()

@when("the user goes back to previous step on Template Info Page the Template Info should not be cleared")
def step_impl(context):
    template_page.previous_step_after_progress_checklist()
    template_page.verify_template_info_fields_not_empty()


@when("the user again moves to next step and validate Progress Checklist Add, Delete Groups and Items are working correctly")
def step_impl(context):
    template_page.next_step_after_template_info()
    template_page.verify_progress_checklist_fields_not_empty()


@then("the user navigates to template tab in the course page")
def step_impl(context):
    template_page.verify_current_page_is_courses_page()

@when("the user provides the Template Info and Progress Checklist details on their mandatory fields")
def step_impl(context):
    template_page.add_mandatory_fields_in_template_info()
    template_page.next_step_after_template_info()
    template_page.add_progress_checklist()
    template_page.save_template()


@when("the user provides the Template Info with invalid course attachment")
def step_impl(context):
    template_page.add_mandatory_fields_in_template_info()
    template_page.upload_invalid_course_image_in_template_info()
    template_page.next_step_after_template_info()

@when("the user provides Progress Checklist details")
def step_impl(context):
    template_page.add_progress_checklist()
    template_page.save_template()

@when("the user provides the Template Info details and moves to next step after inputting mandatory fields")
def step_impl(context):
    template_page.add_mandatory_fields_in_template_info()
    template_page.next_step_after_template_info()

@when("the user provides the Template Info and moves to next step")
def step_impl(context):
    template_page.add_template_info()
    template_page.next_step_after_template_info()

@when("the user adds groups and items in Progress Checklist tab and then deletes them")
def step_impl(context):
    no_of_items = json_reader.get_progress_checklist_verification_data("Number of Items")
    no_of_groups = json_reader.get_progress_checklist_verification_data("Number of Groups")
    template_page.add_groups_with_items(no_of_groups,no_of_items)
    template_page.delete_group_with_its_items_and_verify_its_deletion(no_of_groups,no_of_items)

@when("the user adds groups and items in Progress Checklist tab and then saves the template")
def step_impl(context):
    no_of_items = json_reader.get_progress_checklist_verification_data("Number of Items")
    no_of_groups = json_reader.get_progress_checklist_verification_data("Number of Groups")
    template_page.add_groups_with_items(no_of_groups,no_of_items)
    template_page.verify_added_groups_and_items_with_their_values(no_of_groups,no_of_items)
    template_page.save_template()

@then("the default Progress checklist form should be visible")
def step_impl(context):
    template_page.validate_default_progress_checklist_open_only()

@when("the user adds groups and items in Progress Checklist tab and saves the template")
def step_impl(context):
    template_page.validate_progress_checklist_fields_are_mandatory()

@when("the user adds the detail in the Progress Checklist tab form and move to the previous step")
def step_impl(context):
    template_page.add_progress_checklist(2)
    template_page.previous_step_after_progress_checklist()

@then("the Template Info tab data should be present")
def step_impl(context):
    template_page.verify_template_info_fields_not_empty()

@then("on the next step the Progress Checklist data should be present")
def step_impl(context):
    template_page.next_step_after_template_info()
    template_page.verify_progress_checklist_fields_not_empty(2)


@then("the invalid attachment type message should be thrown")
def step_impl(context):
    template_page.validate_invalid_file_message("The file url id must be a file of type: application/pdf, application/msword, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-powerpoint, image/png, image/jpeg, text/plain, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/vnd.openxmlformats-officedocument.presentationml.presentation.")


@then("the user search the added template and its correctly visible in the template list")
def step_impl(context):
    template_page.search_for_template()
    template_page.verify_searched_template()

@then("user edits the record and verify that added data is populating correctly on respective tabs")
def step_impl(context):
    template_page.edit_top_record()
    template_page.verify_template_info_data_populating()
    template_page.click_next_step()
    no_of_items = json_reader.get_progress_checklist_verification_data("Number of Items")
    no_of_groups = json_reader.get_progress_checklist_verification_data("Number of Groups")
    template_page.verify_added_groups_and_items_with_their_values(no_of_groups,no_of_items)

@when("the user search the saved template and its correctly visible in the template list")
def step_impl(context):
    template_page.search_and_verify_template_with_dynamic_groups_and_items()


@then("update the template record and verify its correctly visible in the template list")
def step_impl(context):
    template_page.save_template()
    template_page.validate_alert_message("Template has been updated successfully.")
    template_page.verify_current_page_is_courses_page()


@when("the user navigates to the template list")
def step_impl(context):
    template_page.verify_current_page_is_courses_page()
    template_page.navigate_to_template_list()

@then("the user validates Template Name, Course Classification, Checklist Items and Action columns should be present")
def step_impl(context):
    template_page.validate_template_list_columns()