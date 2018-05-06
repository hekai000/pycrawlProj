#coding:utf-8
import os
import sys
from pyocr import pyocr
from PIL import Image
import pytesseract
image = Image.open('C:\Python27\Lib\site-packages\pytesseract\code.png')
pytesseract.tesseract_cmd = "C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe"
code = pytesseract.image_to_string(image)
print "111111111"
print code

tools = pyocr.get_available_tools()[:]
print "tools-->", tools
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
#查找OCR引擎
print ("Using '%s'" % (tools[0].get_name()))
print (tools[0].image_to_string(Image.open('code.png')))
