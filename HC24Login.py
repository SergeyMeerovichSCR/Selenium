import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
import time
import os,sys,itertools
from datetime import datetime
__author__ = 'sergey.meerovich'


class LoginTestFirefox(unittest.TestCase):
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
        self.driver.get_screenshot_as_file(dir+"/screenshots/logout_page_fail"+date_time_formatted+".png")
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
        self.loggertest(self.__class__.__name__,'Test Login_process_on_Firefox started')
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
                 self.loggertest(self.__class__.__name__,'Not found elements as email,password,btnLogin')
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
                   self.loggertest(self.__class__.__name__,'Login attrmpt failed')
                   loading_attempt=loading_attempt-1;
                   if (loading_attempt==0):
                     self.take_screenshot('login_page_not_loaded_all_elements')
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Firefox finish at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test is finished !')




    def test_Logout_process_on_Firefox(self):
         #logout from main page(dashboard)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'test logout process on Firefox started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test Firefox Log out started...')
        #if dashboardSignoutElement:
        try:
           self.search_field=self.driver.find_element_by_id("signout")
        except NoSuchElementException:
             self.take_screenshot('Fail_log_out')
             self.loggertest(self.__class__.__name__,'Sign out button not found')
             self.fail("There is no element 'signout'")
        self.search_field.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)

        try:
           self.email_field=self.driver.find_element_by_name("email")
           self.password_field=self.driver.find_element_by_name("password")
           self.btnLogin_field=self.driver.find_element_by_id("btnLogin")
        except NoSuchElementException:
             self.take_screenshot('Fail_log_out')
             self.loggertest(self.__class__.__name__,'Not exit to login page')
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
        self.loggertest(self.__class__.__name__,'Test is finished !')
        print 'Test Log out_process_on_Firefox finish at :'+date_time_formatted

    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()

class LoginTestChrome(unittest.TestCase):
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
        self.driver.get_screenshot_as_file(dir+"/screenshots/logout_page_fail"+date_time_formatted+".png")
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

    def test_Login_process_on_Chrome(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Chrome started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test Login_process_on_Chrome started')
        # get to the username field
        #check if all elements loaded:
        loading_attempt=3
        #time i let a page load
        #self.driver.implicitly_wait(5)
        #Load main page and register with username/password
        while(loading_attempt>0):
              try:
                 self.email_field=self.driver.find_element_by_name("email")
                 self.password_field=self.driver.find_element_by_name("password")
                 self.password_field=self.driver.find_element_by_id("btnLogin")
              except NoSuchElementException:
                 self.take_screenshot('Fail_Log_in')
                 self.loggertest(self.__class__.__name__,'Not located all elements as : email,password,btnLogin')
                 self.fail("There is missing elements 'email' or 'password' or 'btnLogin'")
              #self.driver.implicitly_wait(3)
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
                 self.driver.implicitly_wait(10)
                 self.loggertest(self.__class__.__name__,'Press on Login button...')
                 break
              else:
                   loading_attempt=loading_attempt-1;
                   if (loading_attempt==0):
                     self.loggertest(self.__class__.__name__,'one of login attempts failed')
                     self.take_screenshot('login_page_not_loaded_all_elements')
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
              self.take_screenshot('Fail log-out')
              self.fail("There is missing elements 'settings' or 'signout' or 'find_cow' or 'select-date' or 'note_add'")
              self.driver.implicitly_wait(3)
            headerSettingsElement=self.is_element_present(By.ID,"settings")
            headerSignoutElement=self.is_element_present(By.ID,"signout")
            headerFindCowElement=self.is_element_present(By.ID,"find_cow")
            #Check if footer is loaded
            footerTodayButton=self.is_element_present(By.ID,"select-date")
            footerNoteAddButton=self.is_element_present(By.ID,"note_add")
            if (headerSettingsElement and headerSignoutElement and headerFindCowElement and footerNoteAddButton and footerTodayButton ):
              print 'The dashboard fully loaded'
              break;
            else:
                   self.driver.implicitly_wait(3)
                   loading_attempt=loading_attempt-1;
                   if (loading_attempt==0):
                       self.take_screenshot('Dashboard_page_not_loaded_all_elements')

        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Chrome finish at :'+date_time_formatted

    def test_Logout_process_on_Chrome(self):
       #logout from main page(dashboard)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'test logout process on Chrome started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test Log out process_on_Chrome started')

        try:
           self.search_field=self.driver.find_element_by_id("signout")
        except NoSuchElementException:
             self.take_screenshot('Fail_log_out')
             self.fail("There is no element 'signout'")
        self.search_field.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        self.loggertest(self.__class__.__name__,'Click on Log out button..')

        try:
           self.email_field=self.driver.find_element_by_name("email")
           self.password_field=self.driver.find_element_by_name("password")
           self.btnLogin_field=self.driver.find_element_by_id("btnLogin")
        except NoSuchElementException:
           self.loggertest(self.__class__.__name__,'Make sure that user successfully log out and back to login page')
           self.take_screenshot('Fail_log_out')
           self.fail("There is missing elements 'email' or 'password' or 'btnLogin'")
        self.driver.implicitly_wait(3)
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
        print 'Test Log out_process_on_Chrome finish at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Finish Log out test')



    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()


class LoginTestIE(unittest.TestCase):
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

    def test_Login_process_on_IE(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_IE started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test Login_process_on_IE started')

        # get to the username field
        #check if all elements loaded:
        loading_attempt=3
        #time i let a page load
        self.driver.implicitly_wait(10)
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
                 self.driver.implicitly_wait(3)
                 break
            else:
                loading_attempt=loading_attempt-1;
                if (loading_attempt==0):
                     self.take_screenshot('login page not loaded all elements')

        loading_attempt=3
        #time i let a page load
        self.driver.implicitly_wait(10)
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
               headerSettingsElement=self.is_element_present(By.ID,"settings")
               print(headerSettingsElement)
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
                       print loading_attempt
                       self.take_screenshot('Dashboard_page_not_loaded_all_elements')
            except NoSuchElementException:
              self.take_screenshot('Fail_log_in')
              self.fail("There is missing elements 'settings' or 'signout' or 'find_cow' or 'select-date' or 'note_add'")

        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_IE finish at :'+date_time_formatted

    def test_Logout_process_on_IE(self):
       #logout from main page(dashboard)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'test logout process on IE started at :'+date_time_formatted
        self.loggertest(self.__class__.__name__,'Test Log out process_on_IE started')

        try:
           self.search_field=self.driver.find_element_by_id("signout")
        except NoSuchElementException:
             self.take_screenshot('Fail_log_out')
             self.fail("There is no element 'signout'")
        self.search_field.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        self.loggertest(self.__class__.__name__,'Click on Log out button..')

        try:
           self.email_field=self.driver.find_element_by_name("email")
           self.password_field=self.driver.find_element_by_name("password")
           self.btnLogin_field=self.driver.find_element_by_id("btnLogin")
           self.loggertest(self.__class__.__name__,'Make sure that user successfully log out and back to login page')

        except NoSuchElementException:
             self.take_screenshot('Fail_log_out')
             self.fail("There is missing elements 'email' or 'password' or 'btnLogin'")
        self.driver.implicitly_wait(3)

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
        self.loggertest(self.__class__.__name__,'Finish Log out test')

    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()


if __name__=='__main__':
    unittest.main(verbosity=2)
