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
#use for loging console
import logging

from datetime import datetime
__author__ = 'sergey.meerovich'


class OpenHealthReportFirefox(unittest.TestCase):
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
    def console_log_record(self,TestName,browserType):
        try:
            dir=os.path.dirname(__file__)
            new_dir=os.makedirs(dir+'\ConsoleLogs')
            print new_dir+"\\"+TestName+browserType+".log"
        except OSError:
                pass
        dir=os.path.dirname(__file__)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
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
                     self.take_screenshot('login_page_not_loaded_all_elements')
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Firefox finish at :'+date_time_formatted

    def test_2_Open_Health_Report_Firefox(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test ability open Cows Health Report on_Firefox started at :'+date_time_formatted
        for x in range(0,10,1):
           try:
              #Open Cows Health  report
              heat_cows_link=self.driver.find_element_by_xpath(".//*[@id='cowsinhealthreport']")
              heat_cows_link.click()
              self.driver.implicitly_wait(20)
           except NoSuchElementException:
              self.take_screenshot('Fail_click_on_Health_web_link')
              self.fail("There is missing element 'cowsinhealthreport' ")
           try:
              #Check if user get a title 'Choose Report'
              self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='list_header']/div[@id='title']")),"Not opened Report list")
              #Ceck if user get focus and opened Health report
              self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='filters']/li[3]")),"Not find Health button")
              HealthBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[3]")
              checkBtnActive=HealthBtn.get_attribute('class')
              self.assertEqual(checkBtnActive,'report btn active','button is active')
              CowNumber3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              CowNumber3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              Group3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")))
              Group3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
              DIMAge3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              DIMAge3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(30)
              ActivityLow2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              ActivityLow2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              RuminationLow3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[5]/div/span")))
              RuminationLow3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
              DailyRumination3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              DailyRumination3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              self.driver.implicitly_wait(30)
              HealthIndex = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[7]/div/span")))
              HealthIndex=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[7]/div/span")
              if(CowNumber3 and Group3 and DIMAge3 and ActivityLow2 and RuminationLow3 and DailyRumination3 and HealthIndex):
                 pass
              else:
                self.take_screenshot("Health_Report_not_loaded_all_elements")
                self.fail("Problem during load Health titles")
           except NoSuchElementException:
              self.take_screenshot('Fail_click_on_Health_web_link')
              self.fail("There is missing element 'cowsinhealthreport' ")
            #Switch Back to Dashboard
           try:
              dashboard_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='dashboard-tab']/a")
              DASHBOARD_EL=self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='dashboard-tab']/a"))
              if DASHBOARD_EL:
                 dashboard_el.click()
                 self.loggertest(self.__class__.__name__,'Try switch back to Dashboard tab...')
                 self.driver.implicitly_wait(5)
                 lastUpdate_el=self.is_element_present(By.XPATH,".//*[@id='dashboard-pane']/div[1]/div[1]/span")
           except NoSuchElementException:
              self.take_screenshot('Fail_return_to_Dashboard')
              self.loggertest(self.__class__.__name__,'Fail switch back to Dashboard tab')
              self.fail("Problem return to Dashboard tab'")
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test ability open  Cows Health Report on_Firefox finish at :'+date_time_formatted


    def test_3_Logout_process_on_Firefox(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'test logout process on Firefox started at :'+date_time_formatted
        try:
           self.assertTrue(self.is_element_present(By.ID,"signout"),"Did not found Signout button-link")
           self.search_field=self.driver.find_element_by_id("signout")
        except NoSuchElementException:
             self.take_screenshot('Fail_log_out')
             self.fail("There is no element 'signout'")
        self.search_field.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(30)
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


class  OpenHealthReportChrome(unittest.TestCase):
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
    def console_log_record(self,TestName,browserType):
        try:
            dir=os.path.dirname(__file__)
            new_dir=os.makedirs(dir+'\ConsoleLogs')
            print new_dir+"\\"+TestName+browserType+".log"
        except OSError:
                pass
        dir=os.path.dirname(__file__)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
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
                     self.take_screenshot('login_page_not_loaded_all_elements')

        loading_attempt=3
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
                       self.take_screenshot('Dashboard_page_not_loaded_all_elements')
        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Firefox finish at :'+date_time_formatted

    def test_2_Open_Health_Report_Chrome(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test ability open Cows Health Report on_Chrome started at :'+date_time_formatted
        for x in range(0,10,1):
           try:
              #Open Cows Health  report
              heat_cows_link=self.driver.find_element_by_xpath(".//*[@id='cowsinhealthreport']")
              heat_cows_link.click()
              self.driver.implicitly_wait(20)
           except NoSuchElementException:
              self.take_screenshot('Fail_click_on_Health_web_link')
              self.fail("There is missing element 'cowsinhealthreport' ")
           try:
              #Check if user get a title 'Choose Report'
              self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='list_header']/div[@id='title']")),"Not opened Report list")
              #Ceck if user get focus and opened Health report
              self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='filters']/li[3]")),"Not find Health button")
              HealthBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[3]")
              checkBtnActive=HealthBtn.get_attribute('class')
              self.assertEqual(checkBtnActive,'report btn active','button is active')
              CowNumber3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              CowNumber3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              Group3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")))
              Group3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
              DIMAge3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              DIMAge3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(30)
              ActivityLow2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              ActivityLow2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              RuminationLow3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[5]/div/span")))
              RuminationLow3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
              DailyRumination3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              DailyRumination3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              self.driver.implicitly_wait(30)
              HealthIndex = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[7]/div/span")))
              HealthIndex=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[7]/div/span")
              if(CowNumber3 and Group3 and DIMAge3 and ActivityLow2 and RuminationLow3 and DailyRumination3 and HealthIndex):
                 pass
              else:
                self.take_screenshot("Health_Report_not_loaded_all_elements")
                self.fail("Problem during load Health titles")
           except NoSuchElementException:
              self.take_screenshot('Fail_click_on_Health_web_link')
              self.fail("There is missing element 'cowsinhealthreport' ")
            #Switch Back to Dashboard
           try:
              dashboard_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='dashboard-tab']/a")
              DASHBOARD_EL=self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='dashboard-tab']/a"))
              if DASHBOARD_EL:
                 dashboard_el.click()
                 self.loggertest(self.__class__.__name__,'Try switch back to Dashboard tab...')
                 self.driver.implicitly_wait(5)
                 lastUpdate_el=self.is_element_present(By.XPATH,".//*[@id='dashboard-pane']/div[1]/div[1]/span")
           except NoSuchElementException:
              self.take_screenshot('Fail_return_to_Dashboard')
              self.loggertest(self.__class__.__name__,'Fail switch back to Dashboard tab')
              self.fail("Problem return to Dashboard tab'")
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test ability open  Cows Health Report on_Chrome finish at :'+date_time_formatted



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
        self.driver.implicitly_wait(30)

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
           self.take_screenshot('Fail_log_out_did_not_exit_to_login_page')
        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Firefox finish at :'+date_time_formatted

    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()










