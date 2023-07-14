import torch
import os
from docx2python import docx2python
from pdfminer.high_level import extract_text
from transformers import pipeline
import cv2
import pytesseract
import numpy as np

#pytesseract.pytesseract.tesseract_cmd = ''

question_answering = pipeline("question-answering", model="csarron/bert-base-uncased-squad-v1")
#contextfile = ""
"""def processfile(file):
    contextfile = file
    fname,fext = os.path.splitext(contextfile)
    if fext == ".pdf":
        context = extract_text(contextfile)
    elif fext == ".docx":
        doc_result = docx2python(contextfile)
        context = doc_result.text
    elif fext == ".txt":
        with open(contextfile, 'r') as file:
            context = file.read()
            return context
    else:
        img = cv2.imread(contextfile)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        gray = cv2.bitwise_not(img_bin)
        kernel = np.ones((2, 1), np.uint8)
        img = cv2.erode(gray, kernel, iterations=1)
        img = cv2.dilate(img, kernel, iterations=1)
        context = pytesseract.image_to_string(img)
    return(context)"""
def sendResponse(question,context):
    result = question_answering(question=question, context=context)
    #print("Answer:", result['answer'])
    #print("Score:", result['score'])
    return(result['answer'])
