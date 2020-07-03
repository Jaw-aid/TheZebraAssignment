import random
class ci_startPage():

    def __init__(self, browser):
        self.browser = browser

        #list of elements to move to locators
        self.radbtn_YesInsured = '//label[@data-cy="currently_insuredstart-Yes-Radiobutton"]'
        self.radbtn_livingsituationOptions = '//label[starts-with(@data-cy, "residence_ownershipstart-")]'
        self.radbtn_userintent = '//label[starts-with(@data-cy, "user_intentstart-")]'
        self.btn_saveAndCont = '//button[@id="startSaveBtn"]'

    #selects yes for being currently insured
    def click_YESCurrentlyInsuredOption(self):
       self.browser.find_element_by_xpath(self.radbtn_YesInsured).click()

    #selects random radio button when we provide the xpath
    def select_RANDOMRadioBtn(self, xpathLocation):
        radiobtn_options = self.browser.find_elements_by_xpath(xpathLocation)
        clickOne_option = random.choice(radiobtn_options)
        clickOne_option.click()

    #click on the save & con't button
    def click_SaveCont(self):
        self.browser.find_element_by_xpath(self.btn_saveAndCont).click()
