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


class SwitchReportsTestFirefox(unittest.TestCase):
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
    def test_2_SwitchBetweenReports_on_Firefox(self):
        #open All Cows report on firefox
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Open Switch Between Reports_on_Firefox started at :'+date_time_formatted
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
              DistressDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Distress']")
              NoId=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='NoId']")
              GroupAlertsDatareportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='GroupAlerts']")
        except NoSuchElementException:
             self.take_screenshot("Data_Tab_not_loaded_fully")
             self.loggertest(self.__class__.__name__,'Check if Data tab loaded...')
             self.fail("The Data tab not loaded ")

        for y in range(0,20,1):
            #All Cows Report
           try:
              AllCows=self.is_element_present(By.XPATH,".//*[@id='filters']/li[1]")
              if(AllCows):
                 self.driver.implicitly_wait(30)
                 allcows=self.driver.find_element_by_xpath(".//*[@id='filters']/li[1]").click()
                 self.driver.implicitly_wait(30)
               #Select unassigned Tags
              else :
                self.loggertest(self.__class__.__name__,'All Cows button not found...')
                self.take_screenshot("All_cows_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("All_Cows_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find All Cows button or click on it...')
              self.fail("Problem with find and click on All Cows button")
              #Check if All Cows Report loaded
           try:
              CowNumber1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              CowNumber1=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              Group = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              Group=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
              DIMAge = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              DIMAge=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(30)
              ActivityChange = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              ActivityChange=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              RuminationChange = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[5]/div/span")))
              RuminationChange=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
              DailyRumination = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              DailyRumination=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              self.driver.implicitly_wait(30)
              DaysSinceLastHeat = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[7]/div/span")))
              DaysSinceLastHeat=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[7]/div/span")
              DaysSinceAI = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[8]/div/span")))
              DaysSinceAI=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[8]/div/span")
              if(CowNumber1 and Group and DIMAge and ActivityChange and RuminationChange and DailyRumination and DaysSinceLastHeat and DaysSinceAI):
                  pass
              else:
                  self.take_screenshot("All_Cows_Report_not_loaded_all_elements")
                  self.fail("Problem during load All Cows titles")
           except NoSuchElementException:
              self.take_screenshot("All_Cows_Report_not_loaded")
              self.loggertest(self.__class__.__name__,'Could not load All Cows Report...')
              self.fail("Problem during load All Cows report")
            #Heat Report
           try:
              Heat = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[2]")))
              Heat=self.is_element_present(By.XPATH,".//*[@id='filters']/li[2]")
              if(Heat):
                 heat=self.driver.find_element_by_xpath(".//*[@id='filters']/li[2]").click()
                 self.driver.implicitly_wait(30)
              else :
                self.loggertest(self.__class__.__name__,'Heat button not found...')
                self.take_screenshot("Heat_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("Heat_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find Heat button or click on it...')
              self.fail("Problem with find and click on Heat button")
            #Check if Heat Report loaded
           try:
              CowNumber2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))

              CowNumber2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              Group2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")))
              Group2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
              DIMAge2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              DIMAge2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(30)
              ActivityPeak = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              ActivityPeak=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              RuminationLow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[5]/div/span")))
              RuminationLow=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
              HoursToAI = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              HoursToAI=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              DaysSinceLastHeat2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[7]/div/span")))
              DaysSinceLastHeat2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[7]/div/span")
              self.driver.implicitly_wait(30)
              DaysSinceAI2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[8]/div/span")))
              DaysSinceAI2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[8]/div/span")
              if(CowNumber2 and Group2 and DIMAge2 and ActivityPeak and RuminationLow and HoursToAI and DaysSinceLastHeat2 and DaysSinceAI2):
                 pass
              else:
                self.take_screenshot("Heat_Report_not_loaded_all_elements")
                self.fail("Problem during load Heat titles")
           except NoSuchElementException:
              self.take_screenshot("Heat_Report_not_loaded")
              self.loggertest(self.__class__.__name__,'Could not load Heat Report...')
              self.fail("Problem during load Heat report")



            #Health Report
           try:
              Health = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[3]")))
              Health=self.is_element_present(By.XPATH,".//*[@id='filters']/li[3]")
              if(Health):
                 health=self.driver.find_element_by_xpath(".//*[@id='filters']/li[3]").click()
                 self.driver.implicitly_wait(20)
              else :
                self.loggertest(self.__class__.__name__,'Health button not found...')
                self.take_screenshot("Health_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("Health_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find Health button or click on it...')
              self.fail("Problem with find and click on Health button")
              #Check if Health Report loaded
           try:
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
              self.take_screenshot("Health_Report_not_loaded")
              self.loggertest(self.__class__.__name__,'Could not load Health Report...')
              self.fail("Problem during load Health report")

             #Distress Report
           try:
              Distress = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[4]")))
              Distress=self.is_element_present(By.XPATH,".//*[@id='filters']/li[4]")
              if(Distress):
                 distress=self.driver.find_element_by_xpath(".//*[@id='filters']/li[4]").click()
                 self.driver.implicitly_wait(30)
              else :
                self.loggertest(self.__class__.__name__,'Distress button not found...')
                self.take_screenshot("Distress_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("Distress_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find Distress button or click on it...')
              self.fail("Problem with find and click on Distress button")
             #Check if Distress Report loaded
           try:
              CowNumber4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              CowNumber4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              Group4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")))
              Group4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
              AlertType = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              AlertType=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(10)
              HoursWithoutRumination = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              HoursWithoutRumination=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              DailyRumination4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              DailyRumination4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              DaysSinceAI4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              DaysSinceAI4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              self.driver.implicitly_wait(10)
              if(CowNumber4 and Group4 and AlertType and HoursWithoutRumination and DailyRumination4 and DaysSinceAI4):
                 pass
              else:
                self.take_screenshot("Distress_Report_not_loaded_all_elements")
                self.fail("Problem during load Distress titles")
           except NoSuchElementException:
                self.take_screenshot("Distress_Report_not_loaded")
                self.loggertest(self.__class__.__name__,'Could not load Distress Report...')
                self.fail("Problem during load Distress report")


             #NOID Report
           try:
                NOID = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[5]")))
                NOID=self.is_element_present(By.XPATH,".//*[@id='filters']/li[5]")
                if(NOID):
                   NoId=self.driver.find_element_by_xpath(".//*[@id='filters']/li[5]").click()
                   self.driver.implicitly_wait(30)
                else :
                   self.loggertest(self.__class__.__name__,'NOID button not found...')
                   self.take_screenshot("NOID_button_not_found")
           except NoSuchElementException:
                 self.take_screenshot("NOID_button_not_found_or_not_clickable")
                 self.loggertest(self.__class__.__name__,'Could not find NOID button or click on it...')
                 self.fail("Problem with find and click on NOID button")
              #Check if Distress Report loaded
           try:
               CowNumber5 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
               CowNumber5=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
               self.driver.implicitly_wait(30)
               Group5 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")))
               Group5=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
               LastIDTime = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
               LastIDTime=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
               self.driver.implicitly_wait(30)
               HoursSinceLastID2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
               HoursSinceLastID2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
               if(CowNumber5 and Group5 and LastIDTime and HoursSinceLastID2):
                  self.driver.implicitly_wait(30)
                  pass
               else:
                  self.take_screenshot("NOID_Report_not_loaded_all_elements")
                  self.fail("Problem during load NOID titles")
           except NoSuchElementException:
                  self.take_screenshot("NOID_Report_not_loaded")
                  self.loggertest(self.__class__.__name__,'Could not load NOID Report...')
                  self.fail("Problem during load NOID report")

                #Group alerts Report
           try:
              GroupAlerts = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='GroupAlertsBtn']")))
              GroupAlerts=self.is_element_present(By.XPATH,".//*[@id='GroupAlertsBtn']")
              if(GroupAlerts):
                 groupalerts=self.driver.find_element_by_xpath(".//*[@id='GroupAlertsBtn']").click()
                 self.driver.implicitly_wait(30)
              else :
                self.loggertest(self.__class__.__name__,'GroupAlertsBtn button not found...')
                self.take_screenshot("GroupAlerts_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("GroupAlerts_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find GroupAlerts button or click on it...')
              self.fail("Problem with find and click on GroupAlerts button")
             #Check if GroupAlerts Report loaded
           try:
              Group7 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              Group7=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              self.driver.implicitly_wait(30)
              print "group7"
              print Group7
              NumberOfCows = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div/span")))
              NumberOfCows=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div/span")
              self.driver.implicitly_wait(30)
              print "number of cows"
              print NumberOfCows
              ActivityPeak2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              ActivityPeak2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(30)
              print "Activity Peak2"
              print ActivityPeak2
              ActivityLow3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              ActivityLow3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              self.driver.implicitly_wait(30)
              print "ActivityLow2"
              print ActivityLow3
              RuminationPeak3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[5]/div/span")))
              RuminationPeak3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
              self.driver.implicitly_wait(30)
              print "RuminationPeak3"
              print RuminationPeak3
              RuminationLow4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              RuminationLow4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              self.driver.implicitly_wait(30)
              print "RuminationLow4"
              print RuminationLow4
              DailyRumination5 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[7]/div/span")))
              DailyRumination5=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[7]/div/span")
              self.driver.implicitly_wait(30)
              print  "DailyRumination5"
              print DailyRumination5
              if(Group7 and NumberOfCows and ActivityPeak2 and ActivityLow3 and RuminationPeak3 and RuminationLow4 and DailyRumination5):
                  pass
              else:
                 self.take_screenshot("GroupAlerts_Report_not_loaded_all_elements")
                 self.fail("Problem during load GroupAlerts titles")
           except NoSuchElementException:
                self.take_screenshot("GroupAlerts_Report_not_loaded")
                self.loggertest(self.__class__.__name__,'Could not load GroupAlerts Report...')
                self.fail("Problem during load Groupalerts report")
        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch between Reports_on_Firefox finish at :'+date_time_formatted
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





class SwitchReportsTestChrome(unittest.TestCase):
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
    def test_2_SwitchBetweenReports_on_Chrome(self):
        #open All Cows report on firefox
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Open Switch Between Reports_on_Chrome started at :'+date_time_formatted
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
              DistressDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Distress']")
              NoId=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='NoId']")
              GroupAlertsDatareportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='GroupAlerts']")
        except NoSuchElementException:
             self.take_screenshot("Data_Tab_not_loaded_fully")
             self.loggertest(self.__class__.__name__,'Check if Data tab loaded...')
             self.fail("The Data tab not loaded ")

        for y in range(0,20,1):
            #All Cows Report
           try:
              AllCows=self.is_element_present(By.XPATH,".//*[@id='filters']/li[1]")
              if(AllCows):
                 self.driver.implicitly_wait(30)
                 allcows=self.driver.find_element_by_xpath(".//*[@id='filters']/li[1]").click()
                 self.driver.implicitly_wait(30)
               #Select unassigned Tags
              else :
                self.loggertest(self.__class__.__name__,'All Cows button not found...')
                self.take_screenshot("All_cows_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("All_Cows_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find All Cows button or click on it...')
              self.fail("Problem with find and click on All Cows button")
              #Check if All Cows Report loaded
           try:
              time.sleep(1)
              CowNumber1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              CowNumber1=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              Group = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              Group=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
              DIMAge = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              DIMAge=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(30)
              ActivityChange = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              ActivityChange=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              self.driver.implicitly_wait(30)
              RuminationChange = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[5]/div/span")))
              RuminationChange=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
              self.driver.implicitly_wait(30)
              time.sleep(1)
              DailyRumination = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              DailyRumination=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              self.driver.implicitly_wait(30)
              DaysSinceLastHeat = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[7]/div/span")))
              DaysSinceLastHeat=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[7]/div/span")
              self.driver.implicitly_wait(30)
              DaysSinceAI = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[8]/div/span")))
              DaysSinceAI=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[8]/div/span")
              if(CowNumber1 and Group and DIMAge and ActivityChange and RuminationChange and DailyRumination and DaysSinceLastHeat and DaysSinceAI):
                  pass
              else:
                  self.take_screenshot("All_Cows_Report_not_loaded_all_elements")
                  self.fail("Problem during load All Cows titles")
           except NoSuchElementException:
              self.take_screenshot("All_Cows_Report_not_loaded")
              self.loggertest(self.__class__.__name__,'Could not load All Cows Report...')
              self.fail("Problem during load All Cows report")
            #Heat Report
           try:
              Heat = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[2]")))
              Heat=self.is_element_present(By.XPATH,".//*[@id='filters']/li[2]")
              if(Heat):
                 heat=self.driver.find_element_by_xpath(".//*[@id='filters']/li[2]").click()
                 self.driver.implicitly_wait(30)
              else :
                self.loggertest(self.__class__.__name__,'Heat button not found...')
                self.take_screenshot("Heat_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("Heat_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find Heat button or click on it...')
              self.fail("Problem with find and click on Heat button")
            #Check if Heat Report loaded
           try:
              time.sleep(1)
              CowNumber2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              CowNumber2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              Group2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")))
              Group2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
              DIMAge2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              DIMAge2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(30)
              ActivityPeak = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              ActivityPeak=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              RuminationLow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[5]/div/span")))
              RuminationLow=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
              HoursToAI = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              HoursToAI=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              DaysSinceLastHeat2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[7]/div/span")))
              DaysSinceLastHeat2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[7]/div/span")
              self.driver.implicitly_wait(30)
              DaysSinceAI2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[8]/div/span")))
              DaysSinceAI2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[8]/div/span")
              if(CowNumber2 and Group2 and DIMAge2 and ActivityPeak and RuminationLow and HoursToAI and DaysSinceLastHeat2 and DaysSinceAI2):
                 pass
              else:
                self.take_screenshot("Heat_Report_not_loaded_all_elements")
                self.fail("Problem during load Heat titles")
           except NoSuchElementException:
              self.take_screenshot("Heat_Report_not_loaded")
              self.loggertest(self.__class__.__name__,'Could not load Heat Report...')
              self.fail("Problem during load Heat report")



            #Health Report
           try:
              Health = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[3]")))
              Health=self.is_element_present(By.XPATH,".//*[@id='filters']/li[3]")
              if(Health):
                 health=self.driver.find_element_by_xpath(".//*[@id='filters']/li[3]").click()
                 self.driver.implicitly_wait(20)
              else :
                self.loggertest(self.__class__.__name__,'Health button not found...')
                self.take_screenshot("Health_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("Health_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find Health button or click on it...')
              self.fail("Problem with find and click on Health button")
              #Check if Health Report loaded
           try:
              time.sleep(1)
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
              self.take_screenshot("Health_Report_not_loaded")
              self.loggertest(self.__class__.__name__,'Could not load Health Report...')
              self.fail("Problem during load Health report")

             #Distress Report
           try:
              Distress = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[4]")))
              Distress=self.is_element_present(By.XPATH,".//*[@id='filters']/li[4]")
              if(Distress):
                 distress=self.driver.find_element_by_xpath(".//*[@id='filters']/li[4]").click()
                 self.driver.implicitly_wait(30)
              else :
                self.loggertest(self.__class__.__name__,'Distress button not found...')
                self.take_screenshot("Distress_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("Distress_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find Distress button or click on it...')
              self.fail("Problem with find and click on Distress button")
             #Check if Distress Report loaded
           try:
              time.sleep(1)
              CowNumber4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              CowNumber4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              Group4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")))
              Group4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
              AlertType = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              AlertType=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(10)
              HoursWithoutRumination = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              HoursWithoutRumination=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              DailyRumination4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              DailyRumination4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              DaysSinceAI4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              DaysSinceAI4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              self.driver.implicitly_wait(10)
              if(CowNumber4 and Group4 and AlertType and HoursWithoutRumination and DailyRumination4 and DaysSinceAI4):
                 pass
              else:
                self.take_screenshot("Distress_Report_not_loaded_all_elements")
                self.fail("Problem during load Distress titles")
           except NoSuchElementException:
                self.take_screenshot("Distress_Report_not_loaded")
                self.loggertest(self.__class__.__name__,'Could not load Distress Report...')
                self.fail("Problem during load Distress report")


             #NOID Report
           try:
                NOID = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[5]")))
                NOID=self.is_element_present(By.XPATH,".//*[@id='filters']/li[5]")
                if(NOID):
                   NoId=self.driver.find_element_by_xpath(".//*[@id='filters']/li[5]").click()
                   self.driver.implicitly_wait(30)
                else :
                   self.loggertest(self.__class__.__name__,'NOID button not found...')
                   self.take_screenshot("NOID_button_not_found")
           except NoSuchElementException:
                 self.take_screenshot("NOID_button_not_found_or_not_clickable")
                 self.loggertest(self.__class__.__name__,'Could not find NOID button or click on it...')
                 self.fail("Problem with find and click on NOID button")
              #Check if Distress Report loaded
           try:
               time.sleep(1)
               CowNumber5 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
               CowNumber5=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
               self.driver.implicitly_wait(30)
               Group5 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")))
               Group5=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
               LastIDTime = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
               LastIDTime=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
               self.driver.implicitly_wait(30)
               HoursSinceLastID2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
               HoursSinceLastID2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
               if(CowNumber5 and Group5 and LastIDTime and HoursSinceLastID2):
                  self.driver.implicitly_wait(30)
                  pass
               else:
                  self.take_screenshot("NOID_Report_not_loaded_all_elements")
                  self.fail("Problem during load NOID titles")
           except NoSuchElementException:
                  self.take_screenshot("NOID_Report_not_loaded")
                  self.loggertest(self.__class__.__name__,'Could not load NOID Report...')
                  self.fail("Problem during load NOID report")

                #Group alerts Report
           try:
              GroupAlerts = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='GroupAlertsBtn']")))
              GroupAlerts=self.is_element_present(By.XPATH,".//*[@id='GroupAlertsBtn']")
              if(GroupAlerts):
                 groupalerts=self.driver.find_element_by_xpath(".//*[@id='GroupAlertsBtn']").click()
                 self.driver.implicitly_wait(30)
              else :
                self.loggertest(self.__class__.__name__,'GroupAlertsBtn button not found...')
                self.take_screenshot("GroupAlerts_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("GroupAlerts_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find GroupAlerts button or click on it...')
              self.fail("Problem with find and click on GroupAlerts button")
             #Check if GroupAlerts Report loaded
           try:
              time.sleep(1)
              Group7 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              Group7=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              self.driver.implicitly_wait(30)
              print "group7"
              print Group7
              NumberOfCows = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div/span")))
              NumberOfCows=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div/span")
              self.driver.implicitly_wait(30)
              print "number of cows"
              print NumberOfCows
              ActivityPeak2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              ActivityPeak2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(30)
              print "Activity Peak2"
              print ActivityPeak2
              ActivityLow3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              ActivityLow3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              self.driver.implicitly_wait(30)
              print "ActivityLow2"
              print ActivityLow3
              RuminationPeak3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[5]/div/span")))
              RuminationPeak3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
              self.driver.implicitly_wait(30)
              print "RuminationPeak3"
              print RuminationPeak3
              RuminationLow4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              RuminationLow4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              self.driver.implicitly_wait(30)
              print "RuminationLow4"
              print RuminationLow4
              DailyRumination5 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[7]/div/span")))
              DailyRumination5=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[7]/div/span")
              self.driver.implicitly_wait(30)
              print  "DailyRumination5"
              print DailyRumination5
              if(Group7 and NumberOfCows and ActivityPeak2 and ActivityLow3 and RuminationPeak3 and RuminationLow4 and DailyRumination5):
                  pass
              else:
                 self.take_screenshot("GroupAlerts_Report_not_loaded_all_elements")
                 self.fail("Problem during load GroupAlerts titles")
           except NoSuchElementException:
                self.take_screenshot("GroupAlerts_Report_not_loaded")
                self.loggertest(self.__class__.__name__,'Could not load GroupAlerts Report...')
                self.fail("Problem during load Groupalerts report")
        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch between Reports_on_Chrome finish at :'+date_time_formatted
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

class SwitchReportsTestIE(unittest.TestCase):
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

    def test_2_SwitchBetweenReports_on_IE(self):
        #open All Cows report on firefox
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Open Switch Between Reports_on_IE started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Open All Cows Report on IE started...')
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
              DistressDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Distress']")
              NoId=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='NoId']")
              GroupAlertsDatareportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='GroupAlerts']")
        except NoSuchElementException:
             self.take_screenshot("Data_Tab_not_loaded_fully")
             self.loggertest(self.__class__.__name__,'Check if Data tab loaded...')
             self.fail("The Data tab not loaded ")

        for y in range(0,20,1):
            #All Cows Report
           try:
              AllCows=self.is_element_present(By.XPATH,".//*[@id='filters']/li[1]")
              if(AllCows):
                 self.driver.implicitly_wait(30)
                 allcows=self.driver.find_element_by_xpath(".//*[@id='filters']/li[1]").click()
                 self.driver.implicitly_wait(30)
               #Select unassigned Tags
              else :
                self.loggertest(self.__class__.__name__,'All Cows button not found...')
                self.take_screenshot("All_cows_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("All_Cows_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find All Cows button or click on it...')
              self.fail("Problem with find and click on All Cows button")
              #Check if All Cows Report loaded
           try:
              CowNumber1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              CowNumber1=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              Group = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              Group=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
              DIMAge = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              DIMAge=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(30)
              ActivityChange = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              ActivityChange=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              RuminationChange = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[5]/div/span")))
              RuminationChange=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
              DailyRumination = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              DailyRumination=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              self.driver.implicitly_wait(30)
              DaysSinceLastHeat = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[7]/div/span")))
              DaysSinceLastHeat=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[7]/div/span")
              DaysSinceAI = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[8]/div/span")))
              DaysSinceAI=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[8]/div/span")
              if(CowNumber1 and Group and DIMAge and ActivityChange and RuminationChange and DailyRumination and DaysSinceLastHeat and DaysSinceAI):
                  pass
              else:
                  self.take_screenshot("All_Cows_Report_not_loaded_all_elements")
                  self.fail("Problem during load All Cows titles")
           except NoSuchElementException:
              self.take_screenshot("All_Cows_Report_not_loaded")
              self.loggertest(self.__class__.__name__,'Could not load All Cows Report...')
              self.fail("Problem during load All Cows report")
            #Heat Report
           try:
              Heat = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[2]")))
              Heat=self.is_element_present(By.XPATH,".//*[@id='filters']/li[2]")
              if(Heat):
                 heat=self.driver.find_element_by_xpath(".//*[@id='filters']/li[2]").click()
                 self.driver.implicitly_wait(30)
              else :
                self.loggertest(self.__class__.__name__,'Heat button not found...')
                self.take_screenshot("Heat_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("Heat_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find Heat button or click on it...')
              self.fail("Problem with find and click on Heat button")
            #Check if Heat Report loaded
           try:
              CowNumber2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))

              CowNumber2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              Group2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")))
              Group2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
              DIMAge2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              DIMAge2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(30)
              ActivityPeak = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              ActivityPeak=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              RuminationLow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[5]/div/span")))
              RuminationLow=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
              HoursToAI = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              HoursToAI=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              DaysSinceLastHeat2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[7]/div/span")))
              DaysSinceLastHeat2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[7]/div/span")
              self.driver.implicitly_wait(30)
              DaysSinceAI2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[8]/div/span")))
              DaysSinceAI2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[8]/div/span")
              if(CowNumber2 and Group2 and DIMAge2 and ActivityPeak and RuminationLow and HoursToAI and DaysSinceLastHeat2 and DaysSinceAI2):
                 pass
              else:
                self.take_screenshot("Heat_Report_not_loaded_all_elements")
                self.fail("Problem during load Heat titles")
           except NoSuchElementException:
              self.take_screenshot("Heat_Report_not_loaded")
              self.loggertest(self.__class__.__name__,'Could not load Heat Report...')
              self.fail("Problem during load Heat report")



            #Health Report
           try:
              Health = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[3]")))
              Health=self.is_element_present(By.XPATH,".//*[@id='filters']/li[3]")
              if(Health):
                 health=self.driver.find_element_by_xpath(".//*[@id='filters']/li[3]").click()
                 self.driver.implicitly_wait(20)
              else :
                self.loggertest(self.__class__.__name__,'Health button not found...')
                self.take_screenshot("Health_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("Health_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find Health button or click on it...')
              self.fail("Problem with find and click on Health button")
              #Check if Health Report loaded
           try:
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
              self.take_screenshot("Health_Report_not_loaded")
              self.loggertest(self.__class__.__name__,'Could not load Health Report...')
              self.fail("Problem during load Health report")

             #Distress Report
           try:
              Distress = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[4]")))
              Distress=self.is_element_present(By.XPATH,".//*[@id='filters']/li[4]")
              if(Distress):
                 distress=self.driver.find_element_by_xpath(".//*[@id='filters']/li[4]").click()
                 self.driver.implicitly_wait(30)
              else :
                self.loggertest(self.__class__.__name__,'Distress button not found...')
                self.take_screenshot("Distress_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("Distress_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find Distress button or click on it...')
              self.fail("Problem with find and click on Distress button")
             #Check if Distress Report loaded
           try:
              CowNumber4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              CowNumber4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              Group4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")))
              Group4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
              AlertType = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              AlertType=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(10)
              HoursWithoutRumination = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              HoursWithoutRumination=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              DailyRumination4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              DailyRumination4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              DaysSinceAI4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              DaysSinceAI4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              self.driver.implicitly_wait(10)
              if(CowNumber4 and Group4 and AlertType and HoursWithoutRumination and DailyRumination4 and DaysSinceAI4):
                 pass
              else:
                self.take_screenshot("Distress_Report_not_loaded_all_elements")
                self.fail("Problem during load Distress titles")
           except NoSuchElementException:
                self.take_screenshot("Distress_Report_not_loaded")
                self.loggertest(self.__class__.__name__,'Could not load Distress Report...')
                self.fail("Problem during load Distress report")


             #NOID Report
           try:
                NOID = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='filters']/li[5]")))
                NOID=self.is_element_present(By.XPATH,".//*[@id='filters']/li[5]")
                if(NOID):
                   NoId=self.driver.find_element_by_xpath(".//*[@id='filters']/li[5]").click()
                   self.driver.implicitly_wait(30)
                else :
                   self.loggertest(self.__class__.__name__,'NOID button not found...')
                   self.take_screenshot("NOID_button_not_found")
           except NoSuchElementException:
                 self.take_screenshot("NOID_button_not_found_or_not_clickable")
                 self.loggertest(self.__class__.__name__,'Could not find NOID button or click on it...')
                 self.fail("Problem with find and click on NOID button")
              #Check if Distress Report loaded
           try:
               CowNumber5 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
               CowNumber5=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
               self.driver.implicitly_wait(30)
               Group5 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")))
               Group5=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div[2]/span")
               LastIDTime = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
               LastIDTime=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
               self.driver.implicitly_wait(30)
               HoursSinceLastID2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
               HoursSinceLastID2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
               if(CowNumber5 and Group5 and LastIDTime and HoursSinceLastID2):
                  self.driver.implicitly_wait(30)
                  pass
               else:
                  self.take_screenshot("NOID_Report_not_loaded_all_elements")
                  self.fail("Problem during load NOID titles")
           except NoSuchElementException:
                  self.take_screenshot("NOID_Report_not_loaded")
                  self.loggertest(self.__class__.__name__,'Could not load NOID Report...')
                  self.fail("Problem during load NOID report")

                #Group alerts Report
           try:
              GroupAlerts = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='GroupAlertsBtn']")))
              GroupAlerts=self.is_element_present(By.XPATH,".//*[@id='GroupAlertsBtn']")
              if(GroupAlerts):
                 groupalerts=self.driver.find_element_by_xpath(".//*[@id='GroupAlertsBtn']").click()
                 self.driver.implicitly_wait(30)
              else :
                self.loggertest(self.__class__.__name__,'GroupAlertsBtn button not found...')
                self.take_screenshot("GroupAlerts_button_not_found")
           except NoSuchElementException:
              self.take_screenshot("GroupAlerts_button_not_found_or_not_clickable")
              self.loggertest(self.__class__.__name__,'Could not find GroupAlerts button or click on it...')
              self.fail("Problem with find and click on GroupAlerts button")
             #Check if GroupAlerts Report loaded
           try:
              Group7 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[1]/div/span")))
              Group7=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[1]/div/span")
              self.driver.implicitly_wait(30)
              print "group7"
              print Group7
              NumberOfCows = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[2]/div/span")))
              NumberOfCows=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[2]/div/span")
              self.driver.implicitly_wait(30)
              print "number of cows"
              print NumberOfCows
              ActivityPeak2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[3]/div/span")))
              ActivityPeak2=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[3]/div/span")
              self.driver.implicitly_wait(30)
              print "Activity Peak2"
              print ActivityPeak2
              ActivityLow3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[4]/div/span")))
              ActivityLow3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[4]/div/span")
              self.driver.implicitly_wait(30)
              print "ActivityLow2"
              print ActivityLow3
              RuminationPeak3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[5]/div/span")))
              RuminationPeak3=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[5]/div/span")
              self.driver.implicitly_wait(30)
              print "RuminationPeak3"
              print RuminationPeak3
              RuminationLow4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[6]/div/span")))
              RuminationLow4=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[6]/div/span")
              self.driver.implicitly_wait(30)
              print "RuminationLow4"
              print RuminationLow4
              DailyRumination5 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='list_data']/table/thead/tr/th[7]/div/span")))
              DailyRumination5=self.is_element_present(By.XPATH,".//*[@id='list_data']/table/thead/tr/th[7]/div/span")
              self.driver.implicitly_wait(30)
              print  "DailyRumination5"
              print DailyRumination5
              if(Group7 and NumberOfCows and ActivityPeak2 and ActivityLow3 and RuminationPeak3 and RuminationLow4 and DailyRumination5):
                  pass
              else:
                 self.take_screenshot("GroupAlerts_Report_not_loaded_all_elements")
                 self.fail("Problem during load GroupAlerts titles")
           except NoSuchElementException:
                self.take_screenshot("GroupAlerts_Report_not_loaded")
                self.loggertest(self.__class__.__name__,'Could not load GroupAlerts Report...')
                self.fail("Problem during load Groupalerts report")
        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch between Reports_on_IE finish at :'+date_time_formatted
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
