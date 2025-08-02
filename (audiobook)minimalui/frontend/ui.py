import gradio as gr
from backend.tts_engine import convert_text_to_speech

def create_ui():
    custom_css = open("assets/styles.css").read()

    with gr.Blocks(css=custom_css, theme=gr.themes.Monochrome()) as app:
        gr.Markdown("""
            <h1 style="text-align: center; font-size: 40px;">EchoVerse – AI Voice Generator</h1>
            <h2 style="text-align: center; font-weight: normal;">Convert text into stunning audio in multiple languages</h2>
        """)

        with gr.Tabs():
            with gr.TabItem("📝 Type Text"):
                text_input = gr.Textbox(label="Enter Text", lines=5, placeholder="Type something...", elem_id="text_box")

            with gr.TabItem("🎤 Choose Voice"):
                voice_selector = gr.Radio(choices=["Emma (English)", "Aarohi (Hindi)", "Ravi (Telugu)"], value="Emma (English)", label="Select a Voice")

            with gr.TabItem("🎧 Get Audio"):
                convert_button = gr.Button("Convert to Audio")
                audio_output = gr.Audio(label="Output Audio")

        convert_button.click(fn=convert_text_to_speech, inputs=[text_input, voice_selector], outputs=audio_output)

    return app