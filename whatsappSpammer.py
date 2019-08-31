from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

target = input('Enter Target name:\n')
text = input('Enter the message:\n')
count = int(input('Enter the count:\n'))

input('Enter anything after you have scanned QR code: ')
time.sleep(5)
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(target))
user.click()
time.sleep(3)
msg_box = driver.find_element_by_class_name('_3u328')
for i in range(count):
    msg_box.send_keys(text)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()

print('\nMission Accomplished!\n')