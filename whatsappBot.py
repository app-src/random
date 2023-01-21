from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
print("sample test case started")  
driver = webdriver.Chrome()  

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/ashish/.config/google-chrome/Default")

driver.maximize_window()  
#navigate to the url  
driver.get("https://www.google.com/",options=options)
#identify the Google search text box and enter the value  
driver.find_element_by_name("q").send_keys("javatpoint")  
time.sleep(3)  
#click on the Google search button  
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
time.sleep(3)  
#close the browser  
driver.close()  
print("sample test case successfully completed")  
