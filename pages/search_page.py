from selenium.webdriver.common.by import By
from utilities.logger import LogGen
import time


class SearchPage:
    text_search_id = "focus-new"
    li_list_xpath = "//div[@class='spotlight-results']/ul/li//p[@class='searchbox-title']"

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def is_matched_search_item(self, search_item, match_item):
        self.driver.find_element(By.ID, self.text_search_id).clear()
        self.driver.find_element(By.ID, self.text_search_id).send_keys(search_item)
        lists = self.driver.find_elements(By.XPATH, self.li_list_xpath)
        for item in lists:
            if item.text == match_item:
                return True

