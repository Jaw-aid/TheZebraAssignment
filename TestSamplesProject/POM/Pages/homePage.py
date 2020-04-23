

class homePage():

    def __init__(self, browser):
        self.browser = browser

        #list of id's that will be moved to locators
        self.radbtn_Hero_CarInsurance = '//div[@class="hero hero-homepage"]//div[@class="radio-button-group"][1]'
        self.txtbox_Hero_zipcode = '//div[@class="hero hero-homepage"]//div[@class="input-wrapper"]//input[@name="zipcode"]'
        self.btn_Hero_Search = '//button[@data-cy="zipcode-submit-button"]'

    def click_topcarinsurance_radiobtn(self):
        self.browser.find_element_by_xpath(self.radbtn_Hero_CarInsurance).click()

    def type_topzipcode_txtbox(self, zipcode):
        self.browser.find_element_by_xpath(self.txtbox_Hero_zipcode).clear()
        self.browser.find_element_by_xpath(self.txtbox_Hero_zipcode).send_keys(zipcode)

    def click_topsearch_btn(self):
        self.browser.find_element_by_xpath(self.btn_Hero_Search).click()
