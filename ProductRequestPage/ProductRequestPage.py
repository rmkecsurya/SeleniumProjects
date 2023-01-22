from selenium import webdriver
import time
from selenium.webdriver.common.by import By


chromeDriver = webdriver.Chrome()
chromeDriver.maximize_window()
chromeDriver.get("https://epiplex500.com/qa/Licenserequest.htm?")
chromeDriver.implicitly_wait(10)
chromeDriver.find_element(By.ID, 'partnerName').send_keys("This is partnername")

chromeDriver.find_element(By.XPATH, '//*[@id="partnerEmail"]').send_keys("gmail@gmail.com")

chromeDriver.find_element(By.CSS_SELECTOR, "#partnerPhone").send_keys("+91 9876543210")

chromeDriver.find_element(By.ID, 'orderPrice').send_keys("Orderprice")

chromeDriver.find_element(By.XPATH, "/html/body/form/div[2]/div[2]/div[2]/div[5]/input").send_keys("Order Reference")

chromeDriver.find_element(By.ID, "licOnly").click()

chromeDriver.find_element(By.ID, "withAMC").click()

paymentMethod = chromeDriver.find_elements(By.NAME,"payment")
paymentMethod[1].click()

chromeDriver.find_element(By.ID, "contactPersonName").send_keys("Secondary Name")

chromeDriver.find_element(By.CSS_SELECTOR,"#contactPersonEmail").send_keys("personalemail@gmail.com")

chromeDriver.find_element(By.ID,"contactPersonPhonenumber").send_keys("+91 9876543210")

chromeDriver.find_element(By.ID, "pr1").click()

#chromeDriver.find_element(By.CLASS_NAME,"form-control  frmControlWidth").send_keys("30")
chromeDriver.find_element(By.CSS_SELECTOR,"#licenseCount").send_keys("30")
chromeDriver.find_element(By.ID, "comments").send_keys("Comments section")
chromeDriver.find_element(By.XPATH, '//*[@id="cmdsubmit"]').click()
chromeDriver.close()