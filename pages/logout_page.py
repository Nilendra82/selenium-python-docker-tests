from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class LogoutPage:
    link_avatar_xpath = "//a[@title='QA role Assignment Efrain DLS']"
    button_logout_xpath = "//li[@class='logout']//button"

    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        action_chains = ActionChains(self.driver)
        avatar_hover = self.driver.find_element(By.XPATH, self.link_avatar_xpath)
        action_chains.move_to_element(avatar_hover).perform()
        logout_element = self.driver.find_element(By.XPATH, self.button_logout_xpath)
        action_chains.move_to_element(logout_element).click().perform()
