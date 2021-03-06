# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

class TestKycandy():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  # def teardown_method(self, method):
  #   self.driver.quit()
  
  def test_kycandy(self):
    self.driver.get("http://portal.dev.getzense.com/")
    # wait for element and click #
    loginbutton = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.LINK_TEXT, "Log in")))
    loginbutton.click()
    ##############################

    # Authentication
    elementlogin = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "email")))
    elementlogin.click()
    self.driver.find_element(By.ID, "email").send_keys("andyfreddie@freddiemac.com")
    self.driver.find_element(By.ID, "loginForm").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Andy1234=")
    self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[1]/form/div[3]/div[3]/button").click()
######################################

    # Start KYC
    kyctrigger = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[2]/div/div[2]/a")))
    kyctrigger.click()
######################################

    # Step 00 Loan Purpose
    loanpurpose = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "loan_purpose_purchase_button")))
    loanpurpose.click()
    loanjoint = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "type_of_credit_joint_button")))
    loanjoint.click()    
    Select(self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[2]/select")).select_by_value('4')
    # dropdown = self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[2]/select")
    # dropdown.find_element(By.XPATH, "//option[. = '4']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(5)").click()
    # self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[3]/div[1]/div/input[2]").click()
    self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[3]/div[1]/div/input[2]").send_keys("amyfreddie@freddiemac.com")
    # self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[3]/div[2]/div/input[2]").click()
    self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[3]/div[2]/div/input[2]").send_keys("alicefreddie@freddiemac.com")
    # self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[3]/div[3]/div/input[2]").click()
    self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[3]/div[3]/div/input[2]").send_keys("suzifreddie@freddiemac.com")
    # self.driver.find_element(By.XPATH, "div:nth-child(4) > .mb-4 > .appearance-none").click()
    self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[3]/div[4]/div/input[2]").send_keys("elizabethfreddie@freddiemac.com")
    self.driver.find_element(By.XPATH, "/html/body/div/div/main/div[1]/div/div/form/div[1]/div[4]/button").click()
######################################

    # Step 01 Full name
    self.driver.implicitly_wait(5) # seconds
    name = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[first_name]")))
    name.send_keys("Andy")
    self.driver.find_element(By.NAME, "kyc[last_name]").send_keys("Freddie")
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 02 Birth Date
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][0]")).select_by_value('MARCH')
    Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][1]")).select_by_value('23')
    Select(self.driver.find_element(By.NAME, "kyc[date_of_birth][2]")).select_by_value('1971')
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 03 Gender
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    Select(self.driver.find_element(By.NAME, "kyc[gender]")).select_by_value('MALE')
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 04 Dependents
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[dependents_number]")))
    Select(self.driver.find_element(By.NAME, "kyc[dependents_number]")).select_by_value('0')
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 05 Citizenship
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[citizenship]")))
    Select(self.driver.find_element(By.NAME, "kyc[citizenship]")).select_by_value('U.S. CITIZEN')
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 06 Marital Status
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[marital_status]")))
    Select(self.driver.find_element(By.NAME, "kyc[marital_status]")).select_by_value('MARRIED')
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 07 SSN
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "ssn_number")))
    self.driver.find_element(By.ID, "ssn_number").send_keys("990-30-0003")
    self.driver.find_element(By.CSS_SELECTOR, ".fa-2x").click()
    self.driver.find_element(By.ID, "kyc_step7_next_button").click()
