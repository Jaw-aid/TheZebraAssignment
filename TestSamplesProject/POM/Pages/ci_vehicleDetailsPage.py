# this page script is not completed... still work in progress

import random
from time import sleep
class ci_vehicleDetailsPage():

    def __init__(self, browser):
        self.browser = browser

        #list of elements to move to locators

    #selects random radio button when we provide the xpath
    def select_RANDOMRadioBtn(self, xpathLocation):
        radiobtn_options = self.browser.find_elements_by_xpath(xpathLocation)
        clickOne_option = random.choice(radiobtn_options)
        clickOne_option.click()

    def enter_randomMileage(self):
        #generate random 5 digit number
        number = random.randint(10000, 11000)
        address_textbox = self.browser.find_element_by_xpath(self.txtbox_address)
        address_textbox.clear()
        address_textbox.send_keys(number)
