import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
import time
import os
#use for loging console
import logging

from datetime import datetime
__author__ = 'sergey.meerovich'


class FarmTrendsSwitchFirefox(unittest.TestCase):
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

    def test_2_Switch_Farm_Trends(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch Farm Trends on_Firefox started at :'+date_time_formatted
        for x in range(0,10,1):
         try:
           #check that you located on Dashboard
           dashboard_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='dashboard-tab']/a")
           DASHBOARD_EL=self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='dashboard-tab']/a"))
           lastUpdate_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[@class='statistics']/div[@class='last-update']/span")
           #Check if Last update label is present
           self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[@class='statistics']/div[@class='last-update']/span")),"Not located on Dashboard")
           #Heard Health Compasses view
           self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[@class='statistics']/div[3]/div[@class='span4']/div[@class='basicgaugemain']/ul/li[@class='basicgaugecontainer']/div[@id='check']/*[local-name()='svg' and namespace-uri()='http://www.w3.org/2000/svg']")),"Not located on Dashboard")
         except NoSuchElementException:
           self.take_screenshot('Not_located_at_Dashboard')
           self.loggertest(self.__class__.__name__,'Not Located at Dashboard...')
           self.fail("There is missing element 'dashboard-tab'")
         #Detect Health/Heat/Rumination tab-link buttons
         healthtrend=self.is_element_present(By.XPATH,".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[1]/a")
         heattrend=self.is_element_present(By.XPATH,".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[2]/a")
         ruminationtrend=self.is_element_present(By.XPATH,".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[3]/a")
         #print "Healthtrend :"+str(healthtrend)
         #print "Heattrend :"+str(heattrend)
         #print "Ruminationtrend :"+str(ruminationtrend)
         if (healthtrend and heattrend and ruminationtrend):
           #switch to heat trend graph
           heattrend=self.driver.find_element_by_xpath(".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[2]/a")
           heattrend.click()
           time.sleep(1)
           #check if it actually switched
           h=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='dashboard-pane']/div[@class='trends']/div[2]/div[@class='tab-content']/div[@id='trend-heat']/div[1]/div[2]/div[@id='heat_graph']/div[1]/*[name()='svg']/*[name()='g']")
           nodes = self.driver.find_elements_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='dashboard-pane']/div[@class='trends']/div[2]/div[@class='tab-content']/div[@id='trend-heat']/div[1]/div[2]/div[@id='heat_graph']/div[1]/*[name()='svg']/*[name()='g']")
           #nodes2=self.driver.find_elements_by_xpath("//g[@class='g'# ]")
           html_source=self.driver.page_source
           if "Heat Rate Performance" in html_source:
               print "Heat Farm Trend loaded"
           else:
               print "Not load Heat Farm Trend"
           #switch to Rumination trend
           RuminationTrend=self.driver.find_element_by_xpath(".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[3]/a")
           RuminationTrend.click()
           time.sleep(1)
           html_source=self.driver.page_source
           if "Daily Rumination" in html_source:
               print "Daily Rumination Farm Trend loaded"
           else:
               print "Not load Daily Rumination Farm Trend"
           #switch to Health Trend
           HealthTrend=self.driver.find_element_by_xpath(".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[1]/a")
           HealthTrend.click()
           time.sleep(1)
           html_source=self.driver.page_source
           if "Healthy" in html_source:
               print "Health Farm Trend loaded"
           else:
               print "Not load Health Farm Trend"
         else:
              self.take_screenshot('Problem_locate_farm_trends')
              self.loggertest(self.__class__.__name__,'Can not focus on farm trends tabs')
              self.fail("There is missing elements of Health,heat,rumination farm trends")


        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch_Farm_Trends_on_Firefox finish at :'+date_time_formatted

    def test_4_Logout_process_on_Firefox(self):
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


class FarmTrendsSwitchChrome(unittest.TestCase):
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
        #self.driver.get_screenshot_as_file(dir+"/screenshots/logout_page_fail"+date_time_formatted+".png")
        #
        #logging.basicConfig(filename=(dir+"/ConsoleLogs"+TestName+browserType+".log"),level=logging.INFO)



    def test_1_Login_process_on_Chrome(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Chrome started at :'+date_time_formatted
        # get to the username field
        #check if all elements loaded:
        loading_attempt=3
        #time i let a page load
        time.sleep(10)
        #Load main page and register with username/password
        while(loading_attempt>0):
              try:
                 self.email_field=self.driver.find_element_by_name("email")
                 self.password_field=self.driver.find_element_by_name("password")
                 self.password_field=self.driver.find_element_by_id("btnLogin")
              except NoSuchElementException:
                 self.take_screenshot('Fai_log_in')
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
                   time.sleep(3)
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
              self.take_screenshot('Fail_log_out')
              self.fail("There is missing elements 'settings' or 'signout' or 'find_cow' or 'select-date' or 'note_add'")
             time.sleep(3)
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
    def test_2_Switch_Farm_Trends(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch Farm Trends on_Firefox started at :'+date_time_formatted
        for x in range(0,10,1):
         try:
           #check that you located on Dashboard
           dashboard_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='dashboard-tab']/a")
           DASHBOARD_EL=self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='dashboard-tab']/a"))
           lastUpdate_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[@class='statistics']/div[@class='last-update']/span")
           #Check if Last update label is present
           self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[@class='statistics']/div[@class='last-update']/span")),"Not located on Dashboard")
           #Heard Health Compasses view
           self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[@class='statistics']/div[3]/div[@class='span4']/div[@class='basicgaugemain']/ul/li[@class='basicgaugecontainer']/div[@id='check']/*[local-name()='svg' and namespace-uri()='http://www.w3.org/2000/svg']")),"Not located on Dashboard")
         except NoSuchElementException:
           self.take_screenshot('Not_located_at_Dashboard')
           self.loggertest(self.__class__.__name__,'Not Located at Dashboard...')
           self.fail("There is missing element 'dashboard-tab'")
         #Detect Health/Heat/Rumination tab-link buttons
         healthtrend=self.is_element_present(By.XPATH,".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[1]/a")
         heattrend=self.is_element_present(By.XPATH,".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[2]/a")
         ruminationtrend=self.is_element_present(By.XPATH,".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[3]/a")
         #print "Healthtrend :"+str(healthtrend)
         #print "Heattrend :"+str(heattrend)
         #print "Ruminationtrend :"+str(ruminationtrend)
         if (healthtrend and heattrend and ruminationtrend):
           #switch to heat trend graph
           heattrend=self.driver.find_element_by_xpath(".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[2]/a")
           heattrend.click()
           time.sleep(1)
           #check if it actually switched
           h=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='dashboard-pane']/div[@class='trends']/div[2]/div[@class='tab-content']/div[@id='trend-heat']/div[1]/div[2]/div[@id='heat_graph']/div[1]/*[name()='svg']/*[name()='g']")
           nodes = self.driver.find_elements_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='dashboard-pane']/div[@class='trends']/div[2]/div[@class='tab-content']/div[@id='trend-heat']/div[1]/div[2]/div[@id='heat_graph']/div[1]/*[name()='svg']/*[name()='g']")
           #nodes2=self.driver.find_elements_by_xpath("//g[@class='g'# ]")
           html_source=self.driver.page_source
           if "Heat Rate Performance" in html_source:
               print "Heat Farm Trend loaded"
           else:
               print "Not load Heat Farm Trend"
           #switch to Rumination trend
           RuminationTrend=self.driver.find_element_by_xpath(".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[3]/a")
           RuminationTrend.click()
           time.sleep(1)
           html_source=self.driver.page_source
           if "Daily Rumination" in html_source:
               print "Daily Rumination Farm Trend loaded"
           else:
               print "Not load Daily Rumination Farm Trend"
           #switch to Health Trend
           HealthTrend=self.driver.find_element_by_xpath(".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[1]/a")
           HealthTrend.click()
           time.sleep(1)
           html_source=self.driver.page_source
           if "Healthy" in html_source:
               print "Health Farm Trend loaded"
           else:
               print "Not load Health Farm Trend"
         else:
              self.take_screenshot('Problem_locate_farm_trends')
              self.loggertest(self.__class__.__name__,'Can not focus on farm trends tabs')
              self.fail("There is missing elements of Health,heat,rumination farm trends")


        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch_Farm_Trends_on_Firefox finish at :'+date_time_formatted
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
        time.sleep(3)

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



class FarmTrendsSwitchIE(unittest.TestCase):
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
        self.driver.get_screenshot_as_file(dir+"/screenshots/logout_page_fail"+date_time_formatted+".png")
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



    def test_1_Login_process_on_IE(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_IE started at :'+date_time_formatted
        # get to the username field
        #check if all elements loaded:
        loading_attempt=3
        #time i let a page load
        time.sleep(10)
        #Load main page and register with username/password
        while(loading_attempt>0):
            try:
                   self.email_field=self.driver.find_element_by_name("email")
                   self.signout_field=self.driver.find_element_by_name("password")
                   self.find_cow_field=self.driver.find_element_by_id("btnLogin")
            except NoSuchElementException:
                   self.take_screenshot('Fail log-out')
                   self.fail("There is missing elements 'email' or 'password' or 'btnLogin'")
            time.sleep(3)
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
                time.sleep(3)
                loading_attempt=loading_attempt-1;
                if (loading_attempt==0):
                     self.take_screenshot('login page not loaded all elements')

        loading_attempt=3
        #time i let a page load
        time.sleep(3)
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
              self.take_screenshot('Fail log-out')
              self.fail("There is missing elements 'settings' or 'signout' or 'find_cow' or 'select-date' or 'note_add'")
            time.sleep(3)

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
                   time.sleep(3)
                   loading_attempt=loading_attempt-1;
                   if (loading_attempt==0):
                       print loading_attempt
                       self.take_screenshot('Dashboard page not loaded all elements')

        print "Test running time:"+str((date_time.now()-date_time))
    def test_2_Switch_Farm_Trends(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch Farm Trends on_Firefox started at :'+date_time_formatted
        for x in range(0,10,1):
         try:
           #check that you located on Dashboard
           dashboard_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='dashboard-tab']/a")
           DASHBOARD_EL=self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/ul/li[@id='dashboard-tab']/a"))
           lastUpdate_el=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[@class='statistics']/div[@class='last-update']/span")
           #Check if Last update label is present
           self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[@class='statistics']/div[@class='last-update']/span")),"Not located on Dashboard")
           #Heard Health Compasses view
           self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[@class='statistics']/div[3]/div[@class='span4']/div[@class='basicgaugemain']/ul/li[@class='basicgaugecontainer']/div[@id='check']/*[local-name()='svg' and namespace-uri()='http://www.w3.org/2000/svg']")),"Not located on Dashboard")
         except NoSuchElementException:
           self.take_screenshot('Not_located_at_Dashboard')
           self.loggertest(self.__class__.__name__,'Not Located at Dashboard...')
           self.fail("There is missing element 'dashboard-tab'")
         #Detect Health/Heat/Rumination tab-link buttons
         healthtrend=self.is_element_present(By.XPATH,".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[1]/a")
         heattrend=self.is_element_present(By.XPATH,".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[2]/a")
         ruminationtrend=self.is_element_present(By.XPATH,".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[3]/a")
         #print "Healthtrend :"+str(healthtrend)
         #print "Heattrend :"+str(heattrend)
         #print "Ruminationtrend :"+str(ruminationtrend)
         if (healthtrend and heattrend and ruminationtrend):
           #switch to heat trend graph
           heattrend=self.driver.find_element_by_xpath(".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[2]/a")
           heattrend.click()
           time.sleep(1)
           #check if it actually switched
           h=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='dashboard-pane']/div[@class='trends']/div[2]/div[@class='tab-content']/div[@id='trend-heat']/div[1]/div[2]/div[@id='heat_graph']/div[1]/*[name()='svg']/*[name()='g']")
           nodes = self.driver.find_elements_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='dashboard-pane']/div[@class='trends']/div[2]/div[@class='tab-content']/div[@id='trend-heat']/div[1]/div[2]/div[@id='heat_graph']/div[1]/*[name()='svg']/*[name()='g']")
           #nodes2=self.driver.find_elements_by_xpath("//g[@class='g'# ]")
           html_source=self.driver.page_source
           if "Heat Rate Performance" in html_source:
               print "Heat Farm Trend loaded"
           else:
               print "Not load Heat Farm Trend"
           #switch to Rumination trend
           RuminationTrend=self.driver.find_element_by_xpath(".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[3]/a")
           RuminationTrend.click()
           time.sleep(1)
           html_source=self.driver.page_source
           if "Daily Rumination" in html_source:
               print "Daily Rumination Farm Trend loaded"
           else:
               print "Not load Daily Rumination Farm Trend"
           #switch to Health Trend
           HealthTrend=self.driver.find_element_by_xpath(".//*[@id='dashboard-pane']/div[2]/div[2]/ul/li[1]/a")
           HealthTrend.click()
           time.sleep(1)
           html_source=self.driver.page_source
           if "Healthy" in html_source:
               print "Health Farm Trend loaded"
           else:
               print "Not load Health Farm Trend"
         else:
              self.take_screenshot('Problem_locate_farm_trends')
              self.loggertest(self.__class__.__name__,'Can not focus on farm trends tabs')
              self.fail("There is missing elements of Health,heat,rumination farm trends")


        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch_Farm_Trends_on_Firefox finish at :'+date_time_formatted
    def test_3_Logout_process_on_IE(self):
       #logout from main page(dashboard)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'test logout process on IE started at :'+date_time_formatted
        try:
           self.search_field=self.driver.find_element_by_id("signout")
        except NoSuchElementException:
             self.take_screenshot('Fail log-out')
             self.fail("There is no element 'signout'")
        self.search_field.send_keys(Keys.ENTER)
        time.sleep(3)

        try:
           self.email_field=self.driver.find_element_by_name("email")
           self.password_field=self.driver.find_element_by_name("password")
           self.btnLogin_field=self.driver.find_element_by_id("btnLogin")
        except NoSuchElementException:
             self.take_screenshot('Fail log-out')
             self.fail("There is missing elements 'email' or 'password' or 'btnLogin'")
        time.sleep(3)

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


