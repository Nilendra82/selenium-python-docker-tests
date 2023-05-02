import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.logger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.logger.info("********* Test_001_Login *********")
        self.logger.info("********* Verify Home page title *********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title
        if actual_title == "Wave trial":
            assert True
            self.driver.close()
            self.logger.info("Home page title test is passed")
        else:
            self.driver.save_screenshot("./screenshots/" + "test_homepage_title.png")
            self.driver.close()
            self.logger.info("Home page title test is failed")
            assert False

    @pytest.mark.smoke
    def test_login(self, setup):
        self.logger.info("********* Verify login test *********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        get_url = self.driver.current_url
        if "account/dashboard/" in get_url:
            assert True
            self.driver.close()
            self.logger.info("Login test is passed")
        else:
            self.driver.save_screenshot("./screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.info("Login test is failed")
            assert False
