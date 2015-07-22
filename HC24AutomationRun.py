import unittest
__author__ = 'sergey.meerovich'
import HTMLTestRunner
import os
import time
from selenium import webdriver
#Login and Log out portal
from HC24Login import LoginTestFirefox
from HC24Login import LoginTestChrome
from HC24Login import LoginTestIE
#switch dashboard Data tab
from DashboardData import DashboardDataTestFirefox
from DashboardData import DashboardDataTestChrome
from DashboardData import DashboardDataTestIE
from SettingsEntry import SettingsTestFirefox
from SettingsEntry import SettingsTestChrome
from SettingsEntry import SettingsTestIE

#Switch settings window tabs
from SettingsTabNavigation import SettingsTabSwitchTestFirefox
from SettingsTabNavigation import SettingsTabSwitchTestChrome
from SettingsTabNavigation import SettingsTabSwitchTestIE

#Switch between Farm trends
from FarmTrendsNavigation import FarmTrendsSwitchFirefox
from FarmTrendsNavigation import FarmTrendsSwitchChrome
from FarmTrendsNavigation import FarmTrendsSwitchIE

#Not Identified Cows Report
from NotIdentified import NotIdentifiedNavigationFirefox
from NotIdentified import NotIdentifiedNavigationChrome
from NotIdentified import NotIdentifiednavigationIE

#Open a Heat Cows Report
from OpenHeatReport import OpenHeatReportFirefox
from OpenHeatReport import OpenHeatReportChrome
from OpenHeatReport import OpenHeatReportIE

#Add note to farm graph from dashboard page
from AddDeleteNoteToFarm import AddDeleteNoteToFarmFirefox
from AddDeleteNoteToFarm import AddDeleteNoteToFarmChrome
from AddDeleteNoteToFarm import AddDeleteNoteToFarmIE

#Open More Reports
from OpenMoreReports import openMoreReportsTestFirefox
from OpenMoreReports import openMoreReportsTestChrome
from OpenMoreReports import openMoreReportsTestIE



#Switch between Reports
from SwitchBetweenReports import SwitchReportsTestFirefox
from SwitchBetweenReports import SwitchReportsTestChrome
from SwitchBetweenReports import SwitchReportsTestIE

#Switch between Pages on all Cows reports
from SwtchBetweenPagesOnAllCowsReport import SwitchBetweenPagesOnAllCowsReportTestFirefox
from SwtchBetweenPagesOnAllCowsReport import SwitchBetweenPagesOnAllCowsReportTestChrome
from SwtchBetweenPagesOnAllCowsReport import SwitchBetweenPagesOnAllCowsReportTestIE

#Switch between pages use Left/Right Arrows
from SwitchPagesWithArrows import SwitchPagesWithArrowsTestFirefox
from SwitchPagesWithArrows import  SwitchPagesWithArrowsTestChrome
from SwitchPagesWithArrows import SwitchPagesWithArrowsTestIE

#Open specific Cow Card that user search
from FindCowFromDataTab import FindCowFromDataTabTestFirefox
from FindCowFromDataTab import FindCowFromDataTabTestChrome
from FindCowFromDataTab import FindCowFromDataTabTestIE

#Switch Graph day presentation of specific Cow
from SwitchGraphsOfCowCard import SwitchGraphsOnCowCardTestFirefox
from SwitchGraphsOfCowCard import SwitchGraphsOnCowCardTestChrome
from SwitchGraphsOfCowCard import  SwitchGraphsOnCowCardTestIE

#Open Health Report from dshboard
from OpenHealthReport import OpenHealthReportFirefox
from OpenHealthReport import OpenHealthReportChrome
from OpenHealthReport import OpenHealthReportIE

#Open Cow Card and Switch between Graphs on Cow Card
from CowCardSwitchBetweenGraphs import SwitchBetweenGraphsTestFirefox
from CowCardSwitchBetweenGraphs import SwitchBetweenGraphsTestChrome
from CowCardSwitchBetweenGraphs import SwitchBetweenGraphsTestIE

#Switch between Cow Card by press on Next and Prev button
from NextPrevCowCard import NextPrevCowCardTestFirefox
from NextPrevCowCard import NextPrevCowCardTestChrome
from NextPrevCowCard import NextPrevCowCardTestIE

#Create a new Cow Card and delete it
from AddNewCowCard import AddNewCowCardTestFirefox
from AddNewCowCard import AddNewCowCardTestChrome
from AddNewCowCard import AddNewCowCardTestIE

