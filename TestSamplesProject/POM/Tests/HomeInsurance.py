import unittest
from selenium import webdriver
from time import sleep


class HomeInsuranceTestCase(unittest.TestCase):
    #open browser to TheZebra.com
    def setUp(self):
        self.browser = webdriver.Chrome('/Users/jawaid/PycharmProjects/TheZebraSelenium/drivers/chromedriver')
        self.browser.implicitly_wait(5)
        self.browser.maximize_window()
        self.browser.get('http://www.TheZebra.com')
        self.browser.implicitly_wait(7)
        sleep(3)

    # Test case of buying home insurance and customer has a condo, rental, or mobile home
    def test_ZebraHomeInsurance_Loop(self):
        #check if home insurance button is present and then click on it
        home_insurance_button = self.browser.find_element_by_xpath('//label[@track-label="Home insurance"]')
        home_insurance_button.click()
        sleep(3)
        self.browser.implicitly_wait(7)
        # find zipcode textbox and enter in zipcode
        location_textbox = self.browser.find_element_by_xpath('//input[@name="zipcode"]')
        location_textbox.clear()
        location_textbox.send_keys("78705")
        sleep(3)
        # click on start or submit button
        start_button = self.browser.find_element_by_xpath('//button[@data-cy="zipcode-submit-button"]')
        start_button.click()
        sleep(7)
        #loop for customer to click through condo, rental, mobile home
        insuranceoptions = ["CONDO", "RENTAL", "MOBILE_HOME"]
        for i in insuranceoptions:
            option_button = self.browser.find_element_by_xpath('//label[@for="residence_type-%s"]' %i)
            option_button.click()
            sleep(3)
            self.assertTrue(self.browser.find_element_by_xpath('//div[@role="document"]').is_displayed())
            #close pop up
            x_button_on_popup = self.browser.find_element_by_xpath('//button[@id="modalHeaderCloseBtn"]')
            x_button_on_popup.click()
            sleep(3)

    #close browser
    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
