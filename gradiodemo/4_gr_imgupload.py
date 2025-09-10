import gradio as gr


def save_img(image):
    image.save("uploaded_image.png")
    return "Image saved as uploaded_image.png"


interface = gr.Interface(
    fn=save_img,
    inputs=gr.Image(type="pil", label="Upload an Image"),
    outputs="text",
    title="Image Upload",
    description="Upload an image and save it to the server.",
)

interface.launch()

# input-output interface for image upload and saving
