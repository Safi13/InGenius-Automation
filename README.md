# InGenius Prep Automation - Students High School Entrance Test Preparation

## Description

InGenius Prep Automation is a project focused on automating the High School Entrance Test Preparation Portal. 
## Prerequisites

Before getting started, please ensure the following prerequisites are met:

1. Install Python 3.11.3 (Recommended) [Latest / 3.0 or above]
2. Install Git  

## Recommended IDE's
You can use either of the following IDEs:
1. PyCharm (Ultimate - Recommended, or Community).

## Project Setup Guide

After completing the prerequisites, please follow these steps sequentially:
1. Clone the project to your desired location using Git Bash:
```bash
git clone https://[your-username]@bitbucket.org/folio3/ingenius-prep-automation.git
```
2. Install the project dependencies using `pip`:
```bash
pip install -r requirements.txt
```
3. Run the test scenarios using the following command in the project root folder:
```cmd
behave --format allure_behave.formatter:AllureFormatter -o allure-results
```
4. View Allure report using one of the following commands:
```cmd
allure serve
```
## Project Maintenance Guide

If you want to work on this project, please follow the instructions below to set up your environment.

1. Create a new Behave configuration for different environments in your IDE.
2. Copy the following environment variables and paste them in the Environment Variable section. Set the values based on the environment you are working on.:
`WEB_URL=https://qa-ingenious.folio3.com:5053/login;BROWSER=chrome;EXP_WAIT=10;IMP_WAIT=20;IS_HEADLESS=True;IS_DETACHABLE=True;DB_HOST=10.164.2.112;DB_PORT=3306;DATABASE=ingenius;DB_USER=muhammadhasham;DB_PASSWORD=AADp4H1fQZ51XhM;API_BASE_URL=https://qa-ingenious.folio3.com:5053;ADMIN_EMAIL=admin@test.com;ADMIN_PASSWORD=demouserfolio3@!;
`



