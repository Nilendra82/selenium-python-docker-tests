from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.logger import LogGen
from pages.logout_page import LogoutPage
import pytest


class Test_002_Logout:
    baseUrl = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    @pytest.mark.smoke
    def test_logout(self, setup):
        self.logger.info("********* Test_002_Logout *********")
        self.logger.info("********* Verify logout test *********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.login_page = LoginPage(self.driver)
        self.logout_page = LogoutPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        self.logout_page.click_logout()

        get_url = self.driver.current_url
        if "/login" in get_url:
            assert True
            self.driver.close()
            self.logger.info("Logout test is passed")
        else:
            self.driver.save_screenshot("./screenshots/" + "test_logout.png")
            self.driver.close()
            self.logger.info("Logout test is failed")
            assert False
