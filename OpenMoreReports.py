import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
import time
import os
#pytest use for order testcase running order
#import pytest
from datetime import datetime
__author__ = 'sergey.meerovich'


class openMoreReportsTestFirefox(unittest.TestCase):
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

    def test_1_Login_process_on_Firefox(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Firefox started at :'+date_time_formatted
        #check if all elements loaded:
        loading_attempt=3
        #time i let a page load
        #Load main page and register with username/password
        while(loading_attempt>0):
              try:
                 self.email_field=self.driver.find_element_by_name("email")
                 self.password_field=self.driver.find_element_by_name("password")
                 self.password_field=self.driver.find_element_by_id("btnLogin")
              except NoSuchElementException:
                 self.take_screenshot('Fail_log_in')
                 self.fail("There is missing elements 'email' or 'password' or 'btnLogin'")
              EmailElement=self.is_element_present(By.NAME,"email")
              PasswordElement=self.is_element_present(By.NAME,"password")
              LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
              if (EmailElement and PasswordElement and LoginBtnElement):
                 self.username_field=self.driver.find_element_by_name('email')
                 self.username_field.send_keys('testscr@yahoo.com')
                 self.password_field=self.driver.find_element_by_name('password')
                 self.password_field.send_keys('123')
                 #press on login
                 self.login_btn=self.driver.find_element_by_id('btnLogin')
                 self.login_btn.send_keys(Keys.ENTER)
                 self.driver.implicitly_wait(30)
                 break
              else:
                   loading_attempt=loading_attempt-1;
                   if (loading_attempt==0):
                     self.take_screenshot('login page not loaded all elements')
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Firefox finish at :'+date_time_formatted
    def test_2_OpenMoreReports_on_Firefox(self):
        #test_2DashboardDataSwitch_process_on_Firefox
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test open more reports_on_Firefox started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test Open More reports on Firefox started...')
        try:
              #data_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='data-tab']/a")
              data_el=self.driver.find_element_by_xpath(".//*[@id='data-tab']/a")
              Data_El=self.is_element_present(By.XPATH,".//*[@id='data-tab']/a")
              if(Data_El):
                 data_el.click()
                 self.loggertest(self.__class__.__name__,'Switch to Data tab...')
                 self.driver.implicitly_wait(20)
        except NoSuchElementException:
              self.take_screenshot('Data_Tab_problem')
              self.loggertest(self.__class__.__name__,'Switch to Data tab...')
              self.fail("There is missing element 'data-tab'")
           #test that we switched to Data tab
        try:
              AllCowsDataReportBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[1]")
              HealthDataReportBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[3]")
              HeatDataReportBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[2]")
              DistressDataReportBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[4]")
              NoId=self.driver.find_element_by_xpath(".//*[@id='filters']/li[5]")
              GroupAlertsDatareportBtn=self.driver.find_element_by_xpath(".//*[@id='GroupAlertsBtn']")
        except NoSuchElementException:
             self.take_screenshot("Data_Tab_not_loaded_fully")
             self.loggertest(self.__class__.__name__,'Check if Data tab loaded...')
             self.fail("The Data tab not loaded ")

        # Switch between More reports 20 times
        for x in range(0,20,1):
           #find and click on 'More' drop-down button
           try:
              #MoreDropDownBtn=self.is_element_present(By.XPATH,".//*[@id='more']")
              #MoreDropDownBtnToggle=self.is_element_present(By.XPATH,".//*[@id='filters']/li[7]/div[2]")
              #self.driver.find_element_by_xpath(".//*[@id='filters']/li[7]/div[2]").click()
              MoreDropDownBtn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='more']")))
              MoreDropDownBtnToggle = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[7]/div[2]")))
              self.driver.find_element_by_xpath(".//*[@id='filters']/li[7]/div[2]").click()
              time.sleep(1)
               #Select unassigned Tags
              self.driver.find_element_by_link_text("Unassigned Tags").click()
              time.sleep(1)
              self.loggertest(self.__class__.__name__,'open Unassigned Tags tab...')
              self.driver.implicitly_wait(20)
           except NoSuchElementException:
              self.take_screenshot("More_button_and_dropdown_toggle_not_found")
              self.loggertest(self.__class__.__name__,'Could not find Unassigned tag drop down element...')
              self.fail("Problem find and use drop-down toggle")
            #check if Tag Number title appear
           TagNumber=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th/div/span")
           if(TagNumber):
              pass
           else:
              self.take_screenshot("Unassigned_tags_report_not_loaded")
              self.loggertest(self.__class__.__name__,'Unassigned tags report not loaded...')
              self.fail("Fail load Unassigned Tags Report")
           #Select Suspected Cystic
           #MoreDropDownBtn=self.is_element_present(By.XPATH,".//*[@id='more']")
           MoreDropDownBtn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='more']")))

           #MoreDropDownBtnToggle=self.is_element_present(By.XPATH,".//*[@id='filters']/li[7]/div[2]")
           MoreDropDownBtnToggle = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[7]/div[2]")))

           self.driver.find_element_by_xpath(".//*[@id='filters']/li[7]/div[2]").click()
           time.sleep(1)
           #Select Suspected Cystic Report
           self.driver.find_element_by_link_text("Suspected Cystic").click()
           time.sleep(1)
           CowNumber=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
           self.driver.implicitly_wait(20)
           Group=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
           self.driver.implicitly_wait(20)
           DIM=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
           self.driver.implicitly_wait(20)
           NumberOfSystemHeats=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
           self.driver.implicitly_wait(20)
           DaysSinceLastHeat=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
           self.driver.implicitly_wait(20)
           if(CowNumber and Group and DIM and NumberOfSystemHeats and DaysSinceLastHeat):
              pass
           else:
              self.take_screenshot("Suspected_Cystic_tags_report_not_loaded")
              self.loggertest(self.__class__.__name__,'Suspected cystic report not loaded...')
              self.fail("Fail load Suspected Cystic Report")
         #Select Technical Failures Report
           #MoreDropDownBtn=self.is_element_present(By.XPATH,".//*[@id='more']")
           MoreDropDownBtn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='more']")))

           #MoreDropDownBtnToggle=self.is_element_present(By.XPATH,".//*[@id='filters']/li[7]/div[2]")
           MoreDropDownBtnToggle = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[7]/div[2]")))

           self.driver.find_element_by_xpath(".//*[@id='filters']/li[7]/div[2]").click()
           time.sleep(1)
         #Select Technical Failures Report
           self.driver.find_element_by_link_text("Technical Failures Report").click()
           time.sleep(1)
           NodeAddress=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
           self.driver.implicitly_wait(20)
           LastOfflineTime=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div/span")
           self.driver.implicitly_wait(20)
           OfflineEvents=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
           self.driver.implicitly_wait(20)
           if(NodeAddress and LastOfflineTime and OfflineEvents):
               pass
           else:
               self.take_screenshot("Technical_Failures_report_not_loaded")
               self.loggertest(self.__class__.__name__,'Technical Failures report not loaded...')
               self.fail("Fail load Technical Failures Report")
        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test More reports_on_Firefoxfinish at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test of more reports finished...')

    def test_3_Logout_process_on_Firefox(self):
         #test_Logout_process_on_Firefox
         #logout from main page(dashboard)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'test logout process on Firefox started at :'+date_time_formatted
        try:
           self.search_field=self.driver.find_element_by_id("signout")
        except NoSuchElementException:
             self.take_screenshot('Fail_log_out')
             self.fail("There is no element 'signout'")
        self.search_field.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)

        try:
           self.email_field=self.driver.find_element_by_name("email")
           self.password_field=self.driver.find_element_by_name("password")
           self.btnLogin_field=self.driver.find_element_by_id("btnLogin")
        except NoSuchElementException:
             self.take_screenshot('Fail_log_out')
             self.fail("There is missing elements 'email' or 'password' or 'btnLogin'")
        self.driver.implicitly_wait(3)

        EmailElement=self.is_element_present(By.NAME,"email")
        PasswordElement=self.is_element_present(By.NAME,"password")
        LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
        if( EmailElement and PasswordElement and LoginBtnElement):
            pass
        else:
           self.take_screenshot('Fail_log_out_did_not_exit_to_login_page')
        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Log out_process_on_Firefox finish at :'+date_time_formatted
    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()





