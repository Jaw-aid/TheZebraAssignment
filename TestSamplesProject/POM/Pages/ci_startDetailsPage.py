import random
class ci_startDetailsPage():

    def __init__(self, browser):
        self.browser = browser

        #list of elements to move to locators
        self.txtbox_address = '//input[@id="garaging_addressInput"]'
        self.dropdown_firstRandomAddress = '//div[@data-cy="pac_item"][1]'
        self.txtbox_firstname = '//input[@id="first_namestart"]'
        self.txtbox_lastname = '//input[@id="last_namestart"]'
        self.txtbox_birthday = '//input[@id="date_of_birthstart"]'
        self.btn_saveAndCont = '//button[@id="startDetailsSaveBtn"]'

    #enter random address
    def enter_randomAddress(self):
        #generate random 4 digit number
        number = random.randint(1111, 9999)
        address_textbox = self.browser.find_element_by_xpath(self.txtbox_address)
        address_textbox.clear()
        address_textbox.send_keys(number)

        #select first address option
        firstAddressOption = self.browser.find_element_by_xpath(self.dropdown_firstRandomAddress)
        firstAddressOption.click()

    #enter first name
    def enter_FirstName(self, firstname):
        firstName_Textbox = self.browser.find_element_by_xpath(self.txtbox_firstname)
        firstName_Textbox.clear()
        firstName_Textbox.send_keys(firstname)

    #enter last name
    def enter_LastName(self, lastname):
        lastName_Textbox = self.browser.find_element_by_xpath(self.txtbox_lastname)
        lastName_Textbox.clear()
        lastName_Textbox.send_keys(lastname)

    #enter birthday
    def enter_Birthday(self, date):
        birthday_Textbox = self.browser.find_element_by_xpath(self.txtbox_birthday)
        birthday_Textbox.clear()
        birthday_Textbox.send_keys(date)

    #click on the save & con't button
    def clickSaveCont(self):
        self.browser.find_element_by_xpath(self.btn_saveAndCont).click()
