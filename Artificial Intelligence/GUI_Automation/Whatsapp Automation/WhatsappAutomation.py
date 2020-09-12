from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time 

class WhatsappAutomation():
    def __init__(self):
        try:
            self.message, self.count, self.time_interval = self.parameters()
            self.driver = self.create_chrome_driver()
            self.message_area = self.get_chrome(self.driver)
            self.send_message(self.count, self.message_area, 
                                        self.message, self.time_interval)
        except Exception as E:
            print(E)
            # print('\nPlease report the bug...')

    def create_chrome_driver(self):
        # 1
        BASE_DIR = os.path.dirname("__file__")
        CHROMEDRIVER = os.path.join(BASE_DIR, 'chromedriver.exe')
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
        return driver

    def parameters(self):
        # 2
        try:
            message = input('Enter the message you want to send: ')
            # number of time message is to be sent
            count = int(input('\nNumber of time you want to send: '))
            time_interval = int(input('\nEnter the time interval of sending message: '))
        except:
            print('\nYou have given invalid inputs')
            self.error()
        return message, count, time_interval

    def get_chrome(self, driver):
        # 3
        try:
            driver.get('https://web.whatsapp.com/')
            
            input('''\nProcedure to send automated message:\n 1. Let the browser open.\n 2. Open Whatsapp.\n 3. Open Chat to send message.\n 4. Let me know by pressing the ENTER key.\n\n''')

            message_area  = driver.find_element_by_xpath(
                                    '''//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'''
                                )
        except:
            print('You have network error. Please fix that first.')
            self.error()
        return message_area


    def send_message(self, count, message_area, message, time_interval, ):
        # 4
        try:
            for i in range(count):
                if time_interval:
                    time.sleep(time_interval)
                message_area.send_keys(message)
                message_area.send_keys(Keys.ENTER)
                if not(i%5):
                    print(f"Sent count {i}")
            print('All {} messages are sent keeping time interval of {}!!'
                                            .format(count, time_interval))
            print('\nExiting in 10 seconds...')
            time.sleep(10)
            self.driver.close()
        except Exception as e:
            print(e)
            print('\nYou have not followed the procedure appropriately. Sorry! I cannot help you in this...')
            self.error()


    def error(self, ):
            time.sleep(1)
            print('\nI am exiting...\n')
            time.sleep(3)
            self.driver.close()


if __name__ == "__main__":
    whatsapp_automation = WhatsappAutomation()

