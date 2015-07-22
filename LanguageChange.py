# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os
#use for loging console
import logging



from datetime import datetime
__author__ = 'sergey.meerovich'


class LanguageChangeTestFirefox(unittest.TestCase):
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
        #p=webdriver.FirefoxProfile()
        #p.set_preference('webdriver.log','C:\Users\sergey.meerovich\Desktop\Selenium\ConsoleLogs')

        #driver=webdriver.Firefox(p)
       # print str(new_dir)+"/"+TestName+browserType+".log"
        #logging.info('Start log:')
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
                 self.take_screenshot('Fail log-out')
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
    def test_2_Language_Change_on_Firefox(self):
        #test_2DashboardDataSwitch_process_on_Firefox
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch_languages_on_Settings_on_Firefox started at :'+date_time_formatted
        #open 'Settings' window
        settings_btn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/nav[@class='navbar']/div[1]/div[@class='container']/div[2]/ul/li[3]/a[@id='settings']")
        self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/nav[@class='navbar']/div[1]/div[@class='container']/div[2]/ul/li[3]/a[@id='settings']")),"Do not find Settings link-button")
        settings_btn.click()
        self.driver.implicitly_wait(10)
        self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[2]/div[@class='signup-container']/div[@class='signup-header']/div[@class='title']/div[@class='arrow-deshbord-back']")),"Do not find Back to Dashboard button")
        # Open and Select new language
        for x in range(0,1,1):
        #Open language choice drop-down menu
           try:

             #devices_tab=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[2]/div[@class='signup-container']/div[2]/div[3]/ul/li[@class='devices']/a")
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             #The list of Language flags
             EnglishUS=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[1]/span")
             Nederlands=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[4]/span")
             France=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[5]/span")
             Espaniol=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[6]/span")
             Dansk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[7]/span")
             Italiano=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[8]/span")
             Finish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[1]/span")
             Greek=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[2]/span")
             Portuguese=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[3]/span")
             Russian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[4]/span")
             Turkish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[5]/span")
             Norsk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[6]/span")
             Polish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[7]/span")
             Chech=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[8]/span")
             Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[3]/li[1]/span")
             Koreian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[3]/li[2]/span")
             self.driver.implicitly_wait(10)



             #test Deutsch language
             Deutsch=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[3]/span")
             Deutsch.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #self.driver.refresh()
             #Check if language changed to Deutsch :
             back_to_dashboard_Deutsch=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             #print(back_to_dashboard_Deutsch)
             system_settings_Deutsch=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             #print(system_settings_Deutsch)
             user_details_Deutsch=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             #print(user_details_Deutsch)
             farm_details_Deutsch=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             #print(farm_details_Deutsch)
             if (back_to_dashboard_Deutsch==("Zurück zum Steuerfeld").decode("utf-8") and  system_settings_Deutsch==("System Settings").decode("utf-8") and user_details_Deutsch==("Nutzerdetails").decode("utf-8") and farm_details_Deutsch==("Hofdetails").decode("utf-8")):
                 print "Successfully changed to Deutsch!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Deutsch_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Deutsch')
                 self.fail("There is wrong translation to Deutsch")
             #Back to English Us
             #self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             #LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             #LangArrow.click()
             #EnglishUS=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[1]/span")
             #self.driver.implicitly_wait(10)
             #EnglishUS.click()
             #self.driver.implicitly_wait(20)
             #time.sleep(3)



           #test Nederlands language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             #Nederlands = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[4]/span")))
             #self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[4]/span")),"Look for Nederlands Flag-link Fail")
             Nederlands=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[4]/span")
             Nederlands.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #self.driver.refresh()
             #Check if language changed to Nederlands :
             back_to_dashboard_Nederlands=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             #print(back_to_dashboard_Nederlands)
             system_settings_Nederlands=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             #print(system_settings_Nederlands)
             user_details_Nederlands=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             #print(user_details_Nederlands)
             farm_details_Nederlands=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             #print(farm_details_Nederlands)
             if (back_to_dashboard_Nederlands==("Terug naar dashboard").decode("utf-8") and  system_settings_Nederlands==("System Settings").decode("utf-8") and user_details_Nederlands==("Gebruikersgegevens").decode("utf-8") and farm_details_Nederlands==("Boerderij-informatie").decode("utf-8")):
                 print "Successfully changed to Nederlands!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Nederlands_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Nederlands')
                 self.fail("There is wrong translation to Nederlands")
            #Back to English Us
             #self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             #LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             #LangArrow.click()
             #EnglishUS=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[1]/span")
             #self.driver.implicitly_wait(10)
             #EnglishUS.click()
             #self.driver.implicitly_wait(10)
             #time.sleep(5)

             #test Espaniol language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Espaniol=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[6]/span")
             Espaniol.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Espaniol :
             back_to_dashboard_Espaniol=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             #print(back_to_dashboard_Espaniol)
             system_settings_Espaniol=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             #print(system_settings_Espaniol)
             user_details_Espaniol=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             #print(user_details_Espaniol)
             farm_details_Espaniol=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             #print(farm_details_Espaniol)
             if (back_to_dashboard_Espaniol==("Regresar a panel de control").decode("utf-8") and  system_settings_Espaniol==("System Settings").decode("utf-8") and user_details_Espaniol==("Detalles de usuario").decode("utf-8") and farm_details_Espaniol==("Detalles de la granja").decode("utf-8")):
                 print "Successfully changed to Espaniol!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Espaniol_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Espaniol')
                 self.fail("There is wrong translation to Espaniol")

              #test France language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             France=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[5]/span")
             France.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)

             #Check if language changed to France :
             back_to_dashboard_France=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_France=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_France=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_France=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_France==("Retour au tableau de bord").decode("utf-8") and  system_settings_France==("System Settings").decode("utf-8") and user_details_France==("Détails de l'utilisateur").decode("utf-8") and farm_details_France==("Détails de la ferme").decode("utf-8")):
                 print "Successfully changed to France!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_France_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to France')
                 self.fail("There is wrong translation to France")

             #test Dansk language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Dansk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[7]/span")
             Dansk.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Dansk :
             back_to_dashboard_Dansk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             #print(back_to_dashboard_Espaniol)
             system_settings_Dansk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             #print(system_settings_Dansk)
             user_details_Dansk=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             #print(user_details_Espaniol)
             farm_details_Dansk=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             #print(farm_details_Dansk)
             if (back_to_dashboard_Dansk==("Tilbage til kontrolpanel").decode("utf-8") and  system_settings_Dansk==("System Settings").decode("utf-8") and user_details_Dansk==("Brugerdetaljer").decode("utf-8") and farm_details_Dansk==("Gårddetaljer").decode("utf-8")):
                 print "Successfully changed to Dansk!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Dansk_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Dansk')
                 self.fail("There is wrong translation to Dansk")


             #test Italiano language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Italiano=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[8]/span")
             Italiano.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Italiano :
             back_to_dashboard_Italiano=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Italiano=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Italiano=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Italiano=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Italiano==("Torna al pannello").decode("utf-8") and  system_settings_Italiano==("System Settings").decode("utf-8") and user_details_Italiano==("Dettagli utente").decode("utf-8") and farm_details_Italiano==("Dettagli azienda").decode("utf-8")):
                 print "Successfully changed to Italiano!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Italiano_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Italiano')
                 self.fail("There is wrong translation to Italiano")


             #test Finnish language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Finnish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[1]/span")
             Finnish.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Italiano :
             back_to_dashboard_Finnish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Finnish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Finnish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Finnish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Finnish==("Takaisin koontinäyttöön").decode("utf-8") and  system_settings_Finnish==("System Settings").decode("utf-8") and user_details_Finnish==("Käyttäjätiedot").decode("utf-8") and farm_details_Finnish==("Maatilan tiedot").decode("utf-8")):
                 print "Successfully changed to Finnish!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Finnish_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Finnish')
                 self.fail("There is wrong translation to Finnish")


             #test Greek language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Greek=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[2]/span")
             Greek.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Greek :
             back_to_dashboard_Greek=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Greek=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Greek=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Greek=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Greek==("Πίσω στον πίνακα εργαλείων").decode("utf-8") and  system_settings_Greek==("System Settings").decode("utf-8") and user_details_Greek==("Στοιχεία χρήστη").decode("utf-8") and farm_details_Greek==("Στοιχεία φάρμας").decode("utf-8")):
                 print "Successfully changed to Greek!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Greek_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Greek')
                 self.fail("There is wrong translation to Greek")



             #test Portuguese language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Portuguese=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[3]/span")
             Portuguese.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Portuguese :
             back_to_dashboard_Portuguese=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Portuguese=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Portuguese=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Portuguese=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Portuguese==("Voltar ao painel controle").decode("utf-8") and  system_settings_Portuguese==("System Settings").decode("utf-8") and user_details_Portuguese==("Detalhes do usuário").decode("utf-8") and farm_details_Portuguese==("Detalhes da fazenda").decode("utf-8")):
                 print "Successfully changed to Portuguese!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Portuguese_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Portuguese')
                 self.fail("There is wrong translation to Portuguese")



             #test Russian language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Russian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[4]/span")
             Russian.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Portuguese :
             back_to_dashboard_Russian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Russian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Russian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Russian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Russian==("Назад к клавиатуре").decode("utf-8") and  system_settings_Russian==("System Settings").decode("utf-8") and user_details_Russian==("Данные пользователя").decode("utf-8") and farm_details_Russian==("Данные фермы").decode("utf-8")):
                 print "Successfully changed to Russian!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Russian_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Russian')
                 self.fail("There is wrong translation to Russian")



             #test Turkish language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Turkish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[5]/span")
             Turkish.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Turkish :
             back_to_dashboard_Turkish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Turkish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Turkish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Turkish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Turkish==("Kontrol Paneline Geri Dön").decode("utf-8") and  system_settings_Turkish==("System Settings").decode("utf-8") and user_details_Turkish==("Kullanıcı bilgileri").decode("utf-8") and farm_details_Turkish==("Çiftlik bilgileri").decode("utf-8")):
                 print "Successfully changed to Turkish!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Turkish_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Turkish')
                 self.fail("There is wrong translation to Turkish")



             #test Norsk language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Norsk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[6]/span")
             Norsk.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Norsk :
             back_to_dashboard_Norsk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Norsk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Norsk=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Norsk=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Norsk==("Tilbake til instrumentbordet").decode("utf-8") and  system_settings_Norsk==("System Settings").decode("utf-8") and user_details_Norsk==("Brukeropplysninger").decode("utf-8") and farm_details_Norsk==("Farmdetaljer").decode("utf-8")):
                 print "Successfully changed to Turkish!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Turkish_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Turkish')
                 self.fail("There is wrong translation to Turkish")


             time.sleep(5)
             #test Polish language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Polish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[7]/span")
             Polish.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Polish :
             back_to_dashboard_Polish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Polish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Polish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Polish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Polish==("Powrót do panelu sterowania").decode("utf-8") and  system_settings_Polish==("System Settings").decode("utf-8") and user_details_Polish==("Dane użytkownika").decode("utf-8") and farm_details_Polish==("Dane gospodarstwa").decode("utf-8")):
                 print "Successfully changed to Polish!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Polish_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Polish')
                 self.fail("There is wrong translation to Polish")

             time.sleep(5)
             #test Czech language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Czech=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[8]/span")
             Czech.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Czech :
             back_to_dashboard_Czech=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Czech=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Czech=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Czech=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Czech==("Zpět na řídící panel").decode("utf-8") and  system_settings_Czech==("System Settings").decode("utf-8") and user_details_Czech==("Detaily uživatele").decode("utf-8") and farm_details_Czech==("Detaily farmy").decode("utf-8")):
                 print "Successfully changed to Czech!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Czech_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Czech')
                 self.fail("There is wrong translation to Czech")

             time.sleep(5)
             #test Slovenian language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[3]/li[1]/span")
             Slovenian.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Slovenian :
             back_to_dashboard_Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Slovenian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Slovenian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Slovenian==("Nazaj na nadzorno ploščo").decode("utf-8") and  system_settings_Slovenian==("System Settings").decode("utf-8") and user_details_Slovenian==("Podrobnosti uporabnika").decode("utf-8") and farm_details_Slovenian==("Podrobnosti kmetije").decode("utf-8")):
                 print "Successfully changed to Slovenian!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Slovenian_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Slovenian')
                 self.fail("There is wrong translation to Slovenian")


