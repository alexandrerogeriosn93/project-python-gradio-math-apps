from functions import calc_factorial, calc_primorial, convert_temperature
import gradio as gr

with gr.Blocks() as iface:
    with gr.Accordion("Fatorial"):
        input_number = gr.Number(label="Digite um número para calcular o fatorial")
        output_number = gr.Number(label="Fatorial calculado")
        gr.Button("Calcular").click(calc_factorial, input_number, output_number)

    with gr.Accordion("Primorial"):
        input_number = gr.Number(label="Digite um número para calcular o primorial")
        output_number = gr.Number(label="Primorial calculado")
        gr.Button("Calcular").click(calc_primorial, input_number, output_number)

iface.launch(share=False)
