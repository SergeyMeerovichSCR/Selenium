import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
import time
import os,sys
#pytest use for order testcase running order
#import pytest
from datetime import datetime
__author__ = 'sergey.meerovich'


class FullCowCardEditTestFirefox(unittest.TestCase):
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

    def open_new_cow_record(self):
        try:
           #addcow=self.is_element_present(By.XPATH,"//html/body[@id='top]/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='list_header']/div[@class='pull-right']/div[@data-wm-item='addCow']")
           #/div[@class='pull-right']/div[@data-wm-item='addCow']/span[@id='add_cow']
           #addcow=self.is_element_present(By.LINK_TEXT,'Add Cow')
           addcow=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='list_header']/div[@class='pull-right']/div[@data-wm-item='addCow']/span[@id='add_cow']")
           if addcow:
              AddCow=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='list_header']/div[@class='pull-right']/div[@data-wm-item='addCow']/span[@id='add_cow']")
              AddCow.click()
              self.driver.implicitly_wait(20)
              #Check if iFrame really opened
              new_record_title=self.is_element_present(By.XPATH,".//*[@id='add_cow_modal']/div[1]/div/div")
              return True
           else:
               return False
        except:
           self.take_screenshot('Fail_open_new_cow_card_record')
           self.loggertest(self.__class__.__name__,'Fail open New Cow Card Record')
           self.fail("Fail open New Cow Card Record")
           return False
    def fill_new_record(self,booknumber,burnnumber,scrtag,isonum,lactation):
        try:
            book_edit_box=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='bookNumber']/div[@class='controls']/input[@id='book_number']")
            burn_edit_box=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='bookNumber']/div[@class='controls']/input[@id='book_number']")
            apply_btn=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[@class='modal-footer']/div[@id='modal_apply']")
            if (book_edit_box and burn_edit_box and apply_btn):
                time.sleep(2)
                GroupNumDropDownMenu=self.driver.find_element_by_xpath(".//*[@id='group']")
                GroupNumDropDownMenu.click()
                GroupNum=self.driver.find_element_by_xpath(".//*[@id='edit_cow_card_form row-fluid']/div[1]/form/div[1]/div/div[1]/ul/li[3]/a")
                GroupNum.click()
                Book_Num=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='burnNumber']/div[@class='controls']/input[@id='burn_number']")
                Book_Num.send_keys("")
                time.sleep(1)
                Book_Num.send_keys(booknumber)
                Burn_Num=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='bookNumber']/div[@class='controls']/input[@id='book_number']")
                Burn_Num.send_keys("")
                time.sleep(1)
                Burn_Num.send_keys(burnnumber)
                SCR_tag=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='scrTagNumber']/div[@class='controls']/input[@id='scr_tag']")
                SCR_tag.send_keys("")
                time.sleep(1)
                SCR_tag.send_keys(scrtag)
                ISO_num=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='isoTagNumber']/div[@class='controls']/input[@id='iso_tag']")
                ISO_num.send_keys("")
                time.sleep(1)
                ISO_num.send_keys(isonum)
                Lactation=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[2]/form[@class='form-horizontal']/div[@data-wm-item='lactation']/div[@class='controls']/input[@id='lactation']")
                Lactation.send_keys("")
                time.sleep(1)
                Lactation.send_keys(lactation)
                AllowBreedDoNotBreed=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[2]/form[@class='form-horizontal']/div[6]/div[@class='controls']/span[@id='can_breed']/label[2]/input[@id='option_breed_no']")
                AllowBreedDoNotBreed.click()
                #BirthDateCalendar=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[2]/form[@class='form-horizontal']/div[@data-wm-item='lastAiDate']/div[@class='controls']/div[1]/input[@id='birth_date']")
                BirthDateCalendar=self.driver.find_element_by_xpath(".//*[@id='birth_date']")
                BirthDateCalendar.click()
                time.sleep(1)
                BirthdateChooseFirstDate=self.driver.find_element_by_xpath(".//*[@id='top']/div[6]/div[1]/table/tbody/tr[1]/td[1]")
                BirthdateChooseFirstDate.click()
                LastCalvingCalendar=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[2]/form[@class='form-horizontal']/div[3]/div[@class='controls']/div[1]/input[@id='last_calving']")
                LastCalvingCalendar.click()
                time.sleep(1)
                LastCalvingChooseFirstDate=self.driver.find_element_by_xpath(".//*[@id='top']/div[6]/div[1]/table/tbody/tr[1]/td[1]")
                LastCalvingChooseFirstDate.click()
                self.driver.implicitly_wait(3)
                time.sleep(1)
                LastAIdateCalendar=self.driver.find_element_by_xpath(".//*[@id='last_ai']")
                LastAIdateCalendar.click()
                time.sleep(1)
                LastAIdateCalendarChooseFirstDate=self.driver.find_element_by_xpath(".//*[@id='top']/div[6]/div[1]/table/tbody/tr[1]/td[1]")
                LastAIdateCalendarChooseFirstDate.click()
                time.sleep(1)
                Apply_Btn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[@class='modal-footer']/div[@id='modal_apply']")
                Apply_Btn.send_keys(Keys.NULL)
                Apply_Btn.click()
                time.sleep(1)
                self.driver.implicitly_wait(20)
                #Check if such cow not already exist
                #self.is_element_present(By.XPATH,".//*[@id='add_cow_modal']/div[3]/div")
                if (self.is_element_present(By.XPATH,".//*[@id='add_cow_modal']/div[3]/div")):
                    self.take_screenshot('Such_Cow_card_already_exsist'+booknumber)
                    self.loggertest(self.__class__.__name__,'Fail fill cow card with already exsit data')
                    self.fail("Fail fill cow card with already exsit data'")
                    return False
                else:
                    return True
            else:
                return False
        except:
           self.take_screenshot('Fail_fill_cow_card_record')
           self.loggertest(self.__class__.__name__,'Fail fill opened cow record with book number and burn number')
           self.fail("Fail fill opened cow record with book number and burn number")
           return False
    def check_cow_card_create_result(self,booknumber,burnnumber):
         try:
             self.driver.refresh()
             time.sleep(3)
             FindCow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='find_cow']")))
             fcow=self.is_element_present(By.XPATH,".//*[@id='find_cow']")
             findcow=self.driver.find_element_by_xpath(".//*[@id='find_cow']")
             self.loggertest(self.__class__.__name__,'Focus on Enter Cow number field')
             findcow.click()
             self.driver.implicitly_wait(10)
             findcow.clear()
             findcow.send_keys(booknumber)
             time.sleep(1)
             self.loggertest(self.__class__.__name__,'Look for cow that started with booknumber')
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
                back_to_all_cows=self.driver.find_element_by_xpath(".//*[@id='report']")
                back_to_all_cows.click()
                time.sleep(3)
                return True
             else:
                self.take_screenshot("Opened_wrong_cow_card")
                self.loggertest(self.__class__.__name__,'Opened different cow card from selected on Find Cow field...')
                self.fail("Not correct Cow Card selected")
                return False
         except:
             self.take_screenshot("Fail_look_for_new_cow_card")
             self.loggertest(self.__class__.__name__,'Fail look for new cow card')
             self.fail("Not correct Cow Card selected")
             return False
    def find_cow_card(self,cownumber):
        try:
             self.driver.refresh()
             time.sleep(3)
             FindCow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='find_cow']")))
             fcow=self.is_element_present(By.XPATH,".//*[@id='find_cow']")
             findcow=self.driver.find_element_by_xpath(".//*[@id='find_cow']")
             self.loggertest(self.__class__.__name__,'Focus on Enter Cow number field')
             findcow.click()
             self.driver.implicitly_wait(10)
             findcow.clear()
             findcow.send_keys(cownumber)
             time.sleep(1)
             self.loggertest(self.__class__.__name__,'Look for cow that started with booknumber')
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
                pass
             else:
                self.take_screenshot("Opened_wrong_cow_card")
                self.loggertest(self.__class__.__name__,'Opened different cow card from selected on Find Cow field...')
                self.fail("Not correct Cow Card selected")
                return False
        except:
                self.take_screenshot("Opened_wrong_cow_card")
                self.loggertest(self.__class__.__name__,'Opened different cow card from selected on Find Cow field...')
                self.fail("Not correct Cow Card selected")
                return False
        #Start Delete Process
        editcowcard=self.is_element_present(By.XPATH,".//*[@id='edit-cow-record']")
        EditCowCard=self.driver.find_element_by_xpath(".//*[@id='edit-cow-record']")
        #Press on Edit Cow Card btn
        EditCowCard.click()
        self.driver.implicitly_wait(10)
        #Check if Cow Card opened
        exsist_record_title=self.is_element_present(By.XPATH,".//*[@id='edit_cow_modal']/div[1]/div/div")
        book_edit_box=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='edit_cow_modal']/div[@class='modal-body']/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='bookNumber']/div[@class='controls']/input[@id='book_number']")
        burn_edit_box=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='edit_cow_modal']/div[@class='modal-body']/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='burnNumber']/div[@class='controls']/input[@id='burn_number']")
        if (exsist_record_title and book_edit_box and burn_edit_box):
            return True
        else:
             self.take_screenshot("Fail_open_exist_Cow_card")
             self.loggertest(self.__class__.__name__,'Could not open exsist Cow Card')
             self.fail("Fail open exsist Cow Card")
             return False

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
    def test_2_AddNewCowCard_on_Firefox(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Create new Cow cards_on_Firefox started at :'+date_time_formatted
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

        #Start switch and check between first and second page report of All Cows by use Right/Left Arrows
                  #Create A new Cow Cards
        new_cow_book_numbers=['100000','200000']
        new_cow_burn_numbers=['100000','200000']
        scr_tag_number=['100000','200000']
        iso_number=['100000','200000']
        lactation=['1','2']
        for x in range(0,2,1):
             self.driver.maximize_window()
             #Open a New Cow Card
             result_open_cow_record=self.open_new_cow_record()
             if result_open_cow_record:
                 #Fill opened New Cow Card
                 attempt_edit_card_details=self.fill_new_record(new_cow_book_numbers[x],new_cow_burn_numbers[x],scr_tag_number[x],iso_number[x],lactation[x])
                 #If user fill cow card and Apply it check if cow card exist
                 if attempt_edit_card_details:
                     look_for_cow_card=self.check_cow_card_create_result(new_cow_book_numbers[x],new_cow_burn_numbers[x])
                     if look_for_cow_card:
                        print "Success created cow card :"+new_cow_burn_numbers[x]
                     else:
                        print "Fail find new cow card :"+new_cow_burn_numbers[x]
                 else:
                      print "Fail fill cow card :"+new_cow_burn_numbers[x]
             else:
                self.take_screenshot("Fail_open_cow_card")
                self.loggertest(self.__class__.__name__,'Fail_open_cow_card')
                self.fail("Fail_open_cow_card")

        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test of Create new Cow Card_on_Firefox finish at :'+date_time_formatted
    def test_3_DeleteCowCard_on_Firefox(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Delete cards_on_Firefox started at :'+date_time_formatted
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

        #Start switch and check between first and second page report of All Cows by use Right/Left Arrows
                  #Create A new Cow Cards
        new_cow_book_numbers=['100000','200000']
        new_cow_burn_numbers=['100000','200000']
        for x in range(0,2,1):
             self.driver.maximize_window()
             #Open a New Cow Card
             result=self.find_cow_card(new_cow_book_numbers[x])
             # On this point user should get a correct opened exsist Cow Card that should be deleted
             if result:
                 deletecow=self.driver.find_element_by_xpath(".//*[@id='delete_cow']/div")
                 deletecow.click()
                 self.driver.implicitly_wait(10)
                 warn_message=self.driver.find_element_by_xpath(".//*[@id='confirm']")
                 deletebtn=self.driver.find_element_by_xpath(".//*[@id='confirm_delete_cow']")
                 if (warn_message.is_displayed() and deletebtn.is_displayed()):
                     #Ready for delete
                     deletebtn.click()
                     self.driver.implicitly_wait(20)
                     time.sleep(3)
                     print 'The Cow Card of cow :'+new_cow_burn_numbers[x]+' was deleted successfully.'
                 else:
                     self.take_screenshot("Can_not_get_warning_message_before_delete")
                     print 'The Cow Card of cow :'+new_cow_burn_numbers[x]+' Failed!!!'
                     self.loggertest(self.__class__.__name__,'Did not get a delete message and delete button')
                     self.fail("Did not get a delete message and delete button")
             else:
                self.take_screenshot("Delete_process_fail")
                self.loggertest(self.__class__.__name__,'Stuck on opened cow card and could not delete')
                self.fail("Stuck on opened cow card and could not delete")
             self.driver.refresh()
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test of Delete Cow Cards_on_Firefox finish at :'+date_time_formatted
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





class FullCowCardEditTestChrome(unittest.TestCase):
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

    def open_new_cow_record(self):
        try:
           #addcow=self.is_element_present(By.XPATH,"//html/body[@id='top]/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='list_header']/div[@class='pull-right']/div[@data-wm-item='addCow']")
           #/div[@class='pull-right']/div[@data-wm-item='addCow']/span[@id='add_cow']
           #addcow=self.is_element_present(By.LINK_TEXT,'Add Cow')
           addcow=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='list_header']/div[@class='pull-right']/div[@data-wm-item='addCow']/span[@id='add_cow']")
           if addcow:
              AddCow=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='list_header']/div[@class='pull-right']/div[@data-wm-item='addCow']/span[@id='add_cow']")
              AddCow.click()
              self.driver.implicitly_wait(20)
              #Check if iFrame really opened
              new_record_title=self.is_element_present(By.XPATH,".//*[@id='add_cow_modal']/div[1]/div/div")
              return True
           else:
               return False
        except:
           self.take_screenshot('Fail_open_new_cow_card_record')
           self.loggertest(self.__class__.__name__,'Fail open New Cow Card Record')
           self.fail("Fail open New Cow Card Record")
           return False
    def fill_new_record(self,booknumber,burnnumber,scrtag,isonum,lactation):
        try:
            book_edit_box=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='bookNumber']/div[@class='controls']/input[@id='book_number']")
            burn_edit_box=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='bookNumber']/div[@class='controls']/input[@id='book_number']")
            apply_btn=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[@class='modal-footer']/div[@id='modal_apply']")
            if (book_edit_box and burn_edit_box and apply_btn):
                time.sleep(2)
                GroupNumDropDownMenu=self.driver.find_element_by_xpath(".//*[@id='group']")
                GroupNumDropDownMenu.click()
                GroupNum=self.driver.find_element_by_xpath(".//*[@id='edit_cow_card_form row-fluid']/div[1]/form/div[1]/div/div[1]/ul/li[3]/a")
                GroupNum.click()
                Book_Num=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='burnNumber']/div[@class='controls']/input[@id='burn_number']")
                Book_Num.send_keys("")
                time.sleep(1)
                Book_Num.send_keys(booknumber)
                Burn_Num=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='bookNumber']/div[@class='controls']/input[@id='book_number']")
                Burn_Num.send_keys("")
                time.sleep(1)
                Burn_Num.send_keys(burnnumber)
                SCR_tag=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='scrTagNumber']/div[@class='controls']/input[@id='scr_tag']")
                SCR_tag.send_keys("")
                time.sleep(1)
                SCR_tag.send_keys(scrtag)
                ISO_num=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='isoTagNumber']/div[@class='controls']/input[@id='iso_tag']")
                ISO_num.send_keys("")
                time.sleep(1)
                ISO_num.send_keys(isonum)
                Lactation=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[2]/form[@class='form-horizontal']/div[@data-wm-item='lactation']/div[@class='controls']/input[@id='lactation']")
                Lactation.send_keys("")
                time.sleep(1)
                Lactation.send_keys(lactation)
                AllowBreedDoNotBreed=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[2]/form[@class='form-horizontal']/div[6]/div[@class='controls']/span[@id='can_breed']/label[2]/input[@id='option_breed_no']")
                AllowBreedDoNotBreed.click()
                #BirthDateCalendar=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[2]/form[@class='form-horizontal']/div[@data-wm-item='lastAiDate']/div[@class='controls']/div[1]/input[@id='birth_date']")
                BirthDateCalendar=self.driver.find_element_by_xpath(".//*[@id='birth_date']")
                BirthDateCalendar.click()
                time.sleep(1)
                BirthdateChooseFirstDate=self.driver.find_element_by_xpath(".//*[@id='top']/div[6]/div[1]/table/tbody/tr[1]/td[1]")
                BirthdateChooseFirstDate.click()
                LastCalvingCalendar=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[2]/form[@class='form-horizontal']/div[3]/div[@class='controls']/div[1]/input[@id='last_calving']")
                LastCalvingCalendar.click()
                time.sleep(1)
                LastCalvingChooseFirstDate=self.driver.find_element_by_xpath(".//*[@id='top']/div[6]/div[1]/table/tbody/tr[1]/td[1]")
                LastCalvingChooseFirstDate.click()
                self.driver.implicitly_wait(3)
                time.sleep(1)
                LastAIdateCalendar=self.driver.find_element_by_xpath(".//*[@id='last_ai']")
                LastAIdateCalendar.click()
                time.sleep(1)
                LastAIdateCalendarChooseFirstDate=self.driver.find_element_by_xpath(".//*[@id='top']/div[6]/div[1]/table/tbody/tr[1]/td[1]")
                LastAIdateCalendarChooseFirstDate.click()
                time.sleep(1)
                Apply_Btn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[@class='modal-footer']/div[@id='modal_apply']")
                Apply_Btn.send_keys(Keys.NULL)
                Apply_Btn.click()
                time.sleep(1)
                self.driver.implicitly_wait(20)
                #Check if such cow not already exist
                #self.is_element_present(By.XPATH,".//*[@id='add_cow_modal']/div[3]/div")
                if (self.is_element_present(By.XPATH,".//*[@id='add_cow_modal']/div[3]/div")):
                    self.take_screenshot('Such_Cow_card_already_exsist'+booknumber)
                    self.loggertest(self.__class__.__name__,'Fail fill cow card with already exsit data')
                    self.fail("Fail fill cow card with already exsit data'")
                    return False
                else:
                    return True
            else:
                return False
        except:
           self.take_screenshot('Fail_fill_cow_card_record')
           self.loggertest(self.__class__.__name__,'Fail fill opened cow record with book number and burn number')
           self.fail("Fail fill opened cow record with book number and burn number")
           return False
    def check_cow_card_create_result(self,booknumber,burnnumber):
         try:
             self.driver.refresh()
             time.sleep(3)
             FindCow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='find_cow']")))
             fcow=self.is_element_present(By.XPATH,".//*[@id='find_cow']")
             findcow=self.driver.find_element_by_xpath(".//*[@id='find_cow']")
             self.loggertest(self.__class__.__name__,'Focus on Enter Cow number field')
             findcow.click()
             self.driver.implicitly_wait(10)
             findcow.clear()
             findcow.send_keys(booknumber)
             time.sleep(1)
             self.loggertest(self.__class__.__name__,'Look for cow that started with booknumber')
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
                back_to_all_cows=self.driver.find_element_by_xpath(".//*[@id='report']")
                back_to_all_cows.click()
                time.sleep(3)
                return True
             else:
                self.take_screenshot("Opened_wrong_cow_card")
                self.loggertest(self.__class__.__name__,'Opened different cow card from selected on Find Cow field...')
                self.fail("Not correct Cow Card selected")
                return False
         except:
             self.take_screenshot("Fail_look_for_new_cow_card")
             self.loggertest(self.__class__.__name__,'Fail look for new cow card')
             self.fail("Not correct Cow Card selected")
             return False
    def find_cow_card(self,cownumber):
        try:
             self.driver.refresh()
             time.sleep(3)
             FindCow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='find_cow']")))
             fcow=self.is_element_present(By.XPATH,".//*[@id='find_cow']")
             findcow=self.driver.find_element_by_xpath(".//*[@id='find_cow']")
             self.loggertest(self.__class__.__name__,'Focus on Enter Cow number field')
             findcow.click()
             self.driver.implicitly_wait(10)
             findcow.clear()
             findcow.send_keys(cownumber)
             time.sleep(1)
             self.loggertest(self.__class__.__name__,'Look for cow that started with booknumber')
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
                pass
             else:
                self.take_screenshot("Opened_wrong_cow_card")
                self.loggertest(self.__class__.__name__,'Opened different cow card from selected on Find Cow field...')
                self.fail("Not correct Cow Card selected")
                return False
        except:
                self.take_screenshot("Opened_wrong_cow_card")
                self.loggertest(self.__class__.__name__,'Opened different cow card from selected on Find Cow field...')
                self.fail("Not correct Cow Card selected")
                return False
        #Start Delete Process
        editcowcard=self.is_element_present(By.XPATH,".//*[@id='edit-cow-record']")
        EditCowCard=self.driver.find_element_by_xpath(".//*[@id='edit-cow-record']")
        #Press on Edit Cow Card btn
        EditCowCard.click()
        self.driver.implicitly_wait(10)
        #Check if Cow Card opened
        exsist_record_title=self.is_element_present(By.XPATH,".//*[@id='edit_cow_modal']/div[1]/div/div")
        book_edit_box=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='edit_cow_modal']/div[@class='modal-body']/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='bookNumber']/div[@class='controls']/input[@id='book_number']")
        burn_edit_box=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='edit_cow_modal']/div[@class='modal-body']/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='burnNumber']/div[@class='controls']/input[@id='burn_number']")
        if (exsist_record_title and book_edit_box and burn_edit_box):
            return True
        else:
             self.take_screenshot("Fail_open_exist_Cow_card")
             self.loggertest(self.__class__.__name__,'Could not open exsist Cow Card')
             self.fail("Fail open exsist Cow Card")
             return False


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
    def test_2_AddNewCowCard_on_Chrome(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Create new Cow cards_on_Chrome started at :'+date_time_formatted
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

        #Start switch and check between first and second page report of All Cows by use Right/Left Arrows
                  #Create A new Cow Cards
        new_cow_book_numbers=['100000','200000']
        new_cow_burn_numbers=['100000','200000']
        scr_tag_number=['100000','200000']
        iso_number=['100000','200000']
        lactation=['1','2']
        for x in range(0,2,1):
             self.driver.maximize_window()
             #Open a New Cow Card
             result_open_cow_record=self.open_new_cow_record()
             if result_open_cow_record:
                 #Fill opened New Cow Card
                 attempt_edit_card_details=self.fill_new_record(new_cow_book_numbers[x],new_cow_burn_numbers[x],scr_tag_number[x],iso_number[x],lactation[x])
                 #If user fill cow card and Apply it check if cow card exist
                 if attempt_edit_card_details:
                     look_for_cow_card=self.check_cow_card_create_result(new_cow_book_numbers[x],new_cow_burn_numbers[x])
                     if look_for_cow_card:
                        print "Success created cow card :"+new_cow_burn_numbers[x]
                     else:
                        print "Fail find new cow card :"+new_cow_burn_numbers[x]
                 else:
                      print "Fail fill cow card :"+new_cow_burn_numbers[x]
             else:
                self.take_screenshot("Fail_open_cow_card")
                self.loggertest(self.__class__.__name__,'Fail_open_cow_card')
                self.fail("Fail_open_cow_card")

        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test of Create new Cow Card_on_Chrome finish at :'+date_time_formatted
    def test_3_DeleteCowCard_on_Chrome(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Delete cards_on_Chrome started at :'+date_time_formatted
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

        #Start switch and check between first and second page report of All Cows by use Right/Left Arrows
                  #Create A new Cow Cards
        new_cow_book_numbers=['100000','200000']
        new_cow_burn_numbers=['100000','200000']
        for x in range(0,2,1):
             self.driver.maximize_window()
             #Open a New Cow Card
             result=self.find_cow_card(new_cow_book_numbers[x])
             # On this point user should get a correct opened exsist Cow Card that should be deleted
             if result:
                 deletecow=self.driver.find_element_by_xpath(".//*[@id='delete_cow']/div")
                 deletecow.click()
                 self.driver.implicitly_wait(10)
                 warn_message=self.driver.find_element_by_xpath(".//*[@id='confirm']")
                 deletebtn=self.driver.find_element_by_xpath(".//*[@id='confirm_delete_cow']")
                 if (warn_message.is_displayed() and deletebtn.is_displayed()):
                     #Ready for delete
                     deletebtn.click()
                     self.driver.implicitly_wait(20)
                     time.sleep(3)
                     print 'The Cow Card of cow :'+new_cow_burn_numbers[x]+' was deleted successfully.'
                 else:
                     self.take_screenshot("Can_not_get_warning_message_before_delete")
                     print 'The Cow Card of cow :'+new_cow_burn_numbers[x]+' Failed!!!'
                     self.loggertest(self.__class__.__name__,'Did not get a delete message and delete button')
                     self.fail("Did not get a delete message and delete button")
             else:
                self.take_screenshot("Delete_process_fail")
                self.loggertest(self.__class__.__name__,'Stuck on opened cow card and could not delete')
                self.fail("Stuck on opened cow card and could not delete")
             self.driver.refresh()
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test of Delete Cow Cards_on_Chrome finish at :'+date_time_formatted

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

class FullCowCardEditTestIE(unittest.TestCase):
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

    def open_new_cow_record(self):
        try:
           #addcow=self.is_element_present(By.XPATH,"//html/body[@id='top]/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='list_header']/div[@class='pull-right']/div[@data-wm-item='addCow']")
           #/div[@class='pull-right']/div[@data-wm-item='addCow']/span[@id='add_cow']
           #addcow=self.is_element_present(By.LINK_TEXT,'Add Cow')
           addcow=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='list_header']/div[@class='pull-right']/div[@data-wm-item='addCow']/span[@id='add_cow']")
           if addcow:
              AddCow=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='list_header']/div[@class='pull-right']/div[@data-wm-item='addCow']/span[@id='add_cow']")
              AddCow.click()
              self.driver.implicitly_wait(20)
              #Check if iFrame really opened
              new_record_title=self.is_element_present(By.XPATH,".//*[@id='add_cow_modal']/div[1]/div/div")
              return True
           else:
               return False
        except:
           self.take_screenshot('Fail_open_new_cow_card_record')
           self.loggertest(self.__class__.__name__,'Fail open New Cow Card Record')
           self.fail("Fail open New Cow Card Record")
           return False
    def fill_new_record(self,booknumber,burnnumber,scrtag,isonum,lactation):
        try:
            book_edit_box=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='bookNumber']/div[@class='controls']/input[@id='book_number']")
            burn_edit_box=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='bookNumber']/div[@class='controls']/input[@id='book_number']")
            apply_btn=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[@class='modal-footer']/div[@id='modal_apply']")
            if (book_edit_box and burn_edit_box and apply_btn):
                time.sleep(2)
                GroupNumDropDownMenu=self.driver.find_element_by_xpath(".//*[@id='group']")
                GroupNumDropDownMenu.click()
                GroupNum=self.driver.find_element_by_xpath(".//*[@id='edit_cow_card_form row-fluid']/div[1]/form/div[1]/div/div[1]/ul/li[3]/a")
                GroupNum.click()
                Book_Num=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='burnNumber']/div[@class='controls']/input[@id='burn_number']")
                Book_Num.send_keys("")
                time.sleep(1)
                Book_Num.send_keys(booknumber)
                Burn_Num=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='bookNumber']/div[@class='controls']/input[@id='book_number']")
                Burn_Num.send_keys("")
                time.sleep(1)
                Burn_Num.send_keys(burnnumber)
                SCR_tag=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='scrTagNumber']/div[@class='controls']/input[@id='scr_tag']")
                SCR_tag.send_keys("")
                time.sleep(1)
                SCR_tag.send_keys(scrtag)
                ISO_num=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='isoTagNumber']/div[@class='controls']/input[@id='iso_tag']")
                ISO_num.send_keys("")
                time.sleep(1)
                ISO_num.send_keys(isonum)
                Lactation=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[2]/form[@class='form-horizontal']/div[@data-wm-item='lactation']/div[@class='controls']/input[@id='lactation']")
                Lactation.send_keys("")
                time.sleep(1)
                Lactation.send_keys(lactation)
                AllowBreedDoNotBreed=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[2]/form[@class='form-horizontal']/div[6]/div[@class='controls']/span[@id='can_breed']/label[2]/input[@id='option_breed_no']")
                AllowBreedDoNotBreed.click()
                #BirthDateCalendar=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[2]/form[@class='form-horizontal']/div[@data-wm-item='lastAiDate']/div[@class='controls']/div[1]/input[@id='birth_date']")
                BirthDateCalendar=self.driver.find_element_by_xpath(".//*[@id='birth_date']")
                BirthDateCalendar.click()
                time.sleep(1)
                BirthdateChooseFirstDate=self.driver.find_element_by_xpath(".//*[@id='top']/div[6]/div[1]/table/tbody/tr[1]/td[1]")
                BirthdateChooseFirstDate.click()
                LastCalvingCalendar=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[2]/div[1]/div[2]/form[@class='form-horizontal']/div[3]/div[@class='controls']/div[1]/input[@id='last_calving']")
                LastCalvingCalendar.click()
                time.sleep(1)
                LastCalvingChooseFirstDate=self.driver.find_element_by_xpath(".//*[@id='top']/div[6]/div[1]/table/tbody/tr[1]/td[1]")
                LastCalvingChooseFirstDate.click()
                self.driver.implicitly_wait(3)
                time.sleep(1)
                LastAIdateCalendar=self.driver.find_element_by_xpath(".//*[@id='last_ai']")
                LastAIdateCalendar.click()
                time.sleep(1)
                LastAIdateCalendarChooseFirstDate=self.driver.find_element_by_xpath(".//*[@id='top']/div[6]/div[1]/table/tbody/tr[1]/td[1]")
                LastAIdateCalendarChooseFirstDate.click()
                time.sleep(1)
                Apply_Btn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='modal-container']/div[@id='add_cow_modal']/div[@class='modal-footer']/div[@id='modal_apply']")
                Apply_Btn.send_keys(Keys.NULL)
                Apply_Btn.click()
                time.sleep(1)
                self.driver.implicitly_wait(20)
                #Check if such cow not already exist
                #self.is_element_present(By.XPATH,".//*[@id='add_cow_modal']/div[3]/div")
                if (self.is_element_present(By.XPATH,".//*[@id='add_cow_modal']/div[3]/div")):
                    self.take_screenshot('Such_Cow_card_already_exsist'+booknumber)
                    self.loggertest(self.__class__.__name__,'Fail fill cow card with already exsit data')
                    self.fail("Fail fill cow card with already exsit data'")
                    return False
                else:
                    return True
            else:
                return False
        except:
           self.take_screenshot('Fail_fill_cow_card_record')
           self.loggertest(self.__class__.__name__,'Fail fill opened cow record with book number and burn number')
           self.fail("Fail fill opened cow record with book number and burn number")
           return False
    def check_cow_card_create_result(self,booknumber,burnnumber):
         try:
             self.driver.refresh()
             time.sleep(3)
             FindCow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='find_cow']")))
             fcow=self.is_element_present(By.XPATH,".//*[@id='find_cow']")
             findcow=self.driver.find_element_by_xpath(".//*[@id='find_cow']")
             self.loggertest(self.__class__.__name__,'Focus on Enter Cow number field')
             findcow.click()
             self.driver.implicitly_wait(10)
             findcow.clear()
             findcow.send_keys(booknumber)
             time.sleep(1)
             self.loggertest(self.__class__.__name__,'Look for cow that started with booknumber')
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
                back_to_all_cows=self.driver.find_element_by_xpath(".//*[@id='report']")
                back_to_all_cows.click()
                time.sleep(3)
                return True
             else:
                self.take_screenshot("Opened_wrong_cow_card")
                self.loggertest(self.__class__.__name__,'Opened different cow card from selected on Find Cow field...')
                self.fail("Not correct Cow Card selected")
                return False
         except:
             self.take_screenshot("Fail_look_for_new_cow_card")
             self.loggertest(self.__class__.__name__,'Fail look for new cow card')
             self.fail("Not correct Cow Card selected")
             return False
    def find_cow_card(self,cownumber):
        try:
             self.driver.refresh()
             time.sleep(3)
             FindCow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='find_cow']")))
             fcow=self.is_element_present(By.XPATH,".//*[@id='find_cow']")
             findcow=self.driver.find_element_by_xpath(".//*[@id='find_cow']")
             self.loggertest(self.__class__.__name__,'Focus on Enter Cow number field')
             findcow.click()
             self.driver.implicitly_wait(10)
             findcow.clear()
             findcow.send_keys(cownumber)
             time.sleep(1)
             self.loggertest(self.__class__.__name__,'Look for cow that started with booknumber')
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
                pass
             else:
                self.take_screenshot("Opened_wrong_cow_card")
                self.loggertest(self.__class__.__name__,'Opened different cow card from selected on Find Cow field...')
                self.fail("Not correct Cow Card selected")
                return False
        except:
                self.take_screenshot("Opened_wrong_cow_card")
                self.loggertest(self.__class__.__name__,'Opened different cow card from selected on Find Cow field...')
                self.fail("Not correct Cow Card selected")
                return False
        #Start Delete Process
        editcowcard=self.is_element_present(By.XPATH,".//*[@id='edit-cow-record']")
        EditCowCard=self.driver.find_element_by_xpath(".//*[@id='edit-cow-record']")
        #Press on Edit Cow Card btn
        EditCowCard.click()
        self.driver.implicitly_wait(10)
        #Check if Cow Card opened
        exsist_record_title=self.is_element_present(By.XPATH,".//*[@id='edit_cow_modal']/div[1]/div/div")
        book_edit_box=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='edit_cow_modal']/div[@class='modal-body']/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='bookNumber']/div[@class='controls']/input[@id='book_number']")
        burn_edit_box=self.is_element_present(By.XPATH,"//html/body[@id='top']/div[@id='modal-container']/div[@id='edit_cow_modal']/div[@class='modal-body']/div[1]/div[1]/form[@class='form-horizontal']/div[@data-wm-item='burnNumber']/div[@class='controls']/input[@id='burn_number']")
        if (exsist_record_title and book_edit_box and burn_edit_box):
            return True
        else:
             self.take_screenshot("Fail_open_exist_Cow_card")
             self.loggertest(self.__class__.__name__,'Could not open exsist Cow Card')
             self.fail("Fail open exsist Cow Card")
             return False


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
    def test_2_AddNewCowCard_on_IE(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Create new Cow cards_on_IE started at :'+date_time_formatted
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
              self.driver.implicitly_wait(10)
              DistressDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Distress']")
              NoId=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='NoId']")
              GroupAlertsDatareportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='GroupAlerts']")
        except NoSuchElementException:
             self.take_screenshot("Data_Tab_not_loaded_fully")
             self.loggertest(self.__class__.__name__,'Check if Data tab loaded...')
             self.fail("The Data tab not loaded ")

        #Start switch and check between first and second page report of All Cows by use Right/Left Arrows
                  #Create A new Cow Cards
        new_cow_book_numbers=['100000','200000']
        new_cow_burn_numbers=['100000','200000']
        scr_tag_number=['100000','200000']
        iso_number=['100000','200000']
        lactation=['1','2']
        for x in range(0,2,1):
             self.driver.maximize_window()
             #Open a New Cow Card
             result_open_cow_record=self.open_new_cow_record()
             if result_open_cow_record:
                 #Fill opened New Cow Card
                 attempt_edit_card_details=self.fill_new_record(new_cow_book_numbers[x],new_cow_burn_numbers[x],scr_tag_number[x],iso_number[x],lactation[x])
                 #If user fill cow card and Apply it check if cow card exist
                 if attempt_edit_card_details:
                     look_for_cow_card=self.check_cow_card_create_result(new_cow_book_numbers[x],new_cow_burn_numbers[x])
                     if look_for_cow_card:
                        print "Success created cow card :"+new_cow_burn_numbers[x]
                     else:
                        print "Fail find new cow card :"+new_cow_burn_numbers[x]
                 else:
                      print "Fail fill cow card :"+new_cow_burn_numbers[x]
             else:
                self.take_screenshot("Fail_open_cow_card")
                self.loggertest(self.__class__.__name__,'Fail_open_cow_card')
                self.fail("Fail_open_cow_card")

        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test of Create new Cow Card_on_IE finish at :'+date_time_formatted
    def test_3_DeleteCowCard_on_IE(self):
        #open Data tab
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Delete cards_on_IE started at :'+date_time_formatted
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
              self.driver.implicitly_wait(10)
              DistressDataReportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='Distress']")
              NoId=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='NoId']")
              GroupAlertsDatareportBtn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[1]/div[1]/div[@id='data-pane']/div[@id='list']/div[@id='filters-container']/ul[@id='filters']/li[@data-report='GroupAlerts']")
        except NoSuchElementException:
             self.take_screenshot("Data_Tab_not_loaded_fully")
             self.loggertest(self.__class__.__name__,'Check if Data tab loaded...')
             self.fail("The Data tab not loaded ")

        #Start switch and check between first and second page report of All Cows by use Right/Left Arrows
                  #Create A new Cow Cards
        new_cow_book_numbers=['100000','200000']
        new_cow_burn_numbers=['100000','200000']
        for x in range(0,2,1):
             self.driver.maximize_window()
             #Open a New Cow Card
             result=self.find_cow_card(new_cow_book_numbers[x])
             # On this point user should get a correct opened exsist Cow Card that should be deleted
             if result:
                 deletecow=self.driver.find_element_by_xpath(".//*[@id='delete_cow']/div")
                 deletecow.click()
                 self.driver.implicitly_wait(10)
                 warn_message=self.driver.find_element_by_xpath(".//*[@id='confirm']")
                 deletebtn=self.driver.find_element_by_xpath(".//*[@id='confirm_delete_cow']")
                 if (warn_message.is_displayed() and deletebtn.is_displayed()):
                     #Ready for delete
                     deletebtn.click()
                     self.driver.implicitly_wait(20)
                     time.sleep(3)
                     print 'The Cow Card of cow :'+new_cow_burn_numbers[x]+' was deleted successfully.'
                 else:
                     self.take_screenshot("Can_not_get_warning_message_before_delete")
                     print 'The Cow Card of cow :'+new_cow_burn_numbers[x]+' Failed!!!'
                     self.loggertest(self.__class__.__name__,'Did not get a delete message and delete button')
                     self.fail("Did not get a delete message and delete button")
             else:
                self.take_screenshot("Delete_process_fail")
                self.loggertest(self.__class__.__name__,'Stuck on opened cow card and could not delete')
                self.fail("Stuck on opened cow card and could not delete")
             self.driver.refresh()
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test of Delete Cow Cards_on_IE finish at :'+date_time_formatted


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