#             #test Koreian language
#             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
#             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
#             LangArrow.click()
#             Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[3]/li[1]/span")
#             Koreian.click()
#             self.driver.implicitly_wait(20)
#             time.sleep(5)
#             #Check if language changed to Koreian :
#             back_to_dashboard_Koreian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
#             system_settings_Koreian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
#             user_details_Koreian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
#             farm_details_Koreian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
#             if (back_to_dashboard_Koreian==("계기판으로 돌아가기").decode("utf-8") and  system_settings_Koreian==("System Settings").decode("utf-8") and user_details_Koreian==("사용자 세부 정보").decode("utf-8") and farm_details_Koreian==("목장 세부 정보").decode("utf-8")):
#                 print "Successfully changed to Slovenian!!"
#                 pass
#             else:
#                 self.take_screenshot('Translation_to_Koreian_problem')
#                 self.loggertest(self.__class__.__name__,'Fail switch to Koreian')
#                 self.fail("There is wrong translation to Koreian")




           except NoSuchElementException:
             self.take_screenshot("Can not find 'Settings/Devices' tab-button problem")
             self.fail("There is missing element on 'settings window'")

        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch Languages_on_Firefox finish at :'+date_time_formatted
    def test_3_Logout_process_on_Firefox(self):
         #test_Logout_process_on_Firefox
         #logout from main page(dashboard)
        #Back to English Us
        self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
        LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
        LangArrow.click()
        EnglishUS=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[1]/span")
        self.driver.implicitly_wait(5)
        EnglishUS.click()
        self.driver.implicitly_wait(20)
        time.sleep(3)

        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'test logout process on Firefox started at :'+date_time_formatted
        try:
           self.assertTrue(self.is_element_present(By.ID,"signout"),"Did not found Signout button-link")
           self.search_field=self.driver.find_element_by_id("signout")
        except NoSuchElementException:
             self.take_screenshot('Fail log-out')
             self.fail("There is no element 'signout'")
        self.search_field.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        try:
           self.email_field=self.driver.find_element_by_name("email")
           self.password_field=self.driver.find_element_by_name("password")
           self.btnLogin_field=self.driver.find_element_by_id("btnLogin")
        except NoSuchElementException:
             self.take_screenshot('Fail log-out')
             self.fail("There is missing elements 'email' or 'password' or 'btnLogin'")
        EmailElement=self.is_element_present(By.NAME,"email")
        PasswordElement=self.is_element_present(By.NAME,"password")
        LoginBtnElement=self.is_element_present(By.ID,"btnLogin")
        if( EmailElement and PasswordElement and LoginBtnElement):
            pass
        else:
           self.take_screenshot('Fail log-out did not exit to login page')
        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Log out_process_on_Firefox finish at :'+date_time_formatted
    @classmethod
    def tearDownClass(self):
        #close the browser window

        self.driver.quit()


