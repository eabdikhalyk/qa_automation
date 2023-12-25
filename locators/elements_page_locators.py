from selenium.webdriver.common.by import By

class TextBoxPageLocators:
    # Form fields
    FULL_NAME = (By.CSS_SELECTOR,"input[id='userName']")
    EMAIL = (By.CSS_SELECTOR,"input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR,"textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR,"textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR,"button[id='submit']")
    # Created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR,"p[id='name']")
    CREATED_EMAIL = (By.CSS_SELECTOR,"p[id='email']")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR,"p[id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR,"p[id='permanentAddress']")

class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR,"button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR,"span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR,"svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")

    OUTPUT_RESULT = (By.CSS_SELECTOR,"span[class='text-success']")

class RadioButtonLocators:
    YES_RADIO = (By.CSS_SELECTOR,"label[for='yesRadio']")
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR,"label[for='impressiveRadio']")
    NO_RADIO = (By.CSS_SELECTOR,"label[for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR,"p span[class='text-success']")

class WebTablePageLocators:
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    FIRSTNAME_INPUT = (By.ID,"firstName")
    LASTNAME_INPUT = (By.ID,"lastName")
    EMAIL_INPUT = (By.ID,"userEmail")
    AGE_INPUT = (By.ID,"age")
    SALARY_INPUT = (By.ID,"salary")
    DEPARTMENT_INPUT = (By.ID,"department")
    SUBMIT = (By.ID,"submit")

    FULL_PEOPLE_LIST = (By.CSS_SELECTOR,"div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR,"input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR,"span[title='Delete']")
    ROW_PARENT = (".//ancestor::div[@class='rt-tr-group']")
    NO_ROWS = (By.CSS_SELECTOR,"div[class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR,'select[aria-label="rows per page"]')

    UPDATE_BUTTON = (By.CSS_SELECTOR,'span[title="Edit"]')

class ButtonsPageLocators:

    DOUBLE_BUTTON = (By.ID,"doubleClickBtn")
    RIGHT_CLICK = (By.CSS_SELECTOR,"div[class='mt-4']:nth-child(2n) button")
    CLICK_ME_BUTTON = (By.CSS_SELECTOR,"div[class='mt-4']:nth-child(3n) button")

    OUTPUT_DOUBLE = (By.ID,"doubleClickMessage")
    OUTPUT_RIGHT = (By.ID,"rightClickMessage")
<<<<<<<<< Temporary merge branch 1
    OUTPUT_CLICK_ME = (By.ID,"dynamicClickMessage")
=========
    OUTPUT_CLICK_ME = (By.ID,"dynamicClickMessage")

class LinkPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR,"a[id='simpleLink']")
    BAD_REQUEST = (By.CSS_SELECTOR,"a[id='bad-request']")
>>>>>>>>> Temporary merge branch 2
