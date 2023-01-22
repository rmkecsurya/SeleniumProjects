from selenium import webdriver
import time
from selenium.webdriver.common.by import By

chromeDriver = webdriver.Chrome()
chromeDriver.implicitly_wait(10)
# Name using Full Xpath
chromeDriver.get("http://www.alpacajs.org/demos/bootstrap/registration/index.html")
chromeDriver.maximize_window()
# Name
chromeDriver.find_element(By.NAME, 'name').send_keys("Surya")
time.sleep(1.5)
# Email
chromeDriver.find_element(By.ID, 'alpaca4').send_keys("Surya@gmail.com")
time.sleep(1.5)
# Organization
chromeDriver.find_element(By.XPATH, '//*[@id="alpaca5"]').send_keys("Epiance Software Pvt Ltd")
time.sleep(1.5)
# Work Phone
chromeDriver.find_element(By.CSS_SELECTOR, '#alpaca6').send_keys("9876543210")
time.sleep(1.5)
# Cell Phone
chromeDriver.find_element(By.XPATH, '//*[@id="alpaca7"]').send_keys("9876543210")
time.sleep(1.5)
# Address1
chromeDriver.find_element(By.ID, 'alpaca8').send_keys("Thathuguni")
time.sleep(1.5)
# Address2
chromeDriver.find_element(By.ID, 'alpaca9').send_keys("Bangalore South")
time.sleep(1.5)
# City
chromeDriver.find_element(By.NAME, 'city').send_keys("Bangalore")
time.sleep(1.5)
# City
chromeDriver.find_element(By.NAME, 'state').send_keys("Kansas")
time.sleep(1.5)
# Zip/Postal code:
chromeDriver.find_element(By.NAME, 'zipcode').send_keys("12345-6789")
time.sleep(1.5)
# Country (if other than U.S.):
chromeDriver.find_element(By.NAME, 'country').send_keys("India")
time.sleep(1.5)
# Emergency contact (name and number):
chromeDriver.find_element(By.XPATH, '//*[@id="alpaca14"]').send_keys("Surya and 9876543210")
time.sleep(1.5)
# you a vegetarian:
chromeDriver.find_element(By.XPATH, '//*[@id="contact-info-fields"]/div[13]/div/div/div[2]/label/input').click()
time.sleep(1.5)
# Please specify any other dietary requirements:
chromeDriver.find_element(By.XPATH, '//*[@id="alpaca16"]').send_keys("Nothing")
time.sleep(1.5)
# Will you need a room on Monday, June 3rd?
chromeDriver.find_element(By.XPATH, '//*[@id="contact-info-fields"]/div[15]/div/div/div[2]/label/input').click()
time.sleep(1.5)
# Will you need a room on Tuesday, June 4th?
chromeDriver.find_element(By.XPATH, '//*[@id="contact-info-fields"]/div[16]/div/div/div[2]/label/input').click()
time.sleep(1.5)
# Will you need a room on Wednesday, June 5th?
chromeDriver.find_element(By.XPATH, '//*[@id="contact-info-fields"]/div[17]/div/div/div[2]/label/input').click()
time.sleep(1.5)
# Will you be attending the reception and dinner on Monday, June 3rd?
chromeDriver.find_element(By.XPATH, '//*[@id="contact-info-fields"]/div[19]/div/div/div[2]/label/input').click()
time.sleep(1.5)
# Will you be attending the reception and dinner on Tuesday, June 4th?
chromeDriver.find_element(By.XPATH, '//*[@id="contact-info-fields"]/div[20]/div/div/div[2]/label/input').click()
time.sleep(1.5)
# Cambridge tour (date and time to be determined)?
chromeDriver.find_element(By.XPATH, '//*[@id="contact-info-fields"]/div[21]/div/div/div[2]/label/input').click()
time.sleep(1.5)

# Please specify how you would like to book your travel arrangements.
chromeDriver.find_element(By.XPATH, '//*[@id="travel-arrangements-fields"]/div/div/div/div[1]/label/input').click()
time.sleep(1.5)
chromeDriver.find_element(By.XPATH, '//*[@id="travel-arrangements-fields"]/div/div/div/div[2]/label/input').click()
time.sleep(1.5)
chromeDriver.find_element(By.XPATH, '//*[@id="travel-arrangements-fields"]/div/div/div/div[3]/label/input').click()
time.sleep(1.5)
# Your website:
chromeDriver.find_element(By.XPATH, '//*[@id="alpaca25"]').send_keys("epiplex.com")
time.sleep(1.5)
# File Upload
chromeDriver.find_element(By.NAME, 'photoFile').send_keys("C:\\Users\\Surya\\Downloads\\nature.jpg")
# Your biography (limit of 250 words):
chromeDriver.find_element(By.XPATH, '//*[@id="alpaca27"]').send_keys('''
Biography is the earliest literary genre in history. According to 
Egyptologist Miriam Lichtheim, writing took its first steps toward literature 
in the context of the private tomb funerary inscriptions. These were commemorative 
 texts recounting the careers of deceased high royal officials.[2] The earliest biographical 
 texts are from the 26th century BC. In the 21st century BC, another famous biography was composed 
 in Mesopotamia about Gilgamesh. One of the five versions could be historical. From the same region 
 a couple of centuries later, according to another famous biography, departed Abraham. He and his 3 
 descendants became subjects of ancient Hebrew biographies whether fictional or historical. One of the 
 earliest Roman biographers was Cornelius Nepos, who published his work Excellentium Imperatorum Vitae 
 ("Lives of outstanding generals") in 44 BC. Longer and more extensive biographies were written in Greek 
 by Plutarch, in his Parallel Lives, published about 80 A.D. In this work famous Greeks are paired with 
 famous Romans, for example the orators Demosthenes and Cicero, or the generals Alexander the Great and 
 Julius Caesar; some fifty biographies from the work survive. Another well-known collection of ancient 
 biographies is De vita Caesarum ("On the Lives of the Caesars") by Suetonius, written about AD 121 in 
 the time of the emperor Hadrian. Meanwhile, in the eastern imperial periphery, Gospel described the life 
 of Jesus.''')
time.sleep(1.5)

chromeDriver.quit()
