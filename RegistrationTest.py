import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
import time
import os,sys
#pytest use for order testcase running order
#import pytest
from datetime import datetime
__author__ = 'sergey.meerovich'


class RegistrationTestFirefox(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #create a new Firefox session
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
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



    def test_1_Registretion_New_mail_process_on_Firefox(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Firefox started at :'+date_time_formatted
        dateTime=date_time.strftime("%d%m%Y%H%M%S")
        #Launch to Yopmail web-site
        self.driver.get("http://www.yopmail.com/en/")
        self.driver.implicitly_wait(15)
        main_window = self.driver.current_window_handle
        mail_name="scrRegTest"+str(dateTime)+"@yopmail.com"
        #print mail_name
        mail_edit_box=self.is_element_present(By.XPATH,".//*[@id='login']")
        Mail_Edit_Box=self.driver.find_element_by_xpath(".//*[@id='login']")
        Mail_Edit_Box.click()
        #time.sleep(1)
        Mail_Edit_Box.clear()
        Mail_Edit_Box.send_keys(mail_name)
        CheckInbox=self.driver.find_element_by_xpath(".//*[@id='f']/table/tbody/tr[1]/td[3]/input")
        CheckInbox.click()
        self.driver.implicitly_wait(20)
        #Check if user login to created mail ..
        check_new_mails=self.is_element_present(By.XPATH,".//*[@id='lrefr']/span/span")
        write_mail=self.is_element_present(By.XPATH,".//*[@id='wrmail']")
        if (check_new_mails and write_mail):
            pass
        else:
            self.take_screenshot('Fail_Enter_to_new_mail')
            self.fail("There is problem login to created mail")

        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Registration_process_on_Firefox finish at :'+date_time_formatted
        #close the browser window of mail web-site
        #self.driver.quit()
        llll=Keys.ch
        body=self.driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL+'t')
        self.driver.get("https://hc24-qalab-web.scrdairy.com/")
        self.driver.implicitly_wait(30)
        # start sign up process
        sign_up=self.driver.find_element_by_xpath(".//*[@id='register']")
        sign_up.click()
        self.driver.implicitly_wait(20)
        try:
           signupURL=self.driver.current_url
           accountCreation=self.driver.find_element_by_xpath(".//*[@id='app']/div/div[1]/div[2]/span[2]").text
           if (signupURL=="https://hc24-qalab-web.scrdairy.com/#accounts/register/signup" and accountCreation=="Account Creation"):
               print "You succesfully reach to Sign up page"
           else:
               print "User did not reach to Sign up page"
        except:
            self.loggertest(self.__class__.__name__,'There is problem reach to sign up page...')
            self.take_screenshot('Fail_Reach_to_sign_up_page')
            self.fail("There is problem reach to Sign up page")
        #Start fill Account details
        try:
           Firstname=self.driver.find_element_by_xpath(".//*[@id='first_name']")
           Firstname.send_keys("")
           Firstname.clear()
           Firstname.send_keys("PortalAutomation")
           LastName=self.driver.find_element_by_xpath(".//*[@id='last_name']")
           LastName.send_keys("")
           LastName.clear()
           LastName.send_keys("PortalAutomation")
           phoneNum=self.driver.find_element_by_xpath(".//*[@id='tel_number0']")
           phoneNum.send_keys("")
           phoneNum.clear()
           phoneNum.send_keys("123456789")
           usremail=self.driver.find_element_by_xpath(".//*[@id='email']")
           usremail.send_keys("")
           usremail.clear()
           usremail.send_keys(mail_name)
           confirmusrmail=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[@class='signup-container']/div[2]/form[@id='frmRegister']/div[@class='fields-form']/div[6]/input[@id='confirm_email']")
           confirmusrmail.send_keys("")
           confirmusrmail.clear()
           confirmusrmail.send_keys(mail_name)
           usrpassword=self.driver.find_element_by_xpath(".//*[@id='password']")
           usrpassword.send_keys("")
           usrpassword.clear()
           usrpassword.send_keys("123")
           dealer=self.driver.find_element_by_xpath(".//*[@id='dealer']")
           dealer.send_keys("")
           dealer.clear()
           dealer.send_keys("123")
        except NoSuchElementException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Did not detect one of the fields : Firstname,Lastname,phonename,usermail,confirmmail,dealer')
           self.take_screenshot('Fail_dind_Firstname_Lastname_phonename_usermail_confirmmail_dealer')
           self.fail("id not detect one of the fields : Firstname,Lastname,phonename,usermail,confirmmail,dealer")
        #scroll page dowm
        try:
           self.driver.execute_script("window.scrollTo(0, 200)")
           time.sleep(1)
           f=self.driver.find_element_by_xpath(".//*[@id='farm_type_chzn']/a/span")
           f.click()
           g=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[@class='signup-container']/div[2]/form[@id='frmRegister']/div[@class='fields-form']/div[2]/div[@id='farm_type_chzn']/div[@class='chzn-drop']/div[1]/input")
           g.clear()
           g.send_keys("Free stall")
           #time.sleep(1)
           g.send_keys(Keys.ENTER)
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail choose Farm Type')
           self.take_screenshot('Fail_choose_farm_type')
           self.fail("Fail choose Farm type")
        try:
           frmname=self.driver.find_element_by_xpath(".//*[@id='farm_name']")
           frmname.send_keys("")
           frmname.send_keys("AutoTestFarm"+str(dateTime))
           frmlocation=self.driver.find_element_by_xpath(".//*[@id='farm_country_chzn']/a/span")
           frmlocation.click()
           FarmLocationName=self.driver.find_element_by_xpath(".//*[@id='farm_country_chzn']/div/div/input")
           FarmLocationName.clear()
           FarmLocationName.send_keys("Israel")
           #time.sleep(1)
           FarmLocationName.send_keys(Keys.ENTER)
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail on Farm name or Farm location')
           self.take_screenshot('Fail_during_farm_name_farm_location')
           self.fail("Fail fill farm name or farm location")
        try:
           frmaddress=self.driver.find_element_by_xpath(".//*[@id='farm_address']")
           frmaddress.send_keys("")
           frmaddress.send_keys("Petah Tikva, st. Ben-Gurion 1")
           frmpostcode=self.driver.find_element_by_xpath(".//*[@id='farm_postal']")
           frmpostcode.send_keys("")
           frmpostcode.send_keys("49632")
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail during fill Farm Address,post code')
           self.take_screenshot('Fail_during_fill_Farm_address_postcode')
           self.fail("Fail fill farm Address or postcode")
        try:
          frmbreeds=self.driver.find_element_by_xpath(".//*[@id='farm_breeds_chzn']/ul/li/input")
          frmbreeds.send_keys("")
          frmbreeds.send_keys("Jersey")
          frmbreeds.send_keys(Keys.ENTER)
          frmprivacy=self.driver.find_element_by_xpath(".//*[@id='cb_iagree']")
          frmprivacy.click()
          frmtrial=self.driver.find_element_by_xpath(".//*[@id='cb_trialVersion']")
          frmtrial.click()
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail during fill Farm breeds and agree on Privacy and Trial period')
           self.take_screenshot('Fail_during_fill_Farm_Breeds_Privacy_Agreement_Trial')
           self.fail("Fail during fill Farm breeds and agree on Privacy and Trial period")
        try:
            frmcreateBtn=self.driver.find_element_by_xpath(".//*[@id='btnReg']")
            frmcreateBtn.click()
            time.sleep(10)
            self.driver.implicitly_wait(15)
            webpageafterSignUp=self.driver.current_url
            print webpageafterSignUp
            #print "https://hc24-qalab-web.scrdairy.com/#accounts/register/email_sent/"+mail_name+"/?lang=undefined"
            if webpageafterSignUp=="https://hc24-qalab-web.scrdairy.com/#accounts/register/email_sent/"+mail_name+"/?lang=undefined":
               print "Successfully pass sign-up process"
            else:
               self.loggertest(self.__class__.__name__,'Fail during click on Create Account')
               self.take_screenshot('Fail_during_Click_Create_Acccount')
               self.fail("Fail during click on Create Account")
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail get to web page after fill Sign up details')
           self.take_screenshot('Sign_up_did_not_launch_to_success_page')
           self.fail("Fail get to web page after fill Sign up details")
        try:
           FarmOwnerHeader=self.is_element_present(By.XPATH,".//*[@id='app']/div/div/div[1]/div[2]/span[1]")
           ResendActivationMailBtn=self.is_element_present(By.XPATH,".//*[@id='btnLogin']")
           HeaderThanksYouForSignUp=self.is_element_present(By.XPATH,".//*[@id='app']/div/div/div[2]/form/h1")
           if (FarmOwnerHeader and ResendActivationMailBtn and HeaderThanksYouForSignUp):
               pass
               # return to mail page
               print "You pass Registration page..."
               b=self.driver.find_element_by_tag_name('body')
               b.send_keys(Keys.CONTROL,Keys.SHIFT,Keys.TAB)
               self.driver.switch_to.window(main_window)
           else:
               self.fail("Fail pass registration Page")
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail pass registration page and send mail')
           self.take_screenshot('Sign_up_did_not_launch_to_success_page')
           self.fail("Fail during pass Registration page")
        try:
           #self.driver.refresh()
           time.sleep(1)
           #check that registration mail arrieves...
           for x in range(0,5,1):
              checkmailbtn=self.is_element_present(By.XPATH,".//*[@id='lrefr']/span/span")
              if (checkmailbtn):
                  checkMailBtn=self.driver.find_element_by_xpath(".//*[@id='lrefr']/span/span")
                  checkMailBtn.click()
                  print "Refresh to check if mail received..."
                  time.sleep(10)
                  inboxframe=self.driver.find_element_by_xpath("//iframe[@name='ifinbox']")
                  self.driver.switch_to.frame(inboxframe)
                  p=self.driver.find_element_by_xpath("//html/body/div/div[7]/div/a/span[2]").text
                  if(p=='Complete your HC24 registration process'):
                      print 'You successfully receive registration mail !'
                  else:
                      self.driver.close()
                      self.loggertest(self.__class__.__name__,'Fail receive registration mail')
                      self.take_screenshot('Fail_receive_mail')
                      self.fail("Fail receive registration mail")
                  #back to main iframe
                  self.driver.switch_to.default_content()
                  #Click on Link that mail contain
                  mailframe=self.driver.find_element_by_xpath("//iframe[@name='ifmail']")
                  self.driver.switch_to.frame(mailframe)
                  ff=self.is_element_present(By.XPATH,"//html/body/div/div[3]/div[2]/div/table/tbody/tr/td/p[2]/a")
                  c=self.driver.find_element_by_xpath('//html/body/div/div[3]/div[2]/div/table/tbody/tr/td/p[2]/a').text
                  print c
                  body2=self.driver.find_element_by_tag_name('body')
                  body2.send_keys(Keys.CONTROL+'t')
                  self.driver.get(c)
                  time.sleep(4)
                  #check that activation mail open relevant page
                  #TODO
                  break
              else:
                  x=x+1
                  time.sleep(5)
                  checkMailBtn=self.driver.find_element_by_xpath(".//*[@id='lrefr']/span/span")
                  checkMailBtn.click()
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail during click on Activation mail Link')
           self.take_screenshot('Sign_up_did_not_launch_to_success_page')
           self.fail("Fail during click on Activation mail Link")

    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()





class RegistrationTestChrome(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #get path of chromedriver
        dir=os.path.dirname(__file__)
        chrome_drive_path=dir+"/chromedriver.exe"
        #create a new Chrome session
        self.driver=webdriver.Chrome(chrome_drive_path)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()


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



    def test_1_Registretion_New_mail_process_on_Chrome(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Registration_process_on_Chrome started at :'+date_time_formatted
        dateTime=date_time.strftime("%d%m%Y%H%M%S")
        #Launch to Yopmail web-site
        self.driver.get("http://www.yopmail.com/en/")
        self.driver.implicitly_wait(15)
        main_window = self.driver.current_window_handle
        mail_name="scrRegTest"+str(dateTime)+"@yopmail.com"
        #print mail_name
        mail_edit_box=self.is_element_present(By.XPATH,".//*[@id='login']")
        Mail_Edit_Box=self.driver.find_element_by_xpath(".//*[@id='login']")
        Mail_Edit_Box.click()
        #time.sleep(1)
        Mail_Edit_Box.clear()
        Mail_Edit_Box.send_keys(mail_name)
        CheckInbox=self.driver.find_element_by_xpath(".//*[@id='f']/table/tbody/tr[1]/td[3]/input")
        CheckInbox.click()
        self.driver.implicitly_wait(20)
        #Check if user login to created mail ..
        check_new_mails=self.is_element_present(By.XPATH,".//*[@id='lrefr']/span/span")
        write_mail=self.is_element_present(By.XPATH,".//*[@id='wrmail']")
        if (check_new_mails and write_mail):
            pass
        else:
            self.take_screenshot('Fail_Enter_to_new_mail')
            self.fail("There is problem login to created mail")

        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_Firefox finish at :'+date_time_formatted
        #close the browser window of mail web-site
        #self.driver.quit()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t')
        #body.send_keys(Keys.CONTROL+'t')
        #newTab=ActionChains(self.driver)

        #newTab.send_keys(Keys.CONTROL+"t").perform()
        self.driver.get("https://hc24-qalab-web.scrdairy.com/")
        self.driver.implicitly_wait(30)
        # start sign up process
        sign_up=self.driver.find_element_by_xpath(".//*[@id='register']")
        sign_up.click()
        self.driver.implicitly_wait(20)
        try:
           signupURL=self.driver.current_url
           accountCreation=self.driver.find_element_by_xpath(".//*[@id='app']/div/div[1]/div[2]/span[2]").text
           if (signupURL=="https://hc24-qalab-web.scrdairy.com/#accounts/register/signup" and accountCreation=="Account Creation"):
               print "You succesfully reach to Sign up page"
           else:
               print "User did not reach to Sign up page"
        except:
            self.loggertest(self.__class__.__name__,'There is problem reach to sign up page...')
            self.take_screenshot('Fail_Reach_to_sign_up_page')
            self.fail("There is problem reach to Sign up page")
        #Start fill Account details
        try:
           Firstname=self.driver.find_element_by_xpath(".//*[@id='first_name']")
           Firstname.send_keys("")
           Firstname.clear()
           Firstname.send_keys("PortalAutomation")
           LastName=self.driver.find_element_by_xpath(".//*[@id='last_name']")
           LastName.send_keys("")
           LastName.clear()
           LastName.send_keys("PortalAutomation")
           phoneNum=self.driver.find_element_by_xpath(".//*[@id='tel_number0']")
           phoneNum.send_keys("")
           phoneNum.clear()
           phoneNum.send_keys("123456789")
           usremail=self.driver.find_element_by_xpath(".//*[@id='email']")
           usremail.send_keys("")
           usremail.clear()
           usremail.send_keys(mail_name)
           confirmusrmail=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[@class='signup-container']/div[2]/form[@id='frmRegister']/div[@class='fields-form']/div[6]/input[@id='confirm_email']")
           confirmusrmail.send_keys("")
           confirmusrmail.clear()
           confirmusrmail.send_keys(mail_name)
           usrpassword=self.driver.find_element_by_xpath(".//*[@id='password']")
           usrpassword.send_keys("")
           usrpassword.clear()
           usrpassword.send_keys("123")
           dealer=self.driver.find_element_by_xpath(".//*[@id='dealer']")
           dealer.send_keys("")
           dealer.clear()
           dealer.send_keys("123")
        except NoSuchElementException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Did not detect one of the fields : Firstname,Lastname,phonename,usermail,confirmmail,dealer')
           self.take_screenshot('Fail_dind_Firstname_Lastname_phonename_usermail_confirmmail_dealer')
           self.fail("id not detect one of the fields : Firstname,Lastname,phonename,usermail,confirmmail,dealer")
        #scroll page dowm
        try:
           self.driver.execute_script("window.scrollTo(0, 200)")
           time.sleep(1)
           f=self.driver.find_element_by_xpath(".//*[@id='farm_type_chzn']/a/span")
           f.click()
           g=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[@class='signup-container']/div[2]/form[@id='frmRegister']/div[@class='fields-form']/div[2]/div[@id='farm_type_chzn']/div[@class='chzn-drop']/div[1]/input")
           g.clear()
           g.send_keys("Free stall")
           #time.sleep(1)
           g.send_keys(Keys.ENTER)
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail choose Farm Type')
           self.take_screenshot('Fail_choose_farm_type')
           self.fail("Fail choose Farm type")
        try:
           frmname=self.driver.find_element_by_xpath(".//*[@id='farm_name']")
           frmname.send_keys("")
           frmname.send_keys("AutoTestFarm"+str(dateTime))
           frmlocation=self.driver.find_element_by_xpath(".//*[@id='farm_country_chzn']/a/span")
           frmlocation.click()
           FarmLocationName=self.driver.find_element_by_xpath(".//*[@id='farm_country_chzn']/div/div/input")
           FarmLocationName.clear()
           FarmLocationName.send_keys("Israel")
           #time.sleep(1)
           FarmLocationName.send_keys(Keys.ENTER)
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail on Farm name or Farm location')
           self.take_screenshot('Fail_during_farm_name_farm_location')
           self.fail("Fail fill farm name or farm location")
        try:
           frmaddress=self.driver.find_element_by_xpath(".//*[@id='farm_address']")
           frmaddress.send_keys("")
           frmaddress.send_keys("Petah Tikva, st. Ben-Gurion 1")
           frmpostcode=self.driver.find_element_by_xpath(".//*[@id='farm_postal']")
           frmpostcode.send_keys("")
           frmpostcode.send_keys("49632")
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail during fill Farm Address,post code')
           self.take_screenshot('Fail_during_fill_Farm_address_postcode')
           self.fail("Fail fill farm Address or postcode")
        try:
          frmbreeds=self.driver.find_element_by_xpath(".//*[@id='farm_breeds_chzn']/ul/li/input")
          frmbreeds.send_keys("")
          frmbreeds.send_keys("Jersey")
          frmbreeds.send_keys(Keys.ENTER)
          frmprivacy=self.driver.find_element_by_xpath(".//*[@id='cb_iagree']")
          frmprivacy.click()
          frmtrial=self.driver.find_element_by_xpath(".//*[@id='cb_trialVersion']")
          frmtrial.click()
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail during fill Farm breeds and agree on Privacy and Trial period')
           self.take_screenshot('Fail_during_fill_Farm_Breeds_Privacy_Agreement_Trial')
           self.fail("Fail during fill Farm breeds and agree on Privacy and Trial period")
        try:
            frmcreateBtn=self.driver.find_element_by_xpath(".//*[@id='btnReg']")
            frmcreateBtn.click()
            time.sleep(10)
            self.driver.implicitly_wait(15)
            webpageafterSignUp=self.driver.current_url
            print webpageafterSignUp
            #print "https://hc24-qalab-web.scrdairy.com/#accounts/register/email_sent/"+mail_name+"/?lang=undefined"
            if webpageafterSignUp=="https://hc24-qalab-web.scrdairy.com/#accounts/register/email_sent/"+mail_name+"/?lang=undefined":
               print "Successfully pass sign-up process"
            else:
               self.loggertest(self.__class__.__name__,'Fail during click on Create Account')
               self.take_screenshot('Fail_during_Click_Create_Acccount')
               self.fail("Fail during click on Create Account")
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail get to web page after fill Sign up details')
           self.take_screenshot('Sign_up_did_not_launch_to_success_page')
           self.fail("Fail get to web page after fill Sign up details")
        try:
           FarmOwnerHeader=self.is_element_present(By.XPATH,".//*[@id='app']/div/div/div[1]/div[2]/span[1]")
           ResendActivationMailBtn=self.is_element_present(By.XPATH,".//*[@id='btnLogin']")
           HeaderThanksYouForSignUp=self.is_element_present(By.XPATH,".//*[@id='app']/div/div/div[2]/form/h1")
           if (FarmOwnerHeader and ResendActivationMailBtn and HeaderThanksYouForSignUp):
               pass
               # return to mail page
               print "You pass Registration page..."
               b=self.driver.find_element_by_tag_name('body')
               b.send_keys(Keys.CONTROL,Keys.SHIFT,Keys.TAB)
               self.driver.switch_to.window(main_window)
           else:
               self.fail("Fail pass registration Page")
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail pass registration page and send mail')
           self.take_screenshot('Sign_up_did_not_launch_to_success_page')
           self.fail("Fail during pass Registration page")
        try:
           #self.driver.refresh()
           time.sleep(1)
           #check that registration mail arrieves...
           for x in range(0,5,1):
              checkmailbtn=self.is_element_present(By.XPATH,".//*[@id='lrefr']/span/span")
              if (checkmailbtn):
                  checkMailBtn=self.driver.find_element_by_xpath(".//*[@id='lrefr']/span/span")
                  checkMailBtn.click()
                  print "Refresh to check if mail received..."
                  time.sleep(10)
                  inboxframe=self.driver.find_element_by_xpath("//iframe[@name='ifinbox']")
                  self.driver.switch_to.frame(inboxframe)
                  p=self.driver.find_element_by_xpath("//html/body/div/div[7]/div/a/span[2]").text
                  if(p=='Complete your HC24 registration process'):
                      print 'You successfully receive registration mail !'
                  else:
                      self.driver.close()
                      self.loggertest(self.__class__.__name__,'Fail receive registration mail')
                      self.take_screenshot('Fail_receive_mail')
                      self.fail("Fail receive registration mail")
                  #back to main iframe
                  self.driver.switch_to.default_content()
                  #Click on Link that mail contain
                  mailframe=self.driver.find_element_by_xpath("//iframe[@name='ifmail']")
                  self.driver.switch_to.frame(mailframe)
                  ff=self.is_element_present(By.XPATH,"//html/body/div/div[3]/div[2]/div/table/tbody/tr/td/p[2]/a")
                  c=self.driver.find_element_by_xpath('//html/body/div/div[3]/div[2]/div/table/tbody/tr/td/p[2]/a').text
                  print c
                  body2=self.driver.find_element_by_tag_name('body')
                  body2.send_keys(Keys.CONTROL+'t')
                  self.driver.get(c)
                  time.sleep(4)
                  #check that activation mail open relevant page
                  #TODO
                  break
              else:
                  x=x+1
                  time.sleep(5)
                  checkMailBtn=self.driver.find_element_by_xpath(".//*[@id='lrefr']/span/span")
                  checkMailBtn.click()
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail during click on Activation mail Link')
           self.take_screenshot('Sign_up_did_not_launch_to_success_page')
           self.fail("Fail during click on Activation mail Link")
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test of Registration process and Activation is finished at ::'+date_time_formatted


    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()

class RegistrationTestIE(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #get path of chromedriver
        dir=os.path.dirname(__file__)
        ie_drive_path=dir+"/IEDriverServer.exe"
        #create a new Internet Explorer session
        self.driver=webdriver.Ie(ie_drive_path)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
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


    def test_1_Registretion_New_mail_process_on_IE(self):
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Registration_process_on_IE started at :'+date_time_formatted
        dateTime=date_time.strftime("%d%m%Y%H%M%S")
        #Launch to Yopmail web-site
        self.driver.get("http://www.yopmail.com/en/")
        self.driver.implicitly_wait(15)
        main_window = self.driver.current_window_handle
        mail_name="scrRegTest"+str(dateTime)+"@yopmail.com"
        #print mail_name
        mail_edit_box=self.is_element_present(By.XPATH,".//*[@id='login']")
        Mail_Edit_Box=self.driver.find_element_by_xpath(".//*[@id='login']")
        Mail_Edit_Box.click()
        #time.sleep(1)
        Mail_Edit_Box.clear()
        Mail_Edit_Box.send_keys(mail_name)
        CheckInbox=self.driver.find_element_by_xpath(".//*[@id='f']/table/tbody/tr[1]/td[3]/input")
        CheckInbox.click()
        self.driver.implicitly_wait(20)
        #Check if user login to created mail ..
        check_new_mails=self.is_element_present(By.XPATH,".//*[@id='lrefr']/span/span")
        write_mail=self.is_element_present(By.XPATH,".//*[@id='wrmail']")
        if (check_new_mails and write_mail):
            pass
        else:
            self.take_screenshot('Fail_Enter_to_new_mail')
            self.fail("There is problem login to created mail")
        #close the browser window of mail web-site
        #self.driver.quit()
        body=self.driver.find_element_by_tag_name('body')
        body.send_keys(Keys.CONTROL+'t')
        self.driver.get("https://hc24-qalab-web.scrdairy.com/")
        self.driver.implicitly_wait(30)
        # start sign up process
        sign_up=self.driver.find_element_by_xpath(".//*[@id='register']")
        sign_up.click()
        self.driver.implicitly_wait(20)
        try:
           signupURL=self.driver.current_url
           accountCreation=self.driver.find_element_by_xpath(".//*[@id='app']/div/div[1]/div[2]/span[2]").text
           if (signupURL=="https://hc24-qalab-web.scrdairy.com/#accounts/register/signup" and accountCreation=="Account Creation"):
               print "You succesfully reach to Sign up page"
           else:
               print "User did not reach to Sign up page"
        except:
            self.loggertest(self.__class__.__name__,'There is problem reach to sign up page...')
            self.take_screenshot('Fail_Reach_to_sign_up_page')
            self.fail("There is problem reach to Sign up page")
        #Start fill Account details
        try:
           Firstname=self.driver.find_element_by_xpath(".//*[@id='first_name']")
           Firstname.send_keys("")
           Firstname.clear()
           Firstname.send_keys("PortalAutomation")
           LastName=self.driver.find_element_by_xpath(".//*[@id='last_name']")
           LastName.send_keys("")
           LastName.clear()
           LastName.send_keys("PortalAutomation")
           phoneNum=self.driver.find_element_by_xpath(".//*[@id='tel_number0']")
           phoneNum.send_keys("")
           phoneNum.clear()
           phoneNum.send_keys("123456789")
           usremail=self.driver.find_element_by_xpath(".//*[@id='email']")
           usremail.send_keys("")
           usremail.clear()
           usremail.send_keys(mail_name)
           confirmusrmail=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[@class='signup-container']/div[2]/form[@id='frmRegister']/div[@class='fields-form']/div[6]/input[@id='confirm_email']")
           confirmusrmail.send_keys("")
           confirmusrmail.clear()
           confirmusrmail.send_keys(mail_name)
           usrpassword=self.driver.find_element_by_xpath(".//*[@id='password']")
           usrpassword.send_keys("")
           usrpassword.clear()
           usrpassword.send_keys("123")
           dealer=self.driver.find_element_by_xpath(".//*[@id='dealer']")
           dealer.send_keys("")
           dealer.clear()
           dealer.send_keys("123")
        except NoSuchElementException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Did not detect one of the fields : Firstname,Lastname,phonename,usermail,confirmmail,dealer')
           self.take_screenshot('Fail_dind_Firstname_Lastname_phonename_usermail_confirmmail_dealer')
           self.fail("id not detect one of the fields : Firstname,Lastname,phonename,usermail,confirmmail,dealer")
        #scroll page dowm
        try:
           self.driver.execute_script("window.scrollTo(0, 200)")
           time.sleep(1)
           f=self.driver.find_element_by_xpath(".//*[@id='farm_type_chzn']/a/span")
           f.click()
           g=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[@class='signup-container']/div[2]/form[@id='frmRegister']/div[@class='fields-form']/div[2]/div[@id='farm_type_chzn']/div[@class='chzn-drop']/div[1]/input")
           g.clear()
           g.send_keys("Free stall")
           #time.sleep(1)
           g.send_keys(Keys.ENTER)
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail choose Farm Type')
           self.take_screenshot('Fail_choose_farm_type')
           self.fail("Fail choose Farm type")
        try:
           frmname=self.driver.find_element_by_xpath(".//*[@id='farm_name']")
           frmname.send_keys("")
           frmname.send_keys("AutoTestFarm"+str(dateTime))
           frmlocation=self.driver.find_element_by_xpath(".//*[@id='farm_country_chzn']/a/span")
           frmlocation.click()
           FarmLocationName=self.driver.find_element_by_xpath(".//*[@id='farm_country_chzn']/div/div/input")
           FarmLocationName.clear()
           FarmLocationName.send_keys("Israel")
           #time.sleep(1)
           FarmLocationName.send_keys(Keys.ENTER)
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail on Farm name or Farm location')
           self.take_screenshot('Fail_during_farm_name_farm_location')
           self.fail("Fail fill farm name or farm location")
        try:
           frmaddress=self.driver.find_element_by_xpath(".//*[@id='farm_address']")
           frmaddress.send_keys("")
           frmaddress.send_keys("Petah Tikva, st. Ben-Gurion 1")
           frmpostcode=self.driver.find_element_by_xpath(".//*[@id='farm_postal']")
           frmpostcode.send_keys("")
           frmpostcode.send_keys("49632")
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail during fill Farm Address,post code')
           self.take_screenshot('Fail_during_fill_Farm_address_postcode')
           self.fail("Fail fill farm Address or postcode")
        try:
          frmbreeds=self.driver.find_element_by_xpath(".//*[@id='farm_breeds_chzn']/ul/li/input")
          frmbreeds.send_keys("")
          frmbreeds.send_keys("Jersey")
          frmbreeds.send_keys(Keys.ENTER)
          frmprivacy=self.driver.find_element_by_xpath(".//*[@id='cb_iagree']")
          frmprivacy.click()
          frmtrial=self.driver.find_element_by_xpath(".//*[@id='cb_trialVersion']")
          frmtrial.click()
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail during fill Farm breeds and agree on Privacy and Trial period')
           self.take_screenshot('Fail_during_fill_Farm_Breeds_Privacy_Agreement_Trial')
           self.fail("Fail during fill Farm breeds and agree on Privacy and Trial period")
        try:
            frmcreateBtn=self.driver.find_element_by_xpath(".//*[@id='btnReg']")
            frmcreateBtn.click()
            time.sleep(10)
            self.driver.implicitly_wait(15)
            webpageafterSignUp=self.driver.current_url
            print webpageafterSignUp
            #print "https://hc24-qalab-web.scrdairy.com/#accounts/register/email_sent/"+mail_name+"/?lang=undefined"
            if webpageafterSignUp=="https://hc24-qalab-web.scrdairy.com/#accounts/register/email_sent/"+mail_name+"/?lang=undefined":
               print "Successfully pass sign-up process"
            else:
               self.loggertest(self.__class__.__name__,'Fail during click on Create Account')
               self.take_screenshot('Fail_during_Click_Create_Acccount')
               self.fail("Fail during click on Create Account")
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail get to web page after fill Sign up details')
           self.take_screenshot('Sign_up_did_not_launch_to_success_page')
           self.fail("Fail get to web page after fill Sign up details")
        try:
           FarmOwnerHeader=self.is_element_present(By.XPATH,".//*[@id='app']/div/div/div[1]/div[2]/span[1]")
           ResendActivationMailBtn=self.is_element_present(By.XPATH,".//*[@id='btnLogin']")
           HeaderThanksYouForSignUp=self.is_element_present(By.XPATH,".//*[@id='app']/div/div/div[2]/form/h1")
           if (FarmOwnerHeader and ResendActivationMailBtn and HeaderThanksYouForSignUp):
               pass
               # return to mail page
               print "You pass Registration page..."
               b=self.driver.find_element_by_tag_name('body')
               b.send_keys(Keys.CONTROL,Keys.SHIFT,Keys.TAB)
               self.driver.switch_to.window(main_window)
           else:
               self.fail("Fail pass registration Page")
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail pass registration page and send mail')
           self.take_screenshot('Sign_up_did_not_launch_to_success_page')
           self.fail("Fail during pass Registration page")
        try:
           #self.driver.refresh()
           time.sleep(1)
           #check that registration mail arrieves...
           for x in range(0,5,1):
              checkmailbtn=self.is_element_present(By.XPATH,".//*[@id='lrefr']/span/span")
              if (checkmailbtn):
                  checkMailBtn=self.driver.find_element_by_xpath(".//*[@id='lrefr']/span/span")
                  checkMailBtn.click()
                  print "Refresh to check if mail received..."
                  time.sleep(10)
                  inboxframe=self.driver.find_element_by_xpath("//iframe[@name='ifinbox']")
                  self.driver.switch_to.frame(inboxframe)
                  p=self.driver.find_element_by_xpath("//html/body/div/div[7]/div/a/span[2]").text
                  if(p=='Complete your HC24 registration process'):
                      print 'You successfully receive registration mail !'
                  else:
                      self.driver.close()
                      self.loggertest(self.__class__.__name__,'Fail receive registration mail')
                      self.take_screenshot('Fail_receive_mail')
                      self.fail("Fail receive registration mail")
                  #back to main iframe
                  self.driver.switch_to.default_content()
                  #Click on Link that mail contain
                  mailframe=self.driver.find_element_by_xpath("//iframe[@name='ifmail']")
                  self.driver.switch_to.frame(mailframe)
                  ff=self.is_element_present(By.XPATH,"//html/body/div/div[3]/div[2]/div/table/tbody/tr/td/p[2]/a")
                  c=self.driver.find_element_by_xpath('//html/body/div/div[3]/div[2]/div/table/tbody/tr/td/p[2]/a').text
                  print c
                  body2=self.driver.find_element_by_tag_name('body')
                  body2.send_keys(Keys.CONTROL+'t')
                  self.driver.get(c)
                  time.sleep(4)
                  #check that activation mail open relevant page
                  #TODO
                  break
              else:
                  x=x+1
                  time.sleep(5)
                  checkMailBtn=self.driver.find_element_by_xpath(".//*[@id='lrefr']/span/span")
                  checkMailBtn.click()
        except NoSuchElementException,ElementNotVisibleException:
           self.driver.close()
           self.loggertest(self.__class__.__name__,'Fail during click on Activation mail Link')
           self.take_screenshot('Sign_up_did_not_launch_to_success_page')
           self.fail("Fail during click on Activation mail Link")
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test of Registration process and Activation is finished at :'+date_time_formatted


    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()




if __name__=='__main__':
    unittest.main(verbosity=2)



