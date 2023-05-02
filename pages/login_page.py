from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class LoginPage:
    textbox_username_id = "inputEmail"
    textbox_password_id = "inputPassword"
    button_login_xpath = "//form[@id='regular-login']//button"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
