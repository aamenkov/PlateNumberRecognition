import logging
import argparse
import sys
sys.stdout = sys.__stdout__
from PIL import Image

from characterExtractor import CharacterExtractor
from plateDetector import PlateDetector


if __name__ == '__main__':
    logging.basicConfig(level=logging.FATAL)

    parser = argparse.ArgumentParser(description='Detect license plate and extract characters')
    parser.add_argument('input_image_path', type=str, help='Path to the input image')
    parser.add_argument('output_image_path', type=str, help='Path to the output image')
    args = parser.parse_args()

    input_image_path = args.input_image_path
    output_image_path = args.output_image_path

    # Load the plate detector
    plate_detector = PlateDetector('keremberke/yolov5m-license-plate')

    # Load the character extractor
    character_extractor = CharacterExtractor()

    # Load the image
    image = Image.open(input_image_path)

    # Detect the plate
    result = plate_detector.detect(input_image_path)

    image_croped = image.crop(result['boxes'])

    # Extract the characters
    text = character_extractor.extract(image_croped)

    print(text)

    # Save the image
    image_croped.save(output_image_path)

    print('Saved to', output_image_path)
