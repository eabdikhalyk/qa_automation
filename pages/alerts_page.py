import random
import time

from selenium.webdriver.common.alert import Alert
from locators.alerts_locators import BrowserWindowPageLocators, AlertPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC



class BrowserWindowPage(BasePage):
    locators = BrowserWindowPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title
class AlertPage(BasePage):
    locators = AlertPageLocators()

    def check_alert_button(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert = self.alert_is_present()
        return alert.text
    def check_timer_alert_button(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        alert = self.alert_is_present()
        return alert.text
    def check_alert_with_confirmation(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        choice = random.randint(1,2)
        alert = self.alert_is_present()
        if choice == 1:
            alert.accept()
            return "You selected Ok"
        elif choice == 2:
            alert.dismiss()
            return "You selected Cancel"

    def get_alert_confirmation(self):
        result = self.element_is_visible(self.locators.ALERT_CONFIRMATION_RESULT).text
        return result

    def check_alert_with_prompt(self):
        text_to_send = f"text_{random.randint(1,999)}"
        self.element_is_visible(self.locators.PROMT_BUTTON).click()
        time.sleep(5)
        alert = self.alert_is_present()
        alert.send_keys(text_to_send)
        alert.accept()
        return text_to_send
    def get_sent_prompt(self):
        text = self.element_is_visible(self.locators.ALERT_PROMPT).text
        return text.split(" ")[2]