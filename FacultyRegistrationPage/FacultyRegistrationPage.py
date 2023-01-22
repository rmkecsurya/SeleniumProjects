from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


chromeDriver = webdriver.Chrome()
chromeDriver.maximize_window()
chromeDriver.get("https://www.icaionlineregistration.org/Fac_Reg.aspx")
chromeDriver.implicitly_wait(10)
POUName = Select(chromeDriver.find_element(By.XPATH,'//*[@id="ddlPOU"]'))
for i in POUName.all_selected_options:
    print(i)