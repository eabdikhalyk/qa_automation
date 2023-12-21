import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage
from pages.elements_page import TextBoxPage, CheckBoxPage
from conftest import driver

class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver,'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, 'the full name does not match'
            assert email == output_email, 'the email does not match'
            assert current_address == output_cur_addr, 'the current address does not match'
            assert permanent_address == output_per_addr, 'the permanent address does not match'

    class TestCheckBox:
        def test_check_box(self,driver):
            check_box_page = CheckBoxPage(driver,'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert  input_checkbox == output_result, 'Checkboxes have not been selected'

    class TestRadioButton:
        def test_radio_button(self,driver):
            radio_button_page = RadioButtonPage(driver,'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' has not been selected"
            assert output_impressive == 'Impressive', "Impressive' has not been selected"
            assert output_no == 'No', "'No' has not been selected"
    class TestWebTable:
        def test_web_table_add_person(self,driver):
            web_table_page = WebTablePage(driver,'https://demoqa.com/webtables')
            web_table_page.open()
            input_person = web_table_page.add_new_person()
            output_people = web_table_page.check_new_added_person()
            assert input_person in output_people

        def test_web_table_search_person(self,driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0,5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert  key_word in table_result , "The person was not found in the table"

