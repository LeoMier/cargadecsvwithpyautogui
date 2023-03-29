import pyautogui
import os
from PIL import ImageGrab
import pytesseract
import time
import Levenshtein
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# first, we obtain the name of all files in a list
path_i = r'C:\Users\leomj\Documents\LEO\csvuploader\cargadecsvwithpyautogui\a_subir'
path_f = r'C:\Users\leomj\Documents\LEO\csvuploader\cargadecsvwithpyautogui\subidos'
url = r'https://bubble.io/page?id=sammanger'
directory = 'All TimeCards'
first_run = True
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
    pyautogui.click(435, 49) #access the url
    time.sleep(0.3)
    pyautogui.typewrite(url)
    time.sleep(0.3)
    pyautogui.hotkey('enter')
    time.sleep(2)
    wait_for_confirmation('Data', 6, 294, 56, 313, time_out=60)
    pyautogui.click(22, 295) #click on data onglet
    wait_for_confirmation('App', 342, 182, 418, 209, time_out = 60)
    pyautogui.click(378, 190) #click in APP DATA
    time.sleep(0.5)
    pyautogui.click(216, 365) #search for directory
    time.sleep(1.5)
    pyautogui.typewrite(directory)
    wait_for_confirmation(directory, 115, 412, 216, 440, time_out = 10)
    pyautogui.click(205, 425) #Access the directory
     
def wait_for_confirmation(key_word, a, b, c, d, time_out):
        time.sleep(2)
        str_test = 'ñÍ'
        start_time = time.time()
        temp = key_word
        while key_word not in str_test:
            time.sleep(1)
            if time.time() - start_time > time_out:
                 reload()
            screenshot = ImageGrab.grab(bbox=(a, b, c, d))
            str_test = pytesseract.image_to_string(screenshot)

def upload_data(first_run):
    time.sleep(1)
    pyautogui.click(982, 295) #click upload
    wait_for_confirmation('chosen', 261, 303, 383, 340, time_out= 10)
    pyautogui.click(588, 286) #click the data type 
    time.sleep(1.5)
    pyautogui.typewrite('TimeCard')
    time.sleep(1)
    pyautogui.click(481, 350) # click at TimeCard
    time.sleep(1.5)
    pyautogui.click(889, 284) #click the choose file
    time.sleep(1.5)
    pyautogui.click(687, 47) #click the path
    time.sleep(2)
    if first_run == True:
         pyautogui.typewrite(path_i) #enter the path
    else: pass
    time.sleep(0.1)
    pyautogui.hotkey('enter')
    time.sleep(1.5)
    image = ImageGrab.grab(bbox=(203, 136, 477, 152))
    gray_image = image.convert('L')
    threshold_image = gray_image.point(lambda x: 0 if x < 150 else 255)
    file_name = pytesseract.image_to_string(threshold_image)
    pyautogui.doubleClick(192,140) #select the file
    pyautogui.click(932, 391) 
    pyautogui.hotkey('end') #scroll down
    time.sleep(0.5)
    pyautogui.click(851, 410) #chage the org field
    time.sleep(1)
    pyautogui.typewrite('mig')
    time.sleep(1.5)
    pyautogui.click(843, 442)
    time.sleep(0.5)
    pyautogui.click(839, 493) #chage the shop field
    pyautogui.typewrite('mig')
    time.sleep(1.5)
    pyautogui.click(816, 529)
    time.sleep(0.5)
    pyautogui.click(345, 554) #validate data
    wait_for_confirmation('ready', 439, 540, 667, 562, time_out=10)
    pyautogui.hotkey('end')
    time.sleep(0.5)
    pyautogui.click(344, 554) #upload data
    file_name = search_for_file(file_name)
    wait_for_confirmation('completed', 255, 351, 816, 394, time_out=300)
    pyautogui.click(685, 446)
    pyautogui.hotkey('f5')
    os.rename(path_i + '\\' + file_name, path_f + '\\' + file_name)

acces_the_webb_app()
for _ in os.listdir(path_i):
    upload_data(first_run)
    first_run=False
    wait_for_confirmation('Data', 6, 294, 56, 313, time_out=20)
