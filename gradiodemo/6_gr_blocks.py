import gradio as gr


with gr.Blocks() as demo:
    inp = gr.Textbox(
        label="Your Name: ", lines=1, placeholder="Enter your name here..."
    )
    out = gr.Textbox(lines=1, placeholder="your output...")

    inp.change(lambda name: f"Hello, {name}!", inp, out)

demo.launch()
