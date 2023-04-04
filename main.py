import pyautogui
import os
from PIL import ImageGrab
import pytesseract
import time
import Levenshtein
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path_i = r'C:\Users\JF_db\Desktop\database\timecards\Data\queue'
path_f = r'C:\Users\JF_db\Desktop\database\timecards\Data\done'
url = r'https://bubble.io/page?id=sammanger'
directory = 'All TimeCards'

def click(xcoordinate, ycoordinate):
    pyautogui.click(xcoordinate, ycoordinate)

def search_for_file(image_text):
    closest_name = None
    closest_distance = float('inf')
    for file_name in os.listdir(path_i):
        distance = Levenshtein.distance(image_text, file_name)
        if distance < closest_distance:
            closest_name = file_name
            closest_distance = distance
    return closest_name

def reload(first_run):
    click(162, 48) #access the url
    time.sleep(0.3)
    pyautogui.typewrite(url)
    time.sleep(0.3)
    pyautogui.hotkey('enter')
    time.sleep(2)
    wait_for_confirmation('Data', 12, 263, 48, 279, time_out=10)
    time.sleep(3)
    click(44, 276) #click on data onglet
    wait_for_confirmation('App', 348, 150, 409, 171, time_out = 10)
    click(409, 171) #click in APP DATA
    time.sleep(1.5)
    if first_run == True:
        click(943,226) #click on live server
        time.sleep(10) #wait for the web app to charge
     
def wait_for_confirmation(key_word, a, b, c, d, time_out):
    time.sleep(2)
    str_test = 'ñÍ'
    start_time = time.time()
    while True:
        time.sleep(0.5)
        screenshot = ImageGrab.grab(bbox=(a, b, c, d))
        str_test = pytesseract.image_to_string(screenshot)
        if key_word in str_test: return True
        try:
            for word in str_test.split():
                distance = Levenshtein.distance(key_word, word)
                if distance < 2: return True
        except ValueError: pass
        if time.time() - start_time > time_out:
            return False

pyautogui.hotkey('win', '1')
first_run = True
reload(first_run)
for file_name in os.listdir(path_i):
    u_completed = False
    while u_completed == False:
        validation = wait_for_confirmation('Data', 12, 263, 48, 279, time_out=10)
        if validation == False:
            reload(True)
            continue
        time.sleep(5)
        click(850, 275) #click upload
        validation = wait_for_confirmation('chosen', 93, 280, 195, 299, time_out= 10)
        if validation == False:
            reload(True)
            continue
        time.sleep(3)
        click(342, 256) #click the data type 
        time.sleep(6)
        pyautogui.typewrite('TimeCard')
        time.sleep(0.5)
        click(334, 310) #click at TimeCard
        validation = wait_for_confirmation('Time', 273, 246, 357, 264, time_out=10)
        if validation == False:
            reload(True)
            continue
        time.sleep(1)
        click(733, 255) #cick the choose file button
        time.sleep(1.5)
        if first_run == True:
            click(334, 46) #click the path
            time.sleep(0.5)
            pyautogui.typewrite(path_i) #enter the path
            time.sleep(0.5)
            pyautogui.hotkey('enter')
        elif first_run == False: pass
        time.sleep(1)
        click(385, 448)
        pyautogui.typewrite(file_name)
        pyautogui.hotkey('enter')
        click(574, 321) #click on blank 
        pyautogui.hotkey('end') #scroll down
        time.sleep(0.5)
        click(651, 409) #chage the org field
        time.sleep(1)
        pyautogui.typewrite('mig')
        time.sleep(1)
        click(653, 441)
        time.sleep(0.5)
        click(658, 491) #chage the shop field
        pyautogui.typewrite('mig')
        time.sleep(1)
        click(658, 529)
        time.sleep(0.5)
        click(167, 552) #validate data
        validation = wait_for_confirmation('ready', 269, 539, 497, 561, time_out=15)
        if validation == False:
            reload(True)
            continue
        pyautogui.hotkey('end')
        time.sleep(0.5)
        #click(167, 552) #upload data
        #file_name = search_for_file(file_name)
        validation = wait_for_confirmation('Done', 201, 270, 251, 288, time_out=30)
        if validation == False:
            reload(True)
            continue
        click(509, 420)
        time.sleep(1)
        pyautogui.hotkey('f5')
        os.rename(path_i + '\\' + file_name, path_f + '\\' + file_name)
        u_completed = True
    first_run = False