#####################################

    # Step 08 Phone Number
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[home_phone_number]")))
    # self.driver.find_element(By.NAME, "kyc[home_phone_number]").click()
    self.driver.find_element(By.NAME, "kyc[home_phone_number]").send_keys("(555) 222-2222") #Home 
    # self.driver.find_element(By.NAME, "kyc[cell_phone_number]").click()
    self.driver.find_element(By.NAME, "kyc[cell_phone_number]").send_keys("(555) 333-3333") #Cell
    # self.driver.find_element(By.NAME, "kyc[work_phone_number]").click()
    self.driver.find_element(By.NAME, "kyc[work_phone_number]").send_keys("(555) 999-9999") #Work
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 09 Current Address
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "current_address[street]")))
    # self.driver.find_element(By.NAME, "current_address[street]").click()
    self.driver.find_element(By.NAME, "current_address[street]").send_keys("4321 Cul de Sac St")
    # self.driver.find_element(By.NAME, "current_address[city]").click()
    self.driver.find_element(By.NAME, "current_address[city]").send_keys("Someplace")
    # self.driver.find_element(By.NAME, "current_address[zipcode]").click()
    self.driver.find_element(By.NAME, "current_address[zipcode]").send_keys("02723")
    # self.driver.find_element(By.NAME, "current_address[years]").click()
    Select(self.driver.find_element(By.NAME, "current_address[years]")).select_by_value('2')
    Select(self.driver.find_element(By.NAME, "current_address[months]")).select_by_value('2')
    Select(self.driver.find_element(By.NAME, "current_address[housing]")).select_by_value('RENT')
    # self.driver.find_element(By.NAME, "current_address[rent_per_month]").click()
    self.driver.find_element(By.NAME, "current_address[rent_per_month]").send_keys("1500")
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 10 Mailing Address
    check = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "mailing_address[does_not_apply]")))
    check.click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################
   
    # Step 11 served army
    military = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_military_service_false")))
    military.click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 12 preferred language
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "kyc[language_preference]")))
    Select(self.driver.find_element(By.NAME, "kyc[language_preference]")).select_by_value('ENGLISH')
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 13 Please tell us about your income.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
#     self.driver.find_element(By.ID, "knockout_question_9bd53ae6-99b3-45be-84e3-52b2cdd02849_false").click()
#     self.driver.find_element(By.ID, "knockout_question_9388b75c-b3b6-442c-b955-aabf512902c3_false").click()
#     self.driver.find_element(By.ID, "knockout_question_dafc6a06-83ca-45ff-bd1b-f1586db97cf7_false").click()
#     self.driver.find_element(By.ID, "knockout_question_313120fb-0d79-4a9f-a029-19fce52b28b4_false").click()
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 14 Please tell us about your credit.
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
#     self.driver.find_element(By.ID, "knockout_question_1b338701-2342-43d4-8efe-ee943e34c042_false").click()
#     self.driver.find_element(By.ID, "knockout_question_e0776d4d-d0c5-49cc-896a-d70775c512ec_false").click()
#     self.driver.find_element(By.ID, "knockout_question_48273e18-42b0-4ca9-9651-36f7a45ae77e_false").click()
#     self.driver.find_element(By.ID, "knockout_question_1b5397ba-8223-4260-a483-c18d551415fc_false").click()
#     self.driver.find_element(By.ID, "knockout_question_89bdb434-22b3-444e-b479-cb0330d3dfbf_false").click()
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 15 Tell us about your employment.
#     WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
#     self.driver.find_element(By.NAME, "current_employments[0][employer_name]").send_keys("Employer")
#     # self.driver.find_element(By.NAME, "current_employments[0][position]").click()
#     self.driver.find_element(By.NAME, "current_employments[0][position]").send_keys("Employee")
#     # self.driver.find_element(By.NAME, "current_employments[0][phone]").click()
#     self.driver.find_element(By.NAME, "current_employments[0][phone]").send_keys("(703) 555-1212")
#     # self.driver.find_element(By.NAME, "current_employments[0][street]").click()
#     self.driver.find_element(By.NAME, "current_employments[0][street]").send_keys("Employer Address Rd")
#     # self.driver.find_element(By.NAME, "current_employments[0][city]").click()
#     self.driver.find_element(By.NAME, "current_employments[0][city]").send_keys("Dawson")
#     # self.driver.find_element(By.NAME, "current_employments[0][state]").click()
#     self.driver.find_element(By.NAME, "current_employments[0][state]").send_keys("IA")
#     # self.driver.find_element(By.NAME, "current_employments[0][zipcode]").click()
#     self.driver.find_element(By.NAME, "current_employments[0][zipcode]").send_keys("50066")
#     # self.driver.find_element(By.NAME, "current_employments[0][start_date][0]").click()
#     Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][0]")).select_by_value('JANUARY')
#     Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][1]")).select_by_value('1')
#     Select(self.driver.find_element(By.NAME, "current_employments[0][start_date][2]")).select_by_value('2016')
#     # self.driver.find_element(By.NAME, "current_employments[0][base_income]").click()
#     self.driver.find_element(By.NAME, "current_employments[0][base_income]").send_keys("$7,680")
#     self.driver.find_element(By.ID, "kyc_next_button").click()
# #####################################

#     # Step 16 Tell us about your assets.
#     WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "add_another_job")))
#     Select(self.driver.find_element(By.NAME, "assets[0][account_type]")).select_by_value('OTHER') #CHECKINGS
#     # self.driver.find_element(By.NAME, "assets[0][financial_institution]").click()
#     self.driver.find_element(By.NAME, "assets[0][financial_institution]").send_keys("FinBank Profiles - A")
#     # self.driver.find_element(By.NAME, "assets[0][account_number]").click()
#     self.driver.find_element(By.NAME, "assets[0][account_number]").send_keys("9223")
#     # self.driver.find_element(By.NAME, "assets[0][market_value]").click()
#     self.driver.find_element(By.NAME, "assets[0][market_value]").send_keys("$45,000")

