import gradio as gr

# output-only interface displaying a static image


def get_image():
    url = "https://www.python.org/static/community_logos/python-logo.png"
    return url


interface = gr.Interface(
    fn=get_image,
    inputs=None,
    outputs=gr.Image(type="URL", label="Python Logo"),
    title="Static Image Display",
    description="This interface displays a static image of the Python logo.",
)

interface.launch()


# Image - will accept numpy, file path, or PIL Image object
# numpy - numpy array representation of the image
# file path - local path to an image file
# PIL - Python Imaging Library, used for image processing

# how this demo is processing the image
