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


class NextPrevCowCardTestFirefox(unittest.TestCase):
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
    def test_2_SwitchNextPrevCowCard_on_Firefox(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Open All Cows Report First Page_on_Firefox started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Open All Cows Report on Firefox started...')
        try:
              data_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='data-tab']/a")
              Data_El=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='data-tab']/a")
              if(Data_El):
                 data_el.click()
                 self.loggertest(self.__class__.__name__,'Switch to Data tab...')
                 self.driver.implicitly_wait(5)
        except NoSuchElementException:
              self.take_screenshot('Data_Tab_problem')
              self.loggertest(self.__class__.__name__,'Switch to Data tab...')
              self.fail("There is missing element 'data-tab'")
           #test that we switched to Data tab
        try:
              AllCowsDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='AllCows']")
              HealthDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Health']")
              HeatDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Heat']")
              self.driver.implicitly_wait(10)
              DistressDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Distress']")
              NoId=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='NoId']")
              GroupAlertsDatareportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='GroupAlerts']")
        except NoSuchElementException:
             self.take_screenshot("Data_Tab_not_loaded_fully")
             self.loggertest(self.__class__.__name__,'Check if Data tab loaded...')
             self.fail("The Data tab not loaded ")
                # Open a Cow Card that starts with 1XX

        try:
                  #Open second Page on All Cows report
                  self.driver.maximize_window()
                  #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                  #time.sleep(1)
                  FindCow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='find_cow']")))
                  fcow=self.is_element_present(By.XPATH,".//*[@id='find_cow']")
                  findcow=self.driver.find_element_by_xpath(".//*[@id='find_cow']")
                  self.loggertest(self.__class__.__name__,'Focus on Enter Cow number field')
                  findcow.click()
                  self.driver.implicitly_wait(10)
                  #look for cows that start with '1' digit
                  findcow.clear()
                  findcow.send_keys('1')
                  time.sleep(1)
                  self.loggertest(self.__class__.__name__,'Look for cow that started with number 1XXX')
                  #Chooose the first one that appear on DataBase
                  findcow.send_keys(Keys.ARROW_DOWN)
                  self.driver.implicitly_wait(5)
                  first_result=self.driver.find_element_by_xpath(".//*[@id='app']/div[1]/ul/li[3]/form/span/span[2]/div/span/div[1]/p").text
                  self.loggertest(self.__class__.__name__,'The cow number that selected is :'+first_result)
                  #Select the first one
                  findcow.send_keys(Keys.ENTER)
                  time.sleep(2)
                  #Cow Card number that opened
                  FirstCowCard= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='span-cow-number']")))
                  firstCowCardSelected=self.driver.find_element_by_xpath(".//*[@id='span-cow-number']").text
                  if first_result==firstCowCardSelected:
                    self.loggertest(self.__class__.__name__,'The cow card number that actually opened :'+firstCowCardSelected)
                    pass
                  else:
                    self.take_screenshot("Opened_wrong_cow_card")
                    self.loggertest(self.__class__.__name__,'Opened different cow card from selected on Find Cow field...')
                    self.fail("Not correct Cow Card selected")
        except NoSuchElementException:
                  self.take_screenshot("Can_not_find_Cow_Card_that_starts_with_1XX")
                  self.loggertest(self.__class__.__name__,'Could not find Cow Card that starts with 1XXX...')
                  self.fail("Problem with locate Cow Card")





        #Start switch and check between first and second page report of All Cows by use Right/Left Arrows
        for x in range(0,10,1):
               #Declare Next and Prev buttons
               next = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='next']/i")))
               prev = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='prev']/i")))
               Next=self.driver.find_element_by_xpath(".//*[@id='next']/i")
               Prev=self.driver.find_element_by_xpath(".//*[@id='prev']/i")
               #show current cow card drom total cows that displayed
               current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
               Current_Cow_Card_Status=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
               Current_Cow=Current_Cow_Card_Status[0:3]
               try:
                  #Press on Next button
                  Next.click()
                  #time.sleep(5)
                  element_exist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='navigator']/table/tbody/tr[1]/td[2]")))
                  self.loggertest(self.__class__.__name__,'Go to Next Cow Card')
                  #show current cow card drom total cows that displayed
                  current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
                  Current_Cow_Card_Status2=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
                  print Current_Cow_Card_Status2
                  Current_Cow2=Current_Cow_Card_Status2[0:3]
               except:
                  self.take_screenshot("Fail_switch_to_Next_Cow_Card")
                  self.loggertest(self.__class__.__name__,'Could not switch to next Cow card')
                  self.fail("Problem with switch to next Cow card")

               #Check if it actually change Cow Card
               if Current_Cow!=Current_Cow2:
                   pass
               else:
                   self.take_screenshot("Fail_switch_to_Next_Cow_Card")
                   self.loggertest(self.__class__.__name__,'Could not switch to next Cow card')
                   self.fail("Problem with switch to next Cow card")
               try:
                  #Press one more time on Next button
                  next = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='next']/i")))
                  #prev = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='prev']/i")))
                  Next=self.driver.find_element_by_xpath(".//*[@id='next']/i")
                  #Prev=self.driver.find_element_by_xpath(".//*[@id='prev']/i")
                  Next.click()
                  #time.sleep(5)
                  self.driver.implicitly_wait(20)
                  element_exist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='navigator']/table/tbody/tr[1]/td[2]")))
                  self.loggertest(self.__class__.__name__,'Go to Next Cow Card')
                  #show current cow card drom total cows that displayed
                  current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
                  Current_Cow_Card_Status3=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
                  Current_Cow3=Current_Cow_Card_Status3[0:3]
               except:
                  self.take_screenshot("Fail_switch_to_Next_Cow_Card")
                  self.loggertest(self.__class__.__name__,'Could not switch to next Cow card')
                  self.fail("Problem with switch to next Cow card")
               #Check if it actually change Cow Card
               if Current_Cow3!=Current_Cow2:
                   pass
               else:
                   self.take_screenshot("Fail_switch_to_Next_Cow_Card")
                   self.loggertest(self.__class__.__name__,'Could not switch to next Cow card')
                   self.fail("Problem with switch to next Cow card")
               try:
                  #Press on Prev button return to previous cow card
                  #next = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='next']/i")))
                  prev = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='prev']/i")))
                  #Next=self.driver.find_element_by_xpath(".//*[@id='next']/i")
                  Prev=self.driver.find_element_by_xpath(".//*[@id='prev']/i")
                  Prev.click()
                  #time.sleep(5)
                  self.driver.implicitly_wait(20)
                  self.loggertest(self.__class__.__name__,'Go to Previous Cow Card')
                  #show current cow card drom total cows that displayed
                  current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
                  Current_Cow_Card_Status4=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
                  Current_Cow4=Current_Cow_Card_Status4[0:3]
               except:
                  self.take_screenshot("Fail_switch_to_Prev_Cow_Card")
                  self.loggertest(self.__class__.__name__,'Could not switch to prev Cow card')
                  self.fail("Problem with switch to previous Cow card")
               #Check if it actually change Cow Card
               if Current_Cow2==Current_Cow4:
                   pass
               else:
                   self.take_screenshot("Fail_switch_to_Prev_Cow_Card")
                   self.loggertest(self.__class__.__name__,'Could not switch to previous Cow card')
                   self.fail("Problem with switch to previous Cow card")
               try:
                  #Press on Prev button return to previous cow card
                  #next = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='next']/i")))
                  prev = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='prev']/i")))
                  #Next=self.driver.find_element_by_xpath(".//*[@id='next']/i")
                  Prev=self.driver.find_element_by_xpath(".//*[@id='prev']/i")
                  Prev.click()
                  #time.sleep(5)
                  self.driver.implicitly_wait(20)
                  element_exist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='navigator']/table/tbody/tr[1]/td[2]")))
                  self.loggertest(self.__class__.__name__,'Go to Previous Cow Card')
                  #show current cow card drom total cows that displayed
                  current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
                  Current_Cow_Card_Status5=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
                  Current_Cow5=Current_Cow_Card_Status5[0:3]
               except:
                  self.take_screenshot("Fail_switch_to_Prev_Cow_Card")
                  self.loggertest(self.__class__.__name__,'Could not switch to prev Cow card')
                  self.fail("Problem with switch to previous Cow card")
               #Check if it actually change Cow Card
               if Current_Cow==Current_Cow5:
                   pass
               else:
                   self.take_screenshot("Fail_switch_to_Prev_Cow_Card")
                   self.loggertest(self.__class__.__name__,'Could not switch to previous Cow card')
                   self.fail("Problem with switch to previous Cow card")

        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Find and open Cow Card_on_Firefox finish at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test of Switch between reports finished...')
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





