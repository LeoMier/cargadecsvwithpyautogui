import pyautogui
import os
from PIL import ImageGrab
import pytesseract
import time
import Levenshtein
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# first, we obtain the name of all files in a list
path_i = r'C:\Users\JF_db\Desktop\database\timecards\Data\upload'
path_f = r'C:\Users\JF_db\Desktop\database\timecards\Data\done'
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

def acces_the_webb_app():
    pyautogui.hotkey('win', '1')
    reload()


def reload():
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
    time.sleep(0.5)
    pyautogui.click(133, 351) #search for directory
    time.sleep(1.5)
    pyautogui.typewrite(directory)
    # wait_for_confirmation(directory, 118, 404, 214, 419, time_out = 10)
    time.sleep(0.5)
    pyautogui.click(214, 419) #Access the directory
     
def wait_for_confirmation(key_word, a, b, c, d, time_out):
        time.sleep(2)
        str_test = 'ñÍ'
        start_time = time.time()
        while key_word not in str_test:
            time.sleep(1)
            if time.time() - start_time > time_out:
                 reload()
            screenshot = ImageGrab.grab(bbox=(a, b, c, d))
            str_test = pytesseract.image_to_string(screenshot)

def upload_data(first_run):
    time.sleep(5)
    pyautogui.click(850, 275) #click upload
    wait_for_confirmation('chosen', 93, 280, 195, 299, time_out= 10)
    pyautogui.click(296, 253) #click the data type 
    time.sleep(1.5)
    pyautogui.typewrite('TimeCard')
    time.sleep(1.5)
    pyautogui.click(312, 32) #click at TimeCard
    time.sleep(1)
    pyautogui.click(733,255) #cick the choose file
    time.sleep(1.5)
    if first_run == True:
         pyautogui.click(334, 46) #click the path
         time.sleep(0.5)
         pyautogui.typewrite(path_i) #enter the path
         time.sleep(0.5)
         pyautogui.hotkey('enter')
    else: pass
    image = ImageGrab.grab(bbox=(202, 129, 371, 146))
    gray_image = image.convert('L')
    threshold_image = gray_image.point(lambda x: 0 if x < 150 else 255)
    file_name = pytesseract.image_to_string(threshold_image)
    time.sleep(1)
    pyautogui.doubleClick(371, 146) #select the file
    pyautogui.click(574, 321) #click on blank 
    pyautogui.hotkey('end') #scroll down
    time.sleep(0.5)
    pyautogui.click(651, 409) #chage the org field
    time.sleep(1)
    pyautogui.typewrite('mig')
    time.sleep(1)
    pyautogui.click(653, 441)
    time.sleep(0.5)
    pyautogui.click(658, 491) #chage the shop field
    pyautogui.typewrite('mig')
    time.sleep(1)
    pyautogui.click(658, 529)
    time.sleep(0.5)
    pyautogui.click(167, 552) #validate data
    wait_for_confirmation('ready', 269, 539, 497, 561, time_out=15)
    pyautogui.hotkey('end')
    time.sleep(0.5)
    pyautogui.click(167, 552) #upload data
    file_name = search_for_file(file_name)
    wait_for_confirmation('Done', 201, 270, 251, 288, time_out=30)
    pyautogui.click(509, 420)
    pyautogui.hotkey('f5')
    os.rename(path_i + '\\' + file_name, path_f + '\\' + file_name)

acces_the_webb_app()
first_run = True
for _ in range(len(os.listdir(path_i))):
    upload_data(first_run)
    first_run = False
