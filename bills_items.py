import pyautogui
import os
from PIL import ImageGrab
import pytesseract
import time
import Levenshtein
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path_i = r'C:\Users\JF_db\Desktop\database\Bills\Data\upload'
path_f = r'C:\Users\JF_db\Desktop\database\Bills\Data\done'
url = r'https://bubble.io/page?id=sammanger'
directory = 'All TimeCards'
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
    pyautogui.click(162, 48) #access the url
    time.sleep(0.3)
    pyautogui.typewrite(url)
    time.sleep(0.3)
    pyautogui.hotkey('enter')
    time.sleep(2)
    wait_for_confirmation('Data', 12, 263, 48, 279, time_out=10)
    time.sleep(3)
    pyautogui.click(44, 276) #click on data onglet
    wait_for_confirmation('App', 348, 150, 409, 171, time_out = 10)
    pyautogui.click(409, 171) #click in APP DATA
    time.sleep(2.5)
    if first_run == True:
        pyautogui.click(943,226)
        time.sleep(10)
    time.sleep(1)
    #pyautogui.click(133, 351) #search for directory
    #time.sleep(1.5)
    #pyautogui.typewrite(directory)
    # wait_for_confirmation(directory, 118, 404, 214, 419, time_out = 10)
    #pyautogui.click(214, 419) #Access the directory
     
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

pyautogui.hotkey('win', '1')
first_run = True
reload(first_run)
for _ in range(len(os.listdir(path_i))):
    u_completed = False
    while u_completed == False:
        validation = wait_for_confirmation('Data', 12, 263, 48, 279, time_out=10)
        if validation == False:
            reload(True)
            continue
        time.sleep(5)
        pyautogui.click(850, 275) #click upload
        validation = wait_for_confirmation('chosen', 93, 280, 195, 299, time_out= 10)
        if validation == False:
            reload(True)
            continue
        time.sleep(3)
        pyautogui.click(342, 256) #click the data type 
        time.sleep(6)
        pyautogui.typewrite('Bill')
        time.sleep(0.5)
        pyautogui.click(339, 283) #click at TimeCard
        validation = wait_for_confirmation('Bill', 273, 246, 357, 264, time_out=10)
        if validation == False:
            reload(True)
            continue
        time.sleep(1)
        pyautogui.click(733,255) #cick the choose file
        time.sleep(1.5)
        if first_run == True:
            pyautogui.click(334, 46) #click the path
            time.sleep(0.5)
            pyautogui.typewrite(path_i) #enter the path
            time.sleep(0.5)
            pyautogui.hotkey('enter')
        elif first_run == False: pass
        image = ImageGrab.grab(bbox=(202, 129, 371, 146))
        gray_image = image.convert('L')
        threshold_image = gray_image.point(lambda x: 0 if x < 150 else 255)
        file_name = pytesseract.image_to_string(threshold_image)
        time.sleep(1)
        pyautogui.doubleClick(371, 146) #select the file
        pyautogui.click(749,389) #click on blank 
        time.sleep(0.75)
        pyautogui.hotkey('end') #scroll down
        time.sleep(1)
    
        pyautogui.click(666, 408) #chage the shop field
        pyautogui.typewrite('mig')
        time.sleep(1)
        pyautogui.click(674, 446)
        time.sleep(1)

        pyautogui.click(674, 446) #chage the vendor field
        pyautogui.typewrite('id_vendor')
        time.sleep(1)
        pyautogui.click(674, 488)
        time.sleep(1)

        pyautogui.click(674, 488) #chage the items field
        pyautogui.typewrite('unique id')
        time.sleep(1)
        pyautogui.click(674, 527)
        time.sleep(1)

        pyautogui.click(808, 488) #chage the separator field
        pyautogui.typewrite(',')
        time.sleep(1)
        pyautogui.click(812, 523)
        time.sleep(1)

        pyautogui.click(167, 552) #validate data
        validation = wait_for_confirmation('ready', 269, 539, 497, 561, time_out=15)
        if validation == False:
            reload(True)
            continue
        pyautogui.hotkey('end')
        time.sleep(0.5)
        pyautogui.click(167, 552) #upload data
        file_name = search_for_file(file_name)
        validation = wait_for_confirmation('Done', 201, 270, 251, 288, time_out=120)
        if validation == False:
            reload(True)
            continue
        pyautogui.click(509, 420)
        time.sleep(1)
        pyautogui.hotkey('f5')
        os.rename(path_i + '\\' + file_name, path_f + '\\' + file_name)
        u_completed = True
    first_run = False