class NextPrevCowCardTestChrome(unittest.TestCase):
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
    def test_2_SwitchNextPrevCowCard_on_Chrome(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Open All Cows Report First Page_on_Firefox started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Open All Cows Report on Chrome started...')
        try:
              data_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='data-tab']/a")
              Data_El=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='data-tab']/a")
              if(Data_El):
                 data_el.click()
                 self.loggertest(self.__class__.__name__,'Switch to Data tab...')
                 self.driver.implicitly_wait(5)
        except NoSuchElementException:
              self.take_screenshot('Data_Tab_problem')
              self.loggertest(self.__class__.__name__,'Switch to Data tab...')
              self.fail("There is missing element 'data-tab'")
           #test that we switched to Data tab
        try:
              AllCowsDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='AllCows']")
              HealthDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Health']")
              HeatDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Heat']")
              self.driver.implicitly_wait(10)
              DistressDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Distress']")
              NoId=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='NoId']")
              GroupAlertsDatareportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='GroupAlerts']")
        except NoSuchElementException:
             self.take_screenshot("Data_Tab_not_loaded_fully")
             self.loggertest(self.__class__.__name__,'Check if Data tab loaded...')
             self.fail("The Data tab not loaded ")

        # Open a Cow Card that starts with 1XX

        try:
                  #Open second Page on All Cows report
                  self.driver.maximize_window()
                  #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                  #time.sleep(1)
                  FindCow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='find_cow']")))
                  fcow=self.is_element_present(By.XPATH,".//*[@id='find_cow']")
                  findcow=self.driver.find_element_by_xpath(".//*[@id='find_cow']")
                  self.loggertest(self.__class__.__name__,'Focus on Enter Cow number field')
                  findcow.click()
                  self.driver.implicitly_wait(10)
                  #look for cows that start with '1' digit
                  findcow.clear()
                  findcow.send_keys('1')
                  time.sleep(1)
                  self.loggertest(self.__class__.__name__,'Look for cow that started with number 1XXX')
                  #Chooose the first one that appear on DataBase
                  findcow.send_keys(Keys.ARROW_DOWN)
                  self.driver.implicitly_wait(5)
                  first_result=self.driver.find_element_by_xpath(".//*[@id='app']/div[1]/ul/li[3]/form/span/span[2]/div/span/div[1]/p").text
                  self.loggertest(self.__class__.__name__,'The cow number that selected is :'+first_result)
                  #Select the first one
                  findcow.send_keys(Keys.ENTER)
                  time.sleep(2)
                  #Cow Card number that opened
                  FirstCowCard= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='span-cow-number']")))
                  firstCowCardSelected=self.driver.find_element_by_xpath(".//*[@id='span-cow-number']").text
                  if first_result==firstCowCardSelected:
                    self.loggertest(self.__class__.__name__,'The cow card number that actually opened :'+firstCowCardSelected)
                    pass
                  else:
                    self.take_screenshot("Opened_wrong_cow_card")
                    self.loggertest(self.__class__.__name__,'Opened different cow card from selected on Find Cow field...')
                    self.fail("Not correct Cow Card selected")
        except NoSuchElementException:
                  self.take_screenshot("Can_not_find_Cow_Card_that_starts_with_1XX")
                  self.loggertest(self.__class__.__name__,'Could not find Cow Card that starts with 1XXX...')
                  self.fail("Problem with locate Cow Card")



        #Start switch and check between first and second page report of All Cows by use Right/Left Arrows
        for x in range(0,5,1):
               self.driver.maximize_window()
               #Declare Next and Prev buttons
               next = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='next']/i")))
               prev = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='prev']/i")))
               Next=self.driver.find_element_by_xpath(".//*[@id='next']/i")
               Prev=self.driver.find_element_by_xpath(".//*[@id='prev']/i")
               #show current cow card drom total cows that displayed
               current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
               Current_Cow_Card_Status=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
               Current_Cow=Current_Cow_Card_Status[0:3]
               try:
                  #Press on Next button
                  Next.click()
                  time.sleep(2)
                  element_exist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='navigator']/table/tbody/tr[1]/td[2]")))
                  self.loggertest(self.__class__.__name__,'Go to Next Cow Card')
                  #show current cow card drom total cows that displayed
                  current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
                  Current_Cow_Card_Status2=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
                  print Current_Cow_Card_Status2
                  Current_Cow2=Current_Cow_Card_Status2[0:3]
               except:
                  self.take_screenshot("Fail_switch_to_Next_Cow_Card")
                  self.loggertest(self.__class__.__name__,'Could not switch to next Cow card')
                  self.fail("Problem with switch to next Cow card")
               #Check if it actually change Cow Card
               if Current_Cow!=Current_Cow2:
                   pass
               else:
                   self.take_screenshot("Fail_switch_to_Next_Cow_Card")
                   self.loggertest(self.__class__.__name__,'Could not switch to next Cow card')
                   self.fail("Problem with switch to next Cow card")
               try:
                  #Press one more time on Next button
                  next = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='next']/i")))
                  #prev = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='prev']/i")))
                  Next=self.driver.find_element_by_xpath(".//*[@id='next']/i")
                  #Prev=self.driver.find_element_by_xpath(".//*[@id='prev']/i")
                  Next.click()
                  time.sleep(2)
                  self.driver.implicitly_wait(20)
                  element_exist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='navigator']/table/tbody/tr[1]/td[2]")))
                  self.loggertest(self.__class__.__name__,'Go to Next Cow Card')
                  #show current cow card drom total cows that displayed
                  current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
                  Current_Cow_Card_Status3=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
                  Current_Cow3=Current_Cow_Card_Status3[0:3]
               except:
                  self.take_screenshot("Fail_switch_to_Next_Cow_Card")
                  self.loggertest(self.__class__.__name__,'Could not switch to next Cow card')
                  self.fail("Problem with switch to next Cow card")
               #Check if it actually change Cow Card
               if Current_Cow3!=Current_Cow2:
                   pass
               else:
                   self.take_screenshot("Fail_switch_to_Next_Cow_Card")
                   self.loggertest(self.__class__.__name__,'Could not switch to next Cow card')
                   self.fail("Problem with switch to next Cow card")
               try:
                   #Press on Prev button return to previous cow card
                   #next = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='next']/i")))
                   prev = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='prev']/i")))
                   #Next=self.driver.find_element_by_xpath(".//*[@id='next']/i")
                   Prev=self.driver.find_element_by_xpath(".//*[@id='prev']/i")
                   Prev.click()
                   time.sleep(2)
                   self.driver.implicitly_wait(20)
                   self.loggertest(self.__class__.__name__,'Go to Previous Cow Card')
                   #show current cow card drom total cows that displayed
                   current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
                   Current_Cow_Card_Status4=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
                   Current_Cow4=Current_Cow_Card_Status4[0:3]
               except:
                  self.take_screenshot("Fail_switch_to_Prev_Cow_Card")
                  self.loggertest(self.__class__.__name__,'Could not switch to previous Cow card')
                  self.fail("Problem with switch to previous Cow card")
               #Check if it actually change Cow Card
               if Current_Cow2==Current_Cow4:
                   pass
               else:
                   self.take_screenshot("Fail_switch_to_Prev_Cow_Card")
                   self.loggertest(self.__class__.__name__,'Could not switch to previous Cow card')
                   self.fail("Problem with switch to previous Cow card")
               try:
                   #Press on Prev button return to previous cow card
                   #next = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='next']/i")))
                   prev = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='prev']/i")))
                   #Next=self.driver.find_element_by_xpath(".//*[@id='next']/i")
                   Prev=self.driver.find_element_by_xpath(".//*[@id='prev']/i")
                   Prev.click()
                   time.sleep(2)
                   self.driver.implicitly_wait(20)
                   element_exist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='navigator']/table/tbody/tr[1]/td[2]")))
                   self.loggertest(self.__class__.__name__,'Go to Previous Cow Card')
                   #show current cow card drom total cows that displayed
                   current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
                   Current_Cow_Card_Status5=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
                   Current_Cow5=Current_Cow_Card_Status5[0:3]
               except:
                  self.take_screenshot("Fail_switch_to_Prev_Cow_Card")
                  self.loggertest(self.__class__.__name__,'Could not switch to previous Cow card')
                  self.fail("Problem with switch to previous Cow card")

               #Check if it actually change Cow Card
               if Current_Cow==Current_Cow5:
                   pass
               else:
                   self.take_screenshot("Fail_switch_to_Prev_Cow_Card")
                   self.loggertest(self.__class__.__name__,'Could not switch to previous Cow card')
                   self.fail("Problem with switch to previous Cow card")

        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Find and open Cow Card_on_Chrome finish at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test of Switch between reports finished...')

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

