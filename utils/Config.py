import os
from dotenv import load_dotenv
import logging


class Config:
    logger = logging.getLogger(__name__)

    def __init__(self):
        dotenv_path = './environment.env'
        load_dotenv(dotenv_path)
        self.web_url = os.getenv('WEB_URL')
        self.browser = os.getenv('BROWSER')
        self.exp_wait = int(os.getenv('EXP_WAIT'))
        self.imp_wait = int(os.getenv('IMP_WAIT'))
        self.is_headless = os.getenv('IS_HEADLESS')
        self.is_detachable = os.getenv('IS_DETACHABLE')
        self.db_host = os.getenv('DB_HOST')
        self.db_port = os.getenv('DB_PORT')
        self.database = os.getenv('DATABASE')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.api_base_url = os.getenv('API_BASE_URL')
        self.admin_email = os.getenv('ADMIN_EMAIL')
        self.admin_password = os.getenv('ADMIN_PASSWORD')