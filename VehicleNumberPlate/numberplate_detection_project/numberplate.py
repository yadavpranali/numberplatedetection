import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# to preprocess the image
def preprocess_image(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred

# to detect number plate
def detect_number_plate(frame):
    contours, _ = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   
    number_plate = frame 
    return number_plate

# to perform OCR on number plate

def ocr_number_plate(number_plate):
    
    text = pytesseract.image_to_string(number_plate)
    return text

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()

    
    processed_frame = preprocess_image(frame)

    
    number_plate = detect_number_plate(processed_frame)

    
    text = ocr_number_plate(number_plate)
    print("Detected text:", text)

    
    cv2.imshow('Number Plate', number_plate)

   
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break


cap.release()
cv2.destroyAllWindows()