class LanguageChangeTestChrome(unittest.TestCase):
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
        #Load main page and register with username/password
        while(loading_attempt>0):
              try:
                 self.email_field=self.driver.find_element_by_name("email")
                 self.password_field=self.driver.find_element_by_name("password")
                 self.password_field=self.driver.find_element_by_id("btnLogin")
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
              self.take_screenshot('Fail_log_out')
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
        print 'Test Login_process_on_Chrome finish at :'+ date_time_formatted

    def test_2_Language_Change_on_Chrome(self):
        #test_2DashboardDataSwitch_process_on_Firefox
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch_languages_on_Settings_on_Chrome started at :'+date_time_formatted
        #open 'Settings' window
        settings_btn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/nav[@class='navbar']/div[1]/div[@class='container']/div[2]/ul/li[3]/a[@id='settings']")
        self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/nav[@class='navbar']/div[1]/div[@class='container']/div[2]/ul/li[3]/a[@id='settings']")),"Do not find Settings link-button")
        settings_btn.click()
        self.driver.implicitly_wait(10)
        self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[2]/div[@class='signup-container']/div[@class='signup-header']/div[@class='title']/div[@class='arrow-deshbord-back']")),"Do not find Back to Dashboard button")
        # Open and Select new language
        for x in range(0,1,1):
        #Open language choice drop-down menu
           try:

             #devices_tab=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[2]/div[@class='signup-container']/div[2]/div[3]/ul/li[@class='devices']/a")
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             #The list of Language flags
             EnglishUS=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[1]/span")
             Nederlands=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[4]/span")
             France=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[5]/span")
             Espaniol=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[6]/span")
             Dansk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[7]/span")
             Italiano=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[8]/span")
             Finish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[1]/span")
             Greek=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[2]/span")
             Portuguese=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[3]/span")
             Russian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[4]/span")
             Turkish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[5]/span")
             Norsk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[6]/span")
             Polish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[7]/span")
             Chech=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[8]/span")
             Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[3]/li[1]/span")
             Koreian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[3]/li[2]/span")
             self.driver.implicitly_wait(10)



             #test Deutsch language
             Deutsch=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[3]/span")
             Deutsch.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #self.driver.refresh()
             #Check if language changed to Deutsch :
             back_to_dashboard_Deutsch=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             #print(back_to_dashboard_Deutsch)
             system_settings_Deutsch=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             #print(system_settings_Deutsch)
             user_details_Deutsch=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             #print(user_details_Deutsch)
             farm_details_Deutsch=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             #print(farm_details_Deutsch)
             if (back_to_dashboard_Deutsch==("Zurück zum Steuerfeld").decode("utf-8") and  system_settings_Deutsch==("System Settings").decode("utf-8") and user_details_Deutsch==("Nutzerdetails").decode("utf-8") and farm_details_Deutsch==("Hofdetails").decode("utf-8")):
                 print "Successfully changed to Deutsch!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Deutsch_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Deutsch')
                 self.fail("There is wrong translation to Deutsch")
             #Back to English Us
             #self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             #LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             #LangArrow.click()
             #EnglishUS=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[1]/span")
             #self.driver.implicitly_wait(10)
             #EnglishUS.click()
             #self.driver.implicitly_wait(20)
             #time.sleep(3)



           #test Nederlands language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             #Nederlands = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[4]/span")))
             #self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[4]/span")),"Look for Nederlands Flag-link Fail")
             Nederlands=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[4]/span")
             Nederlands.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #self.driver.refresh()
             #Check if language changed to Nederlands :
             back_to_dashboard_Nederlands=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             #print(back_to_dashboard_Nederlands)
             system_settings_Nederlands=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             #print(system_settings_Nederlands)
             user_details_Nederlands=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             #print(user_details_Nederlands)
             farm_details_Nederlands=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             #print(farm_details_Nederlands)
             if (back_to_dashboard_Nederlands==("Terug naar dashboard").decode("utf-8") and  system_settings_Nederlands==("System Settings").decode("utf-8") and user_details_Nederlands==("Gebruikersgegevens").decode("utf-8") and farm_details_Nederlands==("Boerderij-informatie").decode("utf-8")):
                 print "Successfully changed to Nederlands!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Nederlands_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Nederlands')
                 self.fail("There is wrong translation to Nederlands")
            #Back to English Us
             #self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             #LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             #LangArrow.click()
             #EnglishUS=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[1]/span")
             #self.driver.implicitly_wait(10)
             #EnglishUS.click()
             #self.driver.implicitly_wait(10)
             #time.sleep(5)

             #test Espaniol language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Espaniol=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[6]/span")
             Espaniol.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Espaniol :
             back_to_dashboard_Espaniol=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             #print(back_to_dashboard_Espaniol)
             system_settings_Espaniol=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             #print(system_settings_Espaniol)
             user_details_Espaniol=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             #print(user_details_Espaniol)
             farm_details_Espaniol=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             #print(farm_details_Espaniol)
             if (back_to_dashboard_Espaniol==("Regresar a panel de control").decode("utf-8") and  system_settings_Espaniol==("System Settings").decode("utf-8") and user_details_Espaniol==("Detalles de usuario").decode("utf-8") and farm_details_Espaniol==("Detalles de la granja").decode("utf-8")):
                 print "Successfully changed to Espaniol!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Espaniol_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Espaniol')
                 self.fail("There is wrong translation to Espaniol")

              #test France language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             France=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[5]/span")
             France.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)

             #Check if language changed to France :
             back_to_dashboard_France=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_France=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_France=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_France=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_France==("Retour au tableau de bord").decode("utf-8") and  system_settings_France==("System Settings").decode("utf-8") and user_details_France==("Détails de l'utilisateur").decode("utf-8") and farm_details_France==("Détails de la ferme").decode("utf-8")):
                 print "Successfully changed to France!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_France_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to France')
                 self.fail("There is wrong translation to France")

             #test Dansk language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Dansk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[7]/span")
             Dansk.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Dansk :
             back_to_dashboard_Dansk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             #print(back_to_dashboard_Espaniol)
             system_settings_Dansk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             #print(system_settings_Dansk)
             user_details_Dansk=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             #print(user_details_Espaniol)
             farm_details_Dansk=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             #print(farm_details_Dansk)
             if (back_to_dashboard_Dansk==("Tilbage til kontrolpanel").decode("utf-8") and  system_settings_Dansk==("System Settings").decode("utf-8") and user_details_Dansk==("Brugerdetaljer").decode("utf-8") and farm_details_Dansk==("Gårddetaljer").decode("utf-8")):
                 print "Successfully changed to Dansk!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Dansk_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Dansk')
                 self.fail("There is wrong translation to Dansk")


             #test Italiano language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Italiano=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[8]/span")
             Italiano.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Italiano :
             back_to_dashboard_Italiano=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Italiano=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Italiano=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Italiano=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Italiano==("Torna al pannello").decode("utf-8") and  system_settings_Italiano==("System Settings").decode("utf-8") and user_details_Italiano==("Dettagli utente").decode("utf-8") and farm_details_Italiano==("Dettagli azienda").decode("utf-8")):
                 print "Successfully changed to Italiano!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Italiano_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Italiano')
                 self.fail("There is wrong translation to Italiano")


             #test Finnish language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Finnish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[1]/span")
             Finnish.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Italiano :
             back_to_dashboard_Finnish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Finnish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Finnish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Finnish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Finnish==("Takaisin koontinäyttöön").decode("utf-8") and  system_settings_Finnish==("System Settings").decode("utf-8") and user_details_Finnish==("Käyttäjätiedot").decode("utf-8") and farm_details_Finnish==("Maatilan tiedot").decode("utf-8")):
                 print "Successfully changed to Finnish!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Finnish_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Finnish')
                 self.fail("There is wrong translation to Finnish")


             #test Greek language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Greek=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[2]/span")
             Greek.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Greek :
             back_to_dashboard_Greek=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Greek=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Greek=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Greek=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Greek==("Πίσω στον πίνακα εργαλείων").decode("utf-8") and  system_settings_Greek==("System Settings").decode("utf-8") and user_details_Greek==("Στοιχεία χρήστη").decode("utf-8") and farm_details_Greek==("Στοιχεία φάρμας").decode("utf-8")):
                 print "Successfully changed to Greek!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Greek_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Greek')
                 self.fail("There is wrong translation to Greek")



             #test Portuguese language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Portuguese=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[3]/span")
             Portuguese.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Portuguese :
             back_to_dashboard_Portuguese=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Portuguese=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Portuguese=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Portuguese=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Portuguese==("Voltar ao painel controle").decode("utf-8") and  system_settings_Portuguese==("System Settings").decode("utf-8") and user_details_Portuguese==("Detalhes do usuário").decode("utf-8") and farm_details_Portuguese==("Detalhes da fazenda").decode("utf-8")):
                 print "Successfully changed to Portuguese!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Portuguese_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Portuguese')
                 self.fail("There is wrong translation to Portuguese")



             #test Russian language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Russian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[4]/span")
             Russian.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Portuguese :
             back_to_dashboard_Russian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Russian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Russian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Russian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Russian==("Назад к клавиатуре").decode("utf-8") and  system_settings_Russian==("System Settings").decode("utf-8") and user_details_Russian==("Данные пользователя").decode("utf-8") and farm_details_Russian==("Данные фермы").decode("utf-8")):
                 print "Successfully changed to Russian!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Russian_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Russian')
                 self.fail("There is wrong translation to Russian")



             #test Turkish language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Turkish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[5]/span")
             Turkish.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Turkish :
             back_to_dashboard_Turkish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Turkish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Turkish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Turkish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Turkish==("Kontrol Paneline Geri Dön").decode("utf-8") and  system_settings_Turkish==("System Settings").decode("utf-8") and user_details_Turkish==("Kullanıcı bilgileri").decode("utf-8") and farm_details_Turkish==("Çiftlik bilgileri").decode("utf-8")):
                 print "Successfully changed to Turkish!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Turkish_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Turkish')
                 self.fail("There is wrong translation to Turkish")



             #test Norsk language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Norsk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[6]/span")
             Norsk.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Norsk :
             back_to_dashboard_Norsk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Norsk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Norsk=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Norsk=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Norsk==("Tilbake til instrumentbordet").decode("utf-8") and  system_settings_Norsk==("System Settings").decode("utf-8") and user_details_Norsk==("Brukeropplysninger").decode("utf-8") and farm_details_Norsk==("Farmdetaljer").decode("utf-8")):
                 print "Successfully changed to Turkish!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Turkish_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Turkish')
                 self.fail("There is wrong translation to Turkish")


             time.sleep(5)
             #test Polish language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Polish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[7]/span")
             Polish.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Polish :
             back_to_dashboard_Polish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Polish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Polish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Polish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Polish==("Powrót do panelu sterowania").decode("utf-8") and  system_settings_Polish==("System Settings").decode("utf-8") and user_details_Polish==("Dane użytkownika").decode("utf-8") and farm_details_Polish==("Dane gospodarstwa").decode("utf-8")):
                 print "Successfully changed to Polish!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Polish_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Polish')
                 self.fail("There is wrong translation to Polish")

             time.sleep(5)
             #test Czech language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Czech=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[8]/span")
             Czech.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Czech :
             back_to_dashboard_Czech=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Czech=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Czech=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Czech=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Czech==("Zpět na řídící panel").decode("utf-8") and  system_settings_Czech==("System Settings").decode("utf-8") and user_details_Czech==("Detaily uživatele").decode("utf-8") and farm_details_Czech==("Detaily farmy").decode("utf-8")):
                 print "Successfully changed to Czech!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Czech_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Czech')
                 self.fail("There is wrong translation to Czech")

             time.sleep(5)
             #test Slovenian language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[3]/li[1]/span")
             Slovenian.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Slovenian :
             back_to_dashboard_Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Slovenian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Slovenian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Slovenian==("Nazaj na nadzorno ploščo").decode("utf-8") and  system_settings_Slovenian==("System Settings").decode("utf-8") and user_details_Slovenian==("Podrobnosti uporabnika").decode("utf-8") and farm_details_Slovenian==("Podrobnosti kmetije").decode("utf-8")):
                 print "Successfully changed to Slovenian!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Slovenian_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Slovenian')
                 self.fail("There is wrong translation to Slovenian")