#     WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "add_another_job")))
#     self.driver.find_element(By.ID, "add_another_job").click()
#     Select(self.driver.find_element(By.NAME, "assets[1][account_type]")).select_by_value('OTHER') #SAVING
#     # self.driver.find_element(By.NAME, "assets[1][financial_institution]").click()
#     self.driver.find_element(By.NAME, "assets[1][financial_institution]").send_keys("Dag Site")
#     # self.driver.find_element(By.NAME, "assets[1][account_number]").click()
#     self.driver.find_element(By.NAME, "assets[1][account_number]").send_keys("109027")
#     # self.driver.find_element(By.NAME, "assets[1][market_value]").click()
#     self.driver.find_element(By.NAME, "assets[1][market_value]").send_keys("$45,000")

#     self.driver.find_element(By.CSS_SELECTOR, "div.max-w-xl:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > button:nth-child(1)").click()
#     Select(self.driver.find_element(By.NAME, "other_assets[0][asset_type]")).select_by_value('OTHER') #capitalgain
#     self.driver.find_element(By.NAME, "other_assets[0][market_value]").click()
#     self.driver.find_element(By.NAME, "other_assets[0][market_value]").send_keys("$100")

#     WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.flex-col:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)")))
#     self.driver.find_element(By.CSS_SELECTOR, "div.flex-col:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)").click()
#     Select(self.driver.find_element(By.NAME, "liabilities[0][account_type]")).select_by_value('INSTALLMENT (e.g., car, student, personal loans)')
#     self.driver.find_element(By.NAME, "liabilities[0][company_name]").click()
#     self.driver.find_element(By.NAME, "liabilities[0][company_name]").send_keys("Relentless Bank")
#     self.driver.find_element(By.NAME, "liabilities[0][account_number]").click()
#     self.driver.find_element(By.NAME, "liabilities[0][account_number]").send_keys("87615524")
#     self.driver.find_element(By.NAME, "liabilities[0][unpaid_balance]").click()
#     self.driver.find_element(By.NAME, "liabilities[0][unpaid_balance]").send_keys("$1,554")
#     self.driver.find_element(By.NAME, "liabilities[0][monthly_payment]").click()
#     self.driver.find_element(By.NAME, "liabilities[0][monthly_payment]").send_keys("$46")
#     Select(self.driver.find_element(By.ID, "to_be_paid_off")).select_by_value('No')
#     WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.pt-4:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)")))
#     self.driver.find_element(By.CSS_SELECTOR, "div.pt-4:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)").click()
#     Select(self.driver.find_element(By.NAME, "liabilities[1][account_type]")).select_by_value('REVOLVING (e.g., credit cards)')
#     self.driver.find_element(By.NAME, "liabilities[1][company_name]").click()
#     self.driver.find_element(By.NAME, "liabilities[1][company_name]").send_keys("Bursting Credit")
#     self.driver.find_element(By.NAME, "liabilities[1][account_number]").click()
#     self.driver.find_element(By.NAME, "liabilities[1][account_number]").send_keys("7612121")
#     self.driver.find_element(By.NAME, "liabilities[1][unpaid_balance]").click()
#     self.driver.find_element(By.NAME, "liabilities[1][unpaid_balance]").send_keys("$1,357")
#     self.driver.find_element(By.NAME, "liabilities[1][monthly_payment]").click()
#     self.driver.find_element(By.NAME, "liabilities[1][monthly_payment]").send_keys("$27")
#     Select(self.driver.find_element(By.NAME, "liabilities[1][to_be_paid_off]")).select_by_value('No')

