from pages.login_page import LoginPage
from pages.search_page import SearchPage
from utilities.read_properties import ReadConfig
from utilities.logger import LogGen
import pytest


class Test_003_Search:
    baseUrl = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    search_item = ReadConfig.get_search_item()
    match_item = ReadConfig.get_match_item()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_text(self, setup):
        self.logger.info("********* Test_003_Search *********")
        self.logger.info("********* Verify search item page *********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.login_page = LoginPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        flag = self.search_page.is_matched_search_item(self.search_item, self.match_item)
        if flag:
            assert True
            self.driver.close()
            self.logger.info("test_search_text test is passed")
        else:
            self.driver.save_screenshot("./screenshots/" + "test_search_text.png")
            self.driver.close()
            self.logger.info("test_search_text test is failed")
            assert False
