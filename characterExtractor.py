import re
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


from PIL import Image

def merge_images(image1, image2):
    # Get the size of the first image
    width1, height1 = image1.size

    # Get the size of the second image
    width2, height2 = image2.size

    # Determine the maximum width and height
    max_width = max(width1, width2)
    max_height = max(height1, height2)

    width = 2*max_width
    height = max_height

    # Create a new image with the maximum dimensions
    merged_image = Image.new('RGB', (width, height), (255, 255, 255))

    # Paste the first image onto the merged image
    merged_image.paste(image1, (0, 0))

    # Paste the second image onto the merged image
    merged_image.paste(image2, (max_width-20, 0))

    return merged_image


class CharacterExtractor:
    def __init__(self, method='default'):
        self.method = method

    def postprocess(self, text):
        text = re.sub(r"[^\w\d]+", '', text)
        if len(text) > 9:
            text = text[1:10]
        return text
    def extract(self, img):
        if self.method == 'default':
            # Get the width and height of the image
            width, height = img.size

            # Calculate the coordinates to split the image
            split_height = height // 2

            # Split the image horizontally
            top = img.crop((0, 0, width, split_height))
            bottom = img.crop((0, split_height, width, height))

            merged_image = merge_images(top, bottom)

            merged_image.save('tmp/current_plate.jpg')
            top.save('tmp/top.jpg')
            bottom.save('tmp/bottom.jpg')

            text = pytesseract.image_to_string(Image.open('tmp/current_plate.jpg'), lang='rus')

            if not text:
                print('fallback!!!')
                text_top = pytesseract.image_to_string(Image.open('tmp/top.jpg'), lang='rus')
                text_bottom = pytesseract.image_to_string(Image.open('tmp/bottom.jpg'), lang='rus')
                text = text_top + text_bottom

            text = self.postprocess(text)
            return text

