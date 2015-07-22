import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
import time
import os
#pytest use for order testcase running order
#import pytest
from datetime import datetime
__author__ = 'sergey.meerovich'


class PrivacyTermTestFirefox(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #create a new Firefox session
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        #navigate to the application home page
        self.driver.get("https://hc24-qalab-web.scrdairy.com/")
    def is_element_present(self,how,what):
         try: self.driver.find_element(by=how,value=what)
         except NoSuchElementException ,e: return False
         return True
    def take_screenshot(self,msg):
        try:
            dir=os.path.dirname(__file__)
            new_dir=os.makedirs(dir+'\screenshots')
        except OSError:
                pass
        dir=os.path.dirname(__file__)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
        self.driver.get_screenshot_as_file(dir+"/screenshots/"+msg+date_time_formatted+".png")
                  #self.fail("Login page not loaded all elements")
        print msg
    def loggertest(self,testname,msg):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        try:
            dir=os.path.dirname(__file__)
            newdir=os.makedirs(dir+'\logs')
        except OSError:
                pass
        loggerfile=open(dir+"\logs\loggertest.txt","ab")
        #Add log message
        loggerfile.write(date_time_formatted+" : "+testname+" : "+msg+'\n')
        loggerfile.close()


    def test_1_PrivacyTermPages_Firefox(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Open Privacy Policy Page_on_Firefox started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Open Privacy Policy Page...')
        try:

              privacy=self.driver.find_element_by_xpath(".//*[@id='frmLogin']/div[3]/div[5]/a[1]")
              Privacy_El=self.is_element_present(By.XPATH,".//*[@id='frmLogin']/div[3]/div[5]/a[1]")
              window_before=self.driver.window_handles[0]
              #print window_before
              if(Privacy_El):
                 privacy.click()
                 window_after=self.driver.window_handles[1]
                # print window_after
                 #selectAll=Keys
                 #data_el.send_keys(Keys.CONTROL + 't')
                 self.loggertest(self.__class__.__name__,'Switch to PrivacyPolicy...')
                 self.driver.implicitly_wait(20)
                 self.driver.switch_to_window(window_after)
                 time.sleep(2)
        except NoSuchElementException:
              self.take_screenshot('Problem_open_Privacy_Policy_page')
              self.loggertest(self.__class__.__name__,'Problem open Privacy policy page...')
              self.fail("There is problem to open Privacy Policy page")
        #test that user opened PrivacyPolicy page
        URL=self.driver.current_url
        print URL
        PrivacyURL="https://hc24-qalab-web.scrdairy.com/PrivacyPolicy_en.html"
        if URL==PrivacyURL:
                 header1=self.is_element_present(By.XPATH,"//html/body/div/h1")
                 #print(header1)
                 CollectionOfInfo=self.is_element_present(By.XPATH,"//html/body/div/p[10]/b")
                 #print(CollectionOfInfo)
                 if (header1 and CollectionOfInfo):
                    self.loggertest(self.__class__.__name__,'Successfully loaded Policy Privacy page...')
                    print "Success load Privacy Policy Page !!!"
                 else:
                     self.take_screenshot('policy_Privacy_page_opened_but_not_all_elements_loaded')
                     self.loggertest(self.__class__.__name__,'Problem load all elements on Privacy Policy page...')
                     self.fail("There is problem to load all elements on Privacy Policy page")
        else:
                 self.take_screenshot('problem_get_to_new_url')
                 self.loggertest(self.__class__.__name__,'Problem open url of  Privacy Policy page...')
                 self.fail("There is problem reach to URL of Privacy Policy page")
        # Open termsConditions page
        try:
           self.driver.switch_to_window(window_before)
           time.sleep(2)
           terms=self.driver.find_element_by_xpath(".//*[@id='frmLogin']/div[3]/div[5]/a[2]")
           Terms_El=self.is_element_present(By.XPATH,".//*[@id='frmLogin']/div[3]/div[5]/a[2]")
           if(Terms_El):
                 terms.click()
                 window_after_2=self.driver.window_handles[2]
                # print window_after
                 #selectAll=Keys
                 #data_el.send_keys(Keys.CONTROL + 't')
                 self.loggertest(self.__class__.__name__,'Switch to TermsOfUse...')
                 self.driver.implicitly_wait(20)
                 self.driver.switch_to_window(window_after_2)
                 time.sleep(2)
           else:
              self.take_screenshot('Problem_open_Term_Of_Use_page')
              self.loggertest(self.__class__.__name__,'Problem open Term of Use page...')
              self.fail("There is problem to open term of use  page")
        except NoSuchElementException:
              self.take_screenshot('Problem_open_Term_Of_Use_page')
              self.loggertest(self.__class__.__name__,'Problem open Term of Use page...')
              self.fail("There is problem to open term of use  page")
        try:
             #test that user opened termsOfUse page
             URL2=self.driver.current_url
             print URL2
             TermsURL="https://hc24-qalab-web.scrdairy.com/TermsConditions_en.html"
             if URL2==TermsURL:
                 header1=self.is_element_present(By.XPATH,"//html/body/div/p[1]/b/span")
                 #print(header1)
                 general=self.is_element_present(By.XPATH,"//html/body/div/p[131]/b/u/span")
                 #print(general)
                 if (header1 and general):
                    self.loggertest(self.__class__.__name__,'Successfully loaded Terms Of Use page...')
                    print "Success load Terms Of Use Page !!!"
                 else:
                     self.take_screenshot('Terms_Of_Use_page_opened_but_not_all_elements_loaded')
                     self.loggertest(self.__class__.__name__,'Problem load all elements on Terms Of Use page...')
                     self.fail("There is problem to load all elements on Terms Of Use page")
             else:
                 self.take_screenshot('problem_get_to_new_url')
                 self.loggertest(self.__class__.__name__,'Problem open url of  Terms Of Use page...')
                 self.fail("There is problem reach to URL of Privacy Policy page")
        except:
             self.take_screenshot('problem_get_to_new_url')
             self.loggertest(self.__class__.__name__,'Problem open url of  Terms Of Use page...')
             self.fail("There is problem reach to URL of Privacy Policy page")

        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Open Policy privacy and Terms page on_Firefox finish at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test of open policy privacy page and Terms use page...')

    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()





class PrivacyTermTestTestChrome(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #get path of chromedriver
        dir=os.path.dirname(__file__)
        chrome_drive_path=dir+"/chromedriver.exe"
        #create a new Chrome session
        self.driver=webdriver.Chrome(chrome_drive_path)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        #navigate to the application home page
        self.driver.get("https://hc24-qalab-web.scrdairy.com/")
    def is_element_present(self,how,what):
         try: self.driver.find_element(by=how,value=what)
         except NoSuchElementException ,e:
             return False
         return True
    def take_screenshot(self,msg):
        try:
            dir=os.path.dirname(__file__)
            new_dir=os.makedirs(dir+'\screenshots')
        except OSError:
                pass
        dir=os.path.dirname(__file__)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
        self.driver.get_screenshot_as_file(dir+"/screenshots/"+msg+date_time_formatted+".png")
                  #self.fail("Login page not loaded all elements")
        print msg
    def loggertest(self,testname,msg):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        try:
            dir=os.path.dirname(__file__)
            newdir=os.makedirs(dir+'\logs')
        except OSError:
                pass
        loggerfile=open(dir+"\logs\loggertest.txt","ab")
        #Add log message
        loggerfile.write(date_time_formatted+" : "+testname+" : "+msg+'\n')
        loggerfile.close()

    def test_1_PrivacyTermPages_Chrome(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Open Privacy Policy Page_on_Firefox started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Open Privacy Policy Page...')
        try:

              privacy=self.driver.find_element_by_xpath(".//*[@id='frmLogin']/div[3]/div[5]/a[1]")
              Privacy_El=self.is_element_present(By.XPATH,".//*[@id='frmLogin']/div[3]/div[5]/a[1]")
              window_before=self.driver.window_handles[0]
              #print window_before
              if(Privacy_El):
                 privacy.click()
                 window_after=self.driver.window_handles[1]
                # print window_after
                 #selectAll=Keys
                 #data_el.send_keys(Keys.CONTROL + 't')
                 self.loggertest(self.__class__.__name__,'Switch to PrivacyPolicy...')
                 self.driver.implicitly_wait(20)
                 self.driver.switch_to_window(window_after)
                 time.sleep(2)
        except NoSuchElementException:
              self.take_screenshot('Problem_open_Privacy_Policy_page')
              self.loggertest(self.__class__.__name__,'Problem open Privacy policy page...')
              self.fail("There is problem to open Privacy Policy page")
        #test that user opened PrivacyPolicy page
        URL=self.driver.current_url
        print URL
        PrivacyURL="https://hc24-qalab-web.scrdairy.com/PrivacyPolicy_en.html"
        if URL==PrivacyURL:
                 header1=self.is_element_present(By.XPATH,"//html/body/div/h1")
                 #print(header1)
                 CollectionOfInfo=self.is_element_present(By.XPATH,"//html/body/div/p[10]/b")
                 #print(CollectionOfInfo)
                 if (header1 and CollectionOfInfo):
                    self.loggertest(self.__class__.__name__,'Successfully loaded Policy Privacy page...')
                    print "Success load Privacy Policy Page !!!"
                 else:
                     self.take_screenshot('policy_Privacy_page_opened_but_not_all_elements_loaded')
                     self.loggertest(self.__class__.__name__,'Problem load all elements on Privacy Policy page...')
                     self.fail("There is problem to load all elements on Privacy Policy page")
        else:
                 self.take_screenshot('problem_get_to_new_url')
                 self.loggertest(self.__class__.__name__,'Problem open url of  Privacy Policy page...')
                 self.fail("There is problem reach to URL of Privacy Policy page")
        # Open termsConditions page
        try:
           self.driver.switch_to_window(window_before)
           time.sleep(2)
           terms=self.driver.find_element_by_xpath(".//*[@id='frmLogin']/div[3]/div[5]/a[2]")
           Terms_El=self.is_element_present(By.XPATH,".//*[@id='frmLogin']/div[3]/div[5]/a[2]")
           if(Terms_El):
                 terms.click()
                 window_after_2=self.driver.window_handles[2]
                # print window_after
                 #selectAll=Keys
                 #data_el.send_keys(Keys.CONTROL + 't')
                 self.loggertest(self.__class__.__name__,'Switch to TermsOfUse...')
                 self.driver.implicitly_wait(20)
                 self.driver.switch_to_window(window_after_2)
                 time.sleep(2)
           else:
              self.take_screenshot('Problem_open_Term_Of_Use_page')
              self.loggertest(self.__class__.__name__,'Problem open Term of Use page...')
              self.fail("There is problem to open term of use  page")
        except NoSuchElementException:
              self.take_screenshot('Problem_open_Term_Of_Use_page')
              self.loggertest(self.__class__.__name__,'Problem open Term of Use page...')
              self.fail("There is problem to open term of use  page")
        try:
             #test that user opened termsOfUse page
             URL2=self.driver.current_url
             print URL2
             TermsURL="https://hc24-qalab-web.scrdairy.com/TermsConditions_en.html"
             if URL2==TermsURL:
                 header1=self.is_element_present(By.XPATH,"//html/body/div/p[1]/b/span")
                 #print(header1)
                 general=self.is_element_present(By.XPATH,"//html/body/div/p[131]/b/u/span")
                 #print(general)
                 if (header1 and general):
                    self.loggertest(self.__class__.__name__,'Successfully loaded Terms Of Use page...')
                    print "Success load Terms Of Use Page !!!"
                 else:
                     self.take_screenshot('Terms_Of_Use_page_opened_but_not_all_elements_loaded')
                     self.loggertest(self.__class__.__name__,'Problem load all elements on Terms Of Use page...')
                     self.fail("There is problem to load all elements on Terms Of Use page")
             else:
                 self.take_screenshot('problem_get_to_new_url')
                 self.loggertest(self.__class__.__name__,'Problem open url of  Terms Of Use page...')
                 self.fail("There is problem reach to URL of Privacy Policy page")
        except:
             self.take_screenshot('problem_get_to_new_url')
             self.loggertest(self.__class__.__name__,'Problem open url of  Terms Of Use page...')
             self.fail("There is problem reach to URL of Privacy Policy page")

        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Open Policy privacy and Terms page on_Chrome finish at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test of open policy privacy page and Terms use page...')



    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()

class PrivacyTermTestIE(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #get path of chromedriver
        dir=os.path.dirname(__file__)
        ie_drive_path=dir+"/IEDriverServer.exe"
        #create a new Internet Explorer session
        self.driver=webdriver.Ie(ie_drive_path)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        #navigate to the application home page
        self.driver.get("https://hc24-qalab-web.scrdairy.com/")
    def is_element_present(self,how,what):
         try: self.driver.find_element(by=how,value=what)
         except NoSuchElementException ,e: return False
         return True
    def take_screenshot(self,msg):
        try:
            dir=os.path.dirname(__file__)
            new_dir=os.makedirs(dir+'\screenshots')
        except OSError:
                pass
        dir=os.path.dirname(__file__)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
        self.driver.get_screenshot_as_file(dir+"/screenshots/"+msg+date_time_formatted+".png")
        print msg
    def loggertest(self,testname,msg):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        try:
            dir=os.path.dirname(__file__)
            newdir=os.makedirs(dir+'\logs')
        except OSError:
                pass
        loggerfile=open(dir+"\logs\loggertest.txt","ab")
        #Add log message
        loggerfile.write(date_time_formatted+" : "+testname+" : "+msg+'\n')
        loggerfile.close()


    def test_1_PrivacyTermPages_IE(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Open Privacy Policy Page_on_Firefox started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Open Privacy Policy Page...')
        try:

              privacy=self.driver.find_element_by_xpath(".//*[@id='frmLogin']/div[3]/div[5]/a[1]")
              Privacy_El=self.is_element_present(By.XPATH,".//*[@id='frmLogin']/div[3]/div[5]/a[1]")
              window_before=self.driver.window_handles[0]
              #print window_before
              if(Privacy_El):
                 privacy.click()

                 window_after=self.driver.window_handles[1]
                 #print window_after
                 #selectAll=Keys
                 #data_el.send_keys(Keys.CONTROL + 't')
                 self.loggertest(self.__class__.__name__,'Switch to PrivacyPolicy...')
                 self.driver.implicitly_wait(20)
                 self.driver.switch_to.window(window_after)
                 self.driver.maximize_window()
                 time.sleep(2)
        except NoSuchElementException:
              self.take_screenshot('Problem_open_Privacy_Policy_page')
              self.loggertest(self.__class__.__name__,'Problem open Privacy policy page...')
              self.fail("There is problem to open Privacy Policy page")
        #test that user opened PrivacyPolicy page
        URL=self.driver.current_url
        #print URL
        print URL
        PrivacyURL="https://hc24-qalab-web.scrdairy.com/PrivacyPolicy_en.html"

        if URL==PrivacyURL:
                 header1=self.is_element_present(By.XPATH,"//html/body/div/h1")
                 #print(header1)
                 CollectionOfInfo=self.is_element_present(By.XPATH,"//html/body/div/p[10]/b")
                 #print(CollectionOfInfo)
                 if (header1 and CollectionOfInfo):
                    self.loggertest(self.__class__.__name__,'Successfully loaded Policy Privacy page...')
                    print "Success load Privacy Policy Page !!!"
                    #Close  privace policy
                    self.driver.find_element_by_xpath("//html/body/div/h1").send_keys(Keys.CONTROL + 'w')
                 else:
                     self.take_screenshot('policy_Privacy_page_opened_but_not_all_elements_loaded')
                     self.loggertest(self.__class__.__name__,'Problem load all elements on Privacy Policy page...')
                     self.fail("There is problem to load all elements on Privacy Policy page")
        else:
                 self.take_screenshot('problem_get_to_new_url')
                 self.loggertest(self.__class__.__name__,'Problem open url of  Privacy Policy page...')
                 self.fail("There is problem reach to URL of Privacy Policy page")
        # Open termsConditions page
        try:
           self.driver.switch_to.window(window_before)
           terms=self.driver.find_element_by_xpath(".//*[@id='frmLogin']/div[3]/div[5]/a[2]")
           Terms_El=self.is_element_present(By.XPATH,".//*[@id='frmLogin']/div[3]/div[5]/a[2]")
           #print Terms_El
           if(Terms_El):
                 #self.driver.find_element_by_xpath(".//*[@id='frmLogin']/div[3]/div[5]/a[2]").send_keys(Keys.CONTROL+ 't')
                 terms.click()
                 window_after2=self.driver.window_handles[1]
                 time.sleep(5)
                 self.driver.switch_to.window(window_after2)
                 print window_after2
                 self.loggertest(self.__class__.__name__,'Switch to Terms Of Use...')
                 self.driver.implicitly_wait(20)
                 self.driver.maximize_window()
                 time.sleep(2)

           else:
              self.take_screenshot('Problem_open_Term_Of_Use_page')
              self.loggertest(self.__class__.__name__,'Problem open Term of Use page...')
              self.fail("There is problem to open term of use  page")
        except NoSuchElementException:
              self.take_screenshot('Problem_open_Term_Of_Use_page')
              self.loggertest(self.__class__.__name__,'Problem open Term of Use page...')
              self.fail("There is problem to open term of use  page")
        try:
             #test that user opened termsOfUse page
             #window_last=self.driver.self.driver.window_handles[2]
             #print window_last
             URL2=self.driver.current_url
             print URL2
             TermsURL="https://hc24-qalab-web.scrdairy.com/TermsConditions_en.html"
             if URL2==TermsURL:
                 header1=self.is_element_present(By.XPATH,"//html/body/div/p[1]/b/span")
                 #print(header1)
                 general=self.is_element_present(By.XPATH,"//html/body/div/p[131]/b/u/span")
                 #print(general)
                 if (header1 and general):
                    self.loggertest(self.__class__.__name__,'Successfully loaded Terms Of Use page...')
                    print "Success load Terms Of Use Page !!!"


                    #Close  terms of use
                    self.driver.find_element_by_xpath("//html/body/div/p[1]/b/span").send_keys(Keys.CONTROL + 'w')


                 else:
                     self.take_screenshot('Terms_Of_Use_page_opened_but_not_all_elements_loaded')
                     self.loggertest(self.__class__.__name__,'Problem load all elements on Terms Of Use page...')
                     self.fail("There is problem to load all elements on Terms Of Use page")
             else:
                 self.take_screenshot('problem_get_to_new_url')
                 self.loggertest(self.__class__.__name__,'Problem open url of  Terms Of Use page...')
                 self.fail("There is problem reach to URL of Privacy Policy page")
        except:
             self.take_screenshot('problem_get_to_new_url')
             self.loggertest(self.__class__.__name__,'Problem open url of  Terms Of Use page...')
             self.fail("There is problem reach to URL of Privacy Policy page")

        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Open Policy privacy and Terms page on_Chrome finish at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test of open policy privacy page and Terms use page...')



    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()




if __name__=='__main__':
    unittest.main(verbosity=2)
