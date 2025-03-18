import gradio as gr

def multiply(num):
    return num * 2

demo = gr.Interface(
    fn=multiply,
    inputs=gr.Number(
        label="Número",
        value=5,
        minimum=0,
        maximum=100,
        step=0.5,
        precision=2
    ),
    outputs=gr.Number(label="Resultado")
)

demo.launch()