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


from datetime import datetime
from datetime import timedelta
__author__ = 'sergey.meerovich'


class SwitchGraphsOnCowCardTestFirefox(unittest.TestCase):
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
    def test_2_CowCardGraphs_on_Firefox(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Open Data Tab and specific Cow Card_on_Firefox started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Open Data Tab on Firefox started...')
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

        #Select certain Cow card and switch between graphs
        for x in range(0,5,1):
               #Open second Page on All Cows report
               try:
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
                   #time.sleep(1)
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
                   self.loggertest(self.__class__.__name__,'The cow card number that actually opened :'+firstCowCardSelected)
                   #variables for Days buttons
                   DAY1= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[1]")))
                   Day1=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[1]")
                   DAY7= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[2]")))
                   Days7=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[2]")
                   DAY30= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[3]")))
                   Days30=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[3]")
                   DAY60= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[4]")))
                   Days60=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[4]")
                   DAY90= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[5]")))
                   Days90=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[5]")
                   DAY365= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[6]")))
                   Days365=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[6]")
                   #select 1 Day period
                   Day1.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=1)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                   #time.sleep(10)

                   ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_1_day")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 1 Day')
                   #    self.fail("Failed open period of 1 day")

                   #Test 7 days perioud functionality
                   Days7.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=7)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                    ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_7_days")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 7 Days')
                   #    self.fail("Failed open period of 7 days")

                   #Test 30 days perioud functionality
                   Days30.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=30)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted
                    ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_30_days")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 30 Days')
                   #    self.fail("Failed open period of 30 days")

                   #Test 60 days perioud functionality
                   Days60.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=60)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                   if DayTimeStamp==date_time_formatted:
                       pass
                   else:
                       self.take_screenshot("Not_opened_correct_date_period_of_60_days")
                       self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 60 Days')
                       self.fail("Failed open period of 60 days")

                   #Test 90 days perioud functionality
                   Days90.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=90)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                     ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_90_days")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 90 Days')
                   #    self.fail("Failed open period of 90 days")


                   #Test 90 days perioud functionality
                   Days365.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=365)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                     ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_365_days")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 365 Days')
                   #    self.fail("Failed open period of 365 days")



                    #Search for Cow Card that started with number '2XXX'
                   FindCow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='find_cow']")))
                   fcow=self.is_element_present(By.XPATH,".//*[@id='find_cow']")
                   findcow=self.driver.find_element_by_xpath(".//*[@id='find_cow']")
                   self.loggertest(self.__class__.__name__,'Focus on Enter Cow number field')
                   findcow.click()
                   self.driver.implicitly_wait(10)
                   #look for cows that start with '2' digit
                   findcow.clear()
                   findcow.send_keys('2')
                   time.sleep(1)
                   self.loggertest(self.__class__.__name__,'Look for cow that started with number 2XXX')
                   #Chooose the first one that appear on DataBase
                   findcow.send_keys(Keys.ARROW_DOWN)
                   self.driver.implicitly_wait(5)
                   FirstResult = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='app']/div[1]/ul/li[3]/form/span/span[2]/div/span/div[1]/p")))
                   first_result=self.driver.find_element_by_xpath(".//*[@id='app']/div[1]/ul/li[3]/form/span/span[2]/div/span/div[1]/p").text
                   self.loggertest(self.__class__.__name__,'The cow number that selected is :'+first_result)
                   #Select the first one
                   findcow.send_keys(Keys.ENTER)
                   time.sleep(2)
                   #Cow Card number that opened
                   FirstCowCard= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='span-cow-number']")))
                   firstCowCardSelected=self.driver.find_element_by_xpath(".//*[@id='span-cow-number']").text
                   self.loggertest(self.__class__.__name__,'The cow card number that actually opened :'+firstCowCardSelected)
                   #variables for Days buttons
                   DAY1= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[1]")))
                   Day1=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[1]")
                   DAY7= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[2]")))
                   Days7=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[2]")
                   DAY30= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[3]")))
                   Days30=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[3]")
                   DAY60= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[4]")))
                   Days60=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[4]")
                   DAY90= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[5]")))
                   Days90=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[5]")
                   DAY365= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[6]")))
                   Days365=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[6]")




                   #Date Time stamp
                   date_time=datetime.now()
                   date_time_formatted=date_time.strftime("%m/%d/%y")
                   print 'Current date stamp :'+date_time_formatted

               except NoSuchElementException:
                   self.take_screenshot("Can_not_find_Cow_card")
                   self.loggertest(self.__class__.__name__,'Could not find Cow cards of cows that started with 1XXX or 2XXX...')
                   self.fail("Problem with opening Cow Card")
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





