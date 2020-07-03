# TheZebraAssignment
Assignment for The Zebra QE Interview

Instructions to execute the test:
Option one - Terminal on Mac:
1) Download Zip file from https://github.com/Jaw-aid/TheZebraAssignment
2) Unzip the file
3) Go to TheZebraAssignment-master --> drivers --> chromedriver. Right click on chromedriver and click Get Info. Under General --> Where, right click and copy path of the chromedriver
4) Now go to TheZebraAssignment-master --> TestSamplesProject --> POM --> Tests and open up CarInsruanceTest.py, HomeInsurance.py, and HomepageTest.py. In the setUpClass for each file, look for self.browser or cls.browser = webdriver.Chrome('paste/in/the/new/driver/path'). Paste the new local path to the driver that you just copied in step three and make sure that the path ends with '/chromedriver'. This code should be around line 10 - 15. Save all three files. 
5) Once your path to browser is updated for each file, ensure that python3 is installed, and the selenium and html-testRunner packages are installed too.
a) Instructions to install python3 (https://docs.python-guide.org/starting/install3/osx/)
b) Enter the following into the terminal to install selenium: $ pip3 install selenium
c) Enter the following into the terminal to install html-testRunner: $ pip3 install html-testRunner
6) Change the terminal directory to point to the folder TheZebraAssignment-master (ie: /Users/jawaid/Desktop/TheZebraAssignment-master)
7) Enter in the following in the terminal: python3 -m TestSamplesProject.POM.Tests.TestSuite_HTMLReport
8) All three tests should start executing. In the end, a new folder called "reports" will be created. There will be an HTML file that you can open that will provide a report of the test. 

Note -- sometimes there is an error executing the script in regards to the chromedriver. To fix this, double click on the chromedriver and make sure your Mac settings allow you to work with the chromedriver. (Go to Settings --> Security and Privacy --> General and then click on the lock button on the bottom left to allow and trust the chromedriver)

Option two -- PyCharm
If you have PyCharm Community Edition installed, you can pull in my project from GitHub. Just be sure to change the path for the chromedriver like we did in steps 3 and 4 above. Go to the TestSuite_HTMLReport.py file, and execute the test. A new report folder should be created with the HTML report.

Option three -- YouTube
If the tests cannot be executed from the two options above, I made a YouTube video for your convenience that shows what happens when I execute the tests. 
https://youtu.be/UWHtpv0kmgo
