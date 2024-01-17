from pages.alerts_page import BrowserWindowPage, AlertPage
from conftest import driver

class TestAlertsFrameWindow:
    class TestBrowserWindow:
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowPage(driver,"https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "New tab has not been opened"
        def test_new_window(self,driver):
            new_window_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
            new_window_page.open()
            text_result = new_window_page.check_opened_new_window()
            assert text_result == 'This is a sample page', "New window has not been opened"

    class TestAlert:

        def test_alert_button(self,driver):
            alert_page = AlertPage(driver,"https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_button()
            assert alert_text == "You clicked a button" , "The alert has not been clicked"
        def test_timer_alert_button(self,driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            timer_alert_text = alert_page.check_timer_alert_button()
            assert timer_alert_text == "This alert appeared after 5 seconds", "The timer alert has not been worked"
        def test_alert_with_confirmation(self,driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            choice = alert_page.check_alert_with_confirmation()
            expected_result=alert_page.get_alert_confirmation()
            assert choice == expected_result, "Alert confirmation has not been worked"
        def test_alert_with_prompt(self,driver):
            alert_page = AlertPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            prompt_text = alert_page.check_alert_with_prompt()
            expected_text = alert_page.get_sent_prompt()
            assert prompt_text == expected_text, "Prompt to alert has not been sent"

