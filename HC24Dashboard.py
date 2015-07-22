import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
import time
import os
from datetime import datetime
#Import Login/Logout testcase
from HC24Login import LoginTestFirefox
from HC24Login import LoginTestChrome
from HC24Login import LoginTestIE
__author__ = 'sergey.meerovich'


class LoginTesFirefox(unittest.TestCase):
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


    def test_Login_process_on_Firefox(self):
        #date_time= time.strftime("%d/%m/%%Y  %I:%M:%:S")
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Firefox started at :'+date_time_formatted
        # get to the username field
        #check if all elements loaded:
        loading_attempt=3
        #time i let a page load
        time.sleep(10)
        #Load main page and register with username/password
        while(loading_attempt>0):
              EmailElement=self.is_element_present(By.NAME,"email")
              PasswordElement=self.is_element_present(By.NAME,"password")
              LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
              if (EmailElement and PasswordElement and LoginBtnElement):
                 self.username_field=self.driver.find_element_by_name('email')
                 self.username_field.send_keys('scrtesting@yahoo.com')
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
                  print 'Login page not loaded all elements'
                  #take a screenshoot of main page after login
                  date_time=datetime.now()
                  date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
                  self.driver.get_screenshot_as_file("login_page_fail"+date_time_formatted+".png")
                  self.fail("Login page not loaded all elements")

        loading_attempt=3
        #time i let a page load
        time.sleep(3)
        #Load main page and register with username/password
        while(loading_attempt>0):
              #check if user successfully login on page https://hc24-qalab-web.scrdairy.com/#dashboard/
              #check if headers exist
              headerSettingsElement=self.is_element_present(By.ID,"setting")
              headerSignoutElement=self.is_element_present(By.ID,"signout")
              headerFindCowElement=self.is_element_present(By.ID,"find_cow")

              #Check if footer is loaded
              footerTodayButton=self.is_element_present(By.ID,"select-date")
              footerNoteAddButton=self.is_element_present(By.ID,"note_add")
              self.assertTrue(True,headerSettingsElement)
              self.assertTrue(True,headerSignoutElement)



              if (headerSettingsElement and headerSignoutElement and headerFindCowElement and footerNoteAddButton and footerTodayButton ):
                 print 'The dashboard fully loaded'
                 break
              else:
                   time.sleep(3)
                   loading_attempt=loading_attempt-1;
              if (loading_attempt==0):
                  print 'No all elements loaded on Dashboard page'
                  date_time=datetime.now()
                  date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
                  self.driver.get_screenshot_as_file("dashboard_page_fail"+date_time_formatted+".png")
                  self.fail("'No all elements loaded on Dashboard page'")

        #We are on Dashbord for sure....
        self.main_find_cow=self.driver.find_element_by_id('find_cow')
        self.main_find_cow.send_keys('1')
        self.main_find_cow.send_keys(Keys.ENTER)
        time.sleep(60)
        print "Test running time:"+str((date_time.now()-date_time))


    def test_logout_process_on_Firefox(self):
        #logout from main page(dashboard)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'test logout process on Firefox started at :'+date_time_formatted
        self.search_field=self.driver.find_element_by_id("signout")
        self.search_field.send_keys(Keys.ENTER)
        time.sleep(3)
        EmailElement=self.is_element_present(By.NAME,"email")
        PasswordElement=self.is_element_present(By.NAME,"password")
        LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
        if( EmailElement and PasswordElement and LoginBtnElement):
            pass
        else:
            date_time=datetime.now()
            date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
            self.driver.get_screenshot_as_file("logout_page_fail"+date_time_formatted+".png")
            self.fail("Fail log-out")
        print "Test running time:"+str((date_time.now()-date_time))

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
         except NoSuchElementException ,e: return False
         return True


    def test_Login_process_on_Chrome(self):
        #date_time= time.strftime("%d/%m/%%Y  %I:%M:%:S")
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
              EmailElement=self.is_element_present(By.NAME,"email")
              PasswordElement=self.is_element_present(By.NAME,"password")
              LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
              if (EmailElement and PasswordElement and LoginBtnElement):
                 self.username_field=self.driver.find_element_by_name('email')
                 self.username_field.send_keys('scrtesting@yahoo.com')
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
                  print 'Login page not loaded all elements'
                  #take a screenshoot of main page after login
                  date_time=datetime.now()
                  date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
                  self.driver.get_screenshot_as_file("login_page_fail"+date_time_formatted+".png")
                  self.fail("Login page not loaded all elements")

        loading_attempt=3
        #time i let a page load
        time.sleep(3)
        #Load main page and register with username/password
        while(loading_attempt>0):
              #check if user successfully login on page https://hc24-qalab-web.scrdairy.com/#dashboard/
              #check if headers exist
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
                  print 'No all elements loaded on Dashboard page'
                  date_time=datetime.now()
                  date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
                  self.driver.get_screenshot_as_file("dashboard_page_fail"+date_time_formatted+".png")
                  self.fail("'No all elements loaded on Dashboard page'")
        print "Test running time:"+str((date_time.now()-date_time))

    def test_logout_process_on_Chrome(self):
        #logout from main page(dashboard)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test_logout_process_on_Chrome started at :'+date_time_formatted
        self.search_field=self.driver.find_element_by_id("signout")
        self.search_field.send_keys(Keys.ENTER)
        time.sleep(3)
        EmailElement=self.is_element_present(By.NAME,"email")
        PasswordElement=self.is_element_present(By.NAME,"password")
        LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
        if( EmailElement and PasswordElement and LoginBtnElement):
            pass
        else:
            date_time=datetime.now()
            date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
            self.driver.get_screenshot_as_file("logout_page_fail"+date_time_formatted+".png")
            self.fail("Fail log-out")
        print "Test running time:"+str((date_time.now()-date_time))

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


    def test_Login_process_on_IE(self):
        #date_time= time.strftime("%d/%m/%%Y  %I:%M:%:S")
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
              EmailElement=self.is_element_present(By.NAME,"email")
              PasswordElement=self.is_element_present(By.NAME,"password")
              LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
              if (EmailElement and PasswordElement and LoginBtnElement):
                 self.username_field=self.driver.find_element_by_name('email')
                 self.username_field.send_keys('scrtesting@yahoo.com')
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
                  print 'Login page not loaded all elements'
                  #take a screenshoot of main page after login
                  date_time=datetime.now()
                  date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
                  self.driver.get_screenshot_as_file("login_page_fail"+date_time_formatted+".png")
                  self.fail("Login page not loaded all elements")

        loading_attempt=3
        #time i let a page load
        time.sleep(3)
        #Load main page and register with username/password
        while(loading_attempt>0):
              #check if user successfully login on page https://hc24-qalab-web.scrdairy.com/#dashboard/
              #check if headers exist
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
                  print 'No all elements loaded on Dashboard page'
                  date_time=datetime.now()
                  date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
                  self.driver.get_screenshot_as_file("dashboard_page_fail"+date_time_formatted+".png")
                  self.fail("'No all elements loaded on Dashboard page'")
        print "Test running time:"+str((date_time.now()-date_time))

    def test_logout_process_on_IE(self):
        #logout from main page(dashboard)
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test_logout_process_on_IE started at :'+date_time_formatted
        self.search_field=self.driver.find_element_by_id("signout")
        self.search_field.send_keys(Keys.ENTER)
        time.sleep(3)
        EmailElement=self.is_element_present(By.NAME,"email")
        PasswordElement=self.is_element_present(By.NAME,"password")
        LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
        if( EmailElement and PasswordElement and LoginBtnElement):
            pass
        else:
            date_time=datetime.now()
            date_time_formatted=date_time.strftime("%d_%m_%Y__%H_%M_%S")
            self.driver.get_screenshot_as_file("logout_page_fail"+date_time_formatted+".png")
            self.fail("Fail log-out")
        print "Test running time:"+str((date_time.now()-date_time))

    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()







if __name__=='__main__':
    unittest.main(verbosity=2)
