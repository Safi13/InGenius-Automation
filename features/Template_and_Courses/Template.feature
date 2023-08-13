Feature: Templates
    As an admin I want to add/edit/delete templates
    So that I can add new courses using these templates

  @templates   @regression  @smoke
  Scenario: Add a New Template with valid attachment type
    Given the admin user is logged in to InGenius Prep
    And the user is on the Courses tab
    When the user adds a new template
    When the user provides the Template Info and Progress Checklist details
    Then the template should be successfully created
    And the user search the added template and its correctly visible in the template list
#
#  @templates  @regression
#  Scenario: Add a New Template with only mandatory fields
#    Given the admin user is logged in to InGenius Prep
#    And the user is on the Courses tab
#    When the user adds a new template
#    When the user provides the Template Info and Progress Checklist details on their mandatory fields
#    Then the template should be successfully created
#    And the user search the added template and its correctly visible in the template list
#
#  @templates  @regression
#  Scenario: Add a New Template with invalid attachment type
#    Given the admin user is logged in to InGenius Prep
#    And the user is on the Courses tab
#    When the user adds a new template
#    When the user provides the Template Info with invalid course attachment
#    And the user provides Progress Checklist details
#    Then the invalid attachment type message should be thrown
#
#  @templates  @regression
#  Scenario: Verify that Adding/Deleting of Groups and Items are working correctly
#    Given the admin user is logged in to InGenius Prep
#    And the user is on the Courses tab
#    When the user adds a new template
#    When the user provides the Template Info and moves to next step
#    And the user adds groups and items in Progress Checklist tab and then deletes them
#    Then the default Progress checklist form should be visible
#
#  @templates  @regression   @smoke
#  Scenario: Add / Edit or Update a template and verify that the saved Groups and Items data is populating correctly while editing the template
#    Given the admin user is logged in to InGenius Prep
#    And the user is on the Courses tab
#    When the user adds a new template
#    When the user provides the Template Info and moves to next step
#    And the user adds groups and items in Progress Checklist tab and then saves the template
#    Then the template should be successfully created
#    When the user search the saved template and its correctly visible in the template list
#    Then user edits the record and verify that added data is populating correctly on respective tabs
#    And update the template record and verify its correctly visible in the template list
#
#  @templates  @regression
#  Scenario: Verify that all the Groups and Items added in Progress Checklist should be mandatory
#    Given the admin user is logged in to InGenius Prep
#    And the user is on the Courses tab
#    When the user adds a new template
#    When the user provides the Template Info and moves to next step
#    And the user adds groups and items in Progress Checklist tab and saves the template
#    Then the template should be successfully created
#    And the user search the added template and its correctly visible in the template list
#
#  @templates  @regression
#  Scenario: Verify that switching from Template Info and Progress Checklist should not remove the values from the tab fields
#    Given the admin user is logged in to InGenius Prep
#    And the user is on the Courses tab
#    When the user adds a new template
#    When the user provides the Template Info and moves to next step
#    And the user adds the detail in the Progress Checklist tab form and move to the previous step
#    Then the Template Info tab data should be present
#    And on the next step the Progress Checklist data should be present
#
#  @templates  @regression
#  Scenario: Verify the cancel Template and its form, having Template Info and Progress Checklist tabs with Groups and Items
#    Given the admin user is logged in to InGenius Prep
#    When the user adds a new template and adds Template Info
#    And the user moves to next step and adds Progress checklist details
#    When the user cancels the Template form
#    Then the user navigates to template tab in the course page
#
#  @templates  @regression   @smoke
#  Scenario: Search a Template by [Template Name, Course Classification, Items Checklist]
#    Given the admin user is logged in to InGenius Prep
#    Given the Template record should be present
#    When the user searches for the template by template name
#    Then the searched template information should be listed in the template tab
#    When the user searches for the template by course classification
#    Then the searched template information should be listed in the template tab
#    When the user searches for the template by checklist items
#    Then the searched template information should be listed in the template tab
#
#  @templates  @regression   @smoke
#  Scenario: Verify Template List shows [Template Name, Course Classification, Checklist Items, Actions] in the list
#    Given the admin user is logged in to InGenius Prep
#    When the user navigates to the template list
#    Then the user validates Template Name, Course Classification, Checklist Items and Action columns should be present