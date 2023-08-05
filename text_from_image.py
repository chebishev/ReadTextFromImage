from PIL import Image
from pytesseract import pytesseract

# For windows users: Define the path to your tesseract installation:
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# define the path to the image. It works with paths in this format too:
# "C:\Users\user\Downloads\devices_weekly_23051301.png"
image_path = r"devices_weekly_23051301.png"

# adding object refference with the desired path
image = Image.open(image_path)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(imgage)

# Displaying the extracted text
print(text[:-1])
