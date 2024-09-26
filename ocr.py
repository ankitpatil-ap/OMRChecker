from PIL import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  
def ocr_to_text(input_image_path, output_text_file):
    try:
        with Image.open(input_image_path) as img:
            text = pytesseract.image_to_string(img)
            with open(output_text_file, 'w', encoding='utf-8') as text_file:
                text_file.write(text)
                
            print(f"Text successfully extracted to {output_text_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
input_image_path = input("Enter File Name Properly: ")
output_text_file = 'stud.txt'  

ocr_to_text(input_image_path, output_text_file)