class SwitchGraphsOnCowCardTestChrome(unittest.TestCase):
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
    def test_2_CowCardGraphs_on_Chrome(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Open Data Tab and specific Cow Card_on_Chrome started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Open Data Tab on Chrome started...')
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

        #Select certain Cow card and switch between graphs
        for x in range(0,5,1):
               #Open second Page on All Cows report
               try:
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
                   #time.sleep(1)
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
                   self.loggertest(self.__class__.__name__,'The cow card number that actually opened :'+firstCowCardSelected)
                   #variables for Days buttons
                   DAY1= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[1]")))
                   Day1=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[1]")
                   DAY7= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[2]")))
                   Days7=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[2]")
                   DAY30= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[3]")))
                   Days30=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[3]")
                   DAY60= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[4]")))
                   Days60=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[4]")
                   DAY90= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[5]")))
                   Days90=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[5]")
                   DAY365= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[6]")))
                   Days365=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[6]")
                   #select 1 Day period
                   Day1.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=1)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                   #time.sleep(10)

                   ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_1_day")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 1 Day')
                   #    self.fail("Failed open period of 1 day")

                   #Test 7 days perioud functionality
                   Days7.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=7)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                    ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_7_days")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 7 Days')
                   #    self.fail("Failed open period of 7 days")

                   #Test 30 days perioud functionality
                   Days30.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=30)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted
                    ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_30_days")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 30 Days')
                   #    self.fail("Failed open period of 30 days")

                   #Test 60 days perioud functionality
                   Days60.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=60)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                   if DayTimeStamp==date_time_formatted:
                       pass
                   else:
                       self.take_screenshot("Not_opened_correct_date_period_of_60_days")
                       self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 60 Days')
                       self.fail("Failed open period of 60 days")

                   #Test 90 days perioud functionality
                   Days90.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=90)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                     ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_90_days")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 90 Days')
                   #    self.fail("Failed open period of 90 days")


                   #Test 90 days perioud functionality
                   Days365.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=365)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                     ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_365_days")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 365 Days')
                   #    self.fail("Failed open period of 365 days")



                    #Search for Cow Card that started with number '2XXX'
                   FindCow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='find_cow']")))
                   fcow=self.is_element_present(By.XPATH,".//*[@id='find_cow']")
                   findcow=self.driver.find_element_by_xpath(".//*[@id='find_cow']")
                   self.loggertest(self.__class__.__name__,'Focus on Enter Cow number field')
                   findcow.click()
                   self.driver.implicitly_wait(10)
                   #look for cows that start with '2' digit
                   findcow.clear()
                   findcow.send_keys('2')
                   time.sleep(1)
                   self.loggertest(self.__class__.__name__,'Look for cow that started with number 2XXX')
                   #Chooose the first one that appear on DataBase
                   findcow.send_keys(Keys.ARROW_DOWN)
                   self.driver.implicitly_wait(5)
                   FirstResult = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='app']/div[1]/ul/li[3]/form/span/span[2]/div/span/div[1]/p")))
                   first_result=self.driver.find_element_by_xpath(".//*[@id='app']/div[1]/ul/li[3]/form/span/span[2]/div/span/div[1]/p").text
                   self.loggertest(self.__class__.__name__,'The cow number that selected is :'+first_result)
                   #Select the first one
                   findcow.send_keys(Keys.ENTER)
                   time.sleep(2)
                   #Cow Card number that opened
                   FirstCowCard= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='span-cow-number']")))
                   firstCowCardSelected=self.driver.find_element_by_xpath(".//*[@id='span-cow-number']").text
                   self.loggertest(self.__class__.__name__,'The cow card number that actually opened :'+firstCowCardSelected)
                   #variables for Days buttons
                   DAY1= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[1]")))
                   Day1=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[1]")
                   DAY7= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[2]")))
                   Days7=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[2]")
                   DAY30= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[3]")))
                   Days30=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[3]")
                   DAY60= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[4]")))
                   Days60=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[4]")
                   DAY90= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[5]")))
                   Days90=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[5]")
                   DAY365= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[6]")))
                   Days365=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[6]")




                   #Date Time stamp
                   date_time=datetime.now()
                   date_time_formatted=date_time.strftime("%m/%d/%y")
                   print 'Current date stamp :'+date_time_formatted

               except NoSuchElementException:
                   self.take_screenshot("Can_not_find_Cow_card")
                   self.loggertest(self.__class__.__name__,'Could not find Cow cards of cows that started with 1XXX or 2XXX...')
                   self.fail("Problem with opening Cow Card")
        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Find and open Cow Card_on_Firefox finish at :'+date_time_formatted
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

