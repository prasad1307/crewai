import gradio as gr


# add function to perform addition anf the output of the add function is passed to the multiply function


def add(num1, num2):
    return num1 + num2


def multiply(num3, num4):
    return num3 * num4


with gr.Blocks() as demo:
    num1 = gr.Number(label="Number 1")
    num2 = gr.Number(label="Number 2")

    add_btn = gr.Button("Add")

    add_output = gr.Number(label="Addition Output")
    num4 = gr.Number(label="Number 4")
    add_btn.click(fn=add, inputs=[num1, num2], outputs=add_output)

    multiply_btn = gr.Button("Multiply")
    multiply_output = gr.Number(label="Multiplication Output")
    multiply_btn.click(fn=multiply, inputs=[add_output, num4], outputs=multiply_output)

demo.launch()
