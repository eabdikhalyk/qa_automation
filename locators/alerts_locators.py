from selenium.webdriver.common.by import By


class BrowserWindowPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR,"button[id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR,"button[id='windowButton']")

    TITLE_NEW = (By.CSS_SELECTOR,"h1[id='sampleHeading']")

class AlertPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR,"button[id='alertButton']")
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR,"button[id='timerAlertButton']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR,"button[id='confirmButton']")
    PROMT_BUTTON = (By.CSS_SELECTOR,"button[id='promtButton']")

    ALERT_CONFIRMATION_RESULT = (By.CSS_SELECTOR,"span[id='confirmResult']")
    ALERT_PROMPT = (By.CSS_SELECTOR,"span[id='promptResult']")