class openMoreReportsTestChrome(unittest.TestCase):
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

    def test_1_Login_process_on_Chrome(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Chrome started at :'+date_time_formatted
        # get to the username field
        #check if all elements loaded:
        loading_attempt=3
        #time i let a page load
        #Load main page and register with username/password
        while(loading_attempt>0):
              try:
                 self.email_field=self.driver.find_element_by_name("email")
                 self.password_field=self.driver.find_element_by_name("password")
                 self.password_field=self.driver.find_element_by_id("btnLogin")
              except NoSuchElementException:
                 self.take_screenshot('Fail_log_in')
                 self.fail("There is missing elements 'email' or 'password' or 'btnLogin'")
              EmailElement=self.is_element_present(By.NAME,"email")
              PasswordElement=self.is_element_present(By.NAME,"password")
              LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
              if (EmailElement and PasswordElement and LoginBtnElement):
                 self.username_field=self.driver.find_element_by_name('email')
                 self.username_field.send_keys('testscr@yahoo.com')
                 self.password_field=self.driver.find_element_by_name('password')
                 self.password_field.send_keys('123')
                 #press on login
                 self.login_btn=self.driver.find_element_by_id('btnLogin')
                 self.login_btn.send_keys(Keys.ENTER)
                 self.driver.implicitly_wait(30)
                 break
              else:
                   loading_attempt=loading_attempt-1;
                   if (loading_attempt==0):
                     self.take_screenshot('login page not loaded all elements')
        loading_attempt=3
        #time i let a page load
        #Load main page and register with username/password
        while(loading_attempt>0):
              #check if user successfully login on page https://hc24-qalab-web.scrdairy.com/#dashboard/
              #check if headers exist
             try:
               self.email_field=self.driver.find_element_by_id("settings")
               self.signout_field=self.driver.find_element_by_id("signout")
               self.find_cow_field=self.driver.find_element_by_id("find_cow")
               self.password_field=self.driver.find_element_by_id("select-date")
               self.password_field=self.driver.find_element_by_id("note_add")
             except NoSuchElementException:
              self.take_screenshot('Fail_log_in')
              self.fail("There is missing elements 'settings' or 'signout' or 'find_cow' or 'select-date' or 'note_add'")
             headerSettingsElement=self.is_element_present(By.ID,"settings")
             headerSignoutElement=self.is_element_present(By.ID,"signout")
             headerFindCowElement=self.is_element_present(By.ID,"find_cow")
              #Check if footer is loaded
             footerTodayButton=self.is_element_present(By.ID,"select-date")
             footerNoteAddButton=self.is_element_present(By.ID,"note_add")
             if (headerSettingsElement and headerSignoutElement and headerFindCowElement and footerNoteAddButton and footerTodayButton ):
                 print 'The dashboard fully loaded'
                 break
             else:
                   self.driver.implicitly_wait(3)
                   loading_attempt=loading_attempt-1;
                   if (loading_attempt==0):
                       self.take_screenshot('Dashboard page not loaded all elements')

        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Chrome finish at :'+date_time_formatted
    def test_2_OpenMoreReports_on_Chrome(self):
        #test_2DashboardDataSwitch_process_on_Firefox
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test open more reports_on_Chrome started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test Open More reports on Chrome started...')
        try:
              #data_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='data-tab']/a")
              data_el=self.driver.find_element_by_xpath(".//*[@id='data-tab']/a")
              Data_El=self.is_element_present(By.XPATH,".//*[@id='data-tab']/a")
              if(Data_El):
                 data_el.click()
                 self.loggertest(self.__class__.__name__,'Switch to Data tab...')
                 self.driver.implicitly_wait(20)
        except NoSuchElementException:
              self.take_screenshot('Data_Tab_problem')
              self.loggertest(self.__class__.__name__,'Switch to Data tab...')
              self.fail("There is missing element 'data-tab'")
           #test that we switched to Data tab
        try:
              AllCowsDataReportBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[1]")
              HealthDataReportBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[3]")
              HeatDataReportBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[2]")
              DistressDataReportBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[4]")
              NoId=self.driver.find_element_by_xpath(".//*[@id='filters']/li[5]")
              GroupAlertsDatareportBtn=self.driver.find_element_by_xpath(".//*[@id='GroupAlertsBtn']")
        except NoSuchElementException:
             self.take_screenshot("Data_Tab_not_loaded_fully")
             self.loggertest(self.__class__.__name__,'Check if Data tab loaded...')
             self.fail("The Data tab not loaded ")

        # Switch between More reports 20 times
        for x in range(0,20,1):
           #find and click on 'More' drop-down button
           try:
              #MoreDropDownBtn=self.is_element_present(By.XPATH,".//*[@id='more']")
              #MoreDropDownBtnToggle=self.is_element_present(By.XPATH,".//*[@id='filters']/li[7]/div[2]")
              #self.driver.find_element_by_xpath(".//*[@id='filters']/li[7]/div[2]").click()
              MoreDropDownBtn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='more']")))
              MoreDropDownBtnToggle = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[7]/div[2]")))
              self.driver.find_element_by_xpath(".//*[@id='filters']/li[7]/div[2]").click()
              time.sleep(1)
               #Select unassigned Tags
              self.driver.find_element_by_link_text("Unassigned Tags").click()
              time.sleep(1)
              self.loggertest(self.__class__.__name__,'open Unassigned Tags tab...')
              self.driver.implicitly_wait(20)
           except NoSuchElementException:
              self.take_screenshot("More_button_and_dropdown_toggle_not_found")
              self.loggertest(self.__class__.__name__,'Could not find Unassigned tag drop down element...')
              self.fail("Problem find and use drop-down toggle")
            #check if Tag Number title appear
           TagNumber=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th/div/span")
           if(TagNumber):
              pass
           else:
              self.take_screenshot("Unassigned_tags_report_not_loaded")
              self.loggertest(self.__class__.__name__,'Unassigned tags report not loaded...')
              self.fail("Fail load Unassigned Tags Report")
           #Select Suspected Cystic
           #MoreDropDownBtn=self.is_element_present(By.XPATH,".//*[@id='more']")
           MoreDropDownBtn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='more']")))

           #MoreDropDownBtnToggle=self.is_element_present(By.XPATH,".//*[@id='filters']/li[7]/div[2]")
           MoreDropDownBtnToggle = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[7]/div[2]")))

           self.driver.find_element_by_xpath(".//*[@id='filters']/li[7]/div[2]").click()
           time.sleep(1)
           #Select Suspected Cystic Report
           self.driver.find_element_by_link_text("Suspected Cystic").click()
           time.sleep(1)
           CowNumber=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
           self.driver.implicitly_wait(20)
           Group=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
           self.driver.implicitly_wait(20)
           DIM=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
           self.driver.implicitly_wait(20)
           NumberOfSystemHeats=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
           self.driver.implicitly_wait(20)
           DaysSinceLastHeat=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
           self.driver.implicitly_wait(20)
           if(CowNumber and Group and DIM and NumberOfSystemHeats and DaysSinceLastHeat):
              pass
           else:
              self.take_screenshot("Suspected_Cystic_tags_report_not_loaded")
              self.loggertest(self.__class__.__name__,'Suspected cystic report not loaded...')
              self.fail("Fail load Suspected Cystic Report")
         #Select Technical Failures Report
           #MoreDropDownBtn=self.is_element_present(By.XPATH,".//*[@id='more']")
           MoreDropDownBtn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='more']")))

           #MoreDropDownBtnToggle=self.is_element_present(By.XPATH,".//*[@id='filters']/li[7]/div[2]")
           MoreDropDownBtnToggle = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[7]/div[2]")))

           self.driver.find_element_by_xpath(".//*[@id='filters']/li[7]/div[2]").click()
           time.sleep(1)
         #Select Technical Failures Report
           self.driver.find_element_by_link_text("Technical Failures Report").click()
           time.sleep(1)
           NodeAddress=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
           self.driver.implicitly_wait(20)
           LastOfflineTime=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div/span")
           self.driver.implicitly_wait(20)
           OfflineEvents=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
           self.driver.implicitly_wait(20)
           if(NodeAddress and LastOfflineTime and OfflineEvents):
               pass
           else:
               self.take_screenshot("Technical_Failures_report_not_loaded")
               self.loggertest(self.__class__.__name__,'Technical Failures report not loaded...')
               self.fail("Fail load Technical Failures Report")
        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test More reports_on_Chrome finish at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test of more reports finished...')



    def test_3_Logout_process_on_Chrome(self):
       #logout from main page(dashboard)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'test logout process on Chrome started at :'+date_time_formatted
        try:
           self.search_field=self.driver.find_element_by_id("signout")
        except NoSuchElementException:
             self.take_screenshot('Fail_log_out')
             self.fail("There is no element 'signout'")
        self.search_field.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(20)
        try:
           self.email_field=self.driver.find_element_by_name("email")
           self.password_field=self.driver.find_element_by_name("password")
           self.btnLogin_field=self.driver.find_element_by_id("btnLogin")
        except NoSuchElementException:
             self.take_screenshot('Fail_log_out')
             self.fail("There is missing elements 'email' or 'password' or 'btnLogin'")
        self.driver.implicitly_wait(10)
        EmailElement=self.is_element_present(By.NAME,"email")
        PasswordElement=self.is_element_present(By.NAME,"password")
        LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
        if( EmailElement and PasswordElement and LoginBtnElement):
            print 'Successfully back to Login page!'
            pass
        else:
           self.take_screenshot('Fail log-out did not exit to login page')
        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Log outh_process_on_Chrome finish at :'+date_time_formatted


    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()

