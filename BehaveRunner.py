import subprocess


class BehaveRunner:
    def __init__(self, tags=None):
        self.tags = tags

    def run_tests(self):
        command = "behave --format allure_behave.formatter:AllureFormatter -o allure-results"
        if self.tags:
            command += f" --tags={self.tags}"

        subprocess.call(command, shell=True)

        # Generate Allure report
        subprocess.call("allure serve allure-results", shell=True)


if __name__ == "__main__":
    runner = BehaveRunner()  # Can Include Tags BehaveRunner(tags="@xyz")
    runner.run_tests()
