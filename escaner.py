import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


image = cv2.imread('Captura5.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)

texto = pytesseract.image_to_string(dst, lang='spa')
print('texto: ', texto)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
