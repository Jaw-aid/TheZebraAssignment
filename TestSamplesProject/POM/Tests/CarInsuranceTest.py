import unittest
from selenium import webdriver
from time import sleep
from TestSamplesProject.POM.Pages.homePage import homePage
from TestSamplesProject.POM.Pages.ci_startPage import ci_startPage
from TestSamplesProject.POM.Pages.ci_startDetailsPage import ci_startDetailsPage
from TestSamplesProject.POM.Pages.ci_vehicleAddPage import ci_addVehiclePage


class CarInsuranceTestCase(unittest.TestCase):
    # open browser to TheZebra.com
    @classmethod
    def setUpClass(cls):
        #be sure to update the chromedriver location when executing the tests
        cls.browser = webdriver.Chrome('/Users/jawaid/PycharmProjects/TheZebraAssignmentPOM/drivers/chromedriver')
        cls.browser.implicitly_wait(5)
        cls.browser.maximize_window()


    def test_01_homepageCarInsuranceSearch(self):
        browser = self.browser
        browser.get('http://www.TheZebra.com')
        browser.implicitly_wait(5)
        sleep(3)
        homepage = homePage(browser)
        #select car insurance radio button
        homepage.click_topcarinsurance_radiobtn()
        #enter in zipcode
        homepage.type_topzipcode_txtbox('78705')
        sleep(1)
        #click search
        homepage.click_topsearch_btn()
        browser.implicitly_wait(5)
        sleep(5)

    def test_02_startCarInsurancePage(self):
        browser = self.browser
        ci_startpage = ci_startPage(browser)
        #select YES for currenly insured question
        ci_startpage.click_YESCurrentlyInsuredOption()
        sleep(2)
        #select random living situation
        ci_startpage.select_RANDOMRadioBtn(ci_startpage.radbtn_livingsituationOptions)
        sleep(2)
        #select intent
        ci_startpage.select_RANDOMRadioBtn(ci_startpage.radbtn_userintent)
        sleep(2)
        #click save and cont
        ci_startpage.click_SaveCont()
        sleep(5)

    def test_03_startDetailsCarInsurancePage(self):
        browser = self.browser
        ci_startdetailspage = ci_startDetailsPage(browser)
        #enters random 4 digits in textbox and select first option from dropdown
        ci_startdetailspage.enter_randomAddress()
        sleep(2)
        #fill out personal information
        ci_startdetailspage.enter_FirstName("John")
        sleep(1)
        ci_startdetailspage.enter_LastName("Smith")
        sleep(1)
        ci_startdetailspage.enter_Birthday("10261991")
        sleep(1)
        #click save and continue
        ci_startdetailspage.clickSaveCont()
        sleep(5)

    def test_04_addVehiclesPage(self):
        browser = self.browser
        ci_addvehiclespage = ci_addVehiclePage(browser)
        #select random year from dropdown
        ci_addvehiclespage.select_RANDOMDropdowns(ci_addvehiclespage.dropdown_car1_year,ci_addvehiclespage.dropdown_car1_selectRANDOMyear)
        #select random make from dropdown
        ci_addvehiclespage.select_RANDOMDropdowns(ci_addvehiclespage.dropdown_car1_make, ci_addvehiclespage.dropdown_car1_selectRANDOMmake)
        #select random model from dropdown
        ci_addvehiclespage.select_RANDOMDropdowns(ci_addvehiclespage.dropdown_car1_model, ci_addvehiclespage.dropdown_car1_selectRANDOMmodel)
        #select random trim from dropdown
        ci_addvehiclespage.select_RANDOMDropdowns(ci_addvehiclespage.dropdown_car1_trim, ci_addvehiclespage.dropdown_car1_selectRANDOMtrim)
        #click save and cont
        ci_addvehiclespage.clickSaveCont()
        sleep(5)

    #close browser
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main()
