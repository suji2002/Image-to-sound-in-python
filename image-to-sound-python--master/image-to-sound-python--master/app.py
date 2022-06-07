from pytesseract import image_to_string
from gtts import gTTS
from PIL import Image
from playsound import playsound
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sanjay\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def image_to_sound(path_to_image):
    """
    Function for converting an  image to sound
    """
    try:
        loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        print(cleaned_text)
        sound = gTTS(cleaned_text, lang="en")
        sound.save("sound.mp3")
        playsound("sound.mp3")
        return True

    except Exception as bug:
        print("The bug thrown while excuting the code\n", bug)
        return


if __name__ == "__main__":
    image_to_sound("image.jpg")
