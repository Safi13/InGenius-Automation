import time

from behave import fixture, use_fixture
import logging
import logging.config

from pages.CoursePage import CoursePage
from pages.TemplatePage import TemplatePage
from utils.Config import Config
from utils.Utilities import BrowserDriver

config = Config()


@fixture
def hooks(context):
    pass


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    BrowserDriver.initialize_driver()
    pass


def before_step(context, step):
    pass


def before_tag(context, tag):
    pass


def before_all(context):
    logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
    context.logger = logging.getLogger(__name__)


def after_feature(context, feature):
    pass


def after_scenario(context, scenario):
    BrowserDriver.quit_driver()
    pass


def after_step(context, step):
    pass


def after_tag(context, tag):
    if tag == 'templates':
        template_page = TemplatePage()
        template_page.execute_deletion_of_templates()
    if tag == 'courses':
        course_page = CoursePage()
        course_page.execute_deletion_of_courses()


def after_all(context):
    pass