class NextPrevCowCardTestIE(unittest.TestCase):
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

    def test_2_SwitchNextPrevCowCard_on_IE(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Open All Cows Report First Page_on_IE started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Open All Cows Report on Firefox started...')
        try:
              data_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='data-tab']/a")
              Data_El=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='data-tab']/a")
              if(Data_El):
                 data_el.click()
                 self.loggertest(self.__class__.__name__,'Switch to Data tab...')
                 self.driver.implicitly_wait(5)
        except NoSuchElementException:
              self.take_screenshot('Data_Tab_problem')
              self.loggertest(self.__class__.__name__,'Switch to Data tab...')
              self.fail("There is missing element 'data-tab'")
           #test that we switched to Data tab
        try:
              AllCowsDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='AllCows']")
              HealthDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Health']")
              HeatDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Heat']")
              self.driver.implicitly_wait(10)
              DistressDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Distress']")
              NoId=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='NoId']")
              GroupAlertsDatareportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='GroupAlerts']")
        except NoSuchElementException:
             self.take_screenshot("Data_Tab_not_loaded_fully")
             self.loggertest(self.__class__.__name__,'Check if Data tab loaded...')
             self.fail("The Data tab not loaded ")

            # Open a Cow Card that starts with 1XX

        try:
                  #Open second Page on All Cows report
                  self.driver.maximize_window()
                  #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                  #time.sleep(1)
                  FindCow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='find_cow']")))
                  fcow=self.is_element_present(By.XPATH,".//*[@id='find_cow']")
                  findcow=self.driver.find_element_by_xpath(".//*[@id='find_cow']")
                  self.loggertest(self.__class__.__name__,'Focus on Enter Cow number field')
                  findcow.click()
                  self.driver.implicitly_wait(10)
                  #look for cows that start with '1' digit
                  findcow.clear()
                  findcow.send_keys('1')
                  time.sleep(1)
                  self.loggertest(self.__class__.__name__,'Look for cow that started with number 1XXX')
                  #Chooose the first one that appear on DataBase
                  findcow.send_keys(Keys.ARROW_DOWN)
                  self.driver.implicitly_wait(5)
                  first_result=self.driver.find_element_by_xpath(".//*[@id='app']/div[1]/ul/li[3]/form/span/span[2]/div/span/div[1]/p").text
                  self.loggertest(self.__class__.__name__,'The cow number that selected is :'+first_result)
                  #Select the first one
                  findcow.send_keys(Keys.ENTER)
                  time.sleep(5)
                  #Cow Card number that opened
                  FirstCowCard= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='span-cow-number']")))
                  firstCowCardSelected=self.driver.find_element_by_xpath(".//*[@id='span-cow-number']").text
                  if first_result==firstCowCardSelected:
                    self.loggertest(self.__class__.__name__,'The cow card number that actually opened :'+firstCowCardSelected)
                    pass
                  else:
                    self.take_screenshot("Opened_wrong_cow_card")
                    self.loggertest(self.__class__.__name__,'Opened different cow card from selected on Find Cow field...')
                    self.fail("Not correct Cow Card selected")
        except NoSuchElementException:
                  self.take_screenshot("Can_not_find_Cow_Card_that_starts_with_1XX")
                  self.loggertest(self.__class__.__name__,'Could not find Cow Card that starts with 1XXX...')
                  self.fail("Problem with locate Cow Card")



        #Start switch and check between first and second page report of All Cows by use Right/Left Arrows
        for x in range(0,5,1):
               self.driver.maximize_window()
               #Declare Next and Prev buttons
               next = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='next']/i")))
               prev = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='prev']/i")))
               Next=self.driver.find_element_by_xpath(".//*[@id='next']/i")
               Prev=self.driver.find_element_by_xpath(".//*[@id='prev']/i")
               #show current cow card drom total cows that displayed
               current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
               Current_Cow_Card_Status=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
               Current_Cow=Current_Cow_Card_Status[0:3]
               try:
                  #Press on Next button
                  Next.click()
                  time.sleep(2)
                  element_exist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='navigator']/table/tbody/tr[1]/td[2]")))
                  self.loggertest(self.__class__.__name__,'Go to Next Cow Card')
                  #show current cow card drom total cows that displayed
                  current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
                  Current_Cow_Card_Status2=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
                  print Current_Cow_Card_Status2
                  Current_Cow2=Current_Cow_Card_Status2[0:3]
               except:
                  self.take_screenshot("Fail_switch_to_Next_Cow_Card")
                  self.loggertest(self.__class__.__name__,'Could not switch to next Cow card')
                  self.fail("Problem with switch to next Cow card")
                  #Check if it actually change Cow Card
               if Current_Cow!=Current_Cow2:
                   pass
               else:
                   self.take_screenshot("Fail_switch_to_Next_Cow_Card")
                   self.loggertest(self.__class__.__name__,'Could not switch to next Cow card')
                   self.fail("Problem with switch to next Cow card")
               try:
                  #Press one more time on Next button
                  next = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='next']/i")))
                  #prev = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='prev']/i")))
                  Next=self.driver.find_element_by_xpath(".//*[@id='next']/i")
                  #Prev=self.driver.find_element_by_xpath(".//*[@id='prev']/i")
                  Next.click()
                  time.sleep(2)
                  self.driver.implicitly_wait(20)
                  element_exist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='navigator']/table/tbody/tr[1]/td[2]")))
                  self.loggertest(self.__class__.__name__,'Go to Next Cow Card')
                  #show current cow card drom total cows that displayed
                  current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
                  Current_Cow_Card_Status3=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
                  Current_Cow3=Current_Cow_Card_Status3[0:3]
               except:
                  self.take_screenshot("Fail_switch_to_Next_Cow_Card")
                  self.loggertest(self.__class__.__name__,'Could not switch to next Cow card')
                  self.fail("Problem with switch to next Cow card")
               #Check if it actually change Cow Card
               if Current_Cow3!=Current_Cow2:
                   pass
               else:
                   self.take_screenshot("Fail_switch_to_Next_Cow_Card")
                   self.loggertest(self.__class__.__name__,'Could not switch to next Cow card')
                   self.fail("Problem with switch to next Cow card")
               try:
                  #Press on Prev button return to previous cow card
                  #next = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='next']/i")))
                  prev = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='prev']/i")))
                  #Next=self.driver.find_element_by_xpath(".//*[@id='next']/i")
                  Prev=self.driver.find_element_by_xpath(".//*[@id='prev']/i")
                  Prev.click()
                  time.sleep(2)
                  self.driver.implicitly_wait(20)
                  self.loggertest(self.__class__.__name__,'Go to Previous Cow Card')
                  #show current cow card drom total cows that displayed
                  current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
                  Current_Cow_Card_Status4=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
                  Current_Cow4=Current_Cow_Card_Status4[0:3]
               except:
                  self.take_screenshot("Fail_switch_to_Prev_Cow_Card")
                  self.loggertest(self.__class__.__name__,'Could not switch to prev Cow card')
                  self.fail("Problem with switch to previous Cow card")
               #Check if it actually change Cow Card
               if Current_Cow2==Current_Cow4:
                   pass
               else:
                   self.take_screenshot("Fail_switch_to_Prev_Cow_Card")
                   self.loggertest(self.__class__.__name__,'Could not switch to previous Cow card')
                   self.fail("Problem with switch to previous Cow card")
               try:
                  #Press on Prev button return to previous cow card
                  #next = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='next']/i")))
                  prev = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='prev']/i")))
                  #Next=self.driver.find_element_by_xpath(".//*[@id='next']/i")
                  Prev=self.driver.find_element_by_xpath(".//*[@id='prev']/i")
                  Prev.click()
                  time.sleep(2)
                  self.driver.implicitly_wait(20)
                  element_exist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='navigator']/table/tbody/tr[1]/td[2]")))
                  self.loggertest(self.__class__.__name__,'Go to Previous Cow Card')
                  #show current cow card drom total cows that displayed
                  current_cow_card_status=self.is_element_present(By.XPATH,".//*[@id='navigator']/table/tbody/tr[1]/td[2]")
                  Current_Cow_Card_Status5=self.driver.find_element_by_xpath(".//*[@id='navigator']/table/tbody/tr[1]/td[2]").text
                  Current_Cow5=Current_Cow_Card_Status5[0:3]
               except:
                  self.take_screenshot("Fail_switch_to_Prev_Cow_Card")
                  self.loggertest(self.__class__.__name__,'Could not switch to prev Cow card')
                  self.fail("Problem with switch to previous Cow card")
               #Check if it actually change Cow Card
               if Current_Cow==Current_Cow5:
                   pass
               else:
                   self.take_screenshot("Fail_switch_to_Prev_Cow_Card")
                   self.loggertest(self.__class__.__name__,'Could not switch to previous Cow card')
                   self.fail("Problem with switch to previous Cow card")

        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Find and open Cow Card_on_IE finish at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test of Switch between reports finished...')


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

