import logging
from configparser import ConfigParser


class ApiRouteReader:
    logger = logging.getLogger(__name__)
    filename = "./api/resources/routes.ini"

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(ApiRouteReader.filename)

    def get_route(self, route_name):
        return self.config.get('routes', route_name, fallback='/login')


