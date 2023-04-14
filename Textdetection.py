import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('2.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

## detecting word:
hImg, wImg, _ = img.shape

boxes = pytesseract.image_to_data(img)

for x,b in enumerate(boxes.splitlines()):
     # print(b)
     if x!=0:
         b = b.split()
         print(b)
         if len(b)==12:
             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
             cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 1)
             cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (50, 50, 255), 1)

cv2.imshow('Result',img)
cv2.waitKey(0)

