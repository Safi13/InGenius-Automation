import mysql.connector
import allure
import logging
from utils.Config import Config


class DatabaseConnection:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.connection = None
        self.config = Config()

    def connect_db(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.config.db_host,
                port=self.config.db_port,
                database=self.config.database,
                user=self.config.db_user,
                password=self.config.db_password
            )
            self.logger.info("Connected to the MySQL database!")
        except mysql.connector.Error as e:
            self.logger.error("Error connecting to the MySQL database: " + str(e))

    def disconnect_db(self):
        if self.connection is not None:
            self.connection.close()
            self.logger.info("Disconnected from the MySQL database.")


    def execute_select_query(self, query):
        self.connect_db()
        if self.connection is not None:
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                results = cursor.fetchall()
                cursor.close()
                self.logger.info(query + ": Select query executed successfully.")
                return results
            except mysql.connector.Error as e:
                self.logger.error(query + ": Error executing select query: " + str(e))
        else:
            self.logger.error("Not connected to the MySQL database.")

    def execute_delete_and_update_query(self, query):
        self.connect_db()
        if self.connection is not None:
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
                self.logger.info(query + ": Update or Delete query executed successfully.")
                cursor.close()
            except mysql.connector.Error as e:
                self.logger.error(query + ": Error executing update or delete query: " + str(e))
        else:
            self.logger.error("Not connected to the MySQL database.")

    def execute_insert_query(self, query):
        self.connect_db()
        if self.connection is not None:
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
                self.logger.info(query + ": Insert query executed successfully.")
                cursor.close()
            except mysql.connector.Error as e:
                allure.attach(query + ": Error executing insert query: " + str(e), "Error")
                self.logger.error(query + ": Error executing insert query: %s" % str(e), exc_info=True)
        else:
            self.logger.error("Not connected to the MySQL database.")





