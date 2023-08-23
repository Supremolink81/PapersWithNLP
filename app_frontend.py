import gradio as gr
from app_logic import *

if __name__ == "__main__":

    with gr.Blocks() as paper_analysis_app:

        analysis_inputs_column: gr.Column = gr.Column()

        analysis_outputs_column: gr.Column = gr.Column()

        with analysis_inputs_column:

            paper_file: gr.File = gr.File(label="Upload your paper here:").save_uploaded_file

            analyze_paper_button: gr.Button = gr.Button("Analyze Paper")

        with analysis_outputs_column:

            paper_content: gr.TextArea = gr.TextArea("Hi")

            analyze_paper_button.click(analyze_paper, inputs=[paper_file], outputs=paper_content)

    paper_analysis_app.launch()