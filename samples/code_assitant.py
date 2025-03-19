import gradio as gr
import matplotlib.pyplot as plt
import numpy as np
import ollama
from pydantic import BaseModel
import asyncio
from ollama import AsyncClient

lang = "python"

class CodeResponse(BaseModel):
  message: str
  code: str

async def process_all(code):
    # create 
    code = ''
    response_message = ''
    client = AsyncClient()
    response = await client.chat(model='llama3.2', messages=[{'role': 'user', 'content': 
                                             """contesta con un json con2 campos a la pregunta de que mejoras se pueden hacer en el código. 
                                             Un campo tiene el nombre 'message' y define de modo general las mejoras que se pueden hacer.
                                             El otro campo tiene el nombre 'code' y tiene el código corregido.
                                             el usuario escribe el siguiente código: """ + code }],
                                             format=CodeResponse.model_json_schema(),
                                             options={'temperature': 0})
    code_response = CodeResponse.model_validate_json(response.message.content)
    code = code_response.code
    response_message = code_response.message      
    return code, response_message


with gr.Blocks() as demo:
    gr.Markdown("# Demo Completa")

    with gr.Row():
        user_code = gr.Code(label="Código de usuario", value="print('Hola mundo')", language=lang)

    with gr.Row():
        assistant_code = gr.Code(label="Código de asistente", value="print('Hola mundo')", language=lang)
        assistant_response = gr.Textbox(label="Respuesta de asistente", value="Hola mundo")

    btn = gr.Button("Procesar")
    btn.click(
        fn=process_all,
        inputs=[user_code],
        outputs= [assistant_code, assistant_response]
    )

demo.launch()