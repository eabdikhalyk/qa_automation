import time
from conftest import driver
from pages.form_page import FormsPage


class TestForms:
    class TestFormPage:

        def test_forms_page(self, driver):
            forms_page = FormsPage(driver,'https://demoqa.com/automation-practice-form')
            forms_page.open()
            person = forms_page.fill_form_fields()
            result = forms_page.form_result()
            print(person.firstname, person.lastname, person.email)
            print(result[0], result[1])
            assert [person.firstname + " " + person.lastname, person.email] == [result[0], result[1]] , ("The form"
                                                                                                         "has not been fiiled")