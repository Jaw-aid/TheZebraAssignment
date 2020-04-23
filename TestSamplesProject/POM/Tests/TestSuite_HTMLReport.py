import unittest
import HtmlTestRunner
import os
import TestSamplesProject.POM.Tests.CarInsuranceTest
import TestSamplesProject.POM.Tests.HomepageTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from Homepage and HomeInsurance class
HomepageTest = unittest.TestLoader().loadTestsFromTestCase(TestSamplesProject.POM.Tests.HomepageTest.HomepageTestCase)
CarInsuranceTest = unittest.TestLoader().loadTestsFromTestCase(TestSamplesProject.POM.Tests.CarInsuranceTest.CarInsuranceTestCase)


# create a test suite combining Homepage and HomeInsurance
test_suite = unittest.TestSuite([HomepageTest, CarInsuranceTest])

# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(stream=outfile,report_title='Jawaid\'s Sample of Selenium for The Zebra',combine_reports=True)

# run the suite using HTMLTestRunner
runner.run(test_suite)