class openMoreReportsTestIE(unittest.TestCase):
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

    def test_1_Login_process_on_IE(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_IE started at :'+date_time_formatted
        # get to the username field
        #check if all elements loaded:
        loading_attempt=3
        #time i let a page load
        #Load main page and register with username/password
        while(loading_attempt>0):
            try:
                   self.email_field=self.driver.find_element_by_name("email")
                   self.signout_field=self.driver.find_element_by_name("password")
                   self.find_cow_field=self.driver.find_element_by_id("btnLogin")
            except NoSuchElementException:
                   self.take_screenshot('Fail_log_in')
                   self.fail("There is missing elements 'email' or 'password' or 'btnLogin'")
            self.driver.implicitly_wait(3)
            EmailElement=self.is_element_present(By.NAME,"email")
            PasswordElement=self.is_element_present(By.NAME,"password")
            LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
            if (EmailElement and PasswordElement and LoginBtnElement):
                 self.username_field=self.driver.find_element_by_name('email')
                 self.username_field.send_keys('testscr@yahoo.com')
                 self.password_field=self.driver.find_element_by_name('password')
                 self.password_field.send_keys('123')
                 #press on login
                 self.login_btn=self.driver.find_element_by_id('btnLogin')
                 self.login_btn.send_keys(Keys.ENTER)
                 self.driver.implicitly_wait(30)
                 break
            else:
                loading_attempt=loading_attempt-1;
                if (loading_attempt==0):
                     self.take_screenshot('login page not loaded all elements')

        loading_attempt=3
        #time i let a page load
        #Load main page and register with username/password
        while(loading_attempt>0):
              #check if user successfully login on page https://hc24-qalab-web.scrdairy.com/#dashboard/
              #check if headers exist
            try:
               self.email_field=self.driver.find_element_by_id("settings")
               self.signout_field=self.driver.find_element_by_id("signout")
               self.find_cow_field=self.driver.find_element_by_id("find_cow")
               self.password_field=self.driver.find_element_by_id("select-date")
               self.password_field=self.driver.find_element_by_id("note_add")
            except NoSuchElementException:
              self.take_screenshot('Fail_log_in')
              self.fail("There is missing elements 'settings' or 'signout' or 'find_cow' or 'select-date' or 'note_add'")

            headerSettingsElement=self.is_element_present(By.ID,"settings")
            headerSignoutElement=self.is_element_present(By.ID,"signout")
            headerFindCowElement=self.is_element_present(By.ID,"find_cow")

              #Check if footer is loaded
            footerTodayButton=self.is_element_present(By.ID,"select-date")
            footerNoteAddButton=self.is_element_present(By.ID,"note_add")

            if (headerSettingsElement and headerSignoutElement and headerFindCowElement and footerNoteAddButton and footerTodayButton ):
                 print 'The dashboard fully loaded'
                 break
            else:
                   loading_attempt=loading_attempt-1;
                   if (loading_attempt==0):
                       print loading_attempt
                       self.take_screenshot('Dashboard page not loaded all elements')

        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_IE finish at :'+date_time_formatted

    def test_2_OpenMoreReports_on_IE(self):
        #test_2DashboardDataSwitch_process_on_Firefox
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test open more reports_on_IE started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test Open More reports on IE started...')
        try:
              #data_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='data-tab']/a")
              data_el=self.driver.find_element_by_xpath(".//*[@id='data-tab']/a")
              Data_El=self.is_element_present(By.XPATH,".//*[@id='data-tab']/a")
              if(Data_El):
                 data_el.click()
                 self.loggertest(self.__class__.__name__,'Switch to Data tab...')
                 self.driver.implicitly_wait(20)
        except NoSuchElementException:
              self.take_screenshot('Data_Tab_problem')
              self.loggertest(self.__class__.__name__,'Switch to Data tab...')
              self.fail("There is missing element 'data-tab'")
           #test that we switched to Data tab
        try:
              AllCowsDataReportBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[1]")
              HealthDataReportBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[3]")
              HeatDataReportBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[2]")
              DistressDataReportBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[4]")
              NoId=self.driver.find_element_by_xpath(".//*[@id='filters']/li[5]")
              GroupAlertsDatareportBtn=self.driver.find_element_by_xpath(".//*[@id='GroupAlertsBtn']")
        except NoSuchElementException:
             self.take_screenshot("Data_Tab_not_loaded_fully")
             self.loggertest(self.__class__.__name__,'Check if Data tab loaded...')
             self.fail("The Data tab not loaded ")

        # Switch between More reports 10 times
        for x in range(0,10,1):
           #find and click on 'More' drop-down button
           try:

              MoreDropDownBtn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='more']")))
              MoreDropDownBtnToggle = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[7]/div[2]")))
              self.driver.find_element_by_xpath(".//*[@id='filters']/li[7]/div[2]").click()
              time.sleep(2)
               #Select unassigned Tags
              self.driver.find_element_by_link_text("Unassigned Tags").click()
              time.sleep(2)
              self.loggertest(self.__class__.__name__,'open Unassigned Tags tab...')
              self.driver.implicitly_wait(20)
           except NoSuchElementException:
              self.take_screenshot("More_button_and_dropdown_toggle_not_found")
              self.loggertest(self.__class__.__name__,'Could not find Unassigned tag drop down element...')
              self.fail("Problem find and use drop-down toggle")
            #check if Tag Number title appear
           TagNumber=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th/div/span")
           if(TagNumber):
              pass
           else:
              self.take_screenshot("Unassigned_tags_report_not_loaded")
              self.loggertest(self.__class__.__name__,'Unassigned tags report not loaded...')
              self.fail("Fail load Unassigned Tags Report")
           #Select Suspected Cystic
           #MoreDropDownBtn=self.is_element_present(By.XPATH,".//*[@id='more']")
           MoreDropDownBtn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='more']")))

           #MoreDropDownBtnToggle=self.is_element_present(By.XPATH,".//*[@id='filters']/li[7]/div[2]")
           MoreDropDownBtnToggle = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[7]/div[2]")))

           self.driver.find_element_by_xpath(".//*[@id='filters']/li[7]/div[2]").click()
           time.sleep(1)
           #Select Suspected Cystic Report
           self.driver.find_element_by_link_text("Suspected Cystic").click()
           time.sleep(1)
           CowNumber=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
           self.driver.implicitly_wait(20)
           Group=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
           self.driver.implicitly_wait(20)
           DIM=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
           self.driver.implicitly_wait(20)
           NumberOfSystemHeats=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
           self.driver.implicitly_wait(20)
           DaysSinceLastHeat=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
           self.driver.implicitly_wait(20)
           if(CowNumber and Group and DIM and NumberOfSystemHeats and DaysSinceLastHeat):
              pass
           else:
              self.take_screenshot("Suspected_Cystic_tags_report_not_loaded")
              self.loggertest(self.__class__.__name__,'Suspected cystic report not loaded...')
              self.fail("Fail load Suspected Cystic Report")
         #Select Technical Failures Report
           #MoreDropDownBtn=self.is_element_present(By.XPATH,".//*[@id='more']")
           MoreDropDownBtn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='more']")))

           #MoreDropDownBtnToggle=self.is_element_present(By.XPATH,".//*[@id='filters']/li[7]/div[2]")
           MoreDropDownBtnToggle = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[7]/div[2]")))

           self.driver.find_element_by_xpath(".//*[@id='filters']/li[7]/div[2]").click()
           time.sleep(1)
         #Select Technical Failures Report
           self.driver.find_element_by_link_text("Technical Failures Report").click()
           time.sleep(1)
           NodeAddress=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
           self.driver.implicitly_wait(20)
           LastOfflineTime=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div/span")
           self.driver.implicitly_wait(20)
           OfflineEvents=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
           self.driver.implicitly_wait(20)
           if(NodeAddress and LastOfflineTime and OfflineEvents):
               pass
           else:
               self.take_screenshot("Technical_Failures_report_not_loaded")
               self.loggertest(self.__class__.__name__,'Technical Failures report not loaded...')
               self.fail("Fail load Technical Failures Report")
        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test More reports_on_IE finish at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test of more reports finished...')




    def test_3_Logout_process_on_IE(self):
       #logout from main page(dashboard)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'test logout process on IE started at :'+date_time_formatted
        try:
           self.search_field=self.driver.find_element_by_id("signout")
        except NoSuchElementException:
             self.take_screenshot('Fail_log_out')
             self.fail("There is no element 'signout'")
        self.search_field.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(20)

        try:
           self.email_field=self.driver.find_element_by_name("email")
           self.password_field=self.driver.find_element_by_name("password")
           self.btnLogin_field=self.driver.find_element_by_id("btnLogin")
        except NoSuchElementException:
             self.take_screenshot('Fail_log_out')
             self.fail("There is missing elements 'email' or 'password' or 'btnLogin'")


        EmailElement=self.is_element_present(By.NAME,"email")
        PasswordElement=self.is_element_present(By.NAME,"password")
        LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
        if( EmailElement and PasswordElement and LoginBtnElement):
            print 'Successfully back to Login page!'
            pass
        else:
           self.take_screenshot('Fail log-out did not exit to login page')
        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Log out_process_on_IE finish at :'+date_time_formatted

    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()




if __name__=='__main__':
    unittest.main(verbosity=2)
