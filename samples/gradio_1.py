import gradio as gr
import matplotlib.pyplot as plt
import numpy as np

def chekc_BMI(bmi):
    if bmi < 18.5:
        return "Bajo peso"
    elif bmi < 24.9:
        return "Normal"
    elif bmi < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"
    
# this is a plot that shows bmi compared to a normal bmi
def create_plot(points):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([18.5, 24.9, 29.9], [0, 1, 0], 'r')
    ax.scatter(points, 0, marker='x', color='b')
    ax.set_xlim([15, 35])
    ax.set_ylim([-0.1, 1.1])
    ax.set_yticks([])
    ax.set_title("BMI")
    ax.legend(["Bajo peso", "Normal", "Sobrepeso", "Obesidad", "Tu BMI"])
    return fig


def process_all(height, weight):
    
    # calculate BMI
    height = float(height)
    weight = float(weight)
    bmi = weight / height ** 2

    return f"Tu BMI es {bmi:.2f} y tu estado es {chekc_BMI(bmi)}", create_plot(bmi)

with gr.Blocks() as demo:
    gr.Markdown("# Demo Completa")

    with gr.Row():
        height = gr.Number(label="Altura", value=1.75, minimum=0.5, maximum=2.5, step=0.01)
        weight = gr.Number(label="Peso", value=70, minimum=10, maximum=200, step=0.5)

    with gr.Column():
        gr.Markdown("## Resultado")
        result = gr.Textbox(label="Resultado")
        plot_output = gr.Plot(label="Gráfico")

    btn = gr.Button("Procesar")
    btn.click(
        fn=process_all,
        inputs=[height, weight],
        outputs= [result, plot_output]
    )

demo.launch()