import random

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinkPage, \
    UploadDownloadPage
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

        def test_web_table_update_person_info(self,driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "Person card has not been changed"

        def test_web_table_delete_person(self,driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted_person()
            assert text == 'No rows found'

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5,10,20,25,50,100], ("The number of rows in the table has not "
                                                  "been changed or has changed incorrectly")

    class TestButtonsPage:
        def test_different_click_on_the_buttons(self,driver):
            button_page = ButtonsPage(driver,"https://demoqa.com/buttons")
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == "You have done a double click", "The double click was not clicked"
            assert right == "You have done a right click", "The right click was not clicked"
            assert click == "You have done a dynamic click" ,"The click me was not clicked"

    class TestLinksPage:
       def test_check_link(self, driver):
           link_page = LinkPage(driver,"https://demoqa.com/links")
           link_page.open()
           href_link, current_url = link_page.check_new_tab_simple_link()
           assert href_link == current_url , 'Opened incorrect link'
       def test_broken_link(self,driver):
           link_page = LinkPage(driver, "https://demoqa.com/links")
           link_page.open()
           response_code = link_page.check_broken_link('https://demoqa.com/bad-request')
           assert response_code == 400, 'Bad request is not worked'

    class TestUploadDownloadPage:
        def test_upload_file(self,driver):
            upload_download_page = UploadDownloadPage(driver,'https://demoqa.com/upload-download')
            upload_download_page.open()
            uploaded_name, file_name = upload_download_page.upload_file()
            assert uploaded_name == file_name, f"The {uploaded_name} file was not uploaded"
        def test_download_file(self,driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.upload_file()
            assert check is True, "The file has not been downloaded"