import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"



print(pytesseract.image_to_string(r"C:\Users\Pranali\Downloads\numberplate_files\car-number-plate-printing-service.jpeg"))
