
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
                   time.sleep(2)
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
                   #FirstCowCard= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='span-cow-number']")))
                   firstCowCardSelected=self.driver.find_element_by_xpath(".//*[@id='span-cow-number']").text
                   self.loggertest(self.__class__.__name__,'The cow card number that actually opened :'+firstCowCardSelected)
                   if first_result==firstCowCardSelected:
                      self.loggertest(self.__class__.__name__,'The cow card number that actually opened :'+firstCowCardSelected)
                      pass
                   else:
                       self.take_screenshot("Opened_wrong_cow_card")
                       self.loggertest(self.__class__.__name__,'Opened different cow card from selected on Find Cow field...')
                       self.fail("Not correct Cow Card selected")