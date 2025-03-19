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
def create_plot(bmi):
    fig, ax = plt.subplots()
    # Umbrales de BMI
    thresholds = [18.5, 24.9, 29.9]
    labels = ["Límite bajo peso", "Límite normal", "Límite sobrepeso"]
    colors = ["orange", "green", "red"]
    for thr, lab, col in zip(thresholds, labels, colors):
        ax.axvline(thr, color=col, linestyle='--', label=lab)
    # BMI del usuario
    ax.axvline(bmi, color='blue', linewidth=2, label="Tu BMI")
    
    ax.set_xlim([15, 35])
    ax.set_title("BMI y Umbrales")
    ax.legend()
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