class OpenHealthReportIE(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #get path of Internet Explorer
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
    def console_log_record(self,TestName,browserType):
        try:
            dir=os.path.dirname(__file__)
            new_dir=os.makedirs(dir+'\ConsoleLogs')
            print new_dir+"\\"+TestName+browserType+".log"
        except OSError:
                pass
        dir=os.path.dirname(__file__)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
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
        #Load main page and register with username/password
        while(loading_attempt>0):
            try:
                   self.email_field=self.driver.find_element_by_name("email")
                   self.signout_field=self.driver.find_element_by_name("password")
                   self.find_cow_field=self.driver.find_element_by_id("btnLogin")
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
                   loading_attempt=loading_attempt-1;
                   if (loading_attempt==0):
                       print loading_attempt
                       self.take_screenshot('Dashboard_page_not_loaded_all_elements')
        print "Test running time:"+str((date_time.now()-date_time))

    def test_2_Open_Health_Report_IE(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test ability open Cows Health Report on_IE started at :'+date_time_formatted
        for x in range(0,10,1):
           try:
              #Open Cows Health  report
              heat_cows_link=self.driver.find_element_by_xpath(".//*[@id='cowsinhealthreport']")
              heat_cows_link.click()
              self.driver.implicitly_wait(20)
           except NoSuchElementException:
              self.take_screenshot('Fail_click_on_Health_web_link')
              self.fail("There is missing element 'cowsinhealthreport' ")
           try:
              #Check if user get a title 'Choose Report'
              self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='list_header']/div[@id='title']")),"Not opened Report list")
              #Ceck if user get focus and opened Health report
              self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='filters']/li[3]")),"Not find Health button")
              HealthBtn=self.driver.find_element_by_xpath(".//*[@id='filters']/li[3]")
              checkBtnActive=HealthBtn.get_attribute('class')
              self.assertEqual(checkBtnActive,'report btn active','button is active')
              CowNumber3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              CowNumber3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              Group3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")))
              Group3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
              DIMAge3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              DIMAge3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(30)
              ActivityLow2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              ActivityLow2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              RuminationLow3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[5]/div/span")))
              RuminationLow3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
              DailyRumination3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              DailyRumination3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              self.driver.implicitly_wait(30)
              HealthIndex = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[7]/div/span")))
              HealthIndex=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[7]/div/span")
              if(CowNumber3 and Group3 and DIMAge3 and ActivityLow2 and RuminationLow3 and DailyRumination3 and HealthIndex):
                 pass
              else:
                self.take_screenshot("Health_Report_not_loaded_all_elements")
                self.fail("Problem during load Health titles")
           except NoSuchElementException:
              self.take_screenshot('Fail_click_on_Health_web_link')
              self.fail("There is missing element 'cowsinhealthreport' ")
            #Switch Back to Dashboard
           try:
              dashboard_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='dashboard-tab']/a")
              DASHBOARD_EL=self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='dashboard-tab']/a"))
              if DASHBOARD_EL:
                 dashboard_el.click()
                 self.loggertest(self.__class__.__name__,'Try switch back to Dashboard tab...')
                 self.driver.implicitly_wait(5)
                 lastUpdate_el=self.is_element_present(By.XPATH,".//*[@id='dashboard-pane']/div[1]/div[1]/span")
           except NoSuchElementException:
              self.take_screenshot('Fail_return_to_Dashboard')
              self.loggertest(self.__class__.__name__,'Fail switch back to Dashboard tab')
              self.fail("Problem return to Dashboard tab'")
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test ability open  Cows Health Report on_IE finish at :'+date_time_formatted

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
        self.driver.implicitly_wait(30)

        try:
           self.email_field=self.driver.find_element_by_name("email")
           self.password_field=self.driver.find_element_by_name("password")
           self.btnLogin_field=self.driver.find_element_by_id("btnLogin")
        except NoSuchElementException:
             self.take_screenshot('Fail_log_out')
             self.fail("There is missing elements 'email' or 'password' or 'btnLogin'")
        self.driver.implicitly_wait(30)

        EmailElement=self.is_element_present(By.NAME,"email")
        PasswordElement=self.is_element_present(By.NAME,"password")
        LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
        if( EmailElement and PasswordElement and LoginBtnElement):
            print 'Successfully back to Login page!'
            pass
        else:
           self.take_screenshot('Fail log-out did not exit to login page')
        print "Test running time:"+str((date_time.now()-date_time))


    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()




if __name__=='__main__':
    unittest.main(verbosity=2)


