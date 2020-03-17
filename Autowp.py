from selenium import webdriver

driver = webdriver.Chrome("C:\\webdrivers\\chromedriver.exe")
driver.get('https://web.whatsapp.com/')

input('Enter Anything:')

user = driver.find_element_by_class_name('X7YrQ')      #User to be attacted on
user.click()

msgbox=driver.find_element_by_class_name('_13mgZ')  #Finding messagebox
a=0
while(True):
    a=a+1
    msgbox.send_keys("Hello")
    button = driver.find_element_by_class_name('_3M-N-')  #This is Send button 
    button.click()
    print(a)