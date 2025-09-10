import gradio as gr
import os
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    print(f"Tool 'multiply' invoked with arguments: {a}, {b}")
    return a * b


model = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)
agent = create_react_agent(
    model=model,
    tools=[multiply],
)


def chat_with_agent(user_message):
    response = agent.invoke({"messages": [{"role": "user", "content": user_message}]})
    return response["messages"][-1].content


with gr.Blocks() as demo:
    gr.Markdown("# Calculator Assistant")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Enter your question", placeholder="e.g., 2 times 3?")
    send_btn = gr.Button("Send")

    def respond(message, chat_history):
        reply = chat_with_agent(message)
        chat_history = chat_history + [[message, reply]]
        return "", chat_history

    send_btn.click(respond, [msg, chatbot], [msg, chatbot])
    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()
