# PlateNumberRecognition

## get started

1) Install tesseract: https://tesseract-ocr.github.io/tessdoc/Downloads.html

2) Clone repository and install dependencies:
```
pip install -r -requirements.txt
```

3) In `config.py` change the value of variable `PATH_TO_TESSERACT` to the path to executable of tesseract file installed on the first step:

For example,

`PATH_TO_TESSERACT = r"C:\Program Files\Tesseract-OCR\tesseract.exe"`

4) Make prediction:

`python main.py <path_to_input_image> <path_to_output_image>`

For example,

`python main.py "test_data/444.jpg" "output_img.jpg"`

At the first time, it will take a while for downloading models.