#Open Policy Privacy and Terms of Use
from TermAndPolicyPages import PrivacyTermTestFirefox
from  TermAndPolicyPages import PrivacyTermTestTestChrome
from TermAndPolicyPages import  PrivacyTermTestIE

#Change language from Settings
from LanguageChange import LanguageChangeTestFirefox
from LanguageChange import LanguageChangeTestChrome
from LanguageChange import LanguageChangeTestIE

#Test of create Cow Card and fill all cow card fields
from FullCowCardEdit import FullCowCardEditTestFirefox
from FullCowCardEdit import FullCowCardEditTestChrome
from FullCowCardEdit import FullCowCardEditTestIE

#Test of Create batch Actions
from BatchActions import BatchActionsTestFirefox

#Test Registration process
from RegistrationTest import RegistrationTestFirefox
from RegistrationTest import RegistrationTestChrome
from RegistrationTest import RegistrationTestIE

#get the directory path to output reprt file
dir=os.getcwd()

#get all tests from LoginTest class
login_logout_Firefox=unittest.TestLoader().loadTestsFromTestCase(LoginTestFirefox)
login_logout_Chrome=unittest.TestLoader().loadTestsFromTestCase(LoginTestChrome)
login_logout_IE=unittest.TestLoader().loadTestsFromTestCase(LoginTestIE)

#Switch Dashboard tab with Data tab tests
dashboard_data_Firefox=unittest.TestLoader().loadTestsFromTestCase(DashboardDataTestFirefox)
dashboard_data_Chrome=unittest.TestLoader().loadTestsFromTestCase(DashboardDataTestChrome)
dashboard_data_IE=unittest.TestLoader().loadTestsFromTestCase(DashboardDataTestIE)

#Switch between Settings to Dashboard tests
settings_Firefox=unittest.TestLoader().loadTestsFromTestCase(SettingsTestFirefox)
settings_Chrome=unittest.TestLoader().loadTestsFromTestCase(SettingsTestChrome)
settings_IE=unittest.TestLoader().loadTestsFromTestCase(SettingsTestIE)

#Switch between Settings tabs
devices_alerts_account_switch_Firefox=unittest.TestLoader().loadTestsFromTestCase(SettingsTabSwitchTestFirefox)
devices_alerts_account_switch_Chrome=unittest.TestLoader().loadTestsFromTestCase(SettingsTabSwitchTestChrome)
devices_alerts_account_switch_IE=unittest.TestLoader().loadTestsFromTestCase(SettingsTabSwitchTestIE)

#Not Identification Cow Reports
not_id_report_Firefox=unittest.TestLoader().loadTestsFromTestCase(NotIdentifiedNavigationFirefox)
not_id_report_Chrome=unittest.TestLoader().loadTestsFromTestCase(NotIdentifiedNavigationChrome)
not_id_report_IE=unittest.TestLoader().loadTestsFromTestCase(NotIdentifiednavigationIE)


#Switch between Farm Trends
farm_trends_switch_Firefox=unittest.TestLoader().loadTestsFromTestCase(FarmTrendsSwitchFirefox)
farm_trends_switch_Chrome=unittest.TestLoader().loadTestsFromTestCase(FarmTrendsSwitchChrome)
farm_trends_switch_IE=unittest.TestLoader().loadTestsFromTestCase(FarmTrendsSwitchIE)


#Open a Heat Cows Report from dashboard
cows_heat_report_Firefox=unittest.TestLoader().loadTestsFromTestCase(OpenHeatReportFirefox)
cows_heat_report_Chrome=unittest.TestLoader().loadTestsFromTestCase(OpenHeatReportChrome)
cows_heat_report_IE=unittest.TestLoader().loadTestsFromTestCase(OpenHeatReportIE)

#Add Note to Farm from Dashboard
add_note_to_farm_Firefox=unittest.TestLoader().loadTestsFromTestCase(AddDeleteNoteToFarmFirefox)
add_note_to_farm_Chrome=unittest.TestLoader().loadTestsFromTestCase(AddDeleteNoteToFarmChrome)
add_note_to_farm_IE=unittest.TestLoader().loadTestsFromTestCase(AddDeleteNoteToFarmIE)

#open More reports
open_more_reports_Firefox=unittest.TestLoader().loadTestsFromTestCase(openMoreReportsTestFirefox)
open_more_reports_Chrome=unittest.TestLoader().loadTestsFromTestCase(openMoreReportsTestChrome)
open_more_reports_IE=unittest.TestLoader().loadTestsFromTestCase(openMoreReportsTestIE)

