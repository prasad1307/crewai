import gradio as gr

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")

    # Define the event handler function
    # def greet(name):
    #     return f"Hello {name}!"

    # Attach the event handler to the button click event
    greet_btn.click(fn=lambda name: f"Hello, {name}!", inputs=name, outputs=output)

demo.launch()
