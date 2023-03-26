import pyautogui
import os
from PIL import ImageGrab
import pytesseract
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# first, we obtain the name of all files in a list
path_i = r'c:\Users\leomj\Documents\LEO\csvuploader\cargadecsvwithpyautogui\por_subir'
path_f = r'c:\Users\leomj\Documents\LEO\csvuploader\cargadecsvwithpyautogui\subidos'
url = r'https://bubble.io/page?id=sammanger'
def acces_the_webb_app(x):
    pyautogui.hotkey('win', str(x))
    pyautogui.click(435, 49) #access the url
    time.sleep(0.3)
    pyautogui.typewrite(url)
    time.sleep(0.3)
    pyautogui.hotkey('enter')
    str_test = 'O'
    while str_test != 'Data':
        screenshot = ImageGrab.grab(bbox=(6, 294, 56, 313))
        str_test = pytesseract.image_to_string(screenshot).split()[0]
        print(str_test)
        time.sleep(1)
    time.sleep(3)
    pyautogui.click(22, 295) #click on data onglet
    time.sleep(1.5)
    pyautogui.click(378, 190) #click in APP DATA
    time.sleep(1.5)
    pyautogui.click(216, 365) #search for "All bills_Data"
    pyautogui.typewrite('All bills_Data')
    time.sleep(1.5)
    pyautogui.click(205, 425)

def upload_data(file_name):
    time.sleep(1)
    pyautogui.click(982, 295)
    time.sleep(1)
    pyautogui.click(588, 286)
    time.sleep(1.5)
    pyautogui.click(487, 501)
    time.sleep(1.5)
    pyautogui.click(889, 284)
    time.sleep(1.5)
    pyautogui.click(687, 47)
    time.sleep(2)
    pyautogui.typewrite(path_i)
    time.sleep(0.1)
    pyautogui.hotkey('enter')
    time.sleep(1.5)
    pyautogui.doubleClick(192,140)

    os.rename(path_i + '\\' + file_name, path_f + '\\' + file_name)
    print('Done: ' + file_name)

acces_the_webb_app(input())
print(os.listdir(path_i))
'''for i in os.listdir(path_i):
    upload_data(i)
    pyautogui.hotkey('f5')
    time.sleep(5)
'''
