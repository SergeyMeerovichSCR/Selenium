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


class AddDeleteNoteToFarmFirefox(unittest.TestCase):
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
    def AddNote(self,date_time_formatted):
        add_note_textbox=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[1]/div[@class='textbox']/input[@id='addNote']")
        self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[1]/div[@class='textbox']/input[@id='addNote']").send_keys(Keys.NULL)
        #type a message for note
        self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[1]/div[@class='textbox']/input[@id='addNote']").send_keys("test automation message : "+date_time_formatted)
        #click on 'Add to Farm graph' button
        self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[1]/div[@id='note_add']").click()
        time.sleep(1)
        add_note_textbox.click()
        time.sleep(1)
        n=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[2]/div").text
        return n



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

    def test_2_Add_Note_To_Farm_Firefox(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y %H:%M:%S")
        print 'Test ability Add Note to Farm Report on Firefox started at :'+date_time_formatted
        for x in range(0,10,1):
            try:
                  date_time=datetime.now()
                  date_time_formatted=date_time.strftime("%d/%m/%Y %H:%M:%S")
                  #Focus on Edit text element
                  N=self.AddNote(date_time_formatted)
                  #check if message really added
                  printed_notes=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[2]/div").text
                  self.assertEqual(N,printed_notes,'check if you actually added notes')
                  print 'successfully added : %s' %x
            except NoSuchElementException:
               self.take_screenshot('Fail_add_New_Note')
               self.fail("There is fail during add Note ")
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test ability add Note to Farm on Firefox finish at :'+date_time_formatted

    def test_3_Delete_Note_From_Farm_Firefox(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y %H:%M:%S")
        print 'Test ability Delete Note from Farm Report on Firefox started at :'+date_time_formatted
        for x in range(0,10,1):
            try:

                    delete_btn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[3]/div[1]/div")
                    printed_notes=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[2]/div").text
                    print printed_notes
                    delete_btn.click()
                    time.sleep(1)
                    self.driver.implicitly_wait(20)
                    #check if this message actually removed
                    if(x!=9):
                      printed_notes_after_delete=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[2]/div").text
                      self.assertNotEqual(printed_notes,printed_notes_after_delete,'Bug the Note did not deleted')
            except NoSuchElementException:
               self.take_screenshot('Fail_click_on_Delete_Note')
               self.fail("There was a problem delete note ")
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test ability Delete Note on Firefox finish at :'+date_time_formatted



    def test_4_Logout_process_on_Firefox(self):
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


class AddDeleteNoteToFarmChrome(unittest.TestCase):
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

    def AddNote(self,date_time_formatted):
        #date_time=datetime.now()
        #date_time_formatted=date_time.strftime("%d/%m/%Y %H:%M:%S")
        add_note_textbox=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[1]/div[@class='textbox']/input[@id='addNote']")
        self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[1]/div[@class='textbox']/input[@id='addNote']").send_keys(Keys.NULL)
        #type a message for note
        self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[1]/div[@class='textbox']/input[@id='addNote']").send_keys("test automation message : "+date_time_formatted)
        #click on 'Add to Farm graph' button
        self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[1]/div[@id='note_add']").click()
        time.sleep(1)
        add_note_textbox.click()
        time.sleep(1)
        n=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[2]/div").text
        return n


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



    def test_2_Add_Note_To_Farm_Chrome(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y %H:%M:%S")
        print 'Test ability Add Note to Farm Report on IE started at :'+date_time_formatted
        for x in range(0,10,1):
            try:
                  date_time=datetime.now()
                  date_time_formatted=date_time.strftime("%d/%m/%Y %H:%M:%S")
                  #Focus on Edit text element
                  N=self.AddNote(date_time_formatted)
                  #check if message really added
                  printed_notes=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[2]/div").text
                  self.assertEqual(N,printed_notes,'check if you actually added notes')
                  print 'successfully added : %s' %x
            except NoSuchElementException:
               self.take_screenshot('Fail_add_New_Note')
               self.fail("There is fail during add Note ")
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test ability add Note to Farm on IE finish at :'+date_time_formatted

    def test_3_Delete_Note_From_Farm_Chrome(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y %H:%M:%S")
        print 'Test ability Delete Note from Farm Report on Firefox started at :'+date_time_formatted
        for x in range(0,10,1):
            try:

                    delete_btn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[3]/div[1]/div")
                    printed_notes=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[2]/div").text
                    print printed_notes
                    delete_btn.click()
                    time.sleep(1)
                    self.driver.implicitly_wait(20)
                    #check if this message actually removed
                    if(x!=9):
                      printed_notes_after_delete=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[2]/div").text
                      self.assertNotEqual(printed_notes,printed_notes_after_delete,'Bug the Note did not deleted')
            except NoSuchElementException:
               self.take_screenshot('Fail_click_on_Delete_Note')
               self.fail("There was a problem delete note ")
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test ability Delete Note on Firefox finish at :'+date_time_formatted



    def test_4_Logout_process_on_Chrome(self):
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





class AddDeleteNoteToFarmIE(unittest.TestCase):
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
    def AddNote(self,date_time_formatted):
        #date_time=datetime.now()
        #date_time_formatted=date_time.strftime("%d/%m/%Y %H:%M:%S")
        add_note_textbox=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[1]/div[@class='textbox']/input[@id='addNote']")
        self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[1]/div[@class='textbox']/input[@id='addNote']").send_keys(Keys.NULL)
        #type a message for note
        self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[1]/div[@class='textbox']/input[@id='addNote']").send_keys("test automation message : "+date_time_formatted)
        #click on 'Add to Farm graph' button
        self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[1]/div[@id='note_add']").click()
        time.sleep(1)
        add_note_textbox.click()
        time.sleep(1)
        n=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[2]/div").text
        return n

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
                   self.take_screenshot('Fail_log_out')
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


    def test_2_Add_Note_To_Farm_IE(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y %H:%M:%S")
        print 'Test ability Add Note to Farm Report on Firefox started at :'+date_time_formatted
        for x in range(0,10,1):
            try:
                  date_time=datetime.now()
                  date_time_formatted=date_time.strftime("%d/%m/%Y %H:%M:%S")
                  #Focus on Edit text element
                  N=self.AddNote(date_time_formatted)
                  #check if message really added
                  printed_notes=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[2]/div").text
                  self.assertEqual(N,printed_notes,'check if you actually added notes')
                  print 'successfully added : %s' %x
            except NoSuchElementException:
               self.take_screenshot('Fail_add_New_Note')
               self.fail("There is fail during add Note ")
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test ability add Note to Farm on Firefox finish at :'+date_time_formatted

    def test_3_Delete_Note_From_Farm_IE(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y %H:%M:%S")
        print 'Test ability Delete Note from Farm Report on IE started at :'+date_time_formatted
        for x in range(0,10,1):
            try:

                    delete_btn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[3]/div[1]/div")
                    printed_notes=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[2]/div").text
                    print printed_notes
                    delete_btn.click()
                    time.sleep(1)
                    self.driver.implicitly_wait(20)
                    #printed_notes_after_delete=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[2]/div").text
                    #check if this message actually removed
                    if(x!=9):
                      printed_notes_after_delete=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[@class='tab-content']/div[@id='dashboard-pane']/div[3]/div[@class='notes-inner']/div[@class='table-container']/table/tbody/tr[1]/td[2]/div").text
                      self.assertNotEqual(printed_notes,printed_notes_after_delete,'Bug the Note did not deleted')
            except NoSuchElementException:
               self.take_screenshot('Fail_click_on_Delete_Note')
               self.fail("There was a problem delete note ")
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test ability Delete Note on IE finish at :'+date_time_formatted




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
           self.take_screenshot('Fail_log_out_did_not_exit_to_login_page')
        print "Test running time:"+str((date_time.now()-date_time))


    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()




if __name__=='__main__':
    unittest.main(verbosity=2)


