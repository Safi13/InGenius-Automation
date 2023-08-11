import logging
import requests
from api.config.ApiRouteReader import ApiRouteReader
from utils.Config import Config


class InGeniusApi:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.config = Config()
        self.apiRouteReader = ApiRouteReader()


    def delete_template(self, template_id, token, cookies):
        route = self.apiRouteReader.get_route("delete_template")
        route = route.replace("{id}", template_id)
        url = self.config.api_base_url + route
        data = {
            "_token": token
        }
        response = requests.get(url, json=data, cookies=cookies)
        return response.json()


    def delete_course(self, course_id, token, cookies):
        route = self.apiRouteReader.get_route("delete_course")
        route = route.replace("{id}", course_id)
        url = self.config.api_base_url + route
        data = {
            "_token": token
        }
        response = requests.get(url, json=data, cookies=cookies)
        return response.json()

    def generate_login_token(self):
        route = self.apiRouteReader.get_route("generate_login_token")
        response = requests.get(self.config.api_base_url + route)
        return response.text, response.cookies

    def login_with_admin(self, token, cookies):
        route = self.apiRouteReader.get_route("login")
        url = self.config.api_base_url + route
        data = {
            "email": "admin@test.com",
            "password": "demouserfolio3@!",
            "_token": token
        }
        response = requests.post(url, json=data, cookies=cookies)
        return response.text, response.cookies
