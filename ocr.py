import os
from PIL import Image
import pytesseract

# Ensure the tesseract path is in your PATH, or add it here
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Uncomment if on Windows and Tesseract is in the default directory.

def ocr_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def save_to_txt(text, output_filename):
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    directory_path = r"D:\download\upload"
    for filename in os.listdir(directory_path):
        # Assuming you want to process jpg, jpeg, and png images
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            full_path = os.path.join(directory_path, filename)
            recognized_text = ocr_image(full_path)

            # Construct output file name by replacing image extension with .txt
            output_filename = os.path.join(directory_path, os.path.splitext(filename)[0] + '.txt')
            save_to_txt(recognized_text, output_filename)
            print(f"Saved OCR result of {filename} to {output_filename}")
