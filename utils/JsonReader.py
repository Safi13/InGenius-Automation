import json
import logging


class JsonReader:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.file_path = "./resources/test-data.json"
        self.data = self._load_json_data()

    def _load_json_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError as e:
            self.logger.error(f"File '{self.file_path}' not found: {e}")
            raise
        except json.JSONDecodeError as e:
            self.logger.error("Invalid JSON data: {e}")
            raise ValueError("Invalid JSON data.")

    def get_template_info_tab_data(self, section_name, field_name, screen_record_index = 0):
        try:
            module_data = self.data.get("Templates and Progress Checklist")
            if module_data:
                screen_data = module_data["Template Info"][screen_record_index]
                section_data = screen_data.get(section_name)
                field_data = section_data.get(field_name)
                return field_data
        except Exception as e:
            self.logger.error("An error occurred while processing JSON data: %s" % str(e), exc_info=True)
            raise

    def get_single_student_data(self, section_name, field_name, screen_record_index = 0):
        try:
            module_data = self.data.get("Courses")
            if module_data:
                screen_data = module_data["Single Student"][screen_record_index]
                section_data = screen_data.get(section_name)
                field_data = section_data.get(field_name)
                return field_data
        except Exception as e:
            self.logger.error("An error occurred while processing JSON data: %s" % str(e), exc_info=True)
            raise

    def get_many_students_data(self, section_name, field_name, screen_record_index = 0):
        try:
            module_data = self.data.get("Courses")
            if module_data:
                screen_data = module_data["Many Students"][screen_record_index]
                section_data = screen_data.get(section_name)
                field_data = section_data.get(field_name)
                return field_data
        except Exception as e:
            self.logger.error("An error occurred while processing JSON data: %s" % str(e), exc_info=True)
            raise


    def get_progress_checklist_tab_data(self, section_name, field_name, screen_record_index = 0, section_record_index = 0):
        try:
            module_data = self.data.get("Templates and Progress Checklist")
            if module_data:
                screen_data = module_data["Progress Checklist"][screen_record_index]
                section_data = screen_data[section_name][section_record_index]
                field_data = section_data.get(field_name)
                return field_data
        except Exception as e:
            self.logger.error("An error occurred while processing JSON data: %s" % str(e), exc_info=True)
            raise

    def get_progress_checklist_verification_data(self, field_name, screen_record_index = 0):
        try:
            module_data = self.data.get("Templates and Progress Checklist")
            if module_data:
                screen_data = module_data["Progress Checklist Verification"][screen_record_index]
                field_data = screen_data.get(field_name)
                return field_data
        except Exception as e:
            self.logger.error("An error occurred while processing JSON data: %s" % str(e), exc_info=True)
            raise

    def get_progress_checklist_tab_data_group_count(self, screen_record_index = 0):
        try:
            module_data = self.data.get("Templates and Progress Checklist")
            if module_data:
                screen_data = module_data["Progress Checklist"][screen_record_index]
                section_data = screen_data["Group"]
                return len(section_data)
        except Exception as e:
            self.logger.error("An error occurred while processing JSON data: %s" % str(e), exc_info=True)
            raise


    def get_progress_checklist_tab_data_group_item_count(self, screen_record_index = 0, section_record_index = 0):
        try:
            module_data = self.data.get("Templates and Progress Checklist")
            if module_data:
                screen_data = module_data["Progress Checklist"][screen_record_index]
                section_data = screen_data["Group"][section_record_index]
                field_data = section_data.get("Item")
                return len(field_data)
        except Exception as e:
            self.logger.error("An error occurred while processing JSON data: %s" % str(e), exc_info=True)
            raise





