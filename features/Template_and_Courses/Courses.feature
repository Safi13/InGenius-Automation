Feature: Courses
    As an admin I want to add/edit/delete courses
    So that students can enroll in respective courses

  @courses  @regression  @smoke
  Scenario: Add a New Course with single student template and template rates
    Given the admin user is logged in to InGenius Prep
    Given that a single record of a single student template should be present
    When the user adds a new course
    And the user select a single student template with template rates
    And the user provides data for template with template rates in Course Details, Counselors and sets the rate for single student
    Then the course should be successfully created
    And the user search for the single student course and its correctly visible in the current course list

  @courses  @regression
  Scenario: Add a New Course with single student template and course rates
    Given the admin user is logged in to InGenius Prep
    Given that a single record of a single student template should be present
    When the user adds a new course
    And the user select a single student template with course rates
    And the user provides data for template with course rates in Course Details, Counselors and sets the rate for single student
    Then the course should be successfully created
    And the user search for the single student course and its correctly visible in the current course list


  @courses  @regression  @smoke
  Scenario: Add a New Course with many students template and template rates
    Given the admin user is logged in to InGenius Prep
    Given that a single record of many students template should be present
    When the user adds a new course
    And the user select a many students template with template rates
    And the user provides data for template with template rates in Course Details, Counselors and sets the rate for many students
    Then the course should be successfully created
    And the user search for many students course and its correctly visible in the current course list


  @courses  @regression
  Scenario: Add a New Course with many students template and course rates
    Given the admin user is logged in to InGenius Prep
    Given that a single record of many students template should be present
    When the user adds a new course
    And the user select a many students template with course rates
    And the user provides data for template with course rates in Course Details, Counselors and sets the rate for many students
    Then the course should be successfully created
    And the user search for many students course and its correctly visible in the current course list


  @courses  @regression
  Scenario: Verify that on a template reselection the updated template rates should populate over the previous course rates on respective fields
    Given the admin user is logged in to InGenius Prep
    Given that the single student template record should be present
    When the user adds a new course
    And the user select a single student template with course rates
    Then the user reselect a single student template with template rates and updated template rates should populate on respective fields


  @courses  @regression
  Scenario: Verify that on a template reselection the updated template rates should populate over the previous template rates on respective fields
    Given the admin user is logged in to InGenius Prep
    Given that the single student template record should be present
    When the user adds a new course
    And the user select a single student template with template rates
    Then the user reselect a single student template with template rates and updated template rates should populate on respective fields

  @courses  @regression
  Scenario: Verify that on a template reselection the updated course rates should populate over the previous template rates on respective fields
    Given the admin user is logged in to InGenius Prep
    Given that the single student template record should be present
    When the user adds a new course
    And the user select a single student template with template rates
    Then the user reselect a single student template with course rates and the rates should be empty

  @courses  @regression
  Scenario: Verify that on a template reselection the updated course rates should populate over the previous course rates on respective fields
    Given the admin user is logged in to InGenius Prep
    Given that the single student template record should be present
    When the user adds a new course
    And the user select a single student template with course rates
    Then the user reselect a single student template with course rates and the rates should be empty


  @courses  @regression
  Scenario: Add a New Course with a template and close the template popup
    Given the admin user is logged in to InGenius Prep
    Given that a single record of a single student template should be present
    When the user adds a new course
    And the user select a template with course and close the template popup
    Then the template should not be selected in the create course form

  @courses  @regression
  Scenario: Verify the cancelling the course form lands you on the courses page
    Given the admin user is logged in to InGenius Prep
    Given that a single record of a single student template should be present
    When the user adds a new course
    And the user cancels the Courses form
    Then the user lands on current courses tab

  @courses  @regression
  Scenario: Add a New Course by validating mandatory fields
    Given the admin user is logged in to InGenius Prep
    Given that a single record of many students template should be present
    When the user adds a new course
    And the provides the Course Details, Counselors and sets the rate while validating the mandatory fields
    Then the course should be successfully created
    And the user search for many students course and its correctly visible in the current course list

  @courses  @regression   @smoke
  Scenario: Edit a Course of a single student template
    Given the admin user is logged in to InGenius Prep
    Given that the single student Course record should be present
    When the user search for the single student template course and edits the course record
    And the user validates that only single student templates are populating in the templates
    And the user provides the updated Course Information for single student course
    Then the Course should be updated successfully
    And the user search for the single student course and its correctly visible in the current course list


  @courses  @regression   @smoke
  Scenario: Edit a Course of a many students template
    Given the admin user is logged in to InGenius Prep
    Given that the many students Course record should be present
    When the user search for the many students template course and edits the course record
    And the user validates that only many students templates are populating in the templates
    And provides the updated Course Information for many students course
    Then the Course should be updated successfully
    And the user search for many students course and its correctly visible in the current course list


  @courses  @regression
  Scenario: Search a Course (Current)
    Given the admin user is logged in to InGenius Prep
    Given the current Course record should be present
    Then the user search for many students course and its correctly visible in the current course list

  @courses  @regression
  Scenario: Search a Course (Upcoming)
    Given the admin user is logged in to InGenius Prep
    Given the upcoming Course record should be present
    Then the user search for many students course and its correctly visible in the upcoming course list

  @courses  @regression
  Scenario: Search a Course (Previous)
    Given the admin user is logged in to InGenius Prep
    Given the previous Course record should be present
    Then the user search for many students course and its correctly visible in the previous course list

  @courses  @regression  @smoke
  Scenario: Verify that counselor filter is showing the record of the linked course of current tenure in the list
    Given the admin user is logged in to InGenius Prep
    Given the counselor linked current Course record should be present
    When the user filter for the counselor and validate the course is in the current course list

  @courses  @regression
  Scenario: Verify that counselor filter is showing the record of the linked course of previous tenure in the list
    Given the admin user is logged in to InGenius Prep
    Given the counselor linked previous Course record should be present
    When the user filter for the counselor and validate the course is in the previous course list

  @courses  @regression
  Scenario: Verify that counselor filter is showing the record of the linked course of upcoming tenure in the list
    Given the admin user is logged in to InGenius Prep
    Given the counselor linked upcoming Course record should be present
    When the user filter for the counselor and validate the course is in the upcoming course list