#             #test Koreian language
#             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
#             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
#             LangArrow.click()
#             Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[3]/li[1]/span")
#             Koreian.click()
#             self.driver.implicitly_wait(20)
#             time.sleep(5)
#             #Check if language changed to Koreian :
#             back_to_dashboard_Koreian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
#             system_settings_Koreian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
#             user_details_Koreian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
#             farm_details_Koreian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
#             if (back_to_dashboard_Koreian==("계기판으로 돌아가기").decode("utf-8") and  system_settings_Koreian==("System Settings").decode("utf-8") and user_details_Koreian==("사용자 세부 정보").decode("utf-8") and farm_details_Koreian==("목장 세부 정보").decode("utf-8")):
#                 print "Successfully changed to Slovenian!!"
#                 pass
#             else:
#                 self.take_screenshot('Translation_to_Koreian_problem')
#                 self.loggertest(self.__class__.__name__,'Fail switch to Koreian')
#                 self.fail("There is wrong translation to Koreian")




           except NoSuchElementException:
             self.take_screenshot("Can not find 'Settings/Devices' tab-button problem")
             self.fail("There is missing element on 'settings window'")

        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch Languages_on_Chrome finish at :'+date_time_formatted

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
        self.driver.implicitly_wait(10)
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
        print 'Test Logout_process_on_Chrome finish at :'+date_time_formatted
    @classmethod
    def tearDownClass(self):
        #close the browser window
        self.driver.quit()



class LanguageChangeTestIE(unittest.TestCase):
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
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Login_process_on_IE finish at :'+date_time_formatted
    def test_2_Language_Change_on_IE(self):
        #test_2DashboardDataSwitch_process_on_Firefox
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch_languages_on_Settings_on_IE started at :'+date_time_formatted
        #open 'Settings' window
        settings_btn=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/nav[@class='navbar']/div[1]/div[@class='container']/div[2]/ul/li[3]/a[@id='settings']")
        self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/nav[@class='navbar']/div[1]/div[@class='container']/div[2]/ul/li[3]/a[@id='settings']")),"Do not find Settings link-button")
        settings_btn.click()
        self.driver.implicitly_wait(10)
        self.assertTrue(self.is_element_present(By.XPATH,("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[2]/div[@class='signup-container']/div[@class='signup-header']/div[@class='title']/div[@class='arrow-deshbord-back']")),"Do not find Back to Dashboard button")
        # Open and Select new language
        for x in range(0,1,1):
        #Open language choice drop-down menu
           try:

             #devices_tab=self.driver.find_element_by_xpath("//html/body[@id='top']/div[@id='wrap']/div[@id='app']/div[2]/div[@class='signup-container']/div[2]/div[3]/ul/li[@class='devices']/a")
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             #The list of Language flags
             EnglishUS=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[1]/span")
             Nederlands=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[4]/span")
             France=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[5]/span")
             Espaniol=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[6]/span")
             Dansk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[7]/span")
             Italiano=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[8]/span")
             Finish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[1]/span")
             Greek=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[2]/span")
             Portuguese=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[3]/span")
             Russian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[4]/span")
             Turkish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[5]/span")
             Norsk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[6]/span")
             Polish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[7]/span")
             Chech=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[8]/span")
             Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[3]/li[1]/span")
             Koreian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[3]/li[2]/span")
             self.driver.implicitly_wait(10)



             #test Deutsch language
             Deutsch=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[3]/span")
             Deutsch.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #self.driver.refresh()
             #Check if language changed to Deutsch :
             back_to_dashboard_Deutsch=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             #print(back_to_dashboard_Deutsch)
             system_settings_Deutsch=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             #print(system_settings_Deutsch)
             user_details_Deutsch=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             #print(user_details_Deutsch)
             farm_details_Deutsch=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             #print(farm_details_Deutsch)
             if (back_to_dashboard_Deutsch==("Zurück zum Steuerfeld").decode("utf-8") and  system_settings_Deutsch==("System Settings").decode("utf-8") and user_details_Deutsch==("Nutzerdetails").decode("utf-8") and farm_details_Deutsch==("Hofdetails").decode("utf-8")):
                 print "Successfully changed to Deutsch!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Deutsch_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Deutsch')
                 self.fail("There is wrong translation to Deutsch")
             #Back to English Us
             #self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             #LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             #LangArrow.click()
             #EnglishUS=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[1]/span")
             #self.driver.implicitly_wait(10)
             #EnglishUS.click()
             #self.driver.implicitly_wait(20)
             #time.sleep(3)



           #test Nederlands language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             #Nederlands = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[4]/span")))
             #self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[4]/span")),"Look for Nederlands Flag-link Fail")
             Nederlands=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[4]/span")
             Nederlands.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #self.driver.refresh()
             #Check if language changed to Nederlands :
             back_to_dashboard_Nederlands=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             #print(back_to_dashboard_Nederlands)
             system_settings_Nederlands=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             #print(system_settings_Nederlands)
             user_details_Nederlands=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             #print(user_details_Nederlands)
             farm_details_Nederlands=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             #print(farm_details_Nederlands)
             if (back_to_dashboard_Nederlands==("Terug naar dashboard").decode("utf-8") and  system_settings_Nederlands==("System Settings").decode("utf-8") and user_details_Nederlands==("Gebruikersgegevens").decode("utf-8") and farm_details_Nederlands==("Boerderij-informatie").decode("utf-8")):
                 print "Successfully changed to Nederlands!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Nederlands_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Nederlands')
                 self.fail("There is wrong translation to Nederlands")
            #Back to English Us
             #self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             #LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             #LangArrow.click()
             #EnglishUS=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[1]/span")
             #self.driver.implicitly_wait(10)
             #EnglishUS.click()
             #self.driver.implicitly_wait(10)
             #time.sleep(5)

             #test Espaniol language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Espaniol=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[6]/span")
             Espaniol.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Espaniol :
             back_to_dashboard_Espaniol=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             #print(back_to_dashboard_Espaniol)
             system_settings_Espaniol=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             #print(system_settings_Espaniol)
             user_details_Espaniol=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             #print(user_details_Espaniol)
             farm_details_Espaniol=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             #print(farm_details_Espaniol)
             if (back_to_dashboard_Espaniol==("Regresar a panel de control").decode("utf-8") and  system_settings_Espaniol==("System Settings").decode("utf-8") and user_details_Espaniol==("Detalles de usuario").decode("utf-8") and farm_details_Espaniol==("Detalles de la granja").decode("utf-8")):
                 print "Successfully changed to Espaniol!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Espaniol_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Espaniol')
                 self.fail("There is wrong translation to Espaniol")

              #test France language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             France=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[5]/span")
             France.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)

             #Check if language changed to France :
             back_to_dashboard_France=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_France=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_France=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_France=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_France==("Retour au tableau de bord").decode("utf-8") and  system_settings_France==("System Settings").decode("utf-8") and user_details_France==("Détails de l'utilisateur").decode("utf-8") and farm_details_France==("Détails de la ferme").decode("utf-8")):
                 print "Successfully changed to France!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_France_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to France')
                 self.fail("There is wrong translation to France")

             #test Dansk language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Dansk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[7]/span")
             Dansk.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Dansk :
             back_to_dashboard_Dansk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             #print(back_to_dashboard_Espaniol)
             system_settings_Dansk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             #print(system_settings_Dansk)
             user_details_Dansk=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             #print(user_details_Espaniol)
             farm_details_Dansk=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             #print(farm_details_Dansk)
             if (back_to_dashboard_Dansk==("Tilbage til kontrolpanel").decode("utf-8") and  system_settings_Dansk==("System Settings").decode("utf-8") and user_details_Dansk==("Brugerdetaljer").decode("utf-8") and farm_details_Dansk==("Gårddetaljer").decode("utf-8")):
                 print "Successfully changed to Dansk!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Dansk_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Dansk')
                 self.fail("There is wrong translation to Dansk")


             #test Italiano language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Italiano=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[1]/li[8]/span")
             Italiano.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Italiano :
             back_to_dashboard_Italiano=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Italiano=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Italiano=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Italiano=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Italiano==("Torna al pannello").decode("utf-8") and  system_settings_Italiano==("System Settings").decode("utf-8") and user_details_Italiano==("Dettagli utente").decode("utf-8") and farm_details_Italiano==("Dettagli azienda").decode("utf-8")):
                 print "Successfully changed to Italiano!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Italiano_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Italiano')
                 self.fail("There is wrong translation to Italiano")


             #test Finnish language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Finnish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[1]/span")
             Finnish.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Italiano :
             back_to_dashboard_Finnish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Finnish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Finnish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Finnish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Finnish==("Takaisin koontinäyttöön").decode("utf-8") and  system_settings_Finnish==("System Settings").decode("utf-8") and user_details_Finnish==("Käyttäjätiedot").decode("utf-8") and farm_details_Finnish==("Maatilan tiedot").decode("utf-8")):
                 print "Successfully changed to Finnish!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Finnish_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Finnish')
                 self.fail("There is wrong translation to Finnish")


             #test Greek language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Greek=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[2]/span")
             Greek.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Greek :
             back_to_dashboard_Greek=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Greek=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Greek=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Greek=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Greek==("Πίσω στον πίνακα εργαλείων").decode("utf-8") and  system_settings_Greek==("System Settings").decode("utf-8") and user_details_Greek==("Στοιχεία χρήστη").decode("utf-8") and farm_details_Greek==("Στοιχεία φάρμας").decode("utf-8")):
                 print "Successfully changed to Greek!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Greek_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Greek')
                 self.fail("There is wrong translation to Greek")



             #test Portuguese language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Portuguese=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[3]/span")
             Portuguese.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Portuguese :
             back_to_dashboard_Portuguese=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Portuguese=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Portuguese=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Portuguese=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Portuguese==("Voltar ao painel controle").decode("utf-8") and  system_settings_Portuguese==("System Settings").decode("utf-8") and user_details_Portuguese==("Detalhes do usuário").decode("utf-8") and farm_details_Portuguese==("Detalhes da fazenda").decode("utf-8")):
                 print "Successfully changed to Portuguese!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Portuguese_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Portuguese')
                 self.fail("There is wrong translation to Portuguese")



             #test Russian language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Russian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[4]/span")
             Russian.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Portuguese :
             back_to_dashboard_Russian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Russian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Russian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Russian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Russian==("Назад к клавиатуре").decode("utf-8") and  system_settings_Russian==("System Settings").decode("utf-8") and user_details_Russian==("Данные пользователя").decode("utf-8") and farm_details_Russian==("Данные фермы").decode("utf-8")):
                 print "Successfully changed to Russian!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Russian_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Russian')
                 self.fail("There is wrong translation to Russian")



             #test Turkish language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Turkish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[5]/span")
             Turkish.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Turkish :
             back_to_dashboard_Turkish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Turkish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Turkish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Turkish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Turkish==("Kontrol Paneline Geri Dön").decode("utf-8") and  system_settings_Turkish==("System Settings").decode("utf-8") and user_details_Turkish==("Kullanıcı bilgileri").decode("utf-8") and farm_details_Turkish==("Çiftlik bilgileri").decode("utf-8")):
                 print "Successfully changed to Turkish!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Turkish_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Turkish')
                 self.fail("There is wrong translation to Turkish")



             #test Norsk language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Norsk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[6]/span")
             Norsk.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Norsk :
             back_to_dashboard_Norsk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Norsk=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Norsk=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Norsk=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Norsk==("Tilbake til instrumentbordet").decode("utf-8") and  system_settings_Norsk==("System Settings").decode("utf-8") and user_details_Norsk==("Brukeropplysninger").decode("utf-8") and farm_details_Norsk==("Farmdetaljer").decode("utf-8")):
                 print "Successfully changed to Turkish!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Turkish_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Turkish')
                 self.fail("There is wrong translation to Turkish")


             time.sleep(5)
             #test Polish language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Polish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[7]/span")
             Polish.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Polish :
             back_to_dashboard_Polish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Polish=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Polish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Polish=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Polish==("Powrót do panelu sterowania").decode("utf-8") and  system_settings_Polish==("System Settings").decode("utf-8") and user_details_Polish==("Dane użytkownika").decode("utf-8") and farm_details_Polish==("Dane gospodarstwa").decode("utf-8")):
                 print "Successfully changed to Polish!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Polish_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Polish')
                 self.fail("There is wrong translation to Polish")

             time.sleep(5)
             #test Czech language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Czech=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[2]/li[8]/span")
             Czech.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Czech :
             back_to_dashboard_Czech=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Czech=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Czech=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Czech=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Czech==("Zpět na řídící panel").decode("utf-8") and  system_settings_Czech==("System Settings").decode("utf-8") and user_details_Czech==("Detaily uživatele").decode("utf-8") and farm_details_Czech==("Detaily farmy").decode("utf-8")):
                 print "Successfully changed to Czech!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Czech_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Czech')
                 self.fail("There is wrong translation to Czech")

             time.sleep(5)
             #test Slovenian language
             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
             LangArrow.click()
             Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[3]/li[1]/span")
             Slovenian.click()
             self.driver.implicitly_wait(20)
             time.sleep(5)
             #Check if language changed to Slovenian :
             back_to_dashboard_Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
             system_settings_Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
             user_details_Slovenian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
             farm_details_Slovenian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
             if (back_to_dashboard_Slovenian==("Nazaj na nadzorno ploščo").decode("utf-8") and  system_settings_Slovenian==("System Settings").decode("utf-8") and user_details_Slovenian==("Podrobnosti uporabnika").decode("utf-8") and farm_details_Slovenian==("Podrobnosti kmetije").decode("utf-8")):
                 print "Successfully changed to Slovenian!!"
                 pass
             else:
                 self.take_screenshot('Translation_to_Slovenian_problem')
                 self.loggertest(self.__class__.__name__,'Fail switch to Slovenian')
                 self.fail("There is wrong translation to Slovenian")


#             #test Koreian language
#             self.assertTrue(self.is_element_present(By.XPATH,(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")),"Look for Arrow that open drop-down menu")
#             LangArrow=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]")
#             LangArrow.click()
#             Slovenian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[2]/div[2]/ul[3]/li[1]/span")
#             Koreian.click()
#             self.driver.implicitly_wait(20)
#             time.sleep(5)
#             #Check if language changed to Koreian :
#             back_to_dashboard_Koreian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/div").text
#             system_settings_Koreian=self.driver.find_element_by_xpath(".//*[@id='app']/div[2]/div[1]/div[1]/div/span[2]").text
#             user_details_Koreian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[2]/div").text
#             farm_details_Koreian=self.driver.find_element_by_xpath(".//*[@id='frmSetting']/div[4]/div").text
#             if (back_to_dashboard_Koreian==("계기판으로 돌아가기").decode("utf-8") and  system_settings_Koreian==("System Settings").decode("utf-8") and user_details_Koreian==("사용자 세부 정보").decode("utf-8") and farm_details_Koreian==("목장 세부 정보").decode("utf-8")):
#                 print "Successfully changed to Slovenian!!"
#                 pass
#             else:
#                 self.take_screenshot('Translation_to_Koreian_problem')
#                 self.loggertest(self.__class__.__name__,'Fail switch to Koreian')
#                 self.fail("There is wrong translation to Koreian")




           except NoSuchElementException:
             self.take_screenshot("Can not find 'Settings/Devices' tab-button problem")
             self.fail("There is missing element on 'settings window'")

        print "Test running time:"+str((date_time.now()-date_time))
        date_time=datetime.now()
        date_time_formatted=date_time.strftime("%d/%m/%Y  %H:%M:%S")
        print 'Test Switch Languages_on_IE finish at :'+date_time_formatted
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


