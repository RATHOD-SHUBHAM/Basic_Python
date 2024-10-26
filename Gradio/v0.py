"""
The Interface class is designed to create demos for machine learning models which accept one or more inputs, and return one or more outputs.

The Interface class has three core arguments:

fn: the function to wrap a user interface (UI) around
inputs: the Gradio component(s) to use for the input. The number of components should match the number of arguments in your function.
outputs: the Gradio component(s) to use for the output. The number of components should match the number of return values from your function.


Blocks supports things like controlling where components appear on the page, handling multiple data flows and more complex interactions (e.g. outputs can serve as inputs to other functions), and updating properties/visibility of components based on user interaction — still all in Python.
"""

import gradio as gr


def greet(name, intensity):
    return "Hello" + " " + name+ " " + "!" * intensity


demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"]
)

demo.launch()