class SwitchGraphsOnCowCardTestIE(unittest.TestCase):
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

    def test_2_CowCardGraphs_on_IE(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Open Data Tab and specific Cow Card_on_IE started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Open Data Tab on Chrome started...')
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

        #Select certain Cow card and switch between graphs
        for x in range(0,5,1):
               #Open second Page on All Cows report
               try:
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
                   #time.sleep(1)
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
                   self.loggertest(self.__class__.__name__,'The cow card number that actually opened :'+firstCowCardSelected)
                   #variables for Days buttons
                   DAY1= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[1]")))
                   Day1=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[1]")
                   DAY7= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[2]")))
                   Days7=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[2]")
                   DAY30= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[3]")))
                   Days30=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[3]")
                   DAY60= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[4]")))
                   Days60=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[4]")
                   DAY90= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[5]")))
                   Days90=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[5]")
                   DAY365= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[6]")))
                   Days365=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[6]")
                   #select 1 Day period
                   Day1.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=1)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                   #time.sleep(10)

                   ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_1_day")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 1 Day')
                   #    self.fail("Failed open period of 1 day")

                   #Test 7 days perioud functionality
                   Days7.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=7)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                    ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_7_days")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 7 Days')
                   #    self.fail("Failed open period of 7 days")

                   #Test 30 days perioud functionality
                   Days30.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=30)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted
                    ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_30_days")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 30 Days')
                   #    self.fail("Failed open period of 30 days")

                   #Test 60 days perioud functionality
                   Days60.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=60)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                   if DayTimeStamp==date_time_formatted:
                       pass
                   else:
                       self.take_screenshot("Not_opened_correct_date_period_of_60_days")
                       self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 60 Days')
                       self.fail("Failed open period of 60 days")

                   #Test 90 days perioud functionality
                   Days90.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=90)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                     ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_90_days")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 90 Days')
                   #    self.fail("Failed open period of 90 days")


                   #Test 90 days perioud functionality
                   Days365.click()
                   self.driver.implicitly_wait(5)
                   time.sleep(1)
                   daytimestamp= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]")))
                   DayTimeStamp=self.driver.find_element_by_xpath(".//*[@id='overall-changes']/div/div[1]/div/div[2]/span[1]").text
                   #print DayTimeStamp
                   #Date Time stamp
                   date_time=datetime.now()
                   yesterday= date_time-timedelta(days=365)
                   date_time_formatted=yesterday.strftime("%m/%d/%Y").lstrip("0").replace(" 0", " ")
                   print date_time_formatted

                     ###Disabled because Bug 16195
                   #if DayTimeStamp==date_time_formatted:
                   #    pass
                   #else:
                   #    self.take_screenshot("Not_opened_correct_date_period_of_365_days")
                   #    self.loggertest(self.__class__.__name__,'Not appeared correct period of graph 365 Days')
                   #    self.fail("Failed open period of 365 days")



                    #Search for Cow Card that started with number '2XXX'
                   FindCow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='find_cow']")))
                   fcow=self.is_element_present(By.XPATH,".//*[@id='find_cow']")
                   findcow=self.driver.find_element_by_xpath(".//*[@id='find_cow']")
                   self.loggertest(self.__class__.__name__,'Focus on Enter Cow number field')
                   findcow.click()
                   self.driver.implicitly_wait(10)
                   #look for cows that start with '2' digit
                   findcow.clear()
                   findcow.send_keys('2')
                   time.sleep(1)
                   self.loggertest(self.__class__.__name__,'Look for cow that started with number 2XXX')
                   #Chooose the first one that appear on DataBase
                   findcow.send_keys(Keys.ARROW_DOWN)
                   self.driver.implicitly_wait(5)
                   FirstResult = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='app']/div[1]/ul/li[3]/form/span/span[2]/div/span/div[1]/p")))
                   first_result=self.driver.find_element_by_xpath(".//*[@id='app']/div[1]/ul/li[3]/form/span/span[2]/div/span/div[1]/p").text
                   self.loggertest(self.__class__.__name__,'The cow number that selected is :'+first_result)
                   #Select the first one
                   findcow.send_keys(Keys.ENTER)
                   time.sleep(7)
                   #Cow Card number that opened
                   FirstCowCard= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='span-cow-number']")))
                   firstCowCardSelected=self.driver.find_element_by_xpath(".//*[@id='span-cow-number']").text
                   self.loggertest(self.__class__.__name__,'The cow card number that actually opened :'+firstCowCardSelected)
                   #variables for Days buttons
                   DAY1= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[1]")))
                   Day1=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[1]")
                   DAY7= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[2]")))
                   Days7=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[2]")
                   DAY30= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[3]")))
                   Days30=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[3]")
                   DAY60= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[4]")))
                   Days60=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[4]")
                   DAY90= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[5]")))
                   Days90=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[5]")
                   DAY365= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='date-range']/li[6]")))
                   Days365=self.driver.find_element_by_xpath(".//*[@id='date-range']/li[6]")




                   #Date Time stamp
                   date_time=datetime.now()
                   date_time_formatted=date_time.strftime("%m/%d/%y")
                   print 'Current date stamp :'+date_time_formatted

               except NoSuchElementException:
                   self.take_screenshot("Can_not_find_Cow_card")
                   self.loggertest(self.__class__.__name__,'Could not find Cow cards of cows that started with 1XXX or 2XXX...')
                   self.fail("Problem with opening Cow Card")
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