#Switch between reports
switch_reports_Firefox=unittest.TestLoader().loadTestsFromTestCase(SwitchReportsTestFirefox)
switch_reports_Chrome=unittest.TestLoader().loadTestsFromTestCase(SwitchReportsTestChrome)
switch_reports_IE=unittest.TestLoader().loadTestsFromTestCase(SwitchReportsTestIE)


#Switch between pages on All Cows Report
switch_pages_Firefox=unittest.TestLoader().loadTestsFromTestCase(SwitchBetweenPagesOnAllCowsReportTestFirefox)
switch_pages_Chrome=unittest.TestLoader().loadTestsFromTestCase(SwitchBetweenPagesOnAllCowsReportTestChrome)
switch_pages_IE=unittest.TestLoader().loadTestsFromTestCase(SwitchBetweenPagesOnAllCowsReportTestIE)

#Switch pages with Arrows
switch_Arrows_Firefox=unittest.TestLoader().loadTestsFromTestCase(SwitchPagesWithArrowsTestFirefox)
switch_Arrows_Chrome=unittest.TestLoader().loadTestsFromTestCase(SwitchPagesWithArrowsTestChrome)
switch_Arrows_IE=unittest.TestLoader().loadTestsFromTestCase(SwitchPagesWithArrowsTestIE)

#Open Cow Card from data Tab
open_cow_card_Firefox=unittest.TestLoader().loadTestsFromTestCase(FindCowFromDataTabTestFirefox)
open_cow_card_Chrome=unittest.TestLoader().loadTestsFromTestCase(FindCowFromDataTabTestChrome)
open_cow_card_IE=unittest.TestLoader().loadTestsFromTestCase(FindCowFromDataTabTestIE)

# Open specific Cow card and start switch between it scheduale graph presentation
graph_days_switch_Firefox=unittest.TestLoader().loadTestsFromTestCase(SwitchGraphsOnCowCardTestFirefox)
graph_days_switch_Chrome=unittest.TestLoader().loadTestsFromTestCase(SwitchGraphsOnCowCardTestChrome)
graph_days_switch_IE=unittest.TestLoader().loadTestsFromTestCase(SwitchGraphsOnCowCardTestIE)

# Open Health Report from dashboard
open_Health_report_Firefox=unittest.TestLoader().loadTestsFromTestCase(OpenHealthReportFirefox)
open_Health_report_Chrome=unittest.TestLoader().loadTestsFromTestCase(OpenHealthReportChrome)
open_Health_report_IE=unittest.TestLoader().loadTestsFromTestCase(OpenHealthReportIE)

#Open Cow Card and switch between available graphs
graphs_switch_on_cow_card_Firefox=unittest.TestLoader().loadTestsFromTestCase(SwitchBetweenGraphsTestFirefox)
graphs_switch_on_cow_card_Chrome=unittest.TestLoader().loadTestsFromTestCase(SwitchBetweenGraphsTestChrome)
graphs_switch_on_cow_card_IE=unittest.TestLoader().loadTestsFromTestCase(SwitchBetweenGraphsTestIE)

#Open different Cow cards by switch between each other by press on Next and Prev buttons
next_prev_cow_card_Firefox=unittest.TestLoader().loadTestsFromTestCase(NextPrevCowCardTestFirefox)
next_prev_cow_card_Chrome=unittest.TestLoader().loadTestsFromTestCase(NextPrevCowCardTestChrome)
next_prev_cow_card_IE=unittest.TestLoader().loadTestsFromTestCase(NextPrevCowCardTestIE)

#open/generate a new Cow Card and delete at the end of test
add_delete_cow_card_Firefox=unittest.TestLoader().loadTestsFromTestCase(AddNewCowCardTestFirefox)
add_delete_cow_card_Chrome=unittest.TestLoader().loadTestsFromTestCase(AddNewCowCardTestChrome)
add_delete_cow_card_IE=unittest.TestLoader().loadTestsFromTestCase(AddNewCowCardTestIE)

#Open Privacy Policy and Terms of Use pages
privacy_terms_pages_Firefox=unittest.TestLoader().loadTestsFromTestCase(PrivacyTermTestFirefox)
privacy_terms_pages_Chrome=unittest.TestLoader().loadTestsFromTestCase(PrivacyTermTestTestChrome)
privacy_terms_pages_IE=unittest.TestLoader().loadTestsFromTestCase(PrivacyTermTestIE)

