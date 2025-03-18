import ollama
import gradio as gr

def chat_response(message, history):
    response = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': message}])
    return response['message']['content']

demo = gr.ChatInterface(
    fn=chat_response,
    title="Chat Demo",
    description="Un simple chat de eco",
    examples=[
        ["Hola", "Echo: Hola"],
        ["¿Cómo estás?", "Echo: ¿Cómo estás?"]
    ]
)

demo.launch()