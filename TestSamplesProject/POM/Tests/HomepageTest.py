import unittest
from selenium import webdriver
from time import sleep


class HomepageTestCase(unittest.TestCase):
    # open browser to TheZebra.com
    @classmethod
    def setUpClass(cls):
        #be sure to update the chromedriver location when executing the tests
        cls.browser = webdriver.Chrome('/Users/jawaid/PycharmProjects/TheZebraAssignmentPOM/drivers/chromedriver')
        cls.browser.implicitly_wait(5)
        cls.browser.maximize_window()
        cls.browser.get('http://www.TheZebra.com')
        cls.browser.implicitly_wait(7)
        sleep(3)

    #check to see if hero class is present
    def test_01_HeroclassPresent(self):
        heroclass = self.browser.find_element_by_xpath('//div[@class="hero hero-homepage"]')
        self.assertTrue(heroclass.is_displayed())


    #check if main headline is present "Insurance in Black & White"
    def test_02_Heroclass_Headline(self):
        mainheadline = self.browser.find_element_by_xpath('//h1[@class="hero-headline"]').text
        assert mainheadline == 'Insurance in\nblack & white.®'

    # check to see if Car Insurance Button is present on top
    def test_03_CarInsuranceButtonPresent_Top(self):
        car_insurance_button_top = self.browser.find_element_by_xpath('//div[@class="hero hero-homepage"]//div[@class="radio-button-group"][1]')
        self.assertTrue(car_insurance_button_top.is_displayed())

    # check to see if Home Insurance Button is present on top
    def test_04_HomeInsuranceButtonPresent_Top(self):
        home_insurance_button_top = self.browser.find_element_by_xpath('//div[@class="hero hero-homepage"]//div[@class="radio-button-group"][2]')
        self.assertTrue(home_insurance_button_top.is_displayed())

    # check to see if zip code box is present on top
    def test_05_ZipcodeBoxPresent_Top(self):
        zipcode_box_top = self.browser.find_element_by_xpath('//div[@class="hero hero-homepage"]//div[@class="input-wrapper"]')
        self.assertTrue(zipcode_box_top.is_displayed())

    #check to see if How it works section is present
    def test_06_FeaturesContainerPresent(self):
        HowItWorks = self.browser.find_element_by_xpath('//div[@class="homepage-features-container"]')
        self.browser.execute_script("arguments[0].scrollIntoView();", HowItWorks)
        self.assertTrue(HowItWorks.is_displayed())
        sleep(2)

    #check to see if "How does The Zebra work?" is present
    def test_07_FeaturesContainer_Headline(self):
        HowItWorks_Text = self.browser.find_element_by_xpath('//h2[@class="features-headline display-5"]').text
        assert HowItWorks_Text == 'How does\nThe Zebra work?'

    #check to see if Our Privacy Pledge section is present
    def test_08_PrivacyContainer(self):
        privacypledgesection = self.browser.find_element_by_xpath('//div[@class="homepage-privacy-container"]')
        self.browser.execute_script("arguments[0].scrollIntoView();", privacypledgesection)
        self.assertTrue(privacypledgesection.is_displayed())
        sleep(2)

    #check to see if "Our Privacy Pledge" text is present
    def test_09_PrivacyContainer_Headline(self):
        privacypledgesection_Text = self.browser.find_element_by_xpath('//h2[@class="privacy-headline h1"]').text
        assert privacypledgesection_Text == 'Our Privacy Pledge'

    #check to see if bottom container is present
    def test_10_BottomContainer_Preset(self):
        bottomcontainer = self.browser.find_element_by_xpath('//div[@class="homepage-bottom-cta-container"]')
        self.browser.execute_script("arguments[0].scrollIntoView();", bottomcontainer)
        self.assertTrue(bottomcontainer.is_displayed())
        sleep(2)

    #check to see if "It's easy to start saving" text is present on bottom container
    def test_11_BottomContainer_Headline(self):
        bottomcontainer_Text = self.browser.find_element_by_xpath('//h2[@class="h1"]').text
        assert bottomcontainer_Text == "It's easy to\nstart saving."

    #check to see if Car Insurance Button is present on main body
    def test_12_CarInsuranceButtonPresent_MainBody(self):
        car_insurance_button_mainbody = self.browser.find_element_by_xpath('//div[@class="main-content-container"]//div[@class="radio-button-group"][1]')
        self.assertTrue(car_insurance_button_mainbody.is_displayed())

    #check to see if Home Insurance Button is present on main body
    def test_13_HomeInsuranceButtonPresent_MainBody(self):
        home_insurance_button_mainbody = self.browser.find_element_by_xpath('//div[@class="main-content-container"]//div[@class="radio-button-group"][2]')
        self.assertTrue(home_insurance_button_mainbody.is_displayed())

    #check to see if Zipcode box is present on main body
    def test_14_ZipcodeBoxPresent_MainBody(self):
        zipcode_box_mainbody = self.browser.find_element_by_xpath('//div[@class="main-content-container"]//div[@class="input-wrapper"][1]')
        self.assertTrue(zipcode_box_mainbody.is_displayed())

    #scroll down to bottom of page and see if Compare is present in navigation bar on top
    def test_15_HeaderComparePresentWithScroll(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        headerbarCompare = self.browser.find_element_by_xpath('//div[contains(@class, "header-nav-item")][1]')
        self.assertTrue(headerbarCompare.is_displayed())
        headerbarCompare.click()
        sleep(2)

    #check to see if auto insurance is displayed in Compare drop down
    def test_16_Comparedropdown(self):
        autoinsurancedropdown = self.browser.find_element_by_xpath('//a[contains(@href, "https://www.thezebra.com/auto-insurance/")]')
        self.assertTrue(autoinsurancedropdown.is_displayed())


    # scroll down to bottom of page and see if Tools & Tips is present in navigation bar on top
    def test_16_HeaderToolsTipsPresentWithScroll(self):
        headerbarToolsTips = self.browser.find_element_by_xpath('//div[contains(@class, "header-nav-item")][2]')
        self.assertTrue(headerbarToolsTips.is_displayed())
        headerbarToolsTips.click()
        sleep(2)

    #check to see if resources is displayed in Tools & Tips drop down
    def test_17_ToolsTipsdropdown(self):
        resourcedropdown = self.browser.find_element_by_xpath('//a[contains(@href, "https://www.thezebra.com/resources/")]')
        self.assertTrue(resourcedropdown.is_displayed())

    # scroll down to bottom of page and see if Company is present in navigation bar on top
    def test_18_HeaderCompanyPresentWithScroll(self):
        headerbarCompany = self.browser.find_element_by_xpath('//div[contains(@class, "header-nav-item")][3]')
        self.assertTrue(headerbarCompany.is_displayed())
        headerbarCompany.click()
        sleep(2)

    #check to see if about is displayed in Company drop down
    def test_19_Companydropdown(self):
        aboutdropdown = self.browser.find_element_by_xpath('//a[contains(@href, "https://www.thezebra.com/about/")]')
        aboutdropdown.is_displayed()

    #check to see if naviagation bar has Get Quote and Not Phone Numnber
    def test_20_HeaderGetQuotePresentWithScroll(self):
        #make sure phone number is no longer displayed
        headerbarPhoneNumber = self.browser.find_element_by_xpath('//span[@class="cta-phone-display"]')
        self.assertFalse(headerbarPhoneNumber.is_displayed())
        #make sure that quotes is now displayed
        headerbarGetQuote = self.browser.find_element_by_xpath('//a[@id="desktopStickyCta"]')
        self.assertTrue(headerbarGetQuote.is_displayed())

    #close browser
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


if __name__ == '__main__':
    unittest.main()
