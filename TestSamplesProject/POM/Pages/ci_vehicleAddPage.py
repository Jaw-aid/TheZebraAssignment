import random
from time import sleep
class ci_addVehiclePage():

    def __init__(self, browser):
        self.browser = browser

        #list of elements to move to locators
        self.dropdown_car1_year = '//input[@id="yearYear-0Input-0"]'
        self.dropdown_car1_selectRANDOMyear = '//div[starts-with(@id, "year-0-")]'
        self.dropdown_car1_make = '//input[@id="makeMake-0Input-0"]'
        self.dropdown_car1_selectRANDOMmake = '//div[starts-with(@id, "make-0-")]'
        self.dropdown_car1_model = '//input[@id="modelModel-0Input-0"]'
        self.dropdown_car1_selectRANDOMmodel = '//div[starts-with(@id, "model-0-")]'
        self.dropdown_car1_trim = '//input[@id="submodelSubmodel-0Input-0"]'
        self.dropdown_car1_selectRANDOMtrim = '//div[starts-with(@id, "submodel-0-")]'
        self.btn_saveAndCont = '//button[@id="vehiclesSelectSaveBtn"]'

    def select_RANDOMCarYearDropdown(self):
        Car1_Year_Dropdown = self.browser.find_element_by_xpath(self.dropdown_car1_year)
        Car1_Year_Dropdown.clear()
        Car1_Year_Dropdown.click()
        sleep(1)
        Car1_YearOptions = self.browser.find_elements_by_xpath(self.dropdown_car1_selectRANDOMyear)
        Car1_YearOption = random.choice(Car1_YearOptions)
        Car1_YearOption.click()
        sleep(2)

    def select_RANDOMDropdowns(self, dropdown_xpath, options_xpath):
        Dropdown = self.browser.find_element_by_xpath(dropdown_xpath)
        Dropdown.clear()
        Dropdown.click()
        sleep(1)
        Options = self.browser.find_elements_by_xpath(options_xpath)
        randomOption = random.choice(Options)
        randomOption.click()
        sleep(2)

    #click on the save & con't button
    def clickSaveCont(self):
        self.browser.find_element_by_xpath(self.btn_saveAndCont).click()