#     self.driver.find_element(By.CSS_SELECTOR, "div.pt-4:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)").click()
#     Select(self.driver.find_element(By.NAME, "liabilities[2][account_type]")).select_by_value('REVOLVING (e.g., credit cards)')
#     self.driver.find_element(By.NAME, "liabilities[2][company_name]").click()
#     self.driver.find_element(By.NAME, "liabilities[2][company_name]").send_keys("Prime Visa")
#     self.driver.find_element(By.NAME, "liabilities[2][account_number]").click()
#     self.driver.find_element(By.NAME, "liabilities[2][account_number]").send_keys("71542341")
#     self.driver.find_element(By.NAME, "liabilities[2][unpaid_balance]").click()
#     self.driver.find_element(By.NAME, "liabilities[2][unpaid_balance]").send_keys("$45")
#     self.driver.find_element(By.NAME, "liabilities[2][monthly_payment]").click()
#     self.driver.find_element(By.NAME, "liabilities[2][monthly_payment]").send_keys("$40")
#     Select(self.driver.find_element(By.NAME, "liabilities[2][to_be_paid_off]")).select_by_value('No')



    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 17 Tell us about your property.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_real_estate_false")))
    self.driver.find_element(By.ID, "kyc_real_estate_false").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 19 Let's find out more about your mortgage.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 20 Provide us with your property information.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    self.driver.find_element(By.ID, "questionnaire_a_occupy_as_primary_residence_yes").click()
    self.driver.find_element(By.ID, "questionnaire_b_ownership_interest_no").click()
    self.driver.find_element(By.ID, "questionnaire_b_family_relationship_no").click()
    self.driver.find_element(By.ID, "questionnaire_c_borrowing_money_no").click()
    self.driver.find_element(By.ID, "questionnaire_d_apply_for_mortgage_no").click()
    self.driver.find_element(By.ID, "questionnaire_d_apply_for_new_credit_no").click()
    self.driver.find_element(By.ID, "questionnaire_e_subject_to_lien_no").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 21 Provide us with your finance detail.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    self.driver.find_element(By.ID, "questionnaire_a2_co_signer_no").click()
    self.driver.find_element(By.ID, "questionnaire_b2_outstanding_judgement_no").click()
    self.driver.find_element(By.ID, "questionnaire_c2_delinquent_no").click()
    self.driver.find_element(By.ID, "questionnaire_d2_lawsuit_no").click()
    self.driver.find_element(By.ID, "questionnaire_e2_conveyed_title_to_property_no").click()
    self.driver.find_element(By.ID, "questionnaire_f2_pre_foreclosure_sale_no").click()
    self.driver.find_element(By.ID, "questionnaire_g2_property_foreclosed_no").click()
    self.driver.find_element(By.ID, "questionnaire_h2_bankruptcy_no").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 22 Can you tell us about your race and ethnicity.
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .pt-6:nth-child(3) > .trueblok-radio").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .pt-6:nth-child(4) .trueblok-checkmark").click()
    self.driver.find_element(By.CSS_SELECTOR, ".pt-6:nth-child(6) .trueblok-checkmark").click()
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 23 Purchase
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "kyc_next_button")))
    self.driver.find_element(By.NAME, "property_address[street]").click()
    self.driver.find_element(By.NAME, "property_address[street]").send_keys("2422 Knapps way")
    self.driver.find_element(By.NAME, "property_address[state]").click()
    self.driver.find_element(By.NAME, "property_address[state]").send_keys("MD")
    self.driver.find_element(By.NAME, "property_address[city]").click()
    self.driver.find_element(By.NAME, "property_address[city]").send_keys("Odenton")
    self.driver.find_element(By.NAME, "property_address[zipcode]").click()
    self.driver.find_element(By.NAME, "property_address[zipcode]").send_keys("21113")
    Select(self.driver.find_element(By.NAME, "property_address[occupancy]")).select_by_value('PRIMARY RESIDENCE')
    self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(8) option:nth-child(2)").click()
    Select(self.driver.find_element(By.NAME, "property_address[property_type]")).select_by_value('SINGLE FAMILY RESIDENTIAL')
    self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(9) option:nth-child(2)").click()
    self.driver.find_element(By.NAME, "property_address[loan_amount]").click()
    self.driver.find_element(By.NAME, "property_address[loan_amount]").send_keys("$210,000")
    self.driver.find_element(By.ID, "kyc_next_button").click()
#####################################

    # Step 24 Docusign
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#package_0_li3 > .w-1\\/2:nth-child(2)")))
    self.driver.find_element(By.CSS_SELECTOR, "#package_0_li3 > .w-1\\/2:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bg-trueblok-primary:nth-child(2)").click()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, ".cb_label").click()
    self.driver.find_element(By.ID, "action-bar-btn-continue").click()
    element = self.driver.find_element(By.ID, "action-bar-btn-continue")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#navigate-btn > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".tab-image").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".item-alt-inline-block:nth-child(1)").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.ID, "action-bar-btn-finish").click()
    self.driver.find_element(By.LINK_TEXT, "GO BACK TO DASHBOARD").click()
    self.driver.switch_to.default_content()
    self.driver.find_element(By.CSS_SELECTOR, ".w-3\\/5").click()
  
