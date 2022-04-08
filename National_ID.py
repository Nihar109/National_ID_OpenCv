import cv2
import pytesseract
import numpy as np
#pytesseract.pytesseract.tesseract_cmd=r"/home/neosoft/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/pytesseract/pytesseract.py""
img =cv2.imread('Adhar Card .jpg')
print(img.shape)

#img_crop=img[400:600,0:700]
img=cv2.resize(img,(400,400))
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Image',img_gray)
text = pytesseract.image_to_string(img_gray)
print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()







