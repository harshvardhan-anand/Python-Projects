import re
import datetime as dt

class DataCleaner():

    def clean_log_file(self, file_name=None, backspace='<Backspace>', space=' ', replace_key_by=None, 
                        special_keys_used_flag_as_set=False, print_cleaned_text=True):
        '''
        replace_key_by will not override backspace and space

        file_name = Provide the log file name created by KeyLogger to prettify.
        backspace = Key.backspace is to be replaced by.
        space = Key.space is to be replaced by
        replace_key_by = Other keys to be replaced by. If None then each key will be replaced by ' key '
        special_keys_used_flag_as_set = Will let you know what all special key used by the subject. Returns a  
                                        list. Provide a tuple (True, 1), means show unique special keys
        print_cleaned_text = Will print the cleaned text in output otherwise, will create a txt file to sace data.
        '''
        if not(file_name):
            raise Exception('Please provide a valid file name.')

        if (file_name.find('.txt')) == -1:
            file_name = str(file_name)+'.txt'

        try:
            with open(file_name, 'r') as logfile:
                data = logfile.read()
            self.__replace_key(data, backspace, space, replace_key_by, 
                                                special_keys_used_flag_as_set, print_cleaned_text)
        except Exception as E:
            print(E)



    def __replace_key(self, string, backspace, space, replace_key_by, 
                                                special_keys_used_flag_as_set, print_cleaned_text):
        '''
        Parameter - 
        string = Provide the data to be cleaned (string)
        backspace = Key.backspace is to be replaced by.
        space = Key.space is to be replaced by
        replace_key_by = Other keys to be replaced by.

        This function is helper function for check(string) function.
        '''
        try:
            regex_quote = re.compile(r'\'')
            # https://regex101.com/r/JiVuWJ/5
            regex_key = re.compile(r'(Key\..*?)(?:\'| |\d|\"|Key.esc|\s)')
            # removing quotes(') from the string and encoding the key
            string = string.replace('Key.backspace', str(backspace)).replace('Key.space', str(space))
            
            # It is not worthy to delete the special keys as the person might changed the window using 
            # hotkey
            # It is also not worth it to delete the word as person has changed the window and then 
            # deleted something else. So it may delete the required information
            # But if you want you can do that.
            # But we will provide space but again the same problem as discussed before.

            # special_keys_used will let us know what all special key subject have used.
            special_keys_used = re.findall(regex_key, string)+['Key.esc']

            if replace_key_by == None:
                for keys in special_keys_used:
                    if keys.strip()=='Key.backspace' :
                        continue
                    string = string.replace(keys, ' '+keys+' ')
            else:
                for keys in special_keys_used:
                    if keys.strip()=='Key.backspace' :
                        continue
                    string = string.replace(keys, replace_key_by)

            cleaned_text = re.sub(regex_quote, '', string)
            if print_cleaned_text:
                print(cleaned_text)
            else:
                try:
                    cleaned_log_file = ("cleaned_log_file_"+str(dt.datetime.now())[0:10]
                                        +'_'+str(dt.datetime.now())[11:]+'.txt').replace(':', '_')
                    with open(cleaned_log_file, 'w') as file:
                        file.write(cleaned_text)
                except Exception as E:
                    print(E)

            if special_keys_used_flag_as_set:
                if type(special_keys_used_flag_as_set) == tuple:
                    if special_keys_used_flag_as_set[1]:
                        print(set(special_keys_used))
                    else:
                        print(special_keys_used)
  
        except Exception as E:
            print(E)


d = DataCleaner()
d.clean_log_file(file_name='log', replace_key_by='', print_cleaned_text=False)