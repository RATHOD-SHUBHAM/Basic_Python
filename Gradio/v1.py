import os
import gradio as gr
from langchain_groq import ChatGroq
from langchain.schema import AIMessage, HumanMessage, SystemMessage

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

system_message = "You are a helpful assistant who acts like a pirate."


# [llama-3.1-8b-instant, llama-3.2-3b-preview, mixtral-8x7b-32768, gemma2-9b-it]
llm = ChatGroq(
    model = 'llama-3.2-3b-preview',
    temperature = 1

)

def stream_response(message, history):
    print(f"Input: {message}. History: {history}\n")

    # Create new history each time when the call is made by appending previous conversations.
    history_langchain_format = []
    history_langchain_format.append(SystemMessage(content=system_message))

    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))

    if message is not None:
        history_langchain_format.append(HumanMessage(content=message))
        partial_message = ""

        # Stream LLM Response
        for response in llm.stream(history_langchain_format):
            partial_message += response.content
            yield partial_message


demo = gr.ChatInterface(
    stream_response,
    textbox=gr.Textbox(
        placeholder="Send to the LLM...",
        container=True,
        show_label=True,
        label="Ask LLM",
        autoscroll=True,
        scale=7,
        submit_btn=True
    ),
    title="My PirateBot"
)

demo.launch()