#Change Language effect from Settings
language_change_Firefox=unittest.TestLoader().loadTestsFromTestCase(LanguageChangeTestFirefox)
language_change_Chrome=unittest.TestLoader().loadTestsFromTestCase(LanguageChangeTestChrome)
language_change_IE=unittest.TestLoader().loadTestsFromTestCase(LanguageChangeTestIE)

#Test of Create A full filled Cow cards
full_new_cow_card_Firefox=unittest.TestLoader().loadTestsFromTestCase(FullCowCardEditTestFirefox)
full_new_cow_card_Chrome=unittest.TestLoader().loadTestsFromTestCase(FullCowCardEditTestChrome)
full_new_cow_card_IE=unittest.TestLoader().loadTestsFromTestCase(FullCowCardEditTestIE)

#Test Batch actions functionality
batch_actions_on_Firefox=unittest.TestLoader().loadTestsFromTestCase(BatchActionsTestFirefox)

#Test option of create a new user
new_user_registration_Firefox=unittest.TestLoader().loadTestsFromTestCase(RegistrationTestFirefox)
#TODO
#new_user_registration_Chrome=unittest.TestLoader().loadTestsFromTestCase(RegistrationTestChrome)
#new_user_registration_IE=unittest.TestLoader().loadTestsFromTestCase(RegistrationTestIE)





general_tests=unittest.TestSuite([login_logout_IE])
#general_tests=unittest.TestSuite([login_logout_Firefox,login_logout_Chrome,login_logout_IE,dashboard_data_Firefox,dashboard_data_Chrome,dashboard_data_IE,settings_Firefox,settings_Chrome,settings_IE,devices_alerts_account_switch_Firefox,devices_alerts_account_switch_Chrome,devices_alerts_account_switch_IE,
#                                 not_id_report_Firefox,not_id_report_Chrome,not_id_report_IE,farm_trends_switch_Firefox,farm_trends_switch_Chrome,farm_trends_switch_IE,cows_heat_report_Firefox,cows_heat_report_Chrome,cows_heat_report_IE,
#                                 add_note_to_farm_Firefox,add_note_to_farm_Chrome,add_note_to_farm_IE,open_more_reports_Firefox,open_more_reports_Chrome,open_more_reports_IE])
#
#general_tests1=unittest.TestSuite([switch_reports_Firefox,switch_reports_Chrome,switch_reports_IE,switch_pages_Firefox,switch_pages_Chrome,switch_pages_IE,switch_Arrows_Firefox,switch_Arrows_Chrome,switch_Arrows_IE,
#                                  open_cow_card_Firefox,open_cow_card_Chrome,open_cow_card_IE,graph_days_switch_Firefox,graph_days_switch_Chrome,graph_days_switch_IE,open_Health_report_Firefox,open_Health_report_Chrome,
#                                  open_Health_report_IE,graphs_switch_on_cow_card_Firefox,graphs_switch_on_cow_card_Chrome,graphs_switch_on_cow_card_IE,next_prev_cow_card_Firefox,next_prev_cow_card_Chrome,next_prev_cow_card_IE,
#                                  add_delete_cow_card_Firefox,add_delete_cow_card_Chrome,add_delete_cow_card_IE,privacy_terms_pages_Firefox,privacy_terms_pages_Chrome,privacy_terms_pages_IE,language_change_Firefox,language_change_Chrome,
#                                  language_change_IE,full_new_cow_card_Firefox,full_new_cow_card_Chrome,full_new_cow_card_IE])

#general_tests=unittest.TestSuite([switch_reports_Firefox,switch_reports_Chrome,switch_reports_IE])
#general_tests=unittest.TestSuite([add_delete_cow_card_Firefox,add_delete_cow_card_Chrome,add_delete_cow_card_IE])
#general_tests=unittest.TestSuite([full_new_cow_card_Chrome])


#open the report file
outfile=open(dir+"\LoginLogoutReport2.html","wb")

#configure HTMLTestRunner options
runner=HTMLTestRunner.HTMLTestRunner(stream=outfile,title="Firefox/Chrome/IE Portal Navigation Tests Report",verbosity=2,description="Test Navigations on Firefox/Chrome/IE")

#run the suite using HTMLTestRunner
runner.run(general_tests)
#runner.run(general_tests1)
