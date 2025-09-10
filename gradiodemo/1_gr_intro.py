import gradio as gr


def greet(name):
    return f"Hello, {name}!"


# interface = gr.Interface(
#     fn=greet,
#     inputs="text",
#     outputs="text",
#     title="Greeting App",
#     description="Greet App.",
# )


# interface = gr.Interface(
#     fn=greet,
#     inputs=gr.Textbox(lines=1, placeholder="Enter your name here..."),
#     outputs="text",
#     title="Greeting App",
#     description="Greet App.",
# )

interface = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=1, placeholder="Enter your name here..."),
    outputs=gr.Textbox(lines=1, placeholder="your output..."),
    title="Greeting App",
    description="Greet App.",
)

interface.launch()

