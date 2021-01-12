from selenium import webdriver

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://web.whatsapp.com/")

names = input('Enter names: ')
s = names.split(',')
names = list(s)

msg = input('Enter message: ')
count = int(input('How many times? '))

input('If you are sure, press enter...')

for name in names:
    user = driver.find_element_by_xpath("//span[@title = '{}']".format(name))
    user.click()
    msgbox = driver.find_element_by_class_name('_3FRCZ')

    for i in range(count):
        msgbox.send_keys(msg)
        button = driver.find_element_by_class_name('_1U1xa')
        button.click()
