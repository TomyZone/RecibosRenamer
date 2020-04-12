import cv2
import pytesseract
import shutil
import os
from PIL import  Image
from numpy.core.defchararray import strip

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# value = Image.open(r'C:\Users\Inner\Documents\Autonamer\0002.jpg')
# nameEmployee = pytesseract.image_to_string(value)
# print(nameEmployee)

# Set specific directory-folder
os.chdir(r'C:\Users\Inner\Documents\Autonamer\RawFiles')
pathraw = r'C:\Users\Inner\Documents\Autonamer\RawFiles'
pathnamed = pathraw + r'\NamedFiles'

# Loop in list files
# os.listdir() esto me muestra las files del dir actual
try:
    for (dirpath, dirnames, filenames) in os.walk(pathraw):
       for name in filenames:
           if '.jpg' in name:
               value = Image.open(name)
               nameEmployee = pytesseract.image_to_string(value)
               rowsOfText = nameEmployee.split('\n')
               for row in rowsOfText:
                   if 'APELLIDO Y NOMBRES' in row:
                       index = rowsOfText.index(row) + 1
                       subName = rowsOfText[index].split('|')
                       if len(subName) >= 2:
                           shutil.copy(name, pathnamed + r'\\' + subName[1] + '.jpg')
                       else:
                           shutil.copy(name, pathnamed + r'\\' + name)
                       break
except:
    print('Algo fallo: '+ name)
    print('Algo fallo: ' + rowsOfText[index])
finally:
    print('Fallo el except jeje')
