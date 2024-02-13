import cv2
import gradio as gr
import numpy as np
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def pre_process_image(image):
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    return image


def upload_file(files):
    result = ""
    for file in files:
        print(file.name)
        image = Image.open(file.name)
        text = pytesseract.image_to_string(pre_process_image(image))
        result += text
    return result
    # return text


# with gr.Blocks() as demo:
#     file_output = gr.File()  # Display the uploaded file(s)
#     upload_button = gr.UploadButton(
#         "Click to Upload Images",
#         file_types=["image"],  # Specify allowed file types (e.g., images)
#         file_count="multiple",  # Allow multiple file uploads
#     )
#     output = upload_button.upload(upload_file, upload_button, file_output)
image_interface = gr.Interface(
    fn=upload_file,
    inputs=gr.UploadButton(
        "Click to Upload Images",
        file_types=["image"],  # Specify allowed file types (e.g., images)
        file_count="multiple",  # Allow multiple file uploads
    ),
    outputs=gr.Textbox(label="Text Output"),
    title="Image OCR",
    description="Upload an image to extract text from it.",
)

if __name__ == '__main__':
    image_interface.launch(share=True)
