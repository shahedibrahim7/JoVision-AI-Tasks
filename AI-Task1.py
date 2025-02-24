import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract(path):
    try:
        img= Image.open(path)
        text= pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        return "Error: "+str(e)
    
def main():
    path= input("Enter image path: ").strip('"')
    print("Extracted text:\n"+extract(path))

main()
