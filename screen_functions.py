import pyautogui
import os
from PIL import ImageGrab
import pytesseract
import time
import Levenshtein
import logging
import json


def access_url(**kwargs):
    pyautogui.click(kwargs["x"], kwargs["y"]) #access the url
    time.sleep(kwargs["timesleep"])
    pyautogui.typewrite(kwargs["url"])
    time.sleep(kwargs["timesleep"])
    pyautogui.hotkey('enter')

def wait_for_confirmation(key_word, a, b, c, d, time_out):
    time.sleep(2)
    str_test = 'ñÍ'
    start_time = time.time()
    while key_word not in str_test:
        time.sleep(1)
        if time.time() - start_time > time_out:
            return False
        screenshot = ImageGrab.grab(bbox=(a, b, c, d))
        str_test = pytesseract.image_to_string(screenshot)
    return True


def reload(**kwargs):
    
    access_url(**kwargs["dict_url"])
    
    time.sleep(2)
    
    wait_for_confirmation(**kwargs["dict_confirmationData"])
    
    time.sleep(3)
    
    pyautogui.click(*kwargs["1st_coord"]) #click on data onglet
    
    wait_for_confirmation(**kwargs["dict_confirmationApp"])
    
    pyautogui.click(*kwargs["2nd_coord"]) #click in APP DATA
    
    time.sleep(2.5)
    pyautogui.click(*kwargs["3rd_coord"])
    time.sleep(10)






def change_field(**kwargs):
    pyautogui.click(kwargs["x1"], kwargs["y1"]) 
    pyautogui.typewrite(kwargs["keyword"])
    time.sleep(kwargs["sleeptime"])
    pyautogui.click(kwargs["x2"], kwargs["y2"])
    time.sleep(kwargs["sleeptime"])

def select_data_type(**kwargs):
    pyautogui.click(*kwargs["type_coord"]) #click the data type 
    time.sleep(kwargs["1st_timesleep"])
    pyautogui.typewrite('lineItems')
    time.sleep(kwargs["2nd_timesleep"])
    pyautogui.click(*kwargs["select_coord"]) #click at TimeCard


def do_process(**kwargs):
    pyautogui.hotkey('win', '1')
    reload(**kwargs["dict_reload"])
    file_list = os.listdir(kwargs["path_i"])
    i_file = 0
    while True:

        file_name = file_list[i_file]

        validation = wait_for_confirmation(**kwargs["1_validation"])
        if not validation:
            reload(**kwargs["dict_reload"])
            continue
        time.sleep(**kwargs["time_sleep"][0])

        pyautogui.click(**kwargs["upload_click"]) #click upload
        validation = wait_for_confirmation(**kwargs["2_validation"])
        if not validation:
            reload(**kwargs["dict_reload"])
            continue
        time.sleep(**kwargs["time_sleep"][1])
        
        select_data_type(**kwargs["type"])
        validation = wait_for_confirmation(**kwargs["3_validation"])
        if not validation:
            reload(**kwargs["dict_reload"])
            continue
        time.sleep(**kwargs["time_sleep"][2])


        pyautogui.click(**kwargs["choose_click"]) #cick the choose file
        time.sleep(**kwargs["time_sleep"][3])

        pyautogui.click(*kwargs["path_click"]) #click the path
        time.sleep(**kwargs["time_sleep"][4])
        pyautogui.typewrite(kwargs["path_i"]) #enter the path
        time.sleep(**kwargs["time_sleep"][5])
        pyautogui.hotkey('enter')


        pyautogui.click(*kwargs["file_name_coord"]) #230 417
        time.sleep(**kwargs["time_sleep"][6])
        pyautogui.typewrite(file_name) #enter the path
        pyautogui.hotkey('enter')


        change_field(**kwargs["field1"])

        pyautogui.click(*kwargs["validate"]) #validate data
        validation = wait_for_confirmation(**kwargs["4_validation"])
        if not validation:
            reload(**kwargs["dict_reload"])
            continue
        pyautogui.hotkey('end')
        time.sleep(**kwargs["time_sleep"][11])
        pyautogui.click(*kwargs["upload_data"]) #upload data
        validation = wait_for_confirmation(**kwargs["5_validation"])
        if not validation:
            reload(**kwargs["dict_reload"])
            continue
        pyautogui.click(*kwargs["new_upload"])
        time.sleep(**kwargs["time_sleep"][12])
        pyautogui.hotkey('f5')

        i_file+=1
        if i_file >= len(file_list):
            break
        


def do_type_file(type_file: str):

    dir=open("directios.json","r")
    dir = json.load(dir)
    file1 = open(dir[type_file],"r")
    args_dict = json.load(file1)

    do_process(**args